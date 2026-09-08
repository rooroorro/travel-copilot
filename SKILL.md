---
name: travel-copilot
description: Turn a rough travel idea or an existing itinerary from text/PDF/images/files into a reviewed, complete, structured trip plan and then package the user-approved plan as a mobile-first interactive single-file HTML travel companion plus optional ICS calendar reminders. Use for trip planning, itinerary audit/completion, travel-plan visualization, interactive travel HTML, offline-friendly trip pages, group travel handoff, and reminder installation. Platform-agnostic: works with Claude Code, Codex, WorkBuddy and other agents that can read SKILL.md; use capability fallbacks when file reading, web research, or script execution is unavailable.
license: MIT
compatibility: Python 3.9+ recommended for deterministic renderer/ICS/validation; browser output uses vanilla HTML/CSS/JS and optional online Leaflet tiles.
metadata:
  version: "1.1.0"
  architecture: "agent-agnostic-trip-json-renderer"
---

# Travel Copilot

Build a trip **with** the user, audit it for practical gaps, wait for explicit approval, then package the frozen plan into a polished interactive travel companion.

The product is not merely an itinerary generator. It is an **execution pack**: structured trip data, an interactive HTML, and reminders the traveler can install into their own phone calendar.

## Use When

Use this skill when the user wants any of the following:

- Plan a trip from destination/dates/preferences.
- Upload or provide an existing trip plan and ask to organize, review, complete, improve, or visualize it.
- Turn a PDF, Word document, spreadsheet, screenshots, notes, chat logs, or old itinerary into a travel plan.
- Generate an interactive, mobile-first travel HTML that can be sent to friends.
- Create traveler-specific calendar reminders from a trip.
- Continue editing a prior Travel Copilot HTML or `trip.json`.

## Don't Use When

- The user only asks one isolated travel fact and does not want a trip plan.
- The user asks you to book or purchase travel services unless another authorized tool explicitly supports that action.
- The user asks for a background reminder service or guaranteed push/phone calls. A static HTML cannot reliably run after the browser is closed; this skill installs reminders into the phone calendar instead.

## Core Architecture

Treat the agent/model as the **planner and auditor**, not the web designer.

All platforms converge on one canonical artifact:

`trip.json -> deterministic renderer -> trip.html + optional .ics`

Do not let each agent freely invent a different web stack. The renderer owns the visual system and interaction contract.

Read these references when relevant:

- `references/trip-schema.md` — canonical `trip.json` data model.
- `references/planning-audit.md` — completeness audit and approval workflow.
- `references/research-guide.md` — current-data research and uncertainty rules.
- `references/reminder-system.md` — reminder priorities and traveler personalization.
- `references/visual-system.md` — baseline themes, motion, map-story interaction.
- `references/visual-director.md` — post-approval style recommendation, creative brief and visual lock workflow.
- `references/platform-compatibility.md` — Claude/Codex/WorkBuddy/other-agent fallbacks.

## Workflow

### 1. Ingest

Accept either:

- **Mode A — plan from scratch:** destination, dates/duration, travelers, interests, pace, budget constraints, must-do items.
- **Mode B — existing plan:** text, file, PDF, images, spreadsheet, screenshots, old HTML, or old `trip.json`.

If the environment can read the supplied file, read it directly. If not, use the fallback in `references/platform-compatibility.md` rather than pretending the file was parsed.

When reading an older Travel Copilot HTML, prefer extracting `<script id="trip-data" type="application/json">` instead of scraping the rendered DOM.

### 2. Normalize before advising

Convert the information into a draft matching `references/trip-schema.md`.

Preserve user-decided facts exactly where possible. Mark uncertain or inferred items explicitly in working notes. Never silently overwrite the user's reservations or fixed commitments.

### 3. Audit the trip

Read `references/planning-audit.md` and inspect for practical gaps such as:

- airport/station departure buffer;
- missing point-to-point transport;
- impossible or overly tight transitions;
- check-in/check-out timing;
- reservation/ticket deadlines;
- weather/season dependency;
- meal gaps when relevant;
- missing addresses/coordinates/navigation targets;
- arrival/departure-day blind spots;
- group responsibilities;
- backup options for fragile outdoor blocks.

Give the user a concise audit. Prioritize material issues; do not manufacture problems just to look helpful.

### 4. Discuss and iterate

Resolve material gaps through conversation. The user owns trade-offs.

Do **not** render the final HTML while the plan is still materially unsettled unless the user explicitly asks for a draft preview.

### 5. Freeze the approved plan

Only after the user clearly approves/finalizes the itinerary:

1. Produce canonical `trip.json`.
2. Set `meta.status` to `approved`.
3. Set a version such as `1.0` and `updatedAt`.
4. Validate it:

```bash
python scripts/validate_trip.py trip.json
```

Fix errors before rendering.

### 6. Visual Director

Before rendering, read `references/visual-director.md`. Recommend 5–8 destination-aware complete visual directions. After the user selects one, create and freeze `creative_brief.json`. A visual choice is a narrative system, not merely a color preset.

When a visual brief exists, it controls imagery, phase-based palette changes, companion/IP, motion storyboard, map treatment and attribution.

### 7. Render the interactive HTML

Preferred deterministic route:

```bash
python scripts/build_visual_html.py trip.json creative_brief.json -o trip.html
```

Fallback when no brief exists:

```bash
python scripts/build_html.py trip.json -o trip.html
```

The output must be a single self-contained HTML for core content and interactions. Internet-dependent map tiles/photos must fail gracefully; the itinerary text, timing, checklists, local completion state, traveler selector, and ICS reminder generator must still work.

The renderer provides:

- cinematic hero and destination-aware theme;
- horizontal day selector;
- daily timeline;
- "now / next" execution card based on device time;
- expandable activity cards;
- local `localStorage` completion/checklist state;
- optional interactive Leaflet/OSM map loaded only when online;
- scroll-driven map focus for itinerary stops;
- Apple/Google/Amap navigation links as appropriate;
- traveler selector;
- local reminder installer that generates a personalized `.ics` file in the browser;
- reduced-motion accessibility mode;
- embedded canonical `trip-data` JSON for future edits.

### 8. Generate a prebuilt ICS when useful

For a known traveler or for convenience:

```bash
python scripts/build_ics.py trip.json -o trip-reminders.ics
```

If multiple travelers exist, pass `--traveler <id>` to personalize responsibilities/reminders.

A static HTML cannot promise reliable alarms by itself after closure. Calendar reminders are delegated to the user's phone calendar after import.

### 9. Package

Optionally run:

```bash
python scripts/package_trip.py trip.json --out-dir output
```

This produces the HTML, a generic ICS, a copy of `trip.json`, and a short usage note.

### 10. Hand off clearly

Tell the user:

- open the HTML on mobile or desktop;
- send the same HTML to companions;
- each companion chooses their identity and installs their own reminders from inside the page;
- completed-state/checklist state is local to each device;
- if the plan changes after reminders were imported, re-export/import the new reminder version;
- time-sensitive facts should still be checked through official sources.

## Rules

1. **Approval gate:** do not treat an inferred draft as final.
2. **Data first:** `trip.json` is the source of truth; HTML is a rendering.
3. **No false background claims:** local HTML cannot guarantee notifications after it is closed.
4. **No hidden rewrites:** preserve fixed bookings and user decisions unless they approve changes.
5. **Current facts:** use current official/high-quality sources where time-sensitive accuracy matters; record uncertainty.
6. **Offline-first core:** map/photo failure must not hide itinerary content.
7. **Mobile first:** design for one-handed phone use before desktop layout.
8. **Motion with restraint:** motion should communicate location/time/state, not become decorative noise.
9. **Traveler privacy:** do not embed unnecessary phone numbers, IDs, booking secrets, or sensitive personal data in a shareable HTML.
10. **Cross-agent portability:** platform-specific tools are enhancements, never required dependencies.

## Examples

### Existing PDF

User: "这是旅行社给我的 PDF，先帮我看看还有没有遗漏，我们聊好以后再生成网页。"

Action: parse if supported -> normalize -> audit -> discuss -> wait for approval -> render.

### Rough idea

User: "国庆三个人去成都四天，节奏轻松，熊猫基地必须去。"

Action: plan -> research current practical constraints -> audit -> iterate -> approval -> `trip.json` -> HTML + reminders.

### Continue an old page

User: "把这个 HTML 的第三天下午换成室内行程。"

Action: extract `trip-data` -> edit structured data -> bump version -> validate -> re-render; warn that previously imported ICS is stale.

## Edge Cases

- No coordinates: render text/navigation search links and omit map pins rather than invent coordinates.
- No internet in the browser: show route list and addresses; do not show broken map containers as if functional.
- Different time zones: every trip/event should carry a trip timezone; do not calculate reminders using the agent machine timezone by accident.
- All-day or vague events: do not invent minute-level timing unless the user accepts it.
- Very large trips: keep all data, but group the UI by day/region and lazy-render optional media.
- Browser blocks downloads from local file: show the ICS text fallback and explain how to save/import it.

## References

- `references/trip-schema.md`
- `references/planning-audit.md`
- `references/research-guide.md`
- `references/reminder-system.md`
- `references/visual-system.md`
- `references/visual-director.md`
- `references/platform-compatibility.md`
