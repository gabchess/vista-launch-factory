# Ralph prompt for the hosted Vista workflow, Phase B

Prepared for Gabe's review. This file is not an active loop or a grant of client approval.

This prompt is for the post-presentation product. Reggie's latest acceptance of local execution makes the [local Ralph prompt](2026-09-09-vista-ralph-prompt.md) the immediate entry.

Use the prompt below after Gabe approves the linked design and implementation plan. The existing authorization permits the public-source direction and the overall $500 ceiling; reconcile remaining spend before any paid call. A prior budget ceiling is not proof of available balance.

```text
Build the Launch Factory operational workflow from the approved SDS follow-up plan.

Read, in this order:
1. AGENTS.md in the selected checkout.
2. docs/superpowers/specs/2026-09-09-vista-operational-loop-design.md.
3. docs/superpowers/plans/2026-09-09-vista-operational-loop.md.
4. docs/audits/sds-trial-2026-09-09/REPORT.md and pre-mortem.md.
5. The current ticket and its existing implementation dependencies.

Select the audited candidate 627c93fb23ae3a1ecd1cdb979396c8d23459b295,
or a reviewed descendant that contains it, as the implementation base.
Recheck PR41 before selecting the commit. Use an isolated worktree.
Carry the approved plan files into that branch. Do not merge PR40 or
PR41 without Gabe. Forge owns Git push and GitHub mutations.

The primary run is Vista Work linked tasks from public release/support
sources. The source URLs are in the design. Capture them through the
implemented intake, preserve their bytes and record a public-source run.
Use Tix as the separate GitHub/regression source. Private Vista folders,
Loom access and client account footage are absent. Do not wait for them
or claim to have exercised them.

Start at L00. Complete one dependency-ready ticket per iteration.
Do not launch an unbounded build or mark several tickets ready.

Each iteration:
- Verify branch, local edits, selected plan digests, board and current run.
- Compare the proposed changes with the approved design. Record any
  deviation before implementation; an unapproved architecture change
  does not become acceptable because it is convenient.
- Select one ticket and state its acceptance line, file ownership,
  dependencies, named builder and different verifier.
- Give a fresh builder only the relevant source, rules and ticket.
  Tell the builder that others share the repo and to preserve their work.
- Write the ticket's failing behavior tests, observe the failure, make
  the smallest change and run focused checks.
- Have the independent verifier inspect the diff and the actual artifact
  or runtime result. An agent's summary is not verification evidence.
- Fix concrete review findings and rerun the affected checks.
- Keep CHANGED and VERIFIED separate in the receipt. Record test command,
  exit status, commit, source context, artifact hashes and remaining work.
- Forge commits an accepted diff and updates only the relevant issue.
  Keep exactly one ready issue during the active build cadence.
- Advance only after the ticket's stated acceptance is observed.

The first hosted milestone is L05: a real URL-to-blog run through the
app and n8n, with one revision, durable review and reload/restart proof.
The complete system requires L06-L11 and every A0-A5 evidence gate.

Runtime rules:
- Python runtime and Postgres own campaign/job/review state. Object
  storage owns immutable media bytes. n8n calls authenticated commands.
- Preparation packets and local browser notes never grant authority.
- A successful HTTP acknowledgement means accepted, not rendered.
- Store job intent and reserve cost before calling a provider.
- An unknown submission result enters reconciliation. Query by provider
  job/idempotency identity if possible. Otherwise hold the affected path
  for recovery. Do not submit a second paid job to hide the uncertainty.
- Duplicate callbacks and late results retain their attempt identity.
  They cannot overwrite a newer artifact or reset retry limits.
- Recheck current source/voice and artifact bindings before and after
  assembling an approved export, before access is granted.
- Keep review_bundle separate from approved_bundle. The former may
  carry pending review. The latter requires the assigned human's exact
  current decisions. Publishing and sending remain disabled.
- Check semantic support for product statements in copy, speech,
  captions and authored UI. A valid source hash alone is insufficient.

Human gates:
- Confirm source/voice/audience/output plan before generation.
- Obtain script/storyboard review before expensive creative generation.
- Show every new generated video to Gabe before continuing its revisions.
- Writing can be reviewed as a batch; each email retains its own version.
- Record Gabe as Gabe during demo review. Barry owns client copy and
  creative decisions. Do not create a Barry event from a test account.
- A missing human response pauses that dependent stage. Preserve useful
  work and current artifacts; do not invent an approval to continue.

Cost and scope:
- Reconcile earlier spend within the original $500 total ceiling.
- Start with local failure fixtures, then the smallest actual hosted
  text and render tests. Record real and estimated costs separately.
- Use one active render and at most two concurrent text jobs initially.
- Stop new spend at the configured allowance. Unknown-job reservations
  remain counted until their result is reconciled.
- Use a simple source-supported social video and original animation
  templates first. Rich UGC actors and extra providers are optional.
- Direct ElevenLabs is the preferred narration route when needed.
  Gabe's cloned voice is only for his own speech.
- Preserve the accepted Tix masters and true provider lineage. Do not
  silently replace them or present a desktop MCP as a proven hosted API.
- Do not introduce a client 30-second video cap; none is in the brief.

Completion evidence:
- One new public Vista Work ingest produces six usable output categories,
  all five email variants and the campaign with a shared source digest.
- The actual app shows source, current artifact, version, comments,
  pending reviewer, findings and recoverable errors together.
- A real revision and the specified stale/duplicate/unknown-result/
  pause/restart tests pass with retained evidence.
- A second operator completes the app journey without builder actions.
- A second product/source checks contamination and reuse boundaries.
- Retain the raw full-run recording, mark generation time jumps in the
  presentation cut, and bind the recording and export to the same run.
- Another engineer installs from an independent checkout/ZIP without
  symlinks to the builder workspace and reaches an actual output/review.

Do not report complete based on preparation tests, a prebuilt preview,
a screenshot, missing-media placeholders or a product film alone.
Report engineering acceptance, Gabe's demo review, Barry's decisions
and Reggie's evaluation as separate observed states.

At interruption or a failed gate, save the current ticket, commit,
run/job IDs, evidence paths, exact failure and next recovery action.
Pause new dispatch while preserving readable artifacts and decisions.
Resume from that record instead of regenerating the full campaign.
```

The runtime parent issue should contain the active L-ticket and link existing output/review issues as specified in the implementation plan. This prompt does not create a recurring automation, mark a GitHub issue ready or start an agent session by itself.
