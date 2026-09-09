# Vista Launch Factory: audit against Reggie's paid-trial brief

**Verdict: NO-GO for claiming the full trial is complete.** The repository provides working local preparation and a substantial Tix review package. Required workflow execution and client acceptance evidence remain open. The previous handoff discloses most of these limits accurately. Its test counts and ZIP integrity claims reproduced. A deeper article verification check failed after relocation; this PR fixes that defect.

Audit baseline: PR #40, `nova/factory-house`, commit `34c887450dbf135bceb320c982f92b707e72f9a8`. Work took place in a separate clone on `codex/sds-trial-audit`. The supplied `ai-ops-workflow-engineer-trial-brief-v2 (3).txt` was read in full; SHA-256 `82652c807fe6123793ff19ab44f8457488ab5c7af0eca38db8110f7c46976769`. Audit date: 9 September 2026 UTC, 8 September in São Paulo at session start. The original brief remains the acceptance reference. Internal Tix or Prospector scope decisions need Reggie's acceptance before they substitute for it.

## Required outputs and campaign

| Requirement | Inspected evidence | Assessment and needed work |
| --- | --- | --- |
| Social video, basic cuts and burned captions | Separate `Dinner-with-Tix-app-reveal-v3.mp4`; recorded SHA matches; 1920 × 1080; 55.083 seconds including container audio tail; complete decode succeeds. Burned captions are visible in decoded frames. | **Partial.** A finished concept film exists. Inspect the final social rendition for mobile caption legibility and for accurate depiction of current versus planned features. No single-ingest generation run establishes its production in this factory. The supplied brief has no numeric duration cap. The 30-second target comes from this repository. |
| Blog ready for Vista Insights | [Article and image metadata](../../../packages/camp_tix_launch_001/01_channel_run/blog/metadata.json), full Markdown/HTML, two images, paragraph provenance and source spans. | **Partial.** The Tix article is complete and readable as an internal preview. It introduces a buying concept and spends several sections on general buying advice. A Vista feature announcement needs a concrete release change, supported access details and a direct next action. Barry's editorial acceptance remains unobserved. |
| Five announcement email segments | [Canonical email JSON](../../../packages/camp_tix_launch_001/01_channel_run/email/emails.json) plus separate Markdown, HTML and JSON renditions. Every required segment appears, with distinct subjects, preheaders and bodies. | **Partial.** The segments meet the structural requirement. Customer variants represent returning preview readers and use an acquisition waitlist CTA. For the client release, map actual customers and leads, distinguish their next actions, and use Barry-reviewed email examples. Sender and unsubscribe fields remain ESP integration work. |
| Changelog | [Entry](../../../packages/camp_tix_launch_001/01_channel_run/changelog/entry.md) and structured claims. | **Partial.** A concise Tix preview announcement exists. It has no verified release date or specific newly shipped delta. Confirm these against the selected real release and return that exact entry to Barry. |
| Login animation | Separate `tixmancer motion.mp4`; SHA matches; 1080 × 1080; 10 seconds; complete decode succeeds; browser loads the video. | **Partial.** The short animation exists. Its delivery as a login-panel asset remains unproved. Test responsive fit, muted looping, a useful still/reduced-motion treatment and any separate HTML CTA. Reggie did not demand a particular aspect ratio or a new login application. |
| In-app popup, graphic and copy | [Popup](../../../packages/camp_tix_launch_001/01_channel_run/popup/popup.html), original vector graphic, copy JSON, accessible dialog and close/dismiss controls. | **Partial.** The draft is visually coherent; dismissal and reopening work in the local review. It uses Tix identity with adapted Vista styling. The chosen popup reference was not a verified Vista announcement popup. Targeting and dismissal persistence remain integration work. Barry must judge the client rendition. |
| Campaign bonus | [Calendar](../../../packages/camp_tix_launch_001/01_channel_run/campaign/calendar.json), CSV and actual LinkedIn, X and Threads copy; 11 planned slots across two weeks, including IG/TikTok placement. | **Substantial draft.** The campaign has a common source, varied channel jobs, dates, audiences, gates and a measurement plan. Media placements carry open dependencies. List suppression and tracking are planning fields. There is no scheduled or measured campaign, which is consistent with v1's publishing boundary. |

A completed source package for the original trial should make all six outputs review-ready for the selected real feature. Existing Tix approval receipts identify Gabe. They confer no Barry approval for Vista work. Reggie's request for a review-ready package does not mean every asset must already have Barry's final sign-off before presentation; the implemented review path must make his decision possible and binding before anything goes out.

## Prioritized findings

### F-01 / P1: the complete generation workflow remains unfinished

Both n8n workflows return preparation packets. The four-channel workflow explicitly returns `execution_authorized: false`, `human_approval_granted: false` and `authentication_verified: false`. A fresh local run with the actual Tix inputs reproduced `ready_for_operator` and four concrete work packets. The [handoff](../../../handoff/ENGINEER-START-HERE.md) lists provider execution and durable job state as the next build phase.

Reggie's workflow requirement covers retrieval, chained execution, validation and retries from one ingest. Frozen source validation is implemented; automatic retrieval of the release folder's Loom, outline and footage through all six outputs is unproved. Scripts render existing authored JSON. They do not generate a new release package. Finish the source-to-worker-to-review path, then demonstrate all six lanes with stored job receipts and a revision. A hosted web app, particular database or specific provider is an implementation choice; demonstrable non-engineer operation and review are the acceptance requirements.

### F-02 / P1: no observed non-engineer end-to-end run or full-run recording

The UI opens an existing campaign. It has no source-ingest or generation trigger. Python setup and packet preparation require an engineer or agent operator. The actual page successfully displays all 11 review items, and local change-request notes survive a reload. That test covers local feedback persistence only. There is no persistent worker run to resume.

No full-run recording was identified in the repository or the supplied handoff archive. The 55-second concept film and the 10-second animation are output assets. Capture the raw-folder-to-package run after implementation, with generation waits edited out transparently. Retain the matching source revision and job evidence. Have a marketing or product operator repeat the run without builder intervention. The trial presentation date is September 9.

### F-03 / P1: client scope and voice acceptance remain open

Tix is explicitly an internal test. There is no inspected acceptance from Reggie that it replaces a real feature release for the original trial. The current writing avoids claims that Vista owns Tix, which is correct.

The selected email voice packet says it used public feature writing and no private newsletter corpus. The broader repository does contain one Barry email seed, labeled as supplied by Reggie. Its historical source provenance was not re-authenticated here; it is still an available reference that the current lane did not select. The next email pass should compare against that seed and any supplied newsletters. One sample cannot establish consistent voice across all segments. Popup style is inferred from public login/brand material. Obtain the actual announcement reference or have Barry assess the draft explicitly.

For a current comparator, the official [Vista Work launch article](https://vistasocial.com/insights/vista-work-social-media-project-management/) opens with availability and access, then explains specific actions with product images. The Tix draft gives more space to generic buying advice. This is an editorial fit issue for the trial. Palette values were checked against [Vista's brand page](https://vistasocial.com/brand-assets/); palette agreement alone cannot establish brand voice.

### F-04 / P1: concept-film approval must remain separate from product accuracy

The written ledger holds live marketplace search, delivered notifications and consumer wallet purchasing. The film depicts marketplace candidates and a continued search, then a wallet limit and approval flow. At 28.0 seconds, the visible UI says “Keep looking and alert me.” At 36.0 seconds, it shows a spending limit and order approval. These inspected frames have no visible simulation or roadmap label. The surrounding blog describes the film as the intended experience, and the public website calls it a concept film. Standalone IG/TikTok distribution may lose that context.

Before a social export, inspect the whole spoken script against the held claims and add an explicit concept/preview treatment wherever needed. Use current product evidence if describing live behavior. Preserve the previously approved creative master and review a separate rendition. This audit makes no finding that a transaction occurred. Creative approval and a source claim are different evidence types.

### F-05 / P2, fixed: the article verifier fails in a recipient checkout

After `route_packets.py` regenerated the local route, `blog/evidence/verify.py` failed one of its 92 original checks: `bound_file` for `../routing/blog.json`. The stored digest described a builder-local file with absolute paths. Moving the workspace changes those bytes. The main 93-check package command still passed before this deeper check was run because it did not invoke the article verifier.

The fix invokes the canonical router against the actual request and source files, checks its readiness and selected role, and compares the portable context digest. It retains the original route hash as historical evidence. Default verification now writes no report; `--write-report` is explicit. Package verification calls this deeper check. Five regression tests cover relocation without a route file, changed article/source bytes, a forged route and report-write behavior.

### F-06 / P2, fixed: current handoff guidance contains stale or misattributed requirements

The video preparation README calls 30 seconds a limit from the brief. The supplied v2 brief contains no numeric limit. The finishing and video references now identify this as the repository's internal target. The renderer policy remains unchanged.

`docs/HUMAN-GAPS.md` previously described the social video, animation and popup solely as stubs. That describes historical fixtures and conflicts with the later Tix artifacts. The file now starts with current human responsibilities and unfinished implementation; the historical assessment remains labeled below it.

### F-07 / P2: operational approval and safe export need evidence

The review page labels browser notes as intent and has no publishing connection. Request changes requires feedback; Save note preserves that request; reopening the page preserves it. This is a useful review interaction. Actual reviewer identity, durable event ordering, stale-event rejection at export, and stored worker state are deferred.

The human role is defined in instructions, but the operational chain must enforce it. Test the recipient system with stale approval, changed source bytes, duplicate callbacks and restart during a render. Show that the wrong version cannot be exported as approved. A legacy `--human-confirmed` boolean remains a documented fixture limit. This audit did not treat it as authenticated approval.

## Copy and creative feedback for the next review

| Asset | Keep | Suggested revision |
| --- | --- | --- |
| Blog | Clear example, restrained claims, source-bound paragraphs, local images and useful preview qualifications. | Reduce repetition about item/location/budget and generic camera advice. Lead with the specific release change, explain what readers can use now and separate future work in a short section. For Vista, use the actual feature and access route. |
| Lead SMB / Agency emails | Distinct equipment versus client-shoot contexts; one CTA per variant. | Tie each opening to the real feature's benefit and available action. Compare cadence and closing with the supplied Barry seed. |
| Reseller / Affiliate email | Avoids invented commissions, margins or entitlements. | Establish the recipient's real relationship. The current copy addresses buyers and content recommenders broadly; it does not prove a partner announcement. |
| Customer SMB / Agency emails | Practical return-to-product exercises. | Replace waitlist acquisition with a verified customer action for a real release. Confirm eligibility, and suppress recipients for whom the CTA is irrelevant. |
| Changelog | Short copy and explicit simulation boundary. | State the shipped change and release date only when supported. General product positioning belongs in the blog. |
| Popup | Legible graphic, contained message, one action, visible dismissal and working reopen. | Have Barry compare it to a real Vista announcement. Test the smallest intended surface, keyboard focus and suppression rules in the receiving app. |
| Film / animation | Playable masters, recorded hashes, visible captions in film and finished visual identity. | Produce separate target renditions after claim review. Check the complete audio mix and captions together; validate mobile reading and login loop behavior. |
| Campaign | Coherent sequence and actual written social drafts. | Add recipient mappings and tracking configuration after the destination is tested. Keep the dates proposed until the assets clear review. |

## Verified evidence and limits

- Baseline automated results reproduced: 72 engine tests, 15 UGC preparation cases, 23 channel preparation cases, five loader tests, 78 matching generated entry points and 93 package checks over 86 files. The channel workflow matched source/registry/schema. The additional baseline check verified eight claim spans and seven source/observation/creative files.
- Both original repository manifests matched: 331 release entries and 196 documentation entries. All 467 archived files matched the original commit, with no missing tracked files. The archive omits the separate media by design. These counts describe the original snapshot; this PR changes the manifests.
- Browser exercise covered all 11 navigation items, desktop popup inspection, a 390-pixel mobile viewport, an empty change-request error, change-note persistence after reload, and popup dismiss/reopen. No browser errors were recorded in this exercise. This is targeted UI coverage, not a complete accessibility or email-client certification.
- Both media masters passed full FFmpeg decoding and matched the recorded SHA-256 values. Film: `1e73f611ecaacaa9aabe1b3cfdc53f571888573ae876aebb65674ad2903604d2`. Animation: `f16b7cfda2d6ef8671fc2add7a404cf77be321dffec56503a1326b387bb7b76a`. Visual sampling covered the timeline, with exact decoded checks at 28 and 36 seconds. Full human listening, every caption-to-word alignment and rights clearance were not repeated here.
- The live [Tix destination](https://tixmancer.xyz/) opened and its waitlist button exposed a form. No personal data was entered and no submission was made. Collection, deduplication and storage remain unverified. The web fetch of the changelog comparator failed; its current rendering is not claimed as checked.
- PR #40 was open, draft and mergeable at the inspected head, with both Socket checks successful. Those GitHub checks cover their declared security scopes. They do not execute the trial or establish editorial quality.
- Recipient n8n cloud execution, paid provider generation, CMS import, ESP rendering, authenticated Barry review, live folder ingestion and a new-release replay were not performed. No publishing, sending, deployment or new generation spend occurred.

## Checks after the suggested fix

The final local suite passed **77 engine tests**, including the five new recipient regressions; **15** UGC preparation cases; **23** channel preparation cases; **five** loader tests; **94** article checks; and **94** package checks over **86** files. All **78** generated entry points match. Re-running the documented render and review builders kept the package valid. Detailed command output is retained in [test-results.json](test-results.json). The negative tests restore altered local inputs and confirm successful verification after restoration. That recovery is limited to this local file seam.

## SDS release review

A1 recorded the load-bearing claims. B1 defined the corrected verification seam. B2 and C1 examined the workflow and human operation in [control review](control-review.md). A2 ran on the current design in [pre-mortem](pre-mortem.md). The operational index is [sds-project.json](sds-project.json). The evaluation separates source support, exact citations, tool outcomes and human judgment; passing one dimension cannot substitute for another.

| C3 gate | Status | Evidence / action to reopen |
| --- | --- | --- |
| Blast radius | Pass for audit scope | Isolated checkout; private review PR; no publishing or provider execution. This scope pass grants no live-release authority. |
| Truth | Fail | Full-trial completion is contradicted by the missing runtime; film claims need rendition-level review. Verify one complete real-release run. |
| Structure | Not evidenced | Preparation contracts pass offline tests; provider, persistence and export boundaries lack integrated evidence. |
| Human | Pending | Local feedback works. Non-engineer operation and assigned-reviewer decisions need a recipient run. |
| Governance | Pending | User authorized local fixes and a PR. Barry's client review and Reggie's acceptance of any substitute demo scope remain open. |
| Evidence | Not evidenced | No complete run, worst-case runtime test or tested operational rollback. A local verification regression test is narrower than operational rollback. |
| Kill switch | Not evidenced | No running recipient worker was available to test pause/cancel and recovery after an uncertain provider result. |

**State:** release review. **Trigger:** verify the handoff against Reggie's brief. **Action:** A1, B1, B2, C1, A2 and C3 artifacts retained with tests and local fixes. **Posture:** NO-GO for full-trial completion; developer review can proceed. **Next:** the receiving engineer implements the source-to-worker-to-review path and retains a complete six-output run. Gabe resolves the demo scope with Reggie; Barry owns client copy and creative approval. This audit accepts no residual production risk.
