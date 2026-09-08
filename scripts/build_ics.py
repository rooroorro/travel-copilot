#!/usr/bin/env python3
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

def esc(s):
    return str(s or "").replace('\\','\\\\').replace('\n','\\n').replace(',','\\,').replace(';','\\;')

def utc_stamp(iso):
    dt=datetime.fromisoformat(iso.replace('Z','+00:00'))
    if dt.tzinfo is None: return None
    return dt.astimezone(timezone.utc).strftime('%Y%m%dT%H%M%SZ')

def local_stamp(day, hhmm): return day.replace('-','')+'T'+hhmm.replace(':','')+'00'

def relevant(item, traveler):
    assigned=item.get('assignedTo') or []
    return not traveler or not assigned or traveler in assigned

def build(data, traveler=None, priorities=None):
    trip=data.get('trip',{}); tzid=trip.get('timezone','UTC'); version=(data.get('meta') or {}).get('version','1.0')
    title=trip.get('title','Trip'); items=[]
    for r in data.get('reminders') or []:
        if not relevant(r,traveler): continue
        if priorities and r.get('priority','P1') not in priorities: continue
        if not r.get('datetime'): continue
        items.append((r.get('id'),r.get('title'),r.get('description',''),r.get('datetime'),None,r.get('alarmMinutes') or ([120,30,10] if r.get('priority')=='P0' else [60,20])))
    explicit_related={r.get('relatedEventId') for r in data.get('reminders') or []}
    for d in data.get('days') or []:
        for e in d.get('events') or []:
            p=e.get('priority','P2')
            if p not in ('P0','P1') or (priorities and p not in priorities) or e.get('id') in explicit_related or not e.get('start') or not relevant(e,traveler): continue
            alarms=[120,30,10] if p=='P0' else [60,20]
            items.append((e.get('id'),e.get('title'),e.get('description',''),None,(d.get('date'),e.get('start')),alarms))
    now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Travel Copilot//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH',f'X-WR-CALNAME:{esc(title)} reminders v{esc(version)}']
    for iid,ititle,desc,iso,local,alarms in items:
        lines += ['BEGIN:VEVENT',f'UID:{esc(iid)}@travel-copilot',f'DTSTAMP:{now}',f'SUMMARY:{esc(ititle)}']
        if iso:
            stamp=utc_stamp(iso)
            if stamp: lines.append('DTSTART:'+stamp)
            else: lines.append(f'DTSTART;TZID={tzid}:{iso[:16].replace("-","").replace(":","").replace("T","T")}00')
        else:
            lines.append(f'DTSTART;TZID={tzid}:{local_stamp(local[0],local[1])}')
        if desc: lines.append('DESCRIPTION:'+esc(desc))
        for m in alarms:
            lines += ['BEGIN:VALARM',f'TRIGGER:-PT{int(m)}M','ACTION:DISPLAY',f'DESCRIPTION:{esc(ititle)}','END:VALARM']
        lines.append('END:VEVENT')
    lines.append('END:VCALENDAR')
    return '\r\n'.join(lines)+'\r\n'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('json_file'); ap.add_argument('-o','--output',default='trip-reminders.ics'); ap.add_argument('--traveler'); ap.add_argument('--priorities',default='P0,P1')
    a=ap.parse_args(); data=json.loads(Path(a.json_file).read_text(encoding='utf-8')); priorities=set(x.strip() for x in a.priorities.split(',') if x.strip())
    with Path(a.output).open('w', encoding='utf-8', newline='') as output:
        output.write(build(data,a.traveler,priorities))
    print(a.output)
if __name__=='__main__': main()
