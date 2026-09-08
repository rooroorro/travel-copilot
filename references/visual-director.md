# Visual Director workflow

After the itinerary is approved, do not render immediately. Run a visual direction pass.

## 1. Recommend 5–8 destination-aware directions

Each option is a complete visual narrative, not a palette. Explain:
- visual story;
- image language;
- motion language;
- map treatment;
- typography mood;
- optional companion/IP concept;
- intensity and practicality.

Recommendations must derive from destination, season, traveler group, pace, architecture, landscape and nightlife. Do not always show the same presets.

## 2. User selects one direction

Treat the selection as a `visual_lock`. Do not keep asking visual questions unless required.

## 3. Build `creative_brief.json`

It should define:
- `id`, `name`, `tagline`, `visualStory`;
- phase/region themes with palette, texture, atmosphere and preferred imagery;
- `typography`;
- `motion` and `motionStoryboard`;
- `companion` (or `none`);
- `assets` and attribution metadata;
- map behavior;
- visual/motion intensity;
- accessibility and reduced-motion behavior.

## 4. Assets

Use factual photographs for real hotels, restaurants, stations and attractions where recognizability matters. Prefer official sources or appropriately licensed sources such as Wikimedia Commons. Record attribution and license.

Generated/original visuals are best for hero artwork, chapter transitions, ornamental textures and fictional travel companions. Never imply an AI-generated guide is a real person or official guide.

## 5. Motion storyboard

Specify motion as scenes with a communication purpose. Examples:
- origin-to-destination route reveal;
- city-to-nature palette transition;
- scroll-driven route progress;
- chapter title transition;
- current stop emphasis.

Avoid decorative animation that harms readability, battery use or navigation.

## 6. Render

Preferred command when a creative brief exists:

```bash
python scripts/build_visual_html.py trip.json creative_brief.json -o trip.html
```

Fallback to `build_html.py` when no brief exists or visual renderer capability is unavailable.
