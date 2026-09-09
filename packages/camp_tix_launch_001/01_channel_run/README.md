# Tix: channel production and review

This run completes the four missing output categories as drafts. Tix provides product facts; Vista Social's actual Insights, changelog and login pages provide the explicitly requested channel style. The two accepted video renditions remain unchanged.

Open [review.html](review.html) through `serve_review.py` to see all outputs in one place. The page includes the full article, five email previews, changelog and popup. A calendar connects them with proposed dates and written social drafts. Source, voice, version and hash records stay next to each asset.

| Output | Actual files | Current review |
| --- | --- | --- |
| Blog | [Article](blog/article.md), [HTML](blog/article.html), [metadata](blog/metadata.json), two bundled images | Pending Gabe |
| Segmented email | [Five variants with claim maps](email/emails.json), one Markdown/HTML/JSON set per segment | Pending Gabe per variant |
| Changelog | [Entry](changelog/entry.md), [HTML](changelog/entry.html), [metadata](changelog/entry.json) | Pending Gabe |
| In-app popup | [Preview](popup/popup.html), [graphic](popup/graphic.svg), [copy](popup/copy.json) | Pending Gabe |
| Campaign | [Calendar + social copy](campaign/calendar.json), [CSV](campaign/calendar.csv) | Proposed, unscheduled |
| Product film | Accepted 55-second master; exact SHA in [review data](review-data.json) | Creative approved; ≤30-second social cut still required |
| Animation | Accepted 10-second square master; exact SHA in [review data](review-data.json) | Creative approved; login-surface packaging still required |

The customer email labels represent returning preview readers in this internal test. There is no claim that Tix has paying customer cohorts or an affiliate program. A real campaign needs actual audience mapping. All CTA destinations use the canonical Tix address; collection is checked before sending or publishing.

## Review procedure

1. Open an asset and inspect its actual copy or creative. Use Mobile preview to check the narrower layout.
2. Mark ready, request a specific change or save a note. Export the review notes, or give the operator your decision in chat.
3. The operator applies the actual human decision to its exact subject. Browser notes alone are not an authenticated approval.
4. A requested revision goes to the named specialist and returns as a new version. Preserve unchanged assets. Source or voice changes invalidate affected review bindings.
5. Review the final calendar and export package after the individual outputs are accepted. Version 1 never auto-publishes.

Local feedback uses the campaign, asset, version, review hash and source/voice context. Notes do not overwrite a prior request for changes. The proposed calendar dates can move without redrafting unchanged content.

## Reproduce this review

From the repository root after installing `requirements.txt` in `.venv`:

```bash
python3 packages/camp_tix_launch_001/01_channel_run/route_packets.py
python3 packages/camp_tix_launch_001/01_channel_run/render_copy.py
python3 packages/camp_tix_launch_001/01_channel_run/build_review.py
python3 packages/camp_tix_launch_001/01_channel_run/serve_review.py
```

Open `http://127.0.0.1:8770/01_channel_run/review.html`. The server accepts optional `--film` and `--animation` paths, checks them against their accepted hashes and serves only the explicit files. The four new drafts work without those external media masters or an API key.

`build_review.py` binds the visible rendition and its supporting files. Editing one email updates that email's binding; shared article imagery also binds the changelog that uses it. Rebuild after any intended change, then record a new artifact version before another human review. The renderer reads each artifact version from its metadata, including per-segment email overrides. A production service must own version allocation and persist the review history.

## Reuse in the automation

The four original prompts live in [channel production](../../../engine/specialists/channel-production/README.md). Existing LF role banks point to them. [Four-channel n8n preparation](../../../automation/n8n/channel-production/README.md) validates the packets and creates work instructions for the operator. It does not generate the assets by itself.

The [engineer handoff](../../../handoff/ENGINEER-START-HERE.md) explains installation, credentials, provider boundaries and the next app-to-worker slice. [Authorization](AUTHORIZATION.md) records why this batch drafted all four outputs before a combined human review. The historical baseline decision remains unchanged.

The [verification record](VERIFICATION.md) distinguishes local checks, browser inspection and untested external integrations. [PACKAGE-MANIFEST.json](PACKAGE-MANIFEST.json) records the exact committed batch files. Generated absolute-path routing receipts remain local; their portable input packets and source bytes are included.
