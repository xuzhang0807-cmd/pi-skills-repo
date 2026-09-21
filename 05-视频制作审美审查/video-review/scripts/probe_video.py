#!/usr/bin/env python3
"""Probe a local video and optionally extract a bounded set of sampled frames."""
from __future__ import annotations
import argparse
import json
import math
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def run(argv: list[str], timeout: int = 60) -> str:
    completed = subprocess.run(argv, capture_output=True, text=True, timeout=timeout, check=False)
    if completed.returncode:
        raise RuntimeError(completed.stderr[-2000:] or f'Process exited {completed.returncode}')
    return completed.stdout


def positive_number(value) -> float | None:
    try:
        number = float(value)
        return number if math.isfinite(number) and number > 0 else None
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Local video; network inputs are not accepted.')
    parser.add_argument('--out', required=True, type=Path, help='New report directory; existing paths are refused.')
    parser.add_argument('--frames', type=int, default=0, help='Optional evenly spaced frame samples (0-24).')
    args = parser.parse_args()
    result = {'schema_version': 1, 'status': 'incomplete', 'samples': [], 'errors': [],
              'scope': 'Metadata plus requested sampled-frame decoding; NOT full playback, all-frame validation, listening or aesthetic approval.'}
    output_created = False
    try:
        source = args.input.resolve(strict=True)
        if not source.is_file():
            raise ValueError('Input must be a local file.')
        if not 0 <= args.frames <= 24:
            raise ValueError('--frames must be between 0 and 24.')
        if args.out.exists():
            raise ValueError('Output already exists; choose a new directory.')
        probe = shutil.which('ffprobe')
        encoder = shutil.which('ffmpeg')
        if not probe or (args.frames and not encoder):
            raise RuntimeError('ffprobe is required; frame extraction additionally requires ffmpeg.')
        args.out.mkdir(parents=True, exist_ok=False)
        output_created = True
        result['file'] = source.name
        entries = 'format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,pix_fmt,avg_frame_rate,r_frame_rate,duration,sample_rate,channels:stream_tags=rotate:stream_side_data=rotation'
        raw = json.loads(run([probe, '-v', 'error', '-protocol_whitelist', 'file,pipe',
                              '-show_entries', entries, '-of', 'json', str(source)]))
        result['format'] = raw.get('format', {})
        result['streams'] = raw.get('streams', [])
        videos = [s for s in result['streams'] if s.get('codec_type') == 'video']
        if not videos:
            raise ValueError('No video stream was found.')
        video = videos[0]
        duration = positive_number(result['format'].get('duration')) or positive_number(video.get('duration'))
        result['duration_seconds'] = duration
        try:
            rate = float(Fraction(video.get('avg_frame_rate', '0/0')))
            result['average_fps'] = rate if math.isfinite(rate) and rate > 0 else None
        except (ValueError, ZeroDivisionError):
            result['average_fps'] = None
        result['has_audio_stream'] = any(s.get('codec_type') == 'audio' for s in result['streams'])
        if args.frames:
            if duration is None:
                raise ValueError('Duration is unknown; cannot select uniform frame timestamps.')
            for index in range(args.frames):
                timestamp = duration * (index + 0.5) / args.frames
                filename = f'frame-{index + 1:02d}.png'
                sample = {'requested_time_seconds': round(timestamp, 6), 'file': filename,
                          'note': 'Seek target; actual decoded frame may be at a nearby timestamp.'}
                result['samples'].append(sample)
                try:
                    run([encoder, '-nostdin', '-hide_banner', '-loglevel', 'error', '-n',
                         '-protocol_whitelist', 'file,pipe', '-ss', f'{timestamp:.6f}', '-i', str(source),
                         '-map', f'0:{video["index"]}', '-frames:v', '1', '-vf', 'scale=1280:1280:force_original_aspect_ratio=decrease',
                         str(args.out / filename)])
                    sample['decoded'] = (args.out / filename).is_file() and (args.out / filename).stat().st_size > 0
                    if not sample['decoded']:
                        result['errors'].append(f'No frame produced for sample {index + 1}.')
                except Exception as exc:
                    sample['decoded'] = False
                    sample['error'] = str(exc)
                    result['errors'].append(f'Sample {index + 1}: {exc}')
        result['status'] = 'incomplete' if result['errors'] else 'probe_complete_not_quality_approval'
    except Exception as exc:
        result['errors'].append(str(exc))
    if output_created:
        with (args.out / 'report.json').open('x', encoding='utf-8') as handle:
            json.dump(result, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
        print(str(args.out / 'report.json'))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)
    return 2 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
