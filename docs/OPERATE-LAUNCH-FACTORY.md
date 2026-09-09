# Operate Launch Factory

## Runtime spine

1. **Marketer Run**: point at a release folder.
2. **Ingest + retrieve**: Loom, outline, footage, brand refs.
3. **Voice pack**: Vista voice; not generic LLM tone.
4. **Claims Lock (Barry once)**: see `barry/claims-lock.md`; every claim traces to source; no invent pricing/features/limits.
5. **Draft first real adapter**: blog (slot 2) when slot 1 is HELD (see HELD-skip). Do not wait on held slots.
6. **Spot-check that artifact**: see `barry/spot-check.md`. Order is **draft first real → Barry spot-check → remaining non-HELD adapters** (never spot-check before a draft exists).
7. **Remaining adapters**: email (3), changelog (4); HELD-skip 1/5/6. See slot map below.
8. **Validate ≤2**: structural / claim ceiling checks; no endless rewrite loops.
9. **Barry pack approve**: see `barry/pack-approve.md`, copy + creative gate.
10. **Package + honesty**: name HOLDs; HubSpot sandbox email only last and only after Barry + authorized tooling.

WIP=1. Drafting ≠ Barry. No Temporal-required. No auto-publish.

## HELD-skip rule

Slots marked **HOLD** are **skipped for completion**, not blocked forever:

- Do **not** wait on slots 1 / 5 / 6 to finish a Run.
- Emit honesty stubs for HOLDs; continue the spine.
- **First real adapter = blog (slot 2)** when the engine is live, then email (3) and changelog (4).
- Never fake held outputs to look like a six-pack.

## Slot map (v0.2.0)

Slot 7 is the **Campaign Plan** (ADR 0016): the day-by-day multi-channel sequence drafted from the same locked claims; `cadence_binder.json` is its data shape.

| Slot | Output | Status | Operate rule |
|---|---|---|---|
| 1 | Social video + burned captions | **HOLD** + honesty stub | HELD-skip |
| 2 | Blog | First real adapter (when engine lands) | **first-real** |
| 3 | Email (segments) | Real adapter when engine lands | After blog |
| 4 | Changelog | Real adapter when engine lands | After blog |
| 5 | Login animation | **HOLD** + honesty stub | HELD-skip |
| 6 | In-app popup | **HOLD** + honesty stub | HELD-skip |
| 7 | Campaign Plan | Adapter `07_campaign_plan.md` | One-release cells only; approved in pack gate |

## Engine

Option B: canonical engine lives under `engine/` (import of `vista/work` schemas in later tickets). Skill tree wraps it; do not fork a third schema copy.

## Scripts

All executable helpers live under `engine/scripts/` (`init_release`, `validate_record`, `transition_slot`, `validate_ledger`, `validate_campaign`, `build_package`) and are **STRUCTURAL_INTEGRITY_ONLY**: they validate structure; they never publish, and `approved`/`packaged` states require Barry's recorded decision (`--human-confirmed`). The one-command door is `./run.sh RELEASE_FOLDER` (ADR 0014). Any scripts under `codex/launch-factory/scripts/` follow the same rule.
