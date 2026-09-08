#!/usr/bin/env python3
import argparse, json, re, sys
from datetime import date
from pathlib import Path

THEMES={"cinematic","urban-neon","nature","island","japan-minimal"}
PRIORITIES={"P0","P1","P2"}
TIME_RE=re.compile(r"^([01]\d|2[0-3]):[0-5]\d$")

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate(data):
    errors=[]; warnings=[]
    meta=data.get("meta") or {}; trip=data.get("trip") or {}; days=data.get("days")
    for key in ("title","startDate","endDate","timezone"):
        if not trip.get(key): errors.append(f"trip.{key} is required")
    if not isinstance(days,list) or not days: errors.append("days must be a non-empty array")
    if meta.get("theme") and meta["theme"] not in THEMES: warnings.append(f"unknown theme: {meta['theme']}")
    try:
        if trip.get("startDate") and trip.get("endDate"):
            if date.fromisoformat(trip["endDate"]) < date.fromisoformat(trip["startDate"]): errors.append("trip.endDate precedes trip.startDate")
    except Exception: errors.append("trip dates must be ISO YYYY-MM-DD")
    traveler_ids=set();
    for i,t in enumerate(data.get("travelers") or []):
        tid=t.get("id")
        if not tid: errors.append(f"travelers[{i}].id is required")
        elif tid in traveler_ids: errors.append(f"duplicate traveler id: {tid}")
        else: traveler_ids.add(tid)
    ids=set()
    if isinstance(days,list):
        for di,d in enumerate(days):
            if not d.get("date"): errors.append(f"days[{di}].date is required")
            for ei,e in enumerate(d.get("events") or []):
                eid=e.get("id")
                if not eid: errors.append(f"days[{di}].events[{ei}].id is required")
                elif eid in ids: errors.append(f"duplicate id: {eid}")
                else: ids.add(eid)
                for k in ("start","end"):
                    if e.get(k) and not TIME_RE.match(str(e[k])): warnings.append(f"{eid or f'event {di}/{ei}'} {k} should be HH:MM")
                p=e.get("priority")
                if p and p not in PRIORITIES: warnings.append(f"{eid}: unknown priority {p}")
                loc=e.get("location") or {}
                if "lat" in loc or "lng" in loc:
                    try:
                        lat=float(loc.get("lat")); lng=float(loc.get("lng"))
                        if not -90<=lat<=90 or not -180<=lng<=180: errors.append(f"{eid}: invalid coordinates")
                    except Exception: errors.append(f"{eid}: lat/lng must both be numeric")
                for who in e.get("assignedTo") or []:
                    if traveler_ids and who not in traveler_ids: warnings.append(f"{eid}: unknown traveler {who}")
    for bucket in ("checklists","reminders"):
        for i,item in enumerate(data.get(bucket) or []):
            iid=item.get("id")
            if not iid: errors.append(f"{bucket}[{i}].id is required")
            elif iid in ids: errors.append(f"duplicate id: {iid}")
            else: ids.add(iid)
            for who in item.get("assignedTo") or []:
                if traveler_ids and who not in traveler_ids: warnings.append(f"{iid}: unknown traveler {who}")
    if meta.get("status") not in (None,"draft","approved"): warnings.append("meta.status should be draft or approved")
    if not data.get("disclaimer"): warnings.append("missing disclaimer")
    return errors,warnings

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("json_file"); args=ap.parse_args()
    try: data=load(args.json_file)
    except Exception as e: print(f"ERROR: cannot load JSON: {e}"); return 2
    errors,warnings=validate(data)
    for w in warnings: print("WARNING:",w)
    for e in errors: print("ERROR:",e)
    if errors: print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)"); return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s)"); return 0
if __name__=="__main__": raise SystemExit(main())
