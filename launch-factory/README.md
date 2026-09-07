# Launch Factory v0.1.0

**Vista Social GTM launch pack.** Release folder in → gated launch package out → Barry HITL.

Spine one-liner: **ingest → retrieve → Claims Lock (Barry once) → adapters (2/3/4 real; 1/5/6 HOLD stubs) → validate ≤2 → Barry pack approve → package + honesty.**

## What it is

An installable Augment for marketers and ops: sticky pack around a factory engine (schemas, validators, adapters). Dual-host doors (Codex skill tree + Claude ZIP in A2). Non-engineer runnable. No auto-publish.

## Package contents

| Path | Role |
|---|---|
| `START-HERE.md` | Install → first ask → Run → Claims Lock → Barry |
| `codex/launch-factory/` | Codex skill (runtime) |
| `claude/` | Claude host door (ZIP arrives in A2) |
| `docs/` | Install, operate, trust, limits, honesty |
| `engine/` | Option B source of truth — wraps future `vista/work` schemas (A1 placeholder) |
| `maintainer-source/` | Maintenance only — **never ship as runtime** |
| `HOST-MATRIX.md` | Verified vs honest unknowns |
| `PROVENANCE.md` / `LICENSE-STATUS.md` | Custody |
| `release-manifest.json` | Integrity list |

Begin with [START-HERE.md](START-HERE.md).

## Install pointers

- Codex: [docs/INSTALL-CODEX.md](docs/INSTALL-CODEX.md)
- Claude: [docs/INSTALL-CLAUDE.md](docs/INSTALL-CLAUDE.md) (stub door until A2 ZIP)

## Version

`0.1.0` — skeleton ship (A1). Engine schemas import and Claude ZIP land in later issues.
