# Install in Codex

## Package

Skill folder:

`codex/launch-factory`

Engine (Option B SoT, **required for structural validate/package**):

`engine/` at this **product root** (sibling of `codex/`, not inside the skill folder).

## Steps

1. Close any active use of an older `launch-factory` skill if you already tried a draft copy.
2. Copy the **entire** folder `codex/launch-factory` into your Codex skills directory so the installed path ends in `skills/launch-factory`.
3. Preserve the top folder name and **all** nested files. Do **not** copy only `SKILL.md` — `knowledge/`, `manifest.json`, schemas **pointers**, examples, evals, fallbacks, and `scripts/` are part of the skill door.
4. **Keep this product root on disk** (or otherwise keep `engine/` reachable). A skill-only copy does **not** carry `engine/`. Relative pointer `codex/launch-factory/schemas/ → ../../../engine/schemas/` only works while the product tree stays intact.
5. Restart or refresh Codex so it discovers the skill.
6. Start a **fresh** Codex task after installation.
7. Ask: “Use Launch Factory. Run on this release folder.”
8. Confirm the skill identifies itself as **Launch Factory**, begins with ingest / Claims Lock (not a six-output menu), and does **not** offer to publish or send.

Installation paths vary by Codex environment. This package has not been freshly installed into your host during release verification, so discovery and activation remain host-level checks you must perform. Folder visible ≠ Augment active.

If the skill is not found, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## After install — engine vs chat-only

- Read [TRUST-PRIVACY-AND-AUTHORITY.md](TRUST-PRIVACY-AND-AUTHORITY.md) before uploading release materials.
- **With product-root `engine/` reachable + Python + jsonschema:** run structural validators from `engine/scripts/` (`validate_ledger`, `validate_campaign`, `build_package`). **STRUCTURAL_INTEGRITY_ONLY** — they never publish. `codex/launch-factory/schemas/` is a pointer only; do not invent a third schema tree.
- **Without `engine/` (skill-folder-only install):** Run is **chat-only** — gated Claims Lock **draft shape** for Barry. Do **not** invent a path to validators, do **not** claim package-validated output, do **not** invent claims/pricing. Fail closed on structural proof.
- Claims Lock honesty still applies either way — Barry remains the gate.

## Dual-host

Claude door: [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md). Same Claims Lock / Barry / HOLD honesty; identical prose not required. See [HOST-MATRIX.md](../HOST-MATRIX.md).
