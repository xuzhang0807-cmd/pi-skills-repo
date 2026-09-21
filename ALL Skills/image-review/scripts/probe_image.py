#!/usr/bin/env python3
"""Read image properties without editing the source or disclosing EXIF metadata."""
from __future__ import annotations
import argparse
import json
import sys
import warnings
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Local source image.')
    parser.add_argument('--output', type=Path, help='New JSON report file; never overwritten.')
    args = parser.parse_args()
    try:
        from PIL import Image, ImageOps
        source = args.input.resolve(strict=True)
        if not source.is_file():
            raise ValueError('Input must be a file.')
        if args.output and (args.output.exists() or args.output.resolve() == source):
            raise ValueError('Output already exists or is the input; choose a new path.')
        with warnings.catch_warnings():
            warnings.simplefilter('error', Image.DecompressionBombWarning)
            with Image.open(source) as image:
                image_format = image.format
                stored_size = list(image.size)
                mode = image.mode
                frames = int(getattr(image, 'n_frames', 1))
                image.seek(0)
                image.load()
                # Orientation is the only EXIF field inspected; no metadata dump.
                oriented = ImageOps.exif_transpose(image)
                result = {
                    'schema_version': 1, 'file': source.name, 'bytes': source.stat().st_size,
                    'format': image_format, 'stored_size': stored_size,
                    'oriented_size': list(oriented.size), 'mode': mode,
                    'has_alpha_channel_or_transparency': 'A' in image.getbands() or 'transparency' in image.info,
                    'frames': frames, 'first_frame_decoded': True,
                    'scope': 'File metadata and first-frame decoding only; no aesthetic, identity, licensing or full animation validation.',
                    'private_metadata_included': False,
                }
        text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with args.output.open('x', encoding='utf-8') as handle:
                handle.write(text)
            print(str(args.output))
        else:
            print(text, end='')
        return 0
    except Exception as exc:
        print(f'Image probe failed: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
