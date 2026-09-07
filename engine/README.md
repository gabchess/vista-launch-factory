# Engine (Option B — pack source of truth)

**A3 wired.** Launch Factory Augment wraps this sibling `engine/` at product root (Tom Decision A; Option B locked). Augment docs/skill sell **Run + Barry HITL**, not a schema catalog. Schemas here are the correctness spine inside the product — not the Wed hero.

## Canonical layout

```text
engine/
  schemas/     claim_ledger, release_campaign, cadence_binder
  scripts/     validate_ledger, validate_campaign, build_package  (STRUCTURAL_INTEGRITY_ONLY)
  adapters/    six slots (2/3/4 real drafts; 1/5/6 HOLD stubs)
  fixtures/    labelled mock release folders (demo-release, vista-work)
  barry/       Claims Lock + pack-approve templates
  honesty/     still-needs-human.md
  packages/    local build output only — not shipped as engine SoT
```

`codex/launch-factory/schemas/` is a **thin pointer** only — do not fork a second schema set. Claude ZIP must mirror the same SoT (no third tree).

## Pack SoT vs repo-root SHOW-ME spine

| Location | Role |
|---|---|
| **`launch-factory/engine/`** | Pack / Augment **canonical** Option B SoT |
| Repo-root `schemas/`, `scripts/`, `adapters/`, `fixtures/`, `tests/` | Developer **SHOW-ME** spine — keep working until later consolidation |

Root mirrors are intentional for pytest / SHOW-ME.md. Do **not** delete the root spine in A3. Demo packages under repo-root `packages/camp_*` are outputs, not engine SoT.

## How to run (from this directory)

Requires Python 3 + `jsonschema` (see repo-root `requirements.txt` / `.venv`).

```bash
cd launch-factory/engine
# or: source ../../.venv/bin/activate from repo root first

# 1) Validate Claim Ledger (kill-switch)
python scripts/validate_ledger.py fixtures/vista-work/claim_ledger.json

# 2) Validate Release Campaign (six slots exist-or-held)
python scripts/validate_campaign.py fixtures/vista-work/release_campaign.json

# 3) Build Drive-ready package (writes under engine/packages/)
python scripts/build_package.py fixtures/vista-work/release_campaign.json packages
```

`work_root` defaults to `campaign_json.parents[2]` → for `fixtures/vista-work/*.json` that is this `engine/` directory. Adapter paths resolve as `engine/adapters/...`.

Repo-root prove (developer spine, still required):

```bash
cd <repo-root>   # vista/work
pytest -q        # expect 13 passed
```

## Hard stops

- **STRUCTURAL_INTEGRITY_ONLY** — validate / package structure; **no publish**, no HubSpot send, no CMS/social mutate.
- **No invent $** / features / limits / competitive claims.
- **Claims Lock before adapters.** Writer ≠ Barry.
- **Slots 1 / 5 / 6 HOLD** — honesty stubs only. A7/A8 video/asset tracks **HOLD**. Do not claim “all six review-ready.”
- **ADR 0001:** Demo Assets ≠ Claim Ledger evidence.
- **No auto-publish. No Temporal-required.**

## Product wrap

Augment (`START-HERE`, Codex/Claude doors, manifests) is the installable product. This engine is what Run invokes for structural validation when Python is available. Chat-only Runs still obey Claims Lock honesty — structural validators do not replace Barry.
