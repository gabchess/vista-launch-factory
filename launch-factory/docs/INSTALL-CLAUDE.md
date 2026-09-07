# Install in Claude

## Package

Skill ZIP (host door):

`claude/launch-factory-v0.1.0.zip`

(one-root zip; mirrors `codex/launch-factory` skill payload — **not** the Option B `engine/` tree)

Engine SoT (structural validate/package):

`engine/` at this **product root**. Keep it reachable after install, same rule as Codex.

## Steps

1. Close any older Launch Factory project/skill copy in the workspace if present.
2. Download or locate `claude/launch-factory-v0.1.0.zip` from this product root.
3. Install per Claude’s project / skill ZIP convention for your workspace (unzip to a single root; do not scatter nested skill files).
4. Confirm the Augment loads in a **fresh** chat/project. Folder visible ≠ Augment active until the host binds it.
5. Ask: “Use Launch Factory. Run on this release folder.”
6. Confirm it identifies as **Launch Factory**, routes to Claims Lock before fan-out, and refuses publish/send.

This ZIP was statically packed for dual-host **skill-door** parity. It does **not** vendor `engine/`. Live Claude activation was **not** freshly verified — treat activation as a host-level check. See [HOST-MATRIX.md](../HOST-MATRIX.md).

If install fails, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md). Prefer [INSTALL-CODEX.md](INSTALL-CODEX.md) when your host is Codex.

## After install

- Read [TRUST-PRIVACY-AND-AUTHORITY.md](TRUST-PRIVACY-AND-AUTHORITY.md) before uploading release materials.
- Same Barry / no auto-publish / slots 1·5·6 HOLD honesty as Codex.
- **ZIP = skill door.** Structural engine lives at product-root `engine/` until a later thin-copy / pointer follow-up. Without `engine/` reachable: chat-only Claims Lock draft — no invent paths, no invent claims/pricing.
