# First run

## Honesty (read first)

v0.1.0 is a **bounded** Augment: Claims Lock + Barry HITL are real doors; slots **1 / 5 / 6** (social video, login animation, in-app popup) are **HOLD stubs** — not review-ready outputs. **A3:** engine is live under product-root `engine/` (schemas + structural validators + adapters). The first **real** adapter is **blog (slot 2)**. When Python is available, structural validate/package helpers in `engine/scripts/` may be used — they never publish. Do not claim a full six-pack ship from this version.

## Goal

Complete one gated Run that ends in a **Claims Lock draft for Barry**, not a published launch.

## Preconditions

- Skill installed ([INSTALL-CODEX.md](INSTALL-CODEX.md) or [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md)).
- One release folder with Loom / outline / footage (or labelled fixture).
- You accept HOLD honesty for slots 1 / 5 / 6.

## First ask

> Use Launch Factory. Run on this release folder.

## Expected flow

1. Ingest / retrieve from the folder.
2. Draft Claims Lock (traceable claims only — no invent pricing/features).
3. **Stop for Barry** on Claims Lock before fan-out.
4. After Barry lock: **first real adapter = blog (slot 2)** (engine adapters live under `engine/adapters/`); then email (3) and changelog (4). **Skip / stub** slots 1, 5, 6 (HELD) — do not block the Run waiting on held slots. Optional: run `engine/scripts/validate_*.py` when **product-root `engine/` + Python + jsonschema** are available (skill folder alone is not enough).
5. Validate ≤2 loops.
6. Barry pack approve → package + honesty note (**name the HOLDs**).

## Do not

- Ask the pack to publish, send, or “just push to HubSpot.”
- Treat Writer output as Barry approval.
- Claim all six outputs are review-ready while 1/5/6 are held.
- Invent fill-ins for held slots to look complete.

See [OPERATE-LAUNCH-FACTORY.md](OPERATE-LAUNCH-FACTORY.md) and [HUMAN-GAPS.md](HUMAN-GAPS.md).
