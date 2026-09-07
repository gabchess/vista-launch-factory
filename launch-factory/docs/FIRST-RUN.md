# First run

## Honesty (read first)

v0.1.0 is a **bounded** Augment: Claims Lock + Barry HITL are real doors; slots **1 / 5 / 6** (social video, login animation, in-app popup) are **HOLD stubs** — not review-ready outputs. **A3:** engine is live under product-root `engine/` (schemas + structural validators + adapters). The first **real** adapter is **blog (slot 2)**. When Python is available, structural validate/package helpers in `engine/scripts/` may be used — they never publish. Do not claim a full six-pack ship from this version. **A6:** E2E proof package for mock-gtm-ship slots 2/3/4 exists at `engine/packages/camp_quorum_desk_001/` (fixture; not a live Vista ship).

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
3. **Stop for Barry** on Claims Lock (`barry/claims-lock.md`) before fan-out.
4. **Draft first real** — blog (slot 2) when O1 is HELD (engine adapters under `engine/adapters/`). **Skip / stub** slots 1, 5, 6 — do not block waiting on held slots.
5. **Barry spot-check** that draft (`barry/spot-check.md`) — order is **draft first real → spot-check → remaining adapters** (never spot-check before a draft exists).
6. Remaining non-HELD adapters: email (3), changelog (4). Optional: run `engine/scripts/validate_*.py` when **product-root `engine/` + Python + jsonschema** are available (skill folder alone is not enough).
7. Validate ≤2 loops.
8. Barry pack approve (`barry/pack-approve.md`) → package + honesty note (**name the HOLDs**).

## Do not

- Ask the pack to publish, send, or “just push to HubSpot.”
- Treat Writer output as Barry approval.
- Claim all six outputs are review-ready while 1/5/6 are held.
- Invent fill-ins for held slots to look complete.

See [OPERATE-LAUNCH-FACTORY.md](OPERATE-LAUNCH-FACTORY.md) and [HUMAN-GAPS.md](HUMAN-GAPS.md).
