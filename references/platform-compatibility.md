# Platform compatibility

The skill must never require a specific vendor feature to work.

## Capability detection

1. **File read available** -> parse user PDF/docs/images with the platform's native tools.
2. **No direct file read but local shell/Python available** -> extract text using installed local libraries if safe and appropriate.
3. **Neither available** -> ask the user to paste/export text; do not claim the file was read.

## Script execution

- Claude Code / Codex / WorkBuddy with local execution: run the Python renderer/validator directly.
- Agent can create files but not execute: generate `trip.json`, then reproduce renderer output only if the environment supports deterministic file generation.
- Chat-only agent: provide the canonical `trip.json` and explain that a file-capable environment is needed for the packaged HTML.

## Web research

Use the platform's web/search tools when available. If unavailable, label volatile facts as unverified rather than fabricating them.

## Platform adapters

Do not fork the domain logic. If a platform needs special install instructions, keep that in README/adapter documentation, not in the canonical schema or renderer.
