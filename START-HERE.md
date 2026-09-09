# Start here

Launch Factory provides an operator and specialist protocols for turning release evidence into six launch deliverables, LinkedIn and written social, plus a weekly campaign calendar. The actual human reviews the content and creative at the workflow's gates. Nothing auto-publishes or auto-sends.

For the current build, read the [engineer handoff](handoff/ENGINEER-START-HERE.md) and [Tix package guide](packages/camp_tix_launch_001/01_channel_run/README.md). Run the included server to open the [local review](packages/camp_tix_launch_001/01_channel_run/review.html): a blog with images, five emails, changelog, popup and proposed two-week calendar. These new drafts await Gabe's review. Two earlier creative renditions retain their exact approvals.

Repository sharing and commit/push are authorized. App/n8n setup and testing are next. The current page previews real local artifacts; the two n8n workflows prepare work packets. A provider worker and authenticated, persistent human review still need implementation. Follow the handoff's working slice before offering the app to a routine operator.

Open the full repository in [Codex](docs/INSTALL-CODEX.md) or [Claude Code](docs/INSTALL-CLAUDE.md), then invoke Launch Factory on one release source. The operator identifies the product and human reviewer, checks claims and selected voice material, and invokes the specialist for the current stage. A host without native delegation uses the same protocol inline and reports that fallback.

Try the [offline specialist fixture](engine/specialists/README.md) to inspect the routing, actual draft text, exact review subject and dependency behavior. This makes no provider calls. It does not prove host invocation, real content quality or a finished campaign.

The new specialist layer lives in the full repository project doors. The retained `claude/launch-factory-v0.2.0.zip` predates it and remains a legacy skill-only archive. No updated whole-repository ZIP is claimed here.

`run.sh`, the old release-record helpers and historical demo packages remain structural fixtures. They do not authenticate a reviewer or implement the new version-bound human workflow. Do not translate model recommendations or Gabe's decisions into a false Barry approval through `--human-confirmed`.

Current media scope begins with [ADR 0017](docs/adr/0017-specialist-routing-and-current-scope.md); [ADR 0019](docs/adr/0019-testable-app-and-next-milestone.md) records the testable-app direction, and [ADR 0020](docs/adr/0020-vista-channel-draft-batch.md) records the completed drafting authorization. Keep older HOLD decisions and recorded-demo-only assumptions as history. Each real provider run requires current source evidence, tool access and the actual human's authorized stage.

Read [the operator skill](codex/launch-factory/SKILL.md), [host evidence](HOST-MATRIX.md) and [the specialist contract](engine/specialists/CONTRACT.md) for the current path.
