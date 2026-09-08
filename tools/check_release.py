#!/usr/bin/env python3
"""Offline smoke checks for the reviewed public package; no third-party packages."""
import ast
import copy
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.entries = []
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.current = [dict(attrs), '']
    def handle_data(self, text):
        if self.current is not None:
            self.current[1] += text
    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            self.entries.append(self.current)
            self.current = None


def main():
    data = json.loads((ROOT / 'examples/demo-trip.json').read_text(encoding='utf-8'))
    validator = module('validate_trip')
    assert validator.validate(data) == ([], [])
    invalid = copy.deepcopy(data)
    invalid['days'][0]['events'][0]['location']['lat'] = 999
    assert validator.validate(invalid)[0], 'invalid coordinates must fail'
    invalid = copy.deepcopy(data)
    invalid['days'][0]['events'][1]['id'] = invalid['days'][0]['events'][0]['id']
    assert validator.validate(invalid)[0], 'duplicate IDs must fail'

    base = module('build_html').build(data)
    assert base == (ROOT / 'examples/demo-trip.html').read_text(encoding='utf-8')
    parser = Scripts()
    parser.feed(base)
    embedded = next(text for attrs, text in parser.entries if attrs.get('id') == 'trip-data')
    assert json.loads(embedded) == data, 'embedded data differs'
    assert 'https://www.openstreetmap.org/copyright' in base
    assert 'https://www.openstreetmap.org/copyright' in (ROOT / 'scripts/visual_template.html').read_text()

    ics = module('build_ics')
    calendar = ics.build(data)
    assert calendar.count('BEGIN:VEVENT') == 6
    assert calendar.count('BEGIN:VEVENT') == calendar.count('END:VEVENT')
    assert calendar.count('BEGIN:VALARM') == calendar.count('END:VALARM')
    assert 'DTSTART:20261002T000000Z' in calendar
    assert 'DTSTART;TZID=Asia/Tokyo:20261002T140000' in calendar
    fixture = copy.deepcopy(data)
    fixture['days'][0]['events'][0]['assignedTo'] = ['traveler-a']
    assert 'UID:d1-arrive@travel-copilot' in ics.build(fixture, 'traveler-a')
    assert 'UID:d1-arrive@travel-copilot' not in ics.build(fixture, 'traveler-b')
    raw = (ROOT / 'examples/demo-reminders.ics').read_bytes()
    assert raw.endswith(b'END:VCALENDAR\r\n')
    assert b'\n' not in raw.replace(b'\r\n', b'')
    normalize = lambda s: re.sub(r'DTSTAMP:[^\r\n]+', 'DTSTAMP:IGNORED', s)
    assert normalize(raw.decode()) == normalize(calendar)

    for path in list((ROOT / 'scripts').glob('*.py')) + list((ROOT / 'tools').glob('*.py')):
        ast.parse(path.read_text(), filename=str(path), feature_version=(3, 9))
    broken = []
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts or 'output' in path.parts:
            continue
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            if not (path.parent / target.split('#')[0]).exists():
                broken.append((str(path.relative_to(ROOT)), target))
    assert not broken, broken

    with tempfile.TemporaryDirectory() as temp:
        out = Path(temp)
        subprocess.run([sys.executable, str(ROOT / 'scripts/package_trip.py'),
                        str(ROOT / 'examples/demo-trip.json'), '--out-dir', str(out / 'pack')], check=True, stdout=subprocess.DEVNULL)
        assert (out / 'pack/trip.json').exists()
        assert len(list((out / 'pack').iterdir())) == 4
        node = shutil.which('node')
        if node:
            template_parser = Scripts()
            template_parser.feed((ROOT / 'scripts/visual_template.html').read_text())
            for idx, (attrs, script) in enumerate(parser.entries + template_parser.entries):
                if attrs.get('type') == 'application/json' or attrs.get('src'):
                    continue
                p = out / ('script-' + str(idx) + '.js')
                p.write_text(script)
                subprocess.run([node, '--check', str(p)], check=True)
            print('PASS: inline JavaScript syntax (Node)')
        else:
            print('SKIP: JavaScript syntax check (Node not installed)')
    print('PASS: demo, validator rejection, HTML data, OSM attribution, ICS UTC/TZID/CRLF/filtering, packaging, Python 3.9 syntax, Markdown links')
    print('Not covered: browser interaction, calendar import, real Python 3.9 runtime, host installation or source provenance')

if __name__ == '__main__':
    main()
