# N01: Tix source, voice and approval baseline

Status: scoped for the current N01 continuation. Acceptance evidence is produced by the baseline work. This specification does not record a completed Claims Lock or an approved first article.

Plan: [NEXT-STEPS (historical)](../NEXT-STEPS.md). Current media evidence: [CHECKPOINT](../CHECKPOINT.md). Execution ticket: [N01 ticket](../tickets/N01-tix-source-baseline.md).

## Problem and result

The next writer needs one current Tix source set, selected expression references and a precise account of prior approvals. Older fixture copy, an authored product scene and a current code checkout establish different things. Mixing them would let the article describe a vision or an untested operation as a working feature.

Produce a checked baseline in `packages/camp_tix_launch_001/00_baseline`. Its `baseline.json` maps the actual brief, source, claim, voice, approval, request and check filenames. Keep one canonical copy of each evidence item. The first writer receives those selected inputs and the actual gate status. N01 creates no article, email, changelog, popup or new media.

## User stories

1. As the operator, I want the current committed source and live observations identified separately, so that I can explain what each statement proves.
2. As the evidence editor, I want each selected claim tied to exact source text, so that I can check its wording and qualifiers.
3. As the writer, I want a specific reader, purpose, voice reference and CTA, so that the first article can start from a usable brief.
4. As Gabe, I want my accepted media and their approval scope preserved, so that source preparation does not reopen completed creative work.
5. As the next agent, I want unresolved claims and the real Claims Lock state recorded, so that I can continue without inventing permission or blocking unrelated work.

## Scope and decisions

Use campaign `camp_tix_launch_001`, product `tixmancer` and requested reviewer `gabe`. Tixmancer is the internal validation product. Prospector remains the separate client-demonstration source. Vista and Reggie references supply expression context only when selected for that campaign; they cannot establish Tix facts or become the publisher's personal experiences.

The source owner supplies the current Tix repository and revision. Freeze selected committed files through their Git revision, recording original repository-relative paths and exact file hashes. The older intake is comparison evidence. A dirty working tree, live page and test receipt each get their own dated entry rather than inheriting the commit's identity. A live page proves only the observed content or interaction described in its receipt. Code presence alone proves no deployed runtime behavior.

Keep the accepted film and animation unchanged. Recheck the current files against the hashes already recorded in CHECKPOINT and retain the actual decision references. The standalone film remains a 55-second creative approval; the animation remains a 10-second square creative approval. Their later social and login-format work stays in N06/N07.

## Required evidence pieces

These are logical pieces. `baseline.json` maps them to the filenames used by the evidence owner; the specification does not require renaming an existing file.

| Piece | Minimum content |
| --- | --- |
| Baseline index | Campaign/product IDs, baseline version, preparation timestamp, source revision, file map, first-writer target and current completion/gate status |
| Source manifest | Source ID, origin kind, original path or URL, commit or observation time, copied path, byte SHA256 and what the source can establish; separate entries for committed, uncommitted and live evidence |
| Claim register | Stable claim ID, proposed statement, source ID, exact quote and character span, evidence basis, required qualifier, eligible/held/excluded use and reason; preserve contrary or missing evidence |
| Voice profile | Actual publisher, selected sample IDs/origins, independently written expression rules, first-person boundaries and channel gaps; mark every sample as expression evidence |
| Campaign/first-writer brief | Reader, job, article purpose, product/release scope, proposed angle, CTA wording and destination, voice-profile ID, selected claim IDs and explicit exclusions |
| Approval index | Actual actor, decision reference, exact subject/version/hash, scope and current applicability; separate existing creative acceptance from the current Claim Ledger's decision |
| Specialist requests | One source-review request and one prepared blog-draft request using the existing strict request schema |
| Check receipt | Commands or equivalent exact checks, inspected source versions, results, current media-hash match and unresolved items; separate mechanical checks from editorial judgments |

The five future email test audiences are `lead_smb`, `lead_agency`, `lead_reseller_affiliate`, `customer_smb` and `customer_agency`. Record them as requested writing contexts. They establish no existing Tix customer segment, subscription tier, reseller agreement or affiliate incentive. If a segment benefit has no evidence, hold that benefit while preserving the test context.

Classify claim basis explicitly, for example source-stated behavior, code present, observed runtime, approved product vision or unknown. Preserve the statement's limits: an approved vision statement may be eligible only as vision. Estimates, service availability, automated purchases, wallet operations, savings, pricing and launch dates require their own supporting evidence before the writer can state them as facts.

## Fit with the current contracts

Use [specialist-request/v1](../../engine/specialists/request.schema.json) as the executable request envelope. Extra classification and approval fields stay in the indexed evidence pieces because the schema rejects additional properties. No production schema or helper change is required for N01.

For source review, use `deliverable: blog`, `stage: source`, `requested_reviewer: gabe` and the actual selected source revision and voice profile. Source objects use `kind: fact` or `kind: voice`. Their paths resolve inside the release workspace. All objects use the campaign's product ID; sample origin and authorship remain explicit in the voice manifest. Include the selected claim spans and voice IDs. `artifacts` is empty and the target is absent or null because there is no blog artifact yet.

For the prepared first-writer request, use the same evidence identity with `stage: draft`. Select only eligible, supported claim IDs and the chosen voice samples. The operator retains the accompanying brief, qualifiers and actual gate record. A successful route projection establishes input consistency; it cannot authorize writing through an unresolved Claims Lock.

Hash exact bytes. Claim spans are zero-based Unicode character offsets, with an exclusive end, matching `source_bytes.decode('utf-8')[start:end]` in the helper. Do not normalize line endings between hashing and slicing. A selected quote must match exactly. A matching quote still needs an editorial check that it supports the proposed statement.

The legacy [ClaimLedger schema](../../engine/schemas/claim_ledger.schema.json) accepts only `loom_transcript`, `github_outline` and `footage_index` source types. Its [validator](../../engine/scripts/validate_ledger.py) checks structure and span shape without reading the referenced files. Keep the richer baseline claim register explicitly identified as baseline evidence. Do not call it legacy-schema compliant or relabel live HTML as a GitHub outline to make validation pass. A legacy projection is unnecessary for N01.

The [route helper](../../engine/scripts/specialist_route.py) can inspect source requests and prepared draft requests. A source-stage projection has no artifact subject, while [specialist-result/v1](../../engine/specialists/result.schema.json) requires one. Record source-review findings in the baseline check receipt; do not invent an article artifact or claim result-schema validation for those findings.

Existing approvals remain valid for their exact scope. If the current claim set has no applicable human Claims Lock, record that state and the concise decision needed next. This is an existing workflow gate, not a new interview about settled product choices. N01 may finish with a complete baseline and a pending Claims Lock. An optional voice example, unknown provider entitlement or later app decision does not block baseline completion.

## Acceptance criteria

| ID | Pass condition | Evidence |
| --- | --- | --- |
| AC01 | The baseline index resolves every required piece and uses one campaign/product/source identity consistently. | Index and file-reference check |
| AC02 | Selected committed files match the recorded Git revision and byte hashes; live or uncommitted evidence is separately dated and classified. | Manifest and source-copy checks |
| AC03 | Every selected claim has an exact matching quote with valid Unicode offsets and a reviewed statement/qualifier relationship. Held and excluded claims remain outside the writer's eligible list. | Claim register and check receipt |
| AC04 | At least one selected fact source and one usable expression source are available to the prepared blog route. An unavailable channel sample is recorded as a voice gap. | Request, voice profile and route projection |
| AC05 | No voice item serves as factual claim evidence. Publisher, sample author and actual reviewer remain distinguishable. | Source kinds, voice IDs and editorial check |
| AC06 | The brief names a reader, job, purpose, scope, angle and CTA; all five future email contexts are recorded without invented benefits or entitlements. | Brief and exclusions |
| AC07 | Both accepted media hashes match current files; approval records preserve their exact scope. No media bytes or original decision receipts change. | Hash check and approval index |
| AC08 | The source request routes to the evidence editor and the prepared draft request routes to the blog editor through the existing helper. Both retain false generation/human-approval authority. | Saved command outputs |
| AC09 | No draft or fake artifact is created to satisfy request/result schemas. N01 findings are identified as baseline review evidence. | File inventory and receipt |
| AC10 | Current Claims Lock applicability is explicit. A missing decision is pending; old creative approval, a requested reviewer name and route success cannot mark it approved. | Approval index and first-writer gate state |
| AC11 | Every copied source is appropriate for the package. No secrets, private account data, full private conversations or purchased skill prose enter the baseline. Private media locations stay in the private receipt. | Scoped content review |
| AC12 | N02 receives the file map, prepared request, brief, eligible claims, voice profile, qualifiers and exact unresolved decision, if any. | First-writer handoff section in the index or brief |

If a core fact source or usable voice reference is absent, record a held baseline with its exact missing item rather than inventing it. That is a truthful result but does not pass AC04. The current source/voice choices can be used without asking Gabe to select Tix or Prospector again.

## Verification and completion

Set the helper workspace to `packages/camp_tix_launch_001/00_baseline`. Resolve each request filename from `baseline.json`, then run the existing command for the source and prepared draft packets:

```text
.venv/bin/python engine/scripts/specialist_route.py route REQUEST_PATH --workspace packages/camp_tix_launch_001/00_baseline
```

The check receipt records the concrete commands used, their outputs and the baseline source hashes. Confirm that the source route selects `evidence_editor`, the draft route selects `blog_editor`, and both outputs retain `generation_authorized: false` and `human_approval_granted: false`. Inspect the quotes for meaning after the mechanical pass. No broad test-suite run or live provider call is needed for this evidence-only ticket.

Completion means AC01 to AC12 pass and the baseline is ready for its recorded next decision or N02 preparation. It does not mean the article is written or the Claims Lock was granted. Report the selected source revision, the two preserved approvals, eligible versus held claims, voice limitations and the exact next action.

## Outside N01

Output drafting, new media, app code, n8n mutation, provider setup or spending, publishing, engineering-schema expansion and GitHub mutations are outside this evidence task. The operator owns board and Git changes under the existing authorization. The N01 phase does not close the later copy work in issue #26 or the client's source and Barry gates.
