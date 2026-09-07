# Host matrix

| Capability | Codex package | Claude package | Grok-crew / leave-behind | Evidence level |
|---|---:|---:|---:|---|
| Skill / pack files included | Yes (`codex/launch-factory/`) | Yes (`claude/launch-factory-v0.2.0.zip`) | N/A for this pack | Package inspection |
| Canonical engine schemas | **Present** at product-root `engine/schemas/` (Option B SoT) | **Not inside ZIP** — same SoT only when product-root `engine/` is kept reachable | Not claimed | A3 files present under `engine/`; ZIP is skill door only |
| Structural helper scripts | **Present** (`engine/scripts/` when product root kept; skill `scripts/` README only) | Same rule — needs product-root `engine/`, not the ZIP alone | Not included | STRUCTURAL_INTEGRITY_ONLY — proven via local Python on product tree; host activation unverified |
| Persistent release-run state | Host and workspace dependent | Project/file dependent | Unknown | Not freshly host-verified |
| CMS, HubSpot, social, or external publishes | Not included | Not included | Not included | Explicit exclusion |
| Auto-send / auto-publish | Not included | Not included | Not included | Explicit exclusion |
| Semantic output parity across hosts | Intended | Intended | Not claimed | Not executed |
| Fresh-host automatic activation | Not proven | Not proven | Not proven | Unverified |
| Slots 1 / 5 / 6 real encode/assets | HOLD | HOLD | HOLD | Documented honesty |

Codex and Claude should preserve the same Claims Lock gate, Barry authority, non-goals, and HOLD honesty. Identical prose is neither required nor expected.

**A3 honesty:** Option B `engine/` is populated in the product tree. Skill-only Codex install or Claude ZIP alone does **not** carry the engine — keep product root (or chat-only Claims Lock draft; fail closed on structural proof). Do **not** invent a third schema tree inside the ZIP. **Honest unknowns:** live host activation and semantic fan-out quality remain **not** verified — folder/ZIP visible ≠ Augment active. A7/A8 HOLD.
