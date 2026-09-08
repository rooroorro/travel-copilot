# Visual and interaction system

The page should feel like a small travel app, not a brochure or admin dashboard.

## Signature interaction

The core signature is **scroll-driven map story**:

1. User scrolls the daily timeline.
2. The current stop card becomes active.
3. The map focuses that stop and highlights the route segment.
4. The “Now / Next” card stays useful for execution.

## Themes

- `cinematic`: high-contrast hero, glass cards, restrained ambient motion.
- `urban-neon`: dark city/night palette, subtle luminous route line.
- `nature`: large imagery, earthy surfaces, soft depth/parallax.
- `island`: airy layout, water-like gradients, bright surfaces.
- `japan-minimal`: whitespace, fine borders, quiet typography, minimal motion.

## Motion rules

Use CSS/vanilla JS first. Motion should communicate:

- reveal/entry;
- day switching;
- route progress;
- selected/current stop;
- completion state.

Avoid constant particles everywhere. Respect `prefers-reduced-motion`.

## Mobile rules

- one-handed controls;
- large tap targets;
- sticky bottom/compact navigation where useful;
- day selector via horizontal scroll/scroll-snap;
- no hover-only critical interactions;
- fast first paint and graceful offline fallback.

## External libraries

Optional enhancements (not dependencies) can include Anime.js, Lenis, Swiper, Atropos, or MapLibre when an environment/project can bundle them reliably. The default renderer uses vanilla CSS/JS + optional Leaflet CDN so the skill remains portable.

## Visual Director mode (v1.1+)

The fixed theme presets above are fallbacks. For a user-approved trip, prefer the destination-aware Visual Director workflow in `visual-director.md`: recommend 5–8 complete narratives, freeze the user's choice as `creative_brief.json`, and render with phase-aware palettes, imagery, map treatment, companion/IP and motion storyboard.
