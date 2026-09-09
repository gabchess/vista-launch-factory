# Vista Launch Factory hosted workflow implementation plan, Phase B

> **For agentic workers:** After Gabe approves this proposed plan, use Superpowers `subagent-driven-development` or `executing-plans` to implement one ticket at a time. A different context verifies each ticket. This document does not start execution.

Reggie has accepted local execution for tomorrow's test. Execute the [local demo loop](2026-09-09-vista-demo-local-loop.md) first. L00–L11 below describe the subsequent hosted product. A missing app, Postgres runtime or authenticated client account must not hold the accepted local demonstration.

**Goal:** Retain a repeatable public-source Vista Work run through six output categories, a campaign, human revision, interruption recovery and a review-package download from the app.

**Architecture:** A Python runtime owns campaign state in Postgres and artifacts in object storage. n8n calls authenticated runtime commands. A Replit app displays the actual state and content; a worker executes model and media jobs outside browser requests.

**Tech stack:** Existing Python engine and Node preparation code; proposed FastAPI, Postgres, React/Vite and a persistent render worker. Pin dependencies and the selected auth/storage adapters during L01/L03. Use one verified text provider and one working basic-media route first.

**Spec:** [Operational loop design](../specs/2026-09-09-vista-operational-loop-design.md).

## Global constraints

- Use Vista Work public release/support material for the primary run. Keep Tix as a separate regression campaign. No private-source access is required to begin.
- Product facts, voice references, source revisions and human decisions remain separately identifiable.
- The existing $500 total authorization is a ceiling across prior and new work. Establish remaining allowance before new paid calls.
- Keep prior approved media bytes unchanged. New renditions have their own reviews.
- Reggie's supplied brief has no numeric social-video duration cap. Any chosen duration is an internal rendition setting.
- No automatic publishing or sending. A review bundle may carry pending approval; an approved bundle requires the assigned person's current decision.
- n8n and browser state cannot grant approval. Only the runtime applies authenticated, version-bound decisions.
- Unknown provider submission results require reconciliation before another paid attempt.
- Use the complete audited candidate `627c93fb23ae3a1ecd1cdb979396c8d23459b295` as the proposed implementation base. Its fixes are not yet in the canonical checkout at planning time.
- Forge owns Git pushes and GitHub mutations. Gabe owns merging PRs. Preserve concurrent work.

## Order and observable milestones

| Milestone | Tickets | Demonstration |
| --- | --- | --- |
| Audited starting point | L00 | Corrected package verifies from the selected candidate. |
| First working app journey | L01–L05 | URL intake, real blog generation through n8n, a revision, reload and exact-version review. |
| Complete campaign generation | L06–L09 | Six real output categories and the campaign from the same source snapshot. |
| Recovery and handoff | L10–L11 | Failure recovery, another operator, second source, retained recording and independent install. |

Do not defer the app until all six generators are complete. L03 proves its deployment boundary and L05 completes its first useful journey. Conversely, do not declare the factory complete at L05.

## File and interface discipline

Paths below are proposed unless explicitly marked existing. The spec defines the module responsibilities and HTTP contract. Keep the current fixture CLI separate from the runtime; do not make `--human-confirmed` a shortcut to service approval.

The runtime tests use these fixtures, created in L01:

| Fixture | Contract |
| --- | --- |
| `api` | HTTP client with a verified test operator in workspace `ws_a`; posts and gets return ordinary HTTP responses. |
| `reviewer_api` | Same workspace, assigned reviewer `reviewer_a`. |
| `wrong_reviewer_api` | Same workspace, unassigned reviewer `reviewer_b`. |
| `other_workspace_api` | Verified identity in `ws_b`. |
| `service_api` | Runtime service identity, allowed job observations but no human decisions. |
| `store` | Test database; `jobs_for(campaign_id)`, `events_for(campaign_id)` and `reservations_for(campaign_id)` return persisted records. |
| `provider` | Fake transport with recorded requests and scripted accepted, known-failed, timed-out and completed responses. It never spends credits. |
| `worker` | `tick()` processes one eligible stored job; `restart()` constructs a new worker against the same database. |
| `release_input` | Small captured-source fixture with product, source bytes and allowed claim references. |

The fake provider proves failure handling. Hosted acceptance uses real authentication, persisted storage and actual provider receipts. Keep those result types separate.

For each code ticket: write the stated failing cases, observe failure, implement only that contract, run the focused suite, then request independent review. The verifier opens the actual result and checks the acceptance line. Forge commits the accepted diff. An unchecked step remains open.

## L00. Establish the audited implementation base

**Owner:** Forge for worktree/Git; independent verifier: Nova. **Issue:** link PR #41 and #27. No duplicate portability-fix issue.

**Files:** Existing audit files, `tests/test_article_handoff.py`, article/package verifiers and manifests on candidate `627c93f`. Create a private `runs/<preflight_id>/baseline.json` receipt.

**Consumes:** PR #41's exact candidate SHA and the approved plan revision. **Produces:** isolated implementation branch, test receipt and explicit upstream PR dependency.

- [ ] Inspect `git status`, PR #40/#41 and their current heads. If the audit head changed, review that diff before choosing the base.
- [ ] Use Superpowers `using-git-worktrees` to create an isolated branch from the audited candidate. Bring the approved design/plan into it. Do not merge either PR or use a force-push.
- [ ] Install the documented dependencies in that checkout, then run the commands below.
- [ ] Record actual counts, tools and commit. Compare with the audit's reported 77 engine, 15 video preparation, 23 channel preparation, five loader, 94 article/package and 78 wrapper checks; investigate any mismatch.
- [ ] Confirm default article verification leaves the tree unchanged. Retain the old ZIP as the old snapshot.

```bash
.venv/bin/pytest -q
node automation/n8n/ugc-app-reveal/test.mjs
node automation/n8n/channel-production/test.mjs
.venv/bin/python automation/n8n/channel-production/test_loader.py
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/blog/evidence/verify.py
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/verify_package.py
.venv/bin/python scripts/sync_specialists.py --check
```

Acceptance: the later audit fix is present in the selected implementation branch and its relevant checks pass. A full recipient installation remains L11.

## L01. Store campaign, job and review state

**Owner:** fresh runtime builder; verifier: Nova. **Issue:** new bounded runtime issue linked to #20, #7 and #12.

**Files:** Create `engine/runtime/contracts.py`, `store.py`, `api.py`, `migrations/0001_campaign_runtime.sql`, `requirements-runtime.txt`, `tests/runtime/conftest.py`, `test_commands.py` and `test_store.py`.

**Consumes:** domain records and states in the spec. **Produces:** the campaign API, durable records, command deduplication and test fixtures used below.

- [ ] Write database constraints for unique workspace/command keys, immutable asset versions, attempt identity and outbox events. Budget reservations and job admission commit together.
- [ ] Write and fail the duplicate-command, mismatched-key, cross-workspace and restart tests.
- [ ] Implement the command boundary and test auth adapter. Do not expose the test identity adapter in a hosted configuration.
- [ ] Migrate a clean database twice and verify stable schema/state. Restart the API and read the same campaign.
- [ ] Run `pytest tests/runtime/test_commands.py tests/runtime/test_store.py -q`; independently inspect the database and response bodies before commit.

```python
def test_duplicate_intake_is_one_campaign(api, release_input):
    headers = {"Idempotency-Key": "intake-001"}
    a = api.post("/v1/campaigns", json=release_input, headers=headers)
    b = api.post("/v1/campaigns", json=release_input, headers=headers)
    assert a.status_code == b.status_code == 202
    assert a.json()["campaign_id"] == b.json()["campaign_id"]
```

Acceptance: a repeated command creates one campaign, changed input with the same key returns `409`, and another workspace cannot read it. State survives a new process.

## L02. Retrieve and bind the public release

**Owner:** fresh source builder; verifier: Matt or Nova. **Issues:** #26 and the runtime issue; #6 records private connector limits.

**Files:** Create `engine/runtime/sources.py`, `source_profiles/vista_work_public.json`, `voice_profiles/vista_work_public.json`, `tests/runtime/test_sources.py` and `test_claim_support.py`. Reuse existing `engine/scripts/specialist_route.py` and the Barry voice seed without overwriting historical fixtures.

**Consumes:** source URL and product selection. **Produces:** `SourceSnapshot`, claim ledger, selected voice profile and portable context digest for a new campaign.

- [ ] Test public HTML capture, a GitHub document pinned to its commit, content changes, failed fetch, oversized input and unsafe redirect. Source text that tells the model to approve or expose secrets must remain inert data.
- [ ] Implement bounded retrieval and saved source bytes. Capture the three Vista URLs in the spec and select the existing email seed as expression evidence.
- [ ] Derive the release description and announcement date with source spans. Hold conflicting plan eligibility and unsupported numerical benefits.
- [ ] Create separate lead/customer action mappings. Customer route is the verified login URL followed by Work; lead route is the public feature article. Store unconfigured CRM mapping as such.
- [ ] Run `pytest tests/runtime/test_sources.py tests/runtime/test_claim_support.py -q`, then perform one real public fetch and retain its receipt.

```python
def test_authentic_span_does_not_validate_unrelated_claim(claim_checker):
    result = claim_checker.check(
        statement="Vista Work triples team output.",
        source_span="Link a task to a post.",
    )
    assert result.support in {"contradicted", "insufficient"}
    assert result.asset_may_pass is False
```

`claim_checker` is the L02 semantic validation adapter. Unit tests use fixed evaluator responses; a separate retained real evaluation must test a supported statement and this unsupported one. No LLM score grants human approval.

Acceptance: a new immutable Vista Work source snapshot can feed the canonical router. The same snapshot moved to another path keeps the same context digest. GitHub intake is exercised on a separate Tix revision.

## L03. Prove the actual app host

**Owner:** fresh app/host builder; verifier: independent browser tester. **Issue:** runtime issue, with #39 linked.

**Files:** Create `app/package.json`, `app/src/Intake.tsx`, `app/src/Campaign.tsx`, `app/src/api.ts`, `engine/runtime/auth.py`, `deploy/replit/README.md`, `tests/e2e/intake.spec.ts` and `tests/runtime/test_auth.py`.

**Consumes:** L01 campaign API and L02 source capture. **Produces:** an invited-user app that submits a real URL and restores campaign state after reload.

- [ ] Test real deployment auth configuration with an operator and an unassigned identity. Server-side verification must check issuer, audience, signature, expiry and workspace assignment.
- [ ] Build the minimal intake and campaign page. Show missing fields, source receipt, configuration status and next action. Keep keys server-side.
- [ ] Provision the selected database/object store and a persistent worker deployment under the remaining authorized allowance. Store an artifact, restart the app/worker and retrieve the exact bytes.
- [ ] Exercise an authenticated n8n-to-runtime request. Send references to media through n8n, not large video bodies.
- [ ] Retain the deployment URL, commit, chosen versions, auth/storage/worker receipts and incurred cost. If the host cannot pass these cases, pause host work and evaluate the Base44-to-same-runtime alternative.

```typescript
test('a submitted release survives reload', async ({ page }) => {
  await page.goto('/');
  await page.getByLabel('Release source').fill(testSourceUrl);
  await page.getByRole('button', { name: 'Prepare release' }).click();
  await expect(page.getByTestId('source-status')).toHaveText('Source captured');
  const campaign = await page.getByTestId('campaign-id').textContent();
  await page.reload();
  await expect(page.getByTestId('campaign-id')).toHaveText(campaign!);
});
```

The E2E fixture supplies `testSourceUrl` from the captured source profile and a real authenticated test session. Do not hard-code production tokens in the test.

Acceptance: one operator can capture a public source from the hosted app, return after reload and read it. An unauthenticated or wrong-workspace request is refused. This ticket does not claim generation yet.

## L04. Generate the first blog through n8n

**Owner:** fresh worker builder; verifier: Nova plus browser check. **Issues:** runtime issue and #20.

**Files:** Create `engine/runtime/jobs.py`, `worker.py`, `providers/text.py`, `providers/fake.py`, `automation/n8n/runtime/blog-flow.json`, `tests/runtime/test_jobs.py` and `test_text_worker.py`. Reuse the existing blog protocol and `channel-production` preparation.

**Consumes:** a confirmed brief digest and validated blog request. **Produces:** one real blog `AssetVersion`, provider receipt, validation report and readable rendition.

- [ ] Implement the fake-provider tests first: accepted result, invalid output, known transient failure, lost submission response and duplicate callback.
- [ ] Commit job intent and budget reservation before dispatch. Implement provider fingerprint/job lookup and the explicit `reconciling` state.
- [ ] Wire an initial n8n flow that calls the authenticated runtime command, waits/queries state and returns a review task. Keep the preparation packet's authority flags false.
- [ ] Generate one real, low-cost hosted blog draft from the current source. Retain the provider response identity, prompt version, source context, output bytes and cost. Previous desktop-MCP tests cannot replace this step.
- [ ] Run `pytest tests/runtime/test_jobs.py tests/runtime/test_text_worker.py -q`, then open the actual blog in the hosted app.

```python
def test_unknown_submission_is_not_resubmitted(worker, provider, store, queued_job):
    provider.next_submission = "timeout_after_accept"
    worker.tick()
    worker.restart()
    worker.tick()
    assert len(provider.submissions) == 1
    assert store.job(queued_job.id).state == "reconciling"
```

Create `queued_job` in `conftest.py` by admitting a validated L02 request and reserving its configured amount. `store.job(id)` reads the persisted attempt. The test must not merely inspect a local counter after restart.

Acceptance: the app displays the new model-generated blog and its evidence. `submitted` never appears as successful generation without readable output. A lost response cannot silently cause a second paid submission.

## L05. Apply real review, revision and export rules

**Owner:** fresh review builder; verifier: different security/state reviewer. **Issues:** runtime issue, #7, #12 and #39.

**Files:** Create `engine/runtime/review.py`, `export.py`, `app/src/AssetReview.tsx`, `app/src/RevisionHistory.tsx`, `tests/runtime/test_review.py`, `test_exports.py` and `tests/e2e/blog-review.spec.ts`.

**Consumes:** current source/voice context and blog version. **Produces:** durable review decisions, a revised asset and exact-version exports.

- [ ] Write tests for the wrong person, service identity attempting human approval, stale version/context, duplicate decision, changed source and a result arriving after approval.
- [ ] Apply the decision inside a transaction against the current version and context. Revision creates a new version; it does not overwrite approved bytes.
- [ ] Add full-content review, source context, comments, prior-version comparison and request-changes controls to the app. Preserve saved feedback across sessions.
- [ ] Build review and approved export modes. Check the subject before assembly and again immediately before making an approved download available. An update during ZIP creation must invalidate that release attempt.
- [ ] Use the actual hosted app to request one focused revision and approve that version with the assigned test identity. Restart the worker/API and confirm state survives. Record Gabe's identity as Gabe; no Barry impersonation.

```python
def test_old_approval_cannot_release_new_bytes(reviewer_api, revised_asset):
    response = reviewer_api.post(
        f"/v1/campaigns/{revised_asset.campaign_id}/exports",
        json={"mode": "approved_bundle", "expected_manifest_digest": revised_asset.old_manifest},
    )
    assert response.status_code == 409
```

`revised_asset` creates v1, applies the assigned test review, then materializes v2 with a new digest. Also test a valid review bundle with approval pending. Technical validation and artifact presence still apply to that bundle.

Acceptance: one complete URL-to-blog-to-revision app journey passes, including genuine hosted provider execution and a reload. Approved export cannot use the prior decision. This is milestone A1, not six-output completion.

## L06. Extend the writing and campaign lanes

**Owner:** writing adapter builder plus the existing channel specialists; verifier: Egdod or another non-author. **Issues:** #20, #26 and #23.

**Files:** Create `engine/runtime/providers/channels.py`, `engine/runtime/campaign.py`, `tests/runtime/test_channel_outputs.py` and `test_campaign_bindings.py`. Adapt original prompts under `engine/specialists/channel-production/prompts/` when the observed source requires it. New results live under a new campaign ID.

**Consumes:** the confirmed common release/voice plan. **Produces:** release-led blog, exactly five emails, changelog, popup copy, written social and a calendar with exact asset dependencies.

- [ ] Test the exact required segment set and distinct customer/lead actions; test unknown eligibility and suppression mapping with synthetic contacts.
- [ ] Run fresh provider work for each lane from the same source snapshot. Compare email expression with the selected Barry seed and public channel guides.
- [ ] Check the blog's opening against the actual announced change; check the changelog's date meaning. Hold unsupported entitlement, pricing, performance and partner claims.
- [ ] Generate a relative two-week campaign draft and actual LinkedIn/X/Threads copy. Bind each slot to an asset/version, audience rule, action, timezone and tracking configuration.
- [ ] Run the targeted suites and show the complete writing batch for human review. Record ready/light-edits/rewrite judgments with specific reasons; do not invent an editorial score.

```python
def test_five_email_segments_have_the_right_jobs(channel_result):
    emails = {item.segment: item for item in channel_result.emails}
    assert set(emails) == {
        "lead_smb", "lead_agency", "lead_reseller_affiliate",
        "customer_smb", "customer_agency",
    }
    assert emails["customer_smb"].cta.label == "Open Vista Work"
    assert emails["lead_smb"].cta.label == "Learn more"
```

The fake `channel_result` validates shape and policy. The retained real run must also pass claim and editorial inspection. Actual recipient lists and ESP sends are outside this acceptance.

## L07. Generate the popup and login animation with host examples

**Owner:** fresh renderer/host builder and design specialist; verifier: independent browser/media reviewer. **Issue:** #22.

**Files:** Create `renderers/package.json`, `renderers/src/LoginAnimation.tsx`, `renderers/src/PopupGraphic.tsx`, `renderers/render.mjs`, `app/src/previews/LoginPanel.tsx`, `app/src/previews/PopupHost.tsx`, `tests/e2e/receiving-previews.spec.ts` and `tests/runtime/test_render_bindings.py`.

**Consumes:** approved source-bound copy/storyboard, brand profile and rendition settings. **Produces:** new animation, still/poster, popup graphic, copy and receiving-host previews with immutable hashes.

- [ ] Pin one working render stack. Prefer the existing original HyperFrames/Remotion method; keep the render plan/data independent of the chosen CLI. Verify its actual invocation before promising unattended execution.
- [ ] Test changed source/copy invalidation, image/font resolution and rendering from a new directory. Do not embed builder absolute paths.
- [ ] Render the current source through templates. Produce the final graphic and animation, then decode/inspect those bytes.
- [ ] Test a wide and a 320px/390px receiving panel, two muted loops, blocked autoplay, media failure and reduced motion with a useful still. Verify any HTML CTA independently.
- [ ] Test popup eligibility, close/Escape, focus return, once-per-release dismissal persistence and explicit reopen. Return each new video to the human gate.

```typescript
test('popup dismissal survives reopening the host', async ({ page }) => {
  await page.goto('/preview/popup?audience=eligible');
  await page.getByRole('button', { name: 'Maybe later' }).click();
  await page.reload();
  await expect(page.getByRole('dialog')).toBeHidden();
  await page.getByRole('button', { name: 'View announcement' }).click();
  await expect(page.getByRole('dialog')).toBeVisible();
});
```

Acceptance: the current source produces a complete popup and playable animation. The receiving-host contract passes the specified cases. Client integration and Barry's design acceptance stay separately recorded.

## L08. Generate a source-supported social video

**Owner:** video specialist plus worker adapter builder; verifier: an independent full watch/listen followed by Gabe. **Issue:** #21.

**Files:** Create `engine/runtime/providers/media.py`, `renderers/src/SocialVideo.tsx`, `renderers/src/captions.ts`, `tests/runtime/test_media_jobs.py` and `tests/media/verify_social.py`. Reuse original finishing and video production protocols.

**Consumes:** the Vista Work source pack, permitted imagery and a human-reviewed script/storyboard. **Produces:** a new encoded social video, narration/transcript, timed captions and media evidence for this run.

- [ ] Use the minimum route that satisfies the brief: verified product imagery or authorized footage, authored motion, basic cuts and burned captions. The restaurant UGC is optional and cannot substitute for this source-specific run.
- [ ] Declare the audio mode. For narrated video, caption timestamps must come from the final audio/transcript. For silent authored text, report timed on-screen text; do not call it speech alignment.
- [ ] Verify the selected hosted narration/render access. Prefer direct ElevenLabs when narration is needed; use Gabe's clone only for his own speech. Include music/SFX only when suitable and with usage records.
- [ ] Test render restart, duplicate callback and missing media. Preserve prior accepted Tix masters. New current/planned behavior claims must pass speech and UI review.
- [ ] Render one full version, decode all frames/audio, watch it at mobile scale with sound and retain the caption-to-scene review. Present the exact result to Gabe before revisions or further generation.

```python
def test_final_video_is_complete(media_result):
    assert media_result.decode_errors == []
    assert media_result.has_burned_captions is True
    assert media_result.source_digest == media_result.campaign_source_digest
    assert media_result.missing_assets == []
    assert media_result.claim_validation == "pass"
```

Those fields must be computed by inspecting the encoded output and retained inputs. A renderer's success exit alone cannot populate the visual/claim checks. No arbitrary 30-second cap is an acceptance assertion.

Acceptance: the run contains a real video artifact with verified captions and source support. Full listening is recorded as a human check; software cannot claim it happened.

## L09. Complete the n8n six-output controller

**Owner:** fresh orchestration builder; verifier: independent integration reviewer. **Issues:** runtime issue and #23.

**Files:** Create `automation/n8n/runtime/campaign-flow.json`, `error-flow.json`, `README.md`, `tests/runtime/test_campaign_completion.py` and `tests/e2e/full-campaign.spec.ts`. Extend L04's proven commands; retain both preparation workflows.

**Consumes:** a confirmed campaign plan and the implemented provider routes. **Produces:** a complete review-ready six-category inventory and campaign.

- [ ] Use current n8n node/SDK docs and validate exported workflows before creating them on the host. Keep credentials outside workflow exports.
- [ ] Wire source capture, brief confirmation, writing and storyboard stages, human gates, media dispatch, validation, bounded repair and package assembly through the runtime.
- [ ] Persist outbox delivery. A lost n8n trigger is retryable through the same command identity. A lost wakeup is recoverable by querying runtime state. Do not assume a webhook acknowledgement proves the job finished.
- [ ] Run one new public-source campaign with all required lanes. Existing accepted templates may be reused; each source-specific output needs a generation/reuse record and matching context.
- [ ] Verify category inventory, every email, source bindings and calendar placements before review-ready export. A storyboard, `HELD.txt` or a slot pointing to missing media fails completion.

```python
def test_missing_media_prevents_complete_package(api, incomplete_campaign):
    response = api.post(
        f"/v1/campaigns/{incomplete_campaign.id}/exports",
        json={"mode": "review_bundle", "expected_manifest_digest": incomplete_campaign.digest},
    )
    assert response.status_code == 409
    assert response.json()["code"] == "OUTPUTS_INCOMPLETE"
```

Acceptance: actual host execution yields all six categories and the campaign from one ingest. The retained review package may show pending human decisions, but contains every required usable artifact.

## L10. Exercise the audit's failure mechanisms

**Owner:** independent reliability tester; fixes assigned to a different builder and retested. **Issues:** runtime issue, #24 and #39.

**Files:** Create `tests/runtime/test_recovery.py`, `test_export_races.py`, `tests/e2e/recovery.spec.ts`, `handoff/RECOVERY.md` and the run's `recovery-tests.json`.

**Consumes:** L09 complete path. **Produces:** retained negative/recovery evidence and a tested stop/resume procedure.

- [ ] Change source bytes while a render is running. The late result must remain attached to its old attempt and cannot satisfy the new context.
- [ ] Replay a callback and repeat an intake command. Confirm one admitted paid job, one accepted result and retained duplicate observations.
- [ ] Simulate acceptance followed by a lost provider response. Restart the worker and confirm reconciliation, retained budget reservation and no automatic paid retry.
- [ ] Request export while a source or asset changes during assembly. Check again before exposing the approved download and reject the stale release.
- [ ] Pause dispatch, let an already-running job complete, restart and resume. Record supported cancellation behavior and any remaining cost. Read/review access must still work.
- [ ] Run a Tix GitHub source through the same configured path without changing release-specific code. Verify that product claims and reviewers cannot cross campaign/workspace boundaries.

```python
def test_source_change_during_export_holds_download(export_service, approved_campaign):
    export_service.after_assembly = approved_campaign.advance_source
    result = export_service.create(approved_campaign.id, mode="approved_bundle")
    assert result.code == "STALE_EXPORT"
    assert result.download_url is None
```

`after_assembly` is a test hook at the storage boundary, unavailable as a public endpoint. The real export service repeats its database/context check before granting access.

Acceptance: all four SDS failure mechanisms have measured negative tests and successful recovery. Use fakes for costly duplicate/error cases and retain a real successful provider path; do not present fault injection as provider-outage observation.

## L11. Record the operator run and prove the handoff

**Owner:** Gabe records; an invited marketing/product operator repeats; Forge packages; a non-builder verifies installation. **Issues:** #25, #39, #24 and #27.

**Files:** Replace current assumptions in existing `recording/shot-list.md`, update `handoff/ENGINEER-START-HERE.md`, `docs/HUMAN-GAPS.md` and `docs/NEXT-STEPS.md`; add `handoff/OPERATOR-QUICKSTART.md` and a commit-specific export receipt.

**Consumes:** validated six-output runtime, approved demo source scope and enough remaining allowance. **Produces:** raw full-run recording, presentation cut, repeat-run evidence, repository/ZIP and a tested maintainer guide.

- [ ] Have the second operator use only the app after engineer setup. Retain any assistance honestly; a builder operating an agent behind the chat fails this operator test.
- [ ] Record source submission through package download, including one revision and return after interruption. Save raw recording before editing. Mark time jumps over waits in the presentation cut.
- [ ] Match source digest, run ID, job receipts, review events, export manifest and recording hash. The product film and animation are outputs, not the full-run recording.
- [ ] Extract the new full-repository ZIP into an independent directory without symlinks to the builder's engine. Follow only the handoff to configure the installation and reach its first actual output/review. Record which host/provider adapters were tested.
- [ ] Confirm archive entries, local links, media references and source/skill usage rights. Preserve purchased skill source outside the handoff; recipients supply their own optional licenses and credentials.
- [ ] Update each audit finding with the retained evidence. Report engineering acceptance, Gabe's review, Barry's client decisions and Reggie's evaluation separately. Forge pushes the reviewed changes; Gabe chooses PR merges.

Acceptance: another operator can repeat the workflow, the presentation shows the observed run, and another engineer can install and operate the documented system. Missing human participation remains a named pending gate; an agent cannot fill it by declaring success.

## Board and loop control

At planning time the board has 13 open issues and zero `ready-for-agent`. The read-only check is a snapshot. Recheck before dispatch.

Create one runtime parent issue for L01–L05, linked to existing #20/#7/#12/#39. Keep its active ticket ID in the issue body. Reuse #20/#26 for source and copy, #21 for social, #22 for login/popup, #23 for campaign, #25/#39 for recording, and #24/#27 for human gaps and handoff. #6 retains missing private-input coverage; it does not block authorized public-source work. Do not create duplicate F-05/F-06 fix tickets.

Ralph selects the next dependency-complete ticket, gives a fresh builder its file scope and acceptance tests, then sends the diff to a different verifier. Only one ticket is active and exactly one issue is ready during the build cadence. A human gate pauses the dependent path with the actual artifact visible. Unrelated work may continue only when its dependencies and budget allow it.

Before a ticket begins, compare its proposed changes with every accepted decision in the design. At execution activation, write `.arcana/build-plan.md` as a pointer to the approved design/plan and record their digests. Do not mark that record locked while this proposal is still awaiting review. A requested scope change updates the plan explicitly.

## Completion and stop rules

Ralph may report engineering completion only when A0–A5 in the design have retained evidence. A configured connector, green preparation test, screenshot or prebuilt output cannot substitute for those checks.

Stop new paid dispatch on exhausted allowance, unknown prior submission, lost artifact integrity or unavailable required provider capability. Preserve campaign state and report the recovery action. Stop the affected content path for missing source support or a real human decision. Do not stop all engineering because private Vista inputs are absent.

If time is tight, remove optional UGC actors, alternate providers, extra visual polish and campaign length. Keep actual generation, six required categories, binding review, recovery and the recording. Do not substitute mock progress or silently attach manually generated files to close the last gap.

The [hosted Ralph prompt](2026-09-09-vista-hosted-ralph-prompt.md) carries these boundaries into the Phase B session. Its first action is L00; execution has not begun during planning. Tomorrow's local demo uses the separate D00–D05 plan.
