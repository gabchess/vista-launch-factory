# Use Launch Factory in Codex

Open the full repository as the Codex project. Keep `engine/`, `.agents/skills/`, `.codex/agents/`, `codex/`, `docs/` and the selected release workspace reachable. The generated project skill at `.agents/skills/launch-factory/SKILL.md` reads the canonical operator, which routes to the specialist skill and reference bank.

Start a fresh task in this project and request Launch Factory on one source folder or supplied packet. Confirm the operator identifies the product, human reviewer and source stage, then reports the selected specialist and actual work. Native project roles are declared in `.codex/agents/*.toml`. A host that cannot delegate must read the same selected skill and bank and work inline with that limitation stated.

These paths follow the current [Codex custom subagent contract](https://developers.openai.com/codex/multi-agent). Do not infer discovery from file presence. Check installation, discovery, invocation, tool access and first useful output separately on the destination host. The local offline checks described in [the specialist README](../engine/specialists/README.md) prove routing and file/reference integrity only.

If an older global `launch-factory` skill exists, inspect the host's selected source path before invoking it. Keep the project version selected; do not overwrite or delete another installation without an explicit migration. To roll back this project layer, restore the prior tracked revision in a separate checkout or remove only this layer's generated project files after backing up local changes. Do not remove user skills or provider credentials.

The former install-by-copying `codex/launch-factory` door is a legacy skill-only route. Copying that folder alone cannot resolve the current specialist protocols. Restore the full repository project to use this layer. Host commands differ by version; inspect local help rather than assume a plugin validate/install command exists.

Provider accounts and n8n configuration belong to the operator. No credentials ship in the pack. A successful MCP connection in another chat does not prove this host can use it. Actual Barry or Gabe decisions stay human; the legacy `--human-confirmed` flag supplies no authenticated authority.

See [Claude Code](INSTALL-CLAUDE.md), [host evidence](../HOST-MATRIX.md) and [current scope](adr/0017-specialist-routing-and-current-scope.md).
