# Install in Claude

## Package

Use the ZIP:

`claude/launch-factory-v0.1.0.zip`

(one-root zip; same skill payload intent as `codex/launch-factory`)

## Steps

1. Close any older Launch Factory project/skill copy in the workspace if present.
2. Download or locate `claude/launch-factory-v0.1.0.zip` from this product root.
3. Install per Claude’s project / skill ZIP convention for your workspace (unzip to a single root; do not scatter nested skill files).
4. Confirm the Augment loads in a **fresh** chat/project. Folder visible ≠ Augment active until the host binds it.
5. Ask: “Use Launch Factory. Run on this release folder.”
6. Confirm it identifies as **Launch Factory**, routes to Claims Lock before fan-out, and refuses publish/send.

This package was statically packed for dual-host parity. Live Claude activation was **not** freshly verified in this release — treat activation as a host-level check. See [HOST-MATRIX.md](../HOST-MATRIX.md).

If install fails, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Prefer [INSTALL-CODEX.md](INSTALL-CODEX.md) when your host is Codex.

## After install

- Read [TRUST-PRIVACY-AND-AUTHORITY.md](TRUST-PRIVACY-AND-AUTHORITY.md) before uploading release materials.
- Same Barry / no auto-publish / slots 1·5·6 HOLD honesty as Codex.
