# Operate Launch Factory

## Runtime spine

1. **Marketer Run** — point at a release folder.
2. **Ingest + retrieve** — Loom, outline, footage, brand refs.
3. **Voice pack** — Vista voice; not generic LLM tone.
4. **Claims Lock (Barry once)** — every claim traces to source; no invent pricing/features/limits.
5. **Adapters** — see slot map + HELD-skip rule below.
6. **Validate ≤2** — structural / claim ceiling checks; no endless rewrite loops.
7. **Barry pack approve** — copy + creative gate.
8. **Package + honesty** — name HOLDs; HubSpot sandbox email only last and only after Barry + authorized tooling.

WIP=1. Writer ≠ Barry. No Temporal-required. No auto-publish.

## HELD-skip rule (Critiquito)

Slots marked **HOLD** are **skipped for completion**, not blocked forever:

- Do **not** wait on slots 1 / 5 / 6 to finish a Run.
- Emit honesty stubs for HOLDs; continue the spine.
- **First real adapter = blog (slot 2)** when the engine is live, then email (3) and changelog (4).
- Never fake held outputs to look like a six-pack.

## Slot map (v0.1.0)

| Slot | Output | Status | Operate rule |
|---|---|---|---|
| 1 | Social video + burned captions | **HOLD** + honesty stub | HELD-skip |
| 2 | Blog | First real adapter (when engine lands) | **first-real** |
| 3 | Email (segments) | Real adapter when engine lands | After blog |
| 4 | Changelog | Real adapter when engine lands | After blog |
| 5 | Login animation | **HOLD** + honesty stub | HELD-skip |
| 6 | In-app popup | **HOLD** + honesty stub | HELD-skip |

## Engine

Option B: canonical engine lives under `engine/` (import of `vista/work` schemas in later tickets). Skill tree wraps it; do not fork a third schema copy.

## Scripts

Any scripts under `codex/launch-factory/scripts/` are **STRUCTURAL_INTEGRITY_ONLY**. They validate structure; they never publish.
