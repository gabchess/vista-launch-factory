# Vista Launch Factory — working tree

Turns **one Vista feature-release folder** into **six review-ready launch artifacts** plus a **one-release cadence binder**, with **Barry** as the only copy/creative ship gate.

This is the executable factory repo (schemas, validators, adapters, fixtures, package builder). It is **not** a prompt pack and **not** an auto-publisher.

## What lives here

| Path | Role |
|---|---|
| `schemas/` | Claim Ledger, Release Campaign, Cadence Binder JSON Schema |
| `scripts/validate_ledger.py` | Evidence spans + forbidden list + kill-switch |
| `scripts/validate_campaign.py` | Six slots exist-or-held; Barry WIP=1 |
| `scripts/build_package.py` | Drive-ready package folder (`auto_publish: false`) |
| `adapters/` | Slot drafts (claims-only). Held slots stay cold. |
| `fixtures/demo-release/` | Labelled fixture (`FEATURE_NAME`) for rehearsal |
| `fixtures/vista-work/` | Wed hero seed: Barry email + outline → `camp_vista_work_001` |
| `packages/` | Built review packs (committed for Gabe review) |
| `honesty/` | Still-needs-human table shipped with every package |
| `docs/` | DESIGN-LOCK, GRILL-LOCK, CONTEXT, design + plan copies |
| `SHOW-ME.md` | ELI5 end-to-end + re-run commands |

## Quick start

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
python -m venv .venv && source .venv/bin/activate   # once
pip install -r requirements.txt                     # once

# Fixture rehearsal
python scripts/validate_ledger.py fixtures/demo-release/claim_ledger.json
python scripts/validate_campaign.py fixtures/demo-release/release_campaign.json
python scripts/build_package.py fixtures/demo-release/release_campaign.json packages

# Vista Work Wed hero (NO video)
python scripts/validate_ledger.py fixtures/vista-work/claim_ledger.json
python scripts/validate_campaign.py fixtures/vista-work/release_campaign.json
python scripts/build_package.py fixtures/vista-work/release_campaign.json packages
# --work-root . if fixture nesting ever differs from fixtures/<name>/file.json

pytest -q
```

## Hard stops

1. **No inventing claims** — every allowed claim needs an evidence span; forbidden list is law.
2. **No auto-publish** — package ends at review-ready; humans publish out of band.
3. **No HubSpot send** from this tree — sandbox draft-only, after Barry, later.
4. **No pricing invent** — no seats, plan $, or dollar-savings claims.
5. **No video encode** for `camp_vista_work_001` — slots 1/5/6 held; Demo Assets ≠ Claim Ledger.
6. **Barry WIP=1** — Writer is never the Barry seat.
7. **Do not git push** until Gabe says Forge/review remote is ready.

## Campaign status (camp_vista_work_001)

- Slots **2 / 3 / 4** review drafts from polished demo adapters.
- Slots **1 / 5 / 6** HELD (no real footage / Lottie / popup source).
- Campaign status: `claims_gate` (Claims Lock not recorded).
- MANIFEST status: `review_ready_pre_claims_lock` (honest pre-Claims-Lock review bundle; not `packaged`).
- Package root includes filled `BARRY.md` review card.
- Video/demo recording: **PAUSED**.

## Language

See `docs/CONTEXT.md` (Launch Factory, Claim Ledger, Claims Lock, Adapter, Held, Kill-switch, Honesty Doc, Demo Asset).
