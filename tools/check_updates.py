#!/usr/bin/env python3
"""Read-only GitHub SKILL.md hash checks; no downloads, installs or auto-updates."""
from __future__ import annotations
import argparse
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def classify(expected: str, actual: str) -> str:
    if not re.fullmatch(r'[0-9a-f]{40}', actual or ''):
        return 'UNKNOWN'
    return 'SAME' if expected == actual else 'CHANGED'


def check_one(skill: dict, timeout: int, offline: bool = False, opener=None) -> dict:
    result = {'name': skill['name'], 'repo': skill.get('repo'), 'expected_blob_sha': skill.get('upstream_blob_sha')}
    if not skill.get('repo'):
        return {**result, 'status': 'LOCAL'}
    if offline:
        return {**result, 'status': 'OFFLINE', 'note': 'No network check performed.'}
    try:
        repo = skill['repo']
        path = skill['source_path']
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
            raise ValueError('Invalid repository name in manifest.')
        if path.startswith('/') or '..' in Path(path).parts:
            raise ValueError('Invalid relative source path in manifest.')
        url = 'https://api.github.com/repos/' + repo + '/contents/' + urllib.parse.quote(path, safe='/')
        request = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'skills-bundle-entrypoint-check/1.0'})
        open_url = opener or urllib.request.urlopen
        with open_url(request, timeout=timeout) as response:
            data = json.load(response)
        actual = data.get('sha') if isinstance(data, dict) else None
        return {**result, 'status': classify(skill['upstream_blob_sha'], actual), 'current_blob_sha': actual}
    except Exception as exc:
        return {**result, 'status': 'UNKNOWN', 'error': str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--offline', action='store_true', help='Validate manifest and list entries WITHOUT checking the network.')
    parser.add_argument('--json', action='store_true', help='Print JSON instead of a compact table.')
    parser.add_argument('--timeout', type=int, default=12)
    args = parser.parse_args()
    try:
        if not 1 <= args.timeout <= 60:
            raise ValueError('--timeout must be between 1 and 60 seconds.')
        manifest = json.loads((args.root / 'manifest.json').read_text(encoding='utf-8'))
        skills = manifest['skills']
        names = [s['name'] for s in skills]
        if len(set(names)) != len(names):
            raise ValueError('Duplicate canonical skill names in manifest.')
        for skill in skills:
            if skill.get('repo') and not re.fullmatch(r'[0-9a-f]{40}', skill.get('upstream_blob_sha') or ''):
                raise ValueError('Missing or invalid recorded hash: ' + skill['name'])
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda s: check_one(s, args.timeout, args.offline), skills))
        if args.json:
            print(json.dumps({'scope': 'SKILL.md only; other upstream files are NOT checked.', 'results': results}, ensure_ascii=False, indent=2))
        else:
            print('ENTRYPOINT CHECK ONLY: scripts, references and repository activity are NOT checked.')
            for row in results:
                print(f'{row["status"]:8} {row["name"]}' + (f' | {row["error"]}' if row.get('error') else ''))
        return 2 if any(r['status'] == 'UNKNOWN' for r in results) else 1 if any(r['status'] == 'CHANGED' for r in results) else 0
    except Exception as exc:
        print(f'Update check failed: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
