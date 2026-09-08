# Start here

Launch Factory provides an operator and specialist protocols for turning release evidence into six launch deliverables, LinkedIn and written social, plus a weekly campaign calendar. The actual human reviews the content and creative at the workflow's gates. Nothing auto-publishes or auto-sends.

Open the full repository in [Codex](docs/INSTALL-CODEX.md) or [Claude Code](docs/INSTALL-CLAUDE.md), then invoke Launch Factory on one release source. The operator identifies the product and human reviewer, checks claims and selected voice material, and invokes the specialist for the current stage. A host without native delegation uses the same protocol inline and reports that fallback.

Try the [offline specialist fixture](engine/specialists/README.md) to inspect the routing, actual draft text, exact review subject and dependency behavior. This makes no provider calls. It does not prove host invocation, real content quality or a finished campaign.

The new specialist layer lives in the full repository project doors. The retained `claude/launch-factory-v0.2.0.zip` predates it and remains a legacy skill-only archive. No updated whole-repository ZIP is claimed here.

`run.sh`, the old release-record helpers and historical demo packages remain structural fixtures. They do not authenticate a reviewer or implement the new version-bound human workflow. Do not translate model recommendations or Gabe's decisions into a false Barry approval through `--human-confirmed`.

Current demo and media scope is recorded in [ADR 0017](docs/adr/0017-specialist-routing-and-current-scope.md), preserving older HOLD decisions as history. Each real provider run requires current source evidence, tool access and the actual human's authorized stage. A web app, deployed n8n service and authenticated event store remain separate work.

Read [the operator skill](codex/launch-factory/SKILL.md), [host evidence](HOST-MATRIX.md) and [the specialist contract](engine/specialists/CONTRACT.md) for the current path.
