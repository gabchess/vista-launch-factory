# Gaps: Voice Bank (INTERIM per ADR 0015)

Honest list of what could not be collected, what is missing versus a real brand guide, and what to ask Reggie for. Updated 2026-09-07.

## Could not collect (walls & limits)

1. **LinkedIn personal activity for Reggie (`linkedin.com/in/reggieaze`):** profile body, posts, and activity feed are login-walled. Only the search-indexed headline/title/location were captured (corpus `20`). No Reggie LinkedIn *posts* are in the corpus. Did not guess or fabricate any.
2. **Instagram (@reggie_azevedo and @vistasocialapp):** bot-walled; only one truncated search-index snippet of a Reggie post captured, date unknown, marked LOW CONFIDENCE (corpus `25`). No Vista Social Instagram posts in corpus.
3. **Facebook, TikTok, Bluesky company posts:** not attempted beyond search: all effectively login/bot-walled for post text; nothing verified, so nothing included.
4. **X/Twitter timeline as a whole:** only individual indexed posts could be fetched (5 captured: corpus `12` to `16`). No full recent timeline, no engagement context beyond like/RT counts on two posts.
5. **vistasocial.com/features/:** returns 404 ("Whoops!"). The site uses per-product pages instead; four of those captured (`03`, `04`, `05`, plus Vista Work). Other product pages (Engagement, Listening, Review Management, Employee Advocacy, DM Automations, AI Knowledge, Vista Page) not captured, same template, diminishing returns.
6. **Long-form X posts truncated:** `16` (Hootsuite five-reasons) captured as verbatim excerpts from head/middle/tail with elisions marked […]; full thread text not reproduced.
7. **LinkedIn company posts:** only public-post views retrievable; `18` ends at LinkedIn's "…more" truncation marker.
8. **Beyond Social podcast episode transcripts:** episode pages exist but transcripts were not retrieved (audio). Reggie's spoken voice is represented by the Plugged In interview only (`21`, `22`).

## Corpus balance issues

- **Email register is a single data point.** The Barry approval-queue email (`01`) is the only email in the corpus. The brief's email rules rest on n=1 plus adjacent website CTA patterns. Highest-priority gap.
- **Reggie-written copy is dated.** His only bylined blog post is from March 2023 (`11`) and reads more formal than current company voice. His current written voice is unrepresented; his spoken voice (2026) is well represented.
- **No customer-facing support/help-center voice** (support.vistasocial.com exists, not collected).
- **Stale item kept for comparison only**: `19` (~1 year old affiliate post).
- **Author-byline nuance**: most 2026 blog posts carry staff bylines (Orion Macapella, Vitaly Veksler), not Reggie's. Company-voiced vs Reggie-voiced is labeled per item in front matter notes.

## Missing vs a real brand guide

A genuine Vista brand guide would have, and we do **not**:

- Official tone-of-voice dimensions (e.g., "we are X but not Y" sliders).
- Approved vocabulary / banned words list (our rule 3 and 12 are inferred, not official).
- Visual/design voice pairing (colors, typography, image style), irrelevant for text adapters but part of a real guide.
- Audience personas and per-segment register (agency vs enterprise vs creator), inferred from copy only.
- Official messaging hierarchy, product naming rules, and trademark/style for "Vista Work", "Ask Vista", etc.
- Positioning claims lock (what numbers are approved for external use, repo rule: never invent Vista pricing; our corpus repeats only figures found live on their pages).
- Email program samples beyond the single seed: newsletters, launch emails, lifecycle sequences.

## What to ask Reggie for

1. The real brand guide / tone-of-voice doc if one exists (this whole bank is interim until it lands, per ADR 0015).
2. **3 to 5 more Barry emails**, especially any approval-queue series siblings, so the email register isn't n=1.
3. Permission + export of Vista's own email newsletter archive (public send samples).
4. Any internal messaging hierarchy or approved-claims list (pricing, "30,000 brands", "60% lift").
5. Reggie's own current writing samples (LinkedIn posts, internal memos) to represent his 2026 written voice, not just spoken.
6. Confirmation of author-voice mapping: which blog bylines reflect house voice vs individual writers.
7. Whether the dry-deadpan humor level (rule 10) is officially sanctioned or emergent.
