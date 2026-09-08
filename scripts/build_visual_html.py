#!/usr/bin/env python3
import argparse, json, html
from pathlib import Path

def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def compact(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</script>', '<\\/script>')

def build(trip, brief):
    t=trip.get('trip',{})
    title=html.escape(t.get('title','Travel Copilot'))
    subtitle=html.escape(t.get('subtitle',''))
    trip_json=compact(trip)
    brief_json=compact(brief)
    template=Path(__file__).with_name('visual_template.html').read_text(encoding='utf-8')
    return (template
            .replace('__TITLE__', title)
            .replace('__SUBTITLE__', subtitle)
            .replace('__TRIP_JSON__', trip_json)
            .replace('__BRIEF_JSON__', brief_json))

def main():
    ap=argparse.ArgumentParser(description='Render Travel Copilot with a frozen creative brief')
    ap.add_argument('trip_json')
    ap.add_argument('creative_brief')
    ap.add_argument('-o','--output', default='trip-visual.html')
    a=ap.parse_args()
    Path(a.output).write_text(build(load(a.trip_json), load(a.creative_brief)), encoding='utf-8')
    print(a.output)

if __name__=='__main__': main()
