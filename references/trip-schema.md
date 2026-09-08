# Canonical trip.json schema

Use JSON (no comments). Keep IDs stable across revisions.

```json
{
  "meta": {
    "schemaVersion": "1.0",
    "status": "draft|approved",
    "version": "1.0",
    "updatedAt": "2026-09-08T10:00:00+08:00",
    "language": "zh-CN",
    "theme": "cinematic|urban-neon|nature|island|japan-minimal"
  },
  "trip": {
    "title": "东京 5 日旅行",
    "subtitle": "城市漫游与镰仓一日",
    "destination": "Tokyo, Japan",
    "startDate": "2026-10-02",
    "endDate": "2026-10-06",
    "timezone": "Asia/Tokyo",
    "heroImage": "https://...",
    "summary": "..."
  },
  "travelers": [
    {"id":"rolin","name":"Rolin","role":"organizer"},
    {"id":"amy","name":"Amy","role":"traveler"}
  ],
  "bookings": [
    {"id":"flight-out","type":"flight","title":"上海 → 东京","start":"2026-10-02T10:30:00+09:00","fixed":true,"reference":"optional"}
  ],
  "days": [
    {
      "date":"2026-10-02",
      "title":"抵达东京",
      "area":"Shinjuku",
      "tips":["..."],
      "events":[
        {
          "id":"d1-airport-train",
          "start":"14:00",
          "end":"15:10",
          "title":"机场前往酒店",
          "type":"transport",
          "description":"...",
          "location":{"name":"Haneda Airport","address":"...","lat":35.5494,"lng":139.7798},
          "transport":{"mode":"train","durationMin":55,"bufferMin":15},
          "priority":"P0|P1|P2",
          "needsReservation":false,
          "assignedTo":["rolin","amy"],
          "links":{"official":"","booking":""},
          "notes":["..."],
          "image":"https://..."
        }
      ]
    }
  ],
  "checklists": [
    {"id":"passport","title":"护照","category":"documents","assignedTo":["rolin","amy"],"due":"2026-10-01"}
  ],
  "budget": {
    "currency":"CNY",
    "perPerson":[{"category":"住宿","min":4500,"max":7000}],
    "totalMin":14000,
    "totalMax":21000,
    "note":"不含购物"
  },
  "reminders": [
    {
      "id":"airport-leave",
      "title":"出发去机场",
      "datetime":"2026-10-02T07:30:00+08:00",
      "priority":"P0",
      "alarmMinutes":[120,30,10],
      "assignedTo":["rolin","amy"],
      "relatedEventId":"flight-out",
      "description":"建议出门时间；请再次核实实时路况。"
    }
  ],
  "planB": [
    {"id":"rain-d3","trigger":"heavy-rain","forDate":"2026-10-04","replacementEventIds":["museum-a"]}
  ],
  "sources": [
    {"name":"Official site","url":"https://...","checkedAt":"2026-09-08"}
  ],
  "disclaimer":"时刻、票价、营业时间和交通信息可能变化，出发前请以官方渠道为准。"
}
```

## Required minimum

`meta`, `trip.title`, `trip.startDate`, `trip.endDate`, `trip.timezone`, `days[]`, and stable event IDs.

## Time rules

- Day dates: `YYYY-MM-DD`.
- Event display times inside one day may be `HH:MM`.
- Reminders/bookings that cross zones must use offset-aware ISO timestamps.
- Never infer timezone from the renderer machine.

## Shareable-data rule

Do not put passport numbers, payment card data, private IDs, passwords, or unnecessary phone numbers into `trip.json`; the HTML may be forwarded widely.
