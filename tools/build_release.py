#!/usr/bin/env python3
"""Package the explicitly reviewed public files; never include the working tree wholesale."""
import argparse
import hashlib
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.1.0'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', default='dist')
    args = parser.parse_args()
    output = Path(args.out_dir).resolve()
    names = [x.strip() for x in (ROOT / 'tools/release-files.txt').read_text().splitlines()
             if x.strip() and not x.startswith('#')]
    if len(names) != len(set(names)):
        raise SystemExit('Duplicate release manifest entry')
    payloads = []
    for name in names:
        relative = Path(name)
        source = ROOT / relative
        if relative.is_absolute() or '..' in relative.parts or source.is_symlink():
            raise SystemExit('Unsafe release path: ' + name)
        if not source.resolve().is_relative_to(ROOT) or not source.is_file():
            raise SystemExit('Missing or external release file: ' + name)
        payloads.append((name, source.read_bytes()))
    output.mkdir(parents=True, exist_ok=True)
    archive = output / ('travel-copilot-v' + VERSION + '.zip')
    with ZipFile(archive, 'w', compression=ZIP_DEFLATED, compresslevel=9) as bundle:
        for name, content in sorted(payloads):
            info = ZipInfo('travel-copilot/' + name, date_time=(2026, 9, 8, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, content, compress_type=ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / 'SHA256SUMS.txt').write_text(digest + '  ' + archive.name + '\n', encoding='ascii')
    print(str(archive))
    print(str(len(payloads)) + ' reviewed files; SHA-256 ' + digest)

if __name__ == '__main__':
    main()
