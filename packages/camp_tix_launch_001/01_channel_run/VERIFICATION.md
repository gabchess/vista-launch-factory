# Verification for the channel run

Verified on 8 September 2026. New drafts are awaiting Gabe. These checks do not grant human approval or establish a live client deployment.

## Source and writing

The existing specialist router accepted all five current packets: blog, email, changelog, popup and campaign. It checked the selected source files, exact SHA-256 values, Unicode quote spans and voice references against the frozen Tix workspace. The external style references are original style analysis, separate from product claims.

The blog has 837 whitespace-separated Markdown words and 29 mapped content blocks. Its own verifier passed 92 checks. Both article images came from the exact accepted creative and were inspected. The metadata includes a 57-character SEO title and a 142-character description. AgentsKit's brand and SEO helpers ran; their generic keyword suggestions did not override source accuracy or the observed feature-post format. See [blog review](blog/REVIEW.md).

The email set has five distinct bodies, subjects, preheaders, reader jobs and paragraph claim maps. The changelog uses the observed short feature-update format and preserves preview status. Matt's independent semantic read found no substantive unsupported product claim in those six pieces. No existing customer base or affiliate program is asserted.

The popup has an original SVG, complete copy and self-contained HTML. Its source references, script syntax, SVG text widths and minimum CTA contrast of 4.74:1 passed local checks. See [popup notes](popup/NOTES.md).

## Browser inspection

The root operator used the Codex in-app browser to inspect the real local review at `http://127.0.0.1:8770/01_channel_run/review.html`.

- The full article, an email variant, changelog and popup rendered with their actual content and source panels.
- The popup and changelog were inspected at 390px iframe width. Text and artwork remained legible. Mobile mode stayed applied when changing the selected asset.
- The embedded popup initially took focus through native `dialog.show()`. That was corrected; a reload and selection retained focus in the outer review page without forcing scroll.
- In the standalone popup, Maybe later and the close button dismissed the modal and returned focus to Meet Tix. Reopening moved focus to the heading.
- Request changes refused empty feedback. A temporary QA note retained its Changes state after more detail was saved and after reload. The test note was cleared through the UI. No human approval was applied.
- A hash-only navigation initially changed the URL without changing the displayed asset. A hashchange listener corrected that path; the calendar and popup deep links were rechecked in the browser.

The 390px check covers each artifact's narrow rendering inside the review. It is not a mobile-device or full screen-reader certification. Native Escape and keyboard trapping are present in the implementation; a complete assistive-technology pass did not run. No waitlist form was submitted. Prior media acceptance is preserved through exact file hashes; this pass did not repeat the complete audio/visual review of the approved masters.

## Automation and independent review

The four-channel preparation passed 23 JavaScript cases and five Python loader cases. A fresh run with the actual Tix request packets returned `ready_for_operator` with four assigned work packets. See [real-input receipt](verification/preparation-run.json) and [workflow validation](../../../automation/n8n/channel-production/VALIDATION.md).

Independent review found and closed malformed-field, revision-counting and caller-authority issues in preparation. It also closed review-context reuse, feedback-state loss, wrong-media attachment and mobile-width persistence issues. [Detailed findings and retests](verification/independent-review.md).

No cloud n8n run, model dispatch, provider render, authenticated approval event or automatic export was executed by the new preparation flow. Its authority flags remain false. The already saved video workflow is a separate preparation stage.

## Package integrity

Run `python3 packages/camp_tix_launch_001/01_channel_run/verify_package.py` to recheck the current files, source routes, channel counts, review bindings and full batch manifest. Review hashes cover the visible rendition and its supporting files. Current source/voice context is part of each binding. The two media records retain their accepted binary SHA-256 values.

After intentional changes and review, `--write-manifest` records a new file snapshot. It does not approve the new version. The repository's tests and manifest checks are also run during the verifier's commit closeout; the resulting commit receipt records their final counts.
