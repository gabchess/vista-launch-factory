# Provenance: Voice Bank (INTERIM per ADR 0015)

**Collection date:** 2026-09-07 (all items retrieved_date 2026-09-07).
**Collector:** an internal research agent, for the Vista Launch Factory project.
**Status:** INTERIM voice bank. Superseded when Vista's real brand guide arrives (ADR 0015).

## Method

- **Web research tools only:** `web_search` (queries: `site:vistasocial.com insights`, `"Reggie Azevedo" "Vista Social"`, `site:x.com OR site:twitter.com vistasocialapp`, `site:linkedin.com/posts "Vista Social"`, `site:linkedin.com/posts/reggieaze`) and `web_extract` (direct fetch + text extraction of public URLs).
- **One internal fixture:** the Barry approval-queue email, copied verbatim read-only from `vista-launch-factory/fixtures/vista-work/sources/barry_email_transcript.txt`, internal email provided by Reggie, used as voice seed per ADR 0015. It is the only non-public item and is labeled as such in corpus item `01`.
- **Excerpts are verbatim.** Where extraction introduced artifacts (line-break splits in headlines, mojibake on LinkedIn emoji), wording was preserved and artifacts normalized or marked `[sic]`. Elisions in long posts are explicit `[…]`. Nothing is paraphrased inside an excerpt block.
- **Login walls respected:** no logins were used anywhere. LinkedIn public-post views and search-indexed profile data were the limit; anything behind a login was logged in `gaps.md` instead of guessed. Instagram snippet (item `25`) is from a search index, marked LOW CONFIDENCE.
- **No fabrication:** zero invented quotes. Items that could not be verified as real and current were excluded and noted in `gaps.md`.

## Guarantees

- **Public sources only** (except the single Barry fixture, provided to the project by Reggie).
- **No Vista personal data:** no private customer data, no employee personal information, no contact details. Reggie's public professional headline/location as indexed by search engines is the most personal data present.
- **No scraped private content:** nothing behind a login, paywall, or bot-wall was circumvented.
- **Read-only discipline:** the vista-launch-factory repo was not modified; only the one fixture file was read. All work lives in the voice-bank staging workspace.

## Corpus inventory (25 items)

| source_type | count | items |
|---|---|---|
| email | 1 | 01 (Barry seed) |
| website | 12 | 02 to 11, 23, 24 |
| social (X + podcast transcript + Instagram snippet) | 8 | 12 to 16, 21, 22, 25 |
| linkedin | 4 | 17 to 20 |

Voice attribution: 20 items company-voiced (Vista Social), 5 items Reggie-voiced (11, 20, 21, 22, 25, labeled in each file's notes), 1 Barry-voiced seed (01). Item 25 is dual-purpose (Reggie personal social). Podcast items 21 to 22 are Reggie spoken; the podcast host is Barry (Plugable).

## Derivation chain

`tone-and-style-brief.md` is derived **only** from the corpus files; every observation cites the corpus filename(s) it came from. `gaps.md` records what could not be collected and what to request from Reggie.
