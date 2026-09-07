# Launch Factory v0.1.0

**Vista Social GTM launch pack.** Release folder in → gated launch package out → Barry HITL.

Spine one-liner: **ingest → retrieve → Claims Lock (Barry once) → adapters (2/3/4 real; 1/5/6 HOLD stubs) → validate ≤2 → Barry pack approve → package + honesty.**

## What it is

An installable Augment for marketers and ops: sticky pack wrapping a factory engine (schemas, validators, adapters). Dual-host doors (Codex skill tree + Claude ZIP). Non-engineer runnable. No auto-publish.

## Package contents

| Path | Role |
|---|---|
| `START-HERE.md` | Install → first ask → Run → Claims Lock → Barry |
| `codex/launch-factory/` | Codex skill (runtime); `schemas/` = thin pointer to engine |
| `claude/` | Claude host door (ZIP present; must not fork engine schemas) |
| `docs/` | Install, operate, trust, limits, honesty |
| `engine/` | **Option B SoT (A3 wired)** — schemas, scripts, adapters, fixtures, barry, honesty |
| `barry/` | **A5 Barry HITL cards** — Claims Lock → spot-check → pack approve (coexists with `engine/barry/` templates) |
| `maintainer-source/` | Maintenance only — **never ship as runtime** |
| `HOST-MATRIX.md` | Verified vs honest unknowns |
| `PROVENANCE.md` / `LICENSE-STATUS.md` | Custody |
| `release-manifest.json` | Integrity list |

Begin with [START-HERE.md](START-HERE.md). Engine run notes: [engine/README.md](engine/README.md).

## Install pointers

- Codex: [docs/INSTALL-CODEX.md](docs/INSTALL-CODEX.md)
- Claude: [docs/INSTALL-CLAUDE.md](docs/INSTALL-CLAUDE.md)

## Version

`0.1.0` — Augment skeleton + **A3 engine wire** (Option B) + **A5 Barry HITL cards** under product-root `barry/`. A7/A8 video/asset tracks HOLD. No auto-publish.
