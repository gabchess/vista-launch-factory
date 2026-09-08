# Launch Factory

Launch Factory gives an agent operator a reusable workflow for a release campaign: source review, specialist drafting, creative production gates and exact-version human review. Barry reviews Vista client work. Gabe reviews his own validation work.

The current repository contains a specialist layer over the v0.2.0 structural engine. It supplies 12 role protocols, channel reference banks, review rubrics and offline packet checks. The [UGC app reveal n8n subworkflow](automation/n8n/ugc-app-reveal/README.md) prepares the video lead's prompts and review context. The app, provider worker and authenticated approval store remain separate work.

The [8 September checkpoint](docs/CHECKPOINT.md) records the two approved Tix creative outputs and the remaining deliverables. Continue through [the ordered next steps](docs/NEXT-STEPS.md); the full six-output app remains under development.

## Open the full project

1. Read [Start here](START-HERE.md).
2. Open the whole repository in [Codex](docs/INSTALL-CODEX.md) or [Claude Code](docs/INSTALL-CLAUDE.md). Keep the project skill folders, engine and reference banks together.
3. Invoke Launch Factory on one source folder. The operator identifies the product and human reviewer, then routes the next stage to a concrete specialist.
4. Inspect the actual draft or media at the human gate, with its version, hash, source references and remaining gaps.

Codex uses `.agents/skills/` and `.codex/agents/`. Claude Code uses `.claude/skills/` and `.claude/agents/`. A host without native delegation can perform the selected role inline after reading its skill and bank. It must report that fallback.

The retained `claude/launch-factory-v0.2.0.zip` is a **legacy skill-only archive**. It excludes the new specialist layer and engine. Copying `codex/launch-factory/` alone also cannot resolve the current project protocols. Use the full repository for this version of the workflow.

## Deliverable routes

| Requested work | Owner |
| --- | --- |
| Social video for IG/TikTok, up to 30 seconds | Video lead |
| Blog article | Blog editor |
| Five segmented announcement emails | Email editor |
| Changelog entry | Changelog editor |
| Login animation | Motion designer |
| In-app popup graphic and copy | Popup designer |
| LinkedIn post | LinkedIn editor |
| X and Threads copy | Social editor |
| Campaign and weekly calendar | Campaign planner |
| Carousel, when explicitly requested | Carousel designer |
| Source claims and artifact review | Evidence editor and quality reviewer |

The email route distinguishes lead SMB, lead Agency, lead Reseller/Affiliate, customer SMB and customer Agency. Each channel draws from selected product facts and its own voice context. The default campaign excludes carousel generation.

## Try the offline route

With Python and the repository dependencies installed:

```bash
.venv/bin/python engine/scripts/specialist_route.py route engine/fixtures/specialist-demo/request.json --workspace engine/fixtures/specialist-demo
.venv/bin/python scripts/sync_specialists.py --check
.venv/bin/pytest -q
```

The fictional fixture returns the chosen skills, source read set, actual draft text and bound review subject. It makes no provider calls. Read [the specialist guide](engine/specialists/README.md) for packet fields and review validation.

The finishing-layer baseline had 48 passing tests; current actor-production checks are described in the specialist guide. A fresh Codex CLI 0.153.3 `skills/list` probe with `forceReload` discovered all 14 enabled project skills, including `lf-short-motion-finishing`, with no missing names or target errors. This was a read-only discovery probe; it made no model turn or native skill invocation. Native role invocation, provider access and first-pass content quality remain untested for this layer. See [host evidence](HOST-MATRIX.md).

## Human authority and source integrity

Every product claim needs an exact source reference. The helper checks hashes and quote spans; the specialist still reviews meaning. Voice samples supply expression guidance and cannot establish product facts. Missing tools and uninspected media remain visible gaps.

A human decision belongs to the exact artifact version and its relevant input bindings. Changing a shared script changes the dependent video's review subject. An unrelated calendar date edit does not rewrite the copy. The helper never authenticates or applies approval events, including repeated events. Actual Barry or Gabe decisions stay human.

Legacy `run.sh`, release-record helpers and demo packages remain available as structural fixtures. Their caller-supplied `--human-confirmed` flag does not implement authenticated approvals or stale-event protection. The new layer does not project its recommendations into that flag. Publishing, sending and external scheduling are excluded.

## Repository map

| Path | Purpose |
| --- | --- |
| `codex/launch-factory/SKILL.md` | Canonical operator protocol |
| `.agents/`, `.codex/`, `.claude/` | Generated project skill and role entry points |
| `engine/specialists/` | Registry, schemas, shared contract and selected reference banks |
| `engine/specialists/video-production/recipes/ugc-app-reveal/` | Reusable actor-and-app film recipe with five named prompts |
| `automation/n8n/ugc-app-reveal/` | Importable n8n video preparation subworkflow, SDK source and tests |
| `engine/scripts/specialist_route.py` | Offline route, recommendation and binding checks |
| `scripts/sync_specialists.py` | Regenerate project wrappers or check for drift |
| `voice-bank/` | Vista voice references and interim tone brief |
| `docs/adr/0017-specialist-routing-and-current-scope.md` | Current scope with historical decisions preserved |
| `engine/fixtures/`, `barry/` | Fixtures and human review templates |
| `release-manifest.json`, `documentation-manifest.json` | File integrity lists |

The original structural package remains version 0.2.0; the added specialist layer is 0.2.0, including the shared short-motion finishing skill. Current media work follows its own source and human stage approvals under [ADR 0017](docs/adr/0017-specialist-routing-and-current-scope.md). Historical HOLD decisions and the old archive are retained as history.
