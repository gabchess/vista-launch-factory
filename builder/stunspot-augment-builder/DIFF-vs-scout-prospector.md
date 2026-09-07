# Diff — Scout & Prospector vs Victor bar (B1-ready)

**For:** stunspot-augment-builder / vista-launch-factory#28  
**Lock:** Strict Victor skeleton. Scout = nearest house reference. Prospector = **negative** (do not use as Augment shape).  
**Source scorecard:** `vista/gaps-past-augments-vs-victor.md` (Nova locks 2026-09-07)

---

## Presence table

| Finished-pack element | Victor v0.1.3 | Scout | Prospector | Builder action |
|---|---|---|---|---|
| START-HERE (install + non-goals) | Yes | Yes (strong) | **No** (README only) | Require Victor-shaped START-HERE |
| Dual host (Claude ZIP + Codex skill) | Yes | Partial | Thin (onboard skill) | Require full dual-host |
| HOST-MATRIX | Yes | **No** | **No** | **Add** |
| PROVENANCE | Yes | Soft | Soft | **Add** dedicated file |
| LICENSE-STATUS (separate) | Yes | LICENSE.md only | LICENSE.md only | **Add** status doc |
| release-manifest (+ hashes) | Yes | Yes (RELEASE-MANIFEST + SHA256) | **No** | Require Victor-shaped manifest |
| documentation-manifest | Yes | **No** | **No** | **Add** |
| OPERATE / FIRST-READ / TROUBLESHOOT / RECOVERY | Yes (suite) | Partial (SUPPORT, WHAT-BROKE) | **No** | Expand to named suite |
| TRUST + VALIDATION-AND-LIMITS | Yes | Partial | Soft | Require pair |
| capability-and-authority.md | Yes (knowledge/) | Split authz | README/comments | **Require** in knowledge/ |
| Claim ceilings ≥3 surfaces | Yes (six places) | CLAIMS.md + START-HERE | No table | Lockstep six HITL places |
| Examples + evals + fallbacks | Yes | evals; fallbacks unclear | **No** | Require interior depth |
| maintainer-source ≠ runtime | Yes | Mixed repo | App = repo | Enforce split |
| First-ask ritual | Yes | Tool examples | `/onboard` | One memorable ask on START-HERE |
| Feels like shippable Augment | **Yes** | **Close** | **No** | Envelope = product |

**Ranking:** Victor = finished Augment. Scout = nearest house pack. Prospector = useful pipeline repo, **not** Stunspot-shaped.

---

## Scout — last mile (keep / add)

| Keep | Add / clarify |
|---|---|
| START-HERE, CLAIMS.md honesty, install doors, RELEASE-MANIFEST + SHA256, evals | HOST-MATRIX, PROVENANCE, LICENSE-STATUS, documentation-manifest |
| Dual-host intent | Claude one-root ZIP parity + Codex full tree as Victor |
| SUPPORT / WHAT-BROKE | Map or rename into OPERATE / FIRST-READ / TROUBLESHOOTING / RECOVERY |
| — | fallbacks + maintainer vs runtime layout |
| — | capability-and-authority + TRUST/VALIDATION lockstep with CLAIMS |

## Prospector — negative only

| Do | Don’t |
|---|---|
| Keep strong product-narrative tone if later wrapped | Use repo/app/MCP layout as Augment topology |
| Move HITL into START-HERE + SKILL + TRUST if ever retrofitted | Treat README gates as finished claim discipline |
| — | Retrofit as pack shape this week |

## Launch Factory implication (one-liner)

Copy **Victor skeleton** around the engine; use Scout as honesty/install reference; **never** shape after Prospector. Finished = install → operate → authority → custody — not schemas-green.

---

## B1 attach note

This file is the scout/prospector diff artifact for B1 ship. Optional follow-up: path-level column against live `gabchess/scout-portfolio-manager` and `gabchess/prospector` @ main (not required to draft B0).
