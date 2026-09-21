#!/usr/bin/env python3
"""Capture limited, non-interactive browser diagnostics. Not a full E2E test."""
from __future__ import annotations
import argparse
import ipaddress
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


def local_url(url: str) -> bool:
    try:
        p = urlsplit(url)
        if p.scheme not in ('http', 'https') or not p.hostname:
            return False
        if p.hostname.lower() == 'localhost':
            return True
        return ipaddress.ip_address(p.hostname).is_loopback
    except ValueError:
        return False


def redacted_url(url: str) -> str:
    try:
        p = urlsplit(url)
        if p.scheme in ('data', 'blob'):
            return p.scheme + ':<omitted>'
        return urlunsplit((p.scheme, p.netloc, p.path, '<redacted>' if p.query else '', ''))
    except ValueError:
        return '<unparseable-url>'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--url', required=True, help='Authorized HTTP(S) target; loopback only by default.')
    parser.add_argument('--out', required=True, type=Path, help='New output directory; existing paths are refused.')
    parser.add_argument('--ready-selector', help='Optional real CSS selector indicating readiness.')
    parser.add_argument('--allow-remote', action='store_true', help='Explicitly allow remote targets AND page resources.')
    parser.add_argument('--timeout-ms', type=int, default=15000)
    args = parser.parse_args()
    try:
        parsed = urlsplit(args.url)
        if parsed.scheme not in ('http', 'https') or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError('Use HTTP(S) without embedded credentials.')
        if not args.allow_remote and not local_url(args.url):
            raise ValueError('Remote targets require --allow-remote after authorization.')
        if not 1000 <= args.timeout_ms <= 120000:
            raise ValueError('--timeout-ms must be between 1000 and 120000.')
        if args.out.exists():
            raise ValueError('Output already exists; choose a new directory.')
        from playwright.sync_api import sync_playwright
    except (ValueError, ImportError) as exc:
        print(f'Cannot run: {exc}', file=sys.stderr)
        return 2
    report = {
        'schema_version': 1, 'created_at': datetime.now(timezone.utc).isoformat(),
        'url': redacted_url(args.url), 'remote_resources_allowed': args.allow_remote,
        'scope': 'Navigation, screenshots, page errors, failed requests and overflow only; no clicks, form submission, login or full E2E coverage.',
        'views': [], 'execution_errors': [],
    }
    try:
        args.out.mkdir(parents=True, exist_ok=False)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            try:
                for label, width, height in [('desktop', 1440, 1000), ('mobile', 390, 844)]:
                    view = {'label': label, 'viewport': {'width': width, 'height': height}, 'page_errors': [],
                            'failed_requests': [], 'blocked_requests': [], 'execution_errors': []}
                    report['views'].append(view)
                    context = browser.new_context(viewport={'width': width, 'height': height}, service_workers='block')
                    def guard(route, request):
                        if args.allow_remote or local_url(request.url):
                            route.continue_()
                        else:
                            view['blocked_requests'].append(redacted_url(request.url))
                            route.abort('blockedbyclient')
                    context.route('**/*', guard)
                    page = context.new_page()
                    page.set_default_timeout(args.timeout_ms)
                    page.on('pageerror', lambda error: view['page_errors'].append(str(error)))
                    page.on('requestfailed', lambda request: view['failed_requests'].append({
                        'url': redacted_url(request.url), 'failure': request.failure}))
                    try:
                        response = page.goto(args.url, wait_until='domcontentloaded', timeout=args.timeout_ms)
                        view['http_status'] = response.status if response else None
                        if args.ready_selector:
                            page.locator(args.ready_selector).first.wait_for(state='visible', timeout=args.timeout_ms)
                        # Allow a rendered frame without waiting for perpetual network idleness.
                        page.evaluate('() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))')
                        view['title'] = page.title()
                        view['final_url'] = redacted_url(page.url)
                        view['layout'] = page.evaluate('''() => ({
                            viewport_width: document.documentElement.clientWidth,
                            content_width: Math.max(document.documentElement.scrollWidth, document.body?.scrollWidth || 0),
                            horizontal_overflow: Math.max(document.documentElement.scrollWidth, document.body?.scrollWidth || 0) > document.documentElement.clientWidth + 1
                        })''')
                        screenshot = f'{label}.png'
                        page.screenshot(path=str(args.out / screenshot), full_page=True, timeout=args.timeout_ms)
                        view['screenshot'] = screenshot
                    except Exception as exc:
                        view['execution_errors'].append(str(exc))
                    finally:
                        context.close()
            finally:
                browser.close()
    except Exception as exc:
        report['execution_errors'].append(str(exc))
    execution_failed = bool(report['execution_errors']) or any(v['execution_errors'] for v in report['views'])
    findings = any(v['page_errors'] or v['failed_requests'] or v['blocked_requests'] or
                   v.get('layout', {}).get('horizontal_overflow') or
                   (v.get('http_status') or 0) >= 400 for v in report['views'])
    report['status'] = 'incomplete' if execution_failed else 'findings' if findings else 'no_findings_in_limited_checks'
    if args.out.is_dir():
        with (args.out / 'report.json').open('x', encoding='utf-8') as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
        print(str(args.out / 'report.json'))
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2), file=sys.stderr)
    return 2 if execution_failed else 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
