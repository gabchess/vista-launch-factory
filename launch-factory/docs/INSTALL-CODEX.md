# Install in Codex

## Package

Use the folder:

`codex/launch-factory`

## Steps

1. Close any active use of an older `launch-factory` skill if you already tried a draft copy.
2. Copy the **entire** folder `codex/launch-factory` into your Codex skills directory so the installed path ends in `skills/launch-factory`.
3. Preserve the top folder name and **all** nested files. Do **not** copy only `SKILL.md` — `knowledge/`, `manifest.json`, schemas pointers, examples, evals, fallbacks, and `scripts/` are part of the product.
4. Restart or refresh Codex so it discovers the skill.
5. Start a **fresh** Codex task after installation.
6. Ask: “Use Launch Factory. Run on this release folder.”
7. Confirm the skill identifies itself as **Launch Factory**, begins with ingest / Claims Lock (not a six-output menu), and does **not** offer to publish or send.

Installation paths vary by Codex environment. This package has not been freshly installed into your host during release verification, so discovery and activation remain host-level checks you must perform. Folder visible ≠ Augment active.

If the skill is not found, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## After install

- Read [TRUST-PRIVACY-AND-AUTHORITY.md](TRUST-PRIVACY-AND-AUTHORITY.md) before uploading release materials.
- Engine SoT is Option B under `../../engine/` (sibling of `codex/`) — schemas import lands in later tickets; do not invent a third schema tree.
- Any scripts under `codex/launch-factory/scripts/` are **STRUCTURAL_INTEGRITY_ONLY** — they never publish.

## Dual-host

Claude door: [INSTALL-CLAUDE.md](INSTALL-CLAUDE.md). Same Claims Lock / Barry / HOLD honesty; identical prose not required. See [HOST-MATRIX.md](../HOST-MATRIX.md).
