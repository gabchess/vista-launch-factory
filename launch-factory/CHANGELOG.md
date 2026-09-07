# Changelog

## 0.1.0 — 2026-09-07

### A5 — Barry HITL cards (product-root `barry/`)

- Critiquito Important nit: OPERATE/FIRST-RUN/barry clarify draft first real then spot-check then remaining; product-root `barry/` vs `engine/barry/` humans-vs-templates line.
- Human card pack: `barry/README.md`, `claims-lock.md`, `spot-check.md`, `pack-approve.md` (three gates in order).
- Docs/skill aligned: START-HERE, FIRST-RUN, OPERATE, SKILL, capability-and-authority, TRUST, VALIDATION point at `barry/` gates.
- Locks: WIP=1; Writer≠Barry; Slack thumbs ≠ approve; no invent $; no auto-publish; no HubSpot before pack approve; HOLD 1/5/6 HELD-skip; first real spot-check = blog.
- Coexists with `engine/barry/` templates from A3; does not delete or replace engine templates.

### A3 — Wire factory engine (Option B)

- Import live factory spine into `launch-factory/engine/`: schemas, scripts (`validate_ledger`, `validate_campaign`, `build_package`), adapters, fixtures, barry templates, honesty note.
- Option B locked: sibling `engine/` is pack SoT; `codex/launch-factory/schemas/` is thin pointer only — no third divergent schema tree.
- Docs/skill/HOST-MATRIX/START-HERE/FIRST-RUN/INSTALL-CODEX updated: engine present; Run may use structural validators when Python available; Claims Lock honesty retained; A7/A8 HOLD.
- Repo-root SHOW-ME spine kept working (pytest). Pack SoT documented as `engine/`; root mirrors until consolidation.
- No auto-publish; no HubSpot send; no invent $; slots 1/5/6 HOLD; ADR 0001 preserved.

### A1 / A2 (prior)

- First Launch Factory Augment **skeleton** ship (A1 / gabchess/vista-launch-factory#15).
- Strict finished-pack envelope around factory engine Option B (`engine/` sibling placeholder → now wired in A3).
- Customer docs: START-HERE, dual-host install doors, FIRST-RUN, OPERATE, TRUST, VALIDATION, TROUBLESHOOTING, HUMAN-GAPS.
- Codex skill stub: SKILL, README claim ceiling, capability-and-authority, structural scripts note.
- HITL locks aligned: Barry Claims Lock; no auto-publish; no invent pricing; slots 1/5/6 HOLD honesty stubs.
- Claude host ZIP door (A2).
