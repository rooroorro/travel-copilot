# Reminder system

A shareable static HTML is **not** a reliable background alarm service. Its job is to generate/install reminders into a real calendar.

## Priority levels

- **P0 critical:** flight/train/departure, timed ticket, hard reservation, check-out or meeting whose miss has high cost.
- **P1 important:** hotel check-in, restaurant, rental pickup, group meetup, time-sensitive transfer.
- **P2 normal:** sightseeing, flexible meals, shopping, walks.

Suggested alarms when the trip does not specify them:

- P0: 120, 30, 10 minutes before.
- P1: 60, 20 minutes before.
- P2: 15 minutes before or none.

Do not create noisy reminders for every flexible event by default.

## Traveler personalization

Each reminder/checklist may contain `assignedTo`. In the HTML, the companion selects their traveler identity; export only relevant assigned reminders plus group-wide items.

If `assignedTo` is absent/empty, treat the item as group-wide.

## Versioning

ICS import is a snapshot, not live synchronization. The HTML must show the itinerary version and warn users to re-export reminders after material schedule changes.

Use stable ICS UIDs derived from trip/event IDs so re-importing is less chaotic across calendar clients.
