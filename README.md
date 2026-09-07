# Launch Factory v0.2.0

**Vista Social GTM launch pack.** Release folder in → gated launch package out → Barry HITL. Nothing auto-publishes.

## Agent install door (AI agents: start here)

You are an AI agent asked to install this Augment. Do this:

1. Read [START-HERE.md](START-HERE.md) for what this pack is and is not.
2. Install for your host:
   - **Codex / file-based skill hosts:** copy the entire `codex/launch-factory/` folder into your host skills directory so the installed path ends in `skills/launch-factory`. Keep this repo root reachable — `engine/` (schemas, validators, adapters) is the source of truth and does not live inside the skill folder.
   - **Claude / ZIP hosts:** unzip `claude/launch-factory-v0.2.0.zip` to a single root per your host's skill/project convention. The ZIP is a skill door only; keep `engine/` reachable for structural validation, or run chat-only (fail closed) per `codex/launch-factory/fallbacks/degraded-capability.md`.
3. Verify: in a fresh session ask *"Use Launch Factory. Run on this release folder."* The skill must identify itself as **Launch Factory**, route to ingest → Claims Lock (never a menu of specialists), and refuse to publish or send. Folder visible ≠ Augment active until the host binds it.

Honesty: live-host activation is not freshly verified — see [HOST-MATRIX.md](HOST-MATRIX.md).

## What it is

One launch-ops operator (never a panel): a sticky Augment wrapping a factory engine (schemas, validators, adapters, one release record). One visible loop — Ingest → Ground → Claims Lock (Barry once) → Create → Review → Package → Learn. Dual-host doors (Codex skill tree + Claude ZIP). Non-engineer runnable via `./run.sh RELEASE_FOLDER`. No auto-publish.

Spine one-liner: **ingest → ground (facts + Voice Bank brief) → Claims Lock (Barry once) → adapters (2/3/4 real + Campaign Plan; 1/5/6 HOLD stubs) → validate ≤2 → Barry pack approve → package + honesty.**

## Repo layout (repo root IS the install door — ADR 0012)

| Path | Role |
|---|---|
| `START-HERE.md` | Install → first ask → Run → Claims Lock → Barry |
| `codex/launch-factory/` | Codex skill (runtime); `schemas/` = thin pointer to engine |
| `claude/` | Claude host door (ZIP; must not fork engine schemas) |
| `docs/` | Install, operate, trust, limits, honesty + CONTEXT/ADRs |
| `engine/` | **Option B single SoT** — schemas, scripts, adapters, fixtures, barry-templates, honesty |
| `barry/` | **Human Barry HITL cards** — Claims Lock → spot-check → pack approve |
| `scripts/regen_manifests.py` | Manifest regeneration (STRUCTURAL_INTEGRITY_ONLY) |
| `voice-bank/` | Interim voice corpus plan (ADR 0015) |
| `runs/` | Per-release workspaces (`release-record.json`) — run output, gitignored |
| `packages/` | Built review packs — run output |
| `maintainer-source/` | Maintenance only — **never ship as runtime** |
| `run.sh` | One-command door (ADR 0014) |
| `HOST-MATRIX.md` | Verified vs honest unknowns |
| `PROVENANCE.md` / `LICENSE-STATUS.md` | Custody |
| `release-manifest.json` / `documentation-manifest.json` | Integrity lists |

Begin with [START-HERE.md](START-HERE.md). Engine run notes: [engine/README.md](engine/README.md). Developer ELI5: [SHOW-ME.md](SHOW-ME.md).

## Quick start (engine)

```bash
cd <repo-root>
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   # once

# One-command door (ADR 0014)
./run.sh engine/fixtures/demo-release

# Or stage by stage
.venv/bin/python engine/scripts/init_release.py engine/fixtures/demo-release
.venv/bin/python engine/scripts/validate_ledger.py engine/fixtures/demo-release/claim_ledger.json
.venv/bin/python engine/scripts/validate_campaign.py engine/fixtures/demo-release/release_campaign.json
.venv/bin/python engine/scripts/build_package.py engine/fixtures/demo-release/release_campaign.json packages --work-root engine

.venv/bin/pytest -q    # expect 22 passed
```

## Install pointers

- Codex: [docs/INSTALL-CODEX.md](docs/INSTALL-CODEX.md)
- Claude: [docs/INSTALL-CLAUDE.md](docs/INSTALL-CLAUDE.md)

## Hard stops

1. **No inventing claims** — every allowed claim needs an evidence span; forbidden list is law.
2. **No auto-publish / auto-send** — packages end at review-ready; humans publish out of band.
3. **No HubSpot send** from this tree — sandbox draft-only, after Barry, with authorized tooling.
4. **No pricing invent** — no seats, plan $, or dollar-savings claims.
5. **Slots 1/5/6 HOLD** until the spine ships (ADR 0013) — never claim "all six review-ready."
6. **Barry WIP=1** — the writer seat is never Barry; `approved`/`packaged` require a recorded human decision.
7. **Do not git push** until Gabe says the Forge/review remote is ready.

## Language

See `docs/CONTEXT.md` (Launch Factory, Release Campaign, Claim Ledger, Claims Lock, Adapter, Campaign Plan, Voice Bank, Run Log, Release Record, Barry, Held, Kill-switch, Honesty Doc).

## Version

`0.2.0` — repo-root install door (ADR 0012), one release record + loop-shaped skill, Campaign Plan as slot 7 (ADR 0016), interim Voice Bank (ADR 0015), `run.sh` one-command door (ADR 0014). History: [CHANGELOG.md](CHANGELOG.md).
