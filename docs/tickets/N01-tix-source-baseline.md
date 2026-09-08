# N01: prepare the Tix source, voice and approval baseline

**Execution phase:** current user-authorized continuation. **Blocked by:** none. **Owner:** Nova/operator with the evidence editor. **Independent verifier:** Forge. **Specification:** [N01-tix-source-baseline.md](../specs/N01-tix-source-baseline.md).

**Tracker mapping:** execute this phase through [#26 — [A12] Voice pack refresh then copy lane pass](https://github.com/gabchess/vista-launch-factory/issues/26). Link [#6](https://github.com/gabchess/vista-launch-factory/issues/6) for source/access context and [#12](https://github.com/gabchess/vista-launch-factory/issues/12) for the actual client Claims Lock. Forge reconciles the board and keeps one live ready execution phase. This document does not claim that a label changed. Completing N01 leaves the later copy work and outstanding client gates open.

## Result

Create a first-writer baseline at `packages/camp_tix_launch_001/00_baseline`. Its index maps the chosen source snapshots, claim register, voice profile, brief, approval evidence, specialist requests and check receipt. Keep the accepted Tix film and animation unchanged. N01 prepares inputs for the blog; N02 writes it.

## Work sequence

1. Read the specification, current source-owner findings and CHECKPOINT. Confirm the selected Tix commit and compare it with the older intake. Freeze selected committed files without mixing dirty working-tree changes into that revision. Keep live observations separately dated.
2. Build the source manifest and claim register. Hash exact bytes and check each eligible quote using zero-based Unicode character offsets. Review whether the statement follows from the evidence. Preserve qualifiers and held claims.
3. Select the Tix expression references and write a brief with publisher, reader, purpose, proposed angle, scope and CTA. Record the five requested email audiences as later test contexts. Keep Reggie/Vista expression material separate from factual proof and from the actual publisher's experiences.
4. Verify both current media files against the approved hashes in CHECKPOINT. Index the existing decisions and exact scope. Record the current claim set's actual Claims Lock state independently.
5. Prepare strict `specialist-request/v1` source-review and blog-draft packets. Map their actual filenames in `baseline.json`. Both use `product_id: tixmancer`, `campaign_id: camp_tix_launch_001`, `deliverable: blog` and `requested_reviewer: gabe`. No blog artifact exists yet.
6. Run the existing route helper for both requests with this baseline as the workspace. Record concrete commands/results, then complete the editorial claim/voice check. Deliver the baseline and the next decision or first-writer action.

## Acceptance checklist

- [x] The baseline index resolves all evidence pieces with consistent IDs and the selected source revision.
- [x] Source-copy hashes match the chosen committed bytes; live/uncommitted observations have separate provenance.
- [x] Every selected quote matches its stated Unicode span and supports the statement with its required qualifiers.
- [x] Held/unknown claims are excluded from eligible writer inputs; product vision and authored UI are not promoted to observed execution.
- [x] The prepared writer request has usable fact and voice sources, with voice samples excluded from factual evidence.
- [x] The brief contains reader, job, purpose, proposed angle, scope and CTA. Five email contexts are listed without fabricated tiers or partner terms.
- [x] The accepted film and animation retain their exact hashes, original receipts and approval scope.
- [x] Existing helper outputs select the evidence and blog roles as expected and retain false generation/approval authority.
- [x] The baseline check receipt contains real findings; no fake article or claimed source-stage result-schema pass is used.
- [x] The current Claims Lock state is accurate. A pending decision remains visible without reopening settled creative approval.
- [x] The packet contains no secrets, private account details, private conversation dump or purchased skill text.
- [x] N02 can locate its prepared request, brief, eligible claims, voice inputs, qualifiers and any pending human decision from the index.

These checkboxes correspond to AC01–AC12 in the specification. A remaining human Claims Lock can be the next action after N01 completes; it does not require a new product interview. A missing core source or usable voice input is an explicit held result and leaves its acceptance item open.

## Verification and handoff

Use `.venv/bin/python engine/scripts/specialist_route.py route` on the concrete request files with `--workspace packages/camp_tix_launch_001/00_baseline`. Record both exact commands in the check receipt. Mechanical success covers hashes, paths, selected source kinds and quote spans. The evidence editor separately assesses meaning and qualifiers.

Return the baseline path, chosen source revision, eligible/held claim summary, two media-hash checks, voice limitations and exact next action. Forge independently verifies the evidence and reconciles this phase on #26. Keep only this execution phase active until it is handed off.

No output drafting, paid work, new media, n8n changes, app scaffolding, production schema changes or publication belongs to this ticket. Other agents own their files; preserve concurrent work. GitHub and Git mutations remain Forge's responsibility.

Independent verification: Forge passed AC01–AC12 for the completed baseline. Both specialist routes retain false generation and approval authority. The actual writing Claims Lock remains pending; later copy work and client gates remain open.
