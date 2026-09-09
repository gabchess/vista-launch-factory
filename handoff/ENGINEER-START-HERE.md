# Engineer handoff: current Launch Factory build

This is the current technical handoff for the branch containing the Tix channel run. Read it before the historical SOP files in this directory. Gabe authorized sharing the repository with a developer for review. No credentials, paid AgentsKit source or client approval events are included.

See the [SDS trial audit](../docs/audits/sds-trial-2026-09-09/REPORT.md) for the requirement-by-requirement verdict and verified limits. The supplied Reggie brief sets no numeric social-video duration cap; this project retains its own 30-second target.

## What is available

The full repository is an agent-operated launch workflow. It includes a Codex/Claude operator, specialist roles, selected source and voice packets, original production prompts, local validators, two importable n8n preparation workflows, and an actual campaign review package.

The Tix test package contains a complete blog with two images, five segmented email drafts, a changelog, popup graphic and copy, and a proposed two-week calendar with LinkedIn, X and Threads drafts. Two prior creative renditions are approved: a 55-second product film and a 10-second square animation. Their hashes and production lineage are retained; the binary masters can be attached separately to the local review.

The four new output categories are awaiting Gabe's content review. The strict social slot still needs a ≤30-second cut and platform crop. The login animation needs integration with a responsive login surface. Tix is the test product; Vista Social supplied the requested writing and design references. This run is not a Vista feature announcement or proof of Vista product ownership.

The web page in the package displays real local content and records version-bound review notes. It does not run a model or authenticate a human decision. The n8n workflows prepare source-bound work packets. They do not yet dispatch the provider worker, resume long jobs or apply approval events. These boundaries are the starting point for engineering work.

## Run the included review

Requirements: Python 3.11 or later, Node.js with ESM support, Git and a modern browser. Install the repository's Python dependencies in a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
python3 packages/camp_tix_launch_001/01_channel_run/route_packets.py
python3 packages/camp_tix_launch_001/01_channel_run/render_copy.py
python3 packages/camp_tix_launch_001/01_channel_run/build_review.py
python3 packages/camp_tix_launch_001/01_channel_run/serve_review.py --port 8770
```

Open `http://127.0.0.1:8770/01_channel_run/review.html`. All four new deliverables and the calendar work without credentials. The approved videos need their separate master files:

```bash
python3 packages/camp_tix_launch_001/01_channel_run/serve_review.py \
  --port 8770 \
  --film /path/to/Dinner-with-Tix-app-reveal-v3.mp4 \
  --animation '/path/to/tixmancer motion.mp4'
```

The server binds to loopback and verifies each attached video against its approved SHA-256. Review notes remain local browser intent until exported. They do not apply approvals to a backend. Changing asset bytes or source/voice context prevents reuse of an old note.

The [campaign README](../packages/camp_tix_launch_001/01_channel_run/README.md) maps the outputs, checks and review procedure. `PACKAGE-MANIFEST.json` covers the committed campaign files; repository manifests cover the reusable engine and documentation. Local routing receipts are regenerated on the recipient's host.

## Operate it through Codex

Open the full checkout as the project and follow [Codex installation](../docs/INSTALL-CODEX.md). The operator entry is [launch-factory](../codex/launch-factory/SKILL.md). Generated role wrappers live in `.agents/skills/` and `.codex/agents/`; copying a single skill folder omits its engine and references.

Use the current campaign as an example:

> Read the Launch Factory operator. Use `packages/camp_tix_launch_001` as the release workspace and the packets under `01_channel_run/requests`. Review the current artifacts and their source claims. Preserve the two accepted media files. Return requested revisions to Gabe as exact new versions. No publishing or sending.

For a new product, create a separate campaign workspace. Ingest its source documents, retain immutable source bytes and source revision, extract claim spans, select its voice reference, and identify the human reviewer. Barry is the required approver for Vista work. The Tix review history grants no authority for a new product or source.

Where native role delegation is available, the host invokes the selected specialist. Otherwise the operator reads the same role protocol and performs the work inline, reporting that path. The current writing run used delegated and inline protocol execution. Role discovery and schema validation are recorded separately from provider execution.

AgentsKit's relevant skills were verified as installed in Codex on the builder's host. Recipients need their own permitted installation to use that optional library. The original channel prompts bundled here work without copying the purchased kit. See the [installation audit](../docs/research/agentskit-install-audit.md).

## Prepare the four n8n lanes

```bash
.venv/bin/python automation/n8n/channel-production/load_requests.py \
  --workspace packages/camp_tix_launch_001 \
  --batch-id tix-channels-v1 \
  --requests \
    packages/camp_tix_launch_001/01_channel_run/requests/blog.json \
    packages/camp_tix_launch_001/01_channel_run/requests/email_segments.json \
    packages/camp_tix_launch_001/01_channel_run/requests/changelog.json \
    packages/camp_tix_launch_001/01_channel_run/requests/in_app_popup.json \
  --output /tmp/tix-channel-input.json
node automation/n8n/channel-production/run.mjs \
  /tmp/tix-channel-input.json /tmp/tix-channel-work-packets.json
```

Import [Four Channels Prepare](../automation/n8n/channel-production/workflow.json) into your n8n instance. A parent calls it with Execute Sub-workflow and passes the validated batch. Follow the [workflow README](../automation/n8n/channel-production/README.md) for the envelope, source checks, revision rules and required `crypto` built-in. Leave it inactive until a controlled host test passes.

The separate [UGC App Reveal preparation](../automation/n8n/ugc-app-reveal/README.md) supplies the video lead's five prompts. The accepted film used ChatCut performances and assembly, HyperFrames scenes, and one Higgsfield enhancement. An in-house HeyGen/HyperFrames/Remotion adapter is an implementation direction. It must establish its own working output before anyone describes it as equivalent to the accepted route.

## Credentials and configuration for the next stage

An engineer configures the recipient's own accounts once. Routine operators should then use the app without handling keys.

| Component | Configuration owner | Where it belongs |
| --- | --- | --- |
| n8n | Recipient instance URL, access credentials, workflow IDs | Backend secrets and n8n credential store |
| Language model | Recipient provider key and selected model | Worker secret store |
| Video / animation | Verified provider access, templates, render worker and job callbacks | Worker adapters; never assumed from an installed MCP |
| Voice | Direct ElevenLabs account key and selected voice ID, or verified organic provider audio | Worker secret store; choose the voice for the actual speaker |
| Artifacts | Storage location, access policy and retention | Backend configuration |
| Human review | Auth provider, reviewer assignment and durable event store | Backend configuration and database |
| Delivery | CMS/ESP credentials only when export adapters are implemented | Server-side draft/export adapters |

Gabe's cloned voice is for his own founder or educator dialogue. Fictional UGC speakers use a separately chosen voice. The reusable instructions retain this preference. The handoff includes no account keys or implicit access to Gabe's paid subscriptions.

Missing configuration should produce a useful setup state in the app. Do not present a silent chat as a working integration. Provider account identity, access and cost must be verified before each paid generation route is first used.

## Next implementation slice

Build one working app-to-worker path before adding every output to the UI:

1. Intake a source URL and brief through an authenticated app endpoint. Retrieve the actual source and record its revision. Return a campaign ID.
2. Dispatch the blog packet to the worker. Save job status and the actual draft, then show the full content in the app.
3. Persist the assigned human's decision against the campaign, asset, version, content hash and source/voice context. Validate ownership and reject stale or duplicate transitions.
4. Request a small revision. Retry only the affected asset, preserve its history and return the new version for review. Confirm the state survives a browser reload.
5. Extend the verified path to five emails, changelog and popup, then asynchronous media jobs. Apply bounded retries and a cost ceiling before spending.
6. Export only the exact reviewed package. Version 1 does not auto-publish.

Replit or Base44 can supply the user interface and application host after a thin slice verifies authenticated requests, background work, callbacks and persistent state. The repository's [app scope decision](../docs/adr/0019-testable-app-and-next-milestone.md) remains the product target. The latest user instruction authorizes setup and testing next; it does not establish that those runtime paths are already implemented.

## Acceptance for the client demo

Use the Prospector source only after the Tix method and app slice are verified. The operator must complete source ingest, the required human decisions, six output previews, a revision and package download from the app. A refresh must preserve progress. Errors must name the failed step and a recoverable action. Record provider job receipts and actual output hashes.

The client trial calls for a real feature release with all six outputs. The current Tix artifacts validate the method internally. A source swap, voice calibration and recipient infrastructure test are still required for the client's own release. Keep the demo's provider lineage and infrastructure ownership explicit. Hosting, in-house API setup, support and training are separate commitments from this repository snapshot.

## Verification commands

```bash
.venv/bin/pytest -q
python3 scripts/sync_specialists.py --check
node automation/n8n/ugc-app-reveal/test.mjs
node automation/n8n/channel-production/test.mjs
.venv/bin/python automation/n8n/channel-production/test_loader.py
python3 automation/n8n/channel-production/build_workflow.py --check
python3 packages/camp_tix_launch_001/01_channel_run/verify_package.py
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/blog/evidence/verify.py
```

Read [current verification](../packages/camp_tix_launch_001/01_channel_run/VERIFICATION.md) for the checks that actually ran. A structural pass does not grade copy, authenticate a reviewer or prove an external API worked.
