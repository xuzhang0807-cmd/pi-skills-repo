#!/usr/bin/env python3
"""Sync canonical skill copies to scenarios. Dry-run by default; refuse local conflicts."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def hashes(folder: Path) -> dict[str, str]:
    if folder.is_symlink():
        raise ValueError(f'Symlink is not supported: {folder}')
    result = {}
    for p in sorted(folder.rglob('*')):
        if p.is_symlink():
            raise ValueError(f'Symlink is not supported: {p}')
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
            result[p.relative_to(folder).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def child(root: Path, component: str) -> Path:
    if not component or component in ('.', '..') or '/' in component or '\\' in component:
        raise ValueError('Unsafe path component in manifest.')
    p = root / component
    if p.is_symlink() or p.resolve().parent != root.resolve():
        raise ValueError('Path escapes expected parent or is a symlink.')
    return p


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--apply', action='store_true', help='Apply the displayed updates with backups; conflicts still stop the run.')
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        manifest_path = root / 'manifest.json'
        manifest_text = manifest_path.read_text(encoding='utf-8')
        manifest = json.loads(manifest_text)
        library = child(root, 'ALL Skills')
        by_name = {s['name']: s for s in manifest['skills']}
        sources = {}
        for name in by_name:
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
                raise ValueError('Invalid skill name: ' + name)
            source = child(library, name)
            if not (source / 'SKILL.md').is_file():
                raise ValueError('Missing canonical SKILL.md: ' + name)
            sources[name] = hashes(source)
        operations = []
        conflicts = []
        for scene in manifest['scenes'].values():
            target_parent = child(root, scene['folder'])
            for name in scene['skills']:
                target = child(target_parent, name)
                current = hashes(target) if target.is_dir() else None
                expected = by_name[name].get('local_file_sha256')
                if current == sources[name]:
                    status = 'SAME'
                elif target.exists() and (not target.is_dir() or expected is None or current != expected):
                    status = 'CONFLICT'
                    conflicts.append(str(target.relative_to(root)))
                else:
                    status = 'UPDATE' if target.exists() else 'ADD'
                    operations.append((name, target))
                print(f'{status:8} {target.relative_to(root)}')
        if conflicts:
            raise ValueError('Scenario copies were edited locally. Merge these edits into ALL Skills and align the corresponding copies manually before retrying: ' + '; '.join(conflicts))
        if not args.apply:
            print(f'DRY RUN: {len(operations)} changes. Nothing written. Add --apply after review.')
            return 0
        if not operations:
            print('No changes needed.')
            return 0
        backup_parent = child(root, 'backups')
        backup_parent.mkdir(exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ-')
        backup_root = Path(tempfile.mkdtemp(prefix=stamp, dir=backup_parent))
        (backup_root / 'manifest.before.json').write_text(manifest_text, encoding='utf-8')
        completed = []
        stages = []
        try:
            # Prepare every new tree before replacing any current tree.
            for name, target in operations:
                target.parent.mkdir(parents=True, exist_ok=True)
                stage = Path(tempfile.mkdtemp(prefix='.skills-stage-', dir=target.parent))
                stages.append(stage)
                shutil.copytree(library / name, stage / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            for (name, target), stage in zip(operations, stages):
                old = None
                if target.exists():
                    old = backup_root / target.relative_to(root)
                    old.parent.mkdir(parents=True, exist_ok=True)
                    target.rename(old)
                completed.append((target, old))
                (stage / name).rename(target)
            for name, skill in by_name.items():
                skill['local_file_sha256'] = sources[name]
            temp_manifest = root / '.manifest-sync.tmp'
            if temp_manifest.exists():
                raise ValueError('Temporary manifest already exists; inspect it before retrying.')
            with temp_manifest.open('x', encoding='utf-8') as handle:
                json.dump(manifest, handle, ensure_ascii=False, indent=2)
                handle.write('\n')
            temp_manifest.replace(manifest_path)
        except Exception:
            for target, old in reversed(completed):
                if target.exists():
                    shutil.rmtree(target)
                if old and old.exists():
                    old.rename(target)
            raise
        finally:
            for stage in stages:
                if stage.exists():
                    shutil.rmtree(stage)
        print(f'Applied {len(operations)} updates. Backup: {backup_root}')
        print('Only scenario skill copies and local integrity baselines changed; no upstream hashes or installed clients changed.')
        return 0
    except Exception as exc:
        print(f'Sync stopped: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
