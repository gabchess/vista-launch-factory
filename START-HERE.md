# Start here

**Launch Factory** turns a feature release folder into a review-ready launch package for Vista Social.

You ingest one release folder (Loom walkthrough, feature outline, raw footage). The run follows one loop: ingest → ground (facts + Voice Bank brief) → **Claims Lock (Barry once)** → create (adapters from locked claims only) → review (four gates) → package (+ honesty doc + Campaign Plan) → learn. Nothing auto-publishes. All state lives in one release record (`runs/<folder>/release-record.json`) — every run resumes from it.

## Fastest path to value

1. Choose your host: [Codex](docs/INSTALL-CODEX.md) or [Claude](docs/INSTALL-CLAUDE.md).
2. Install the matching package (repo root is the install door — ADR 0012).
3. Read [First run](docs/FIRST-RUN.md).
4. Point Launch Factory at one release folder with the strongest materials you have.
5. Start with: **"Run Launch Factory on this release folder."**

One-command door (ADR 0014), from repo root with Python 3 available:

```bash
./run.sh engine/fixtures/demo-release
```

After the first Run, expect a Claims Lock draft for Barry — not six finished assets yet.

**v0.2.0 honesty:** The engine is the single source of truth at repo-root `engine/` (Option B). Keep the repo root reachable after host install — copying only `codex/launch-factory` into `skills/` does **not** bring `engine/` along. When `engine/` + Python are available, Run uses `engine/scripts/` structural helpers (`init_release`, `validate_record`, `transition_slot`, `validate_ledger`, `validate_campaign`, `build_package`) — **STRUCTURAL_INTEGRITY_ONLY**; no publish. If `engine/` is missing, Run is chat-only Claims Lock **draft shape** (fail closed; no invent claims/pricing). Barry remains the quality gate for copy and creative; only Barry's recorded decision moves anything to approved. Slots 1/5/6 HOLD (ADR 0013). Voice is interim (ADR 0015). Claude ZIP is a skill door only (engine not inside the ZIP). See [Trust, privacy, and authority](docs/TRUST-PRIVACY-AND-AUTHORITY.md) and [engine/README.md](engine/README.md).

## What Launch Factory is not

- **Not a CMS publisher.** It does not push to vistasocial.com, changelog, or social networks.
- **Not auto-send.** It does not send HubSpot email or any outbound without Barry approval and separately authorized tooling.
- **Not email-only SaaS.** Email is one adapter among several; CIO tooling is not Vista's ESP.
- **Not inventing claims.** Every claim must trace to source docs or transcript. No invented features, limits, or pricing.
- **Slots 1 / 5 / 6 are HOLD** (social video with burned captions; login animation; in-app popup). Honesty stubs only until encode/asset tracks land. Do not claim "all six review-ready" while they are held.
- **Writer ≠ Barry.** Drafting adapters are not the approval role; the record tooling refuses self-approval.
- **Folder visible ≠ Augment active.** Having files on disk does not mean the host skill is installed and live.

## Next reads

- [Operate Launch Factory](docs/OPERATE-LAUNCH-FACTORY.md)
- [Validation and limits](docs/VALIDATION-AND-LIMITS.md)
- [Human gaps](docs/HUMAN-GAPS.md)
- [Host matrix](HOST-MATRIX.md)

## Barry HITL

After install, Runs stop for Barry three times: Claims Lock → spot-check (on the first real **draft**) → pack approve. Order: draft first real → spot-check → remaining adapters. Cards: `barry/claims-lock.md`, `barry/spot-check.md`, `barry/pack-approve.md` (humans; not `engine/barry-templates/`). Slack thumbs do not count. Nothing publishes from this pack alone.
