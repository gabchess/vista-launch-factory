# ADR 0015: Voice Bank from public + Barry material, labeled interim

Date: 2026-09-07. Status: accepted (Gabe, grill round 1).

## Decision

Build a **Voice Bank**: Barry's approval-queue email (the seed), public
vistasocial.com copy, Vista Social's social channels and LinkedIn, and Reggie's LinkedIn
posts. Scrape/collect once, store as a corpus in the repo (`voice-bank/`, public sources
only), and derive a tone-and-style brief from it. Every voice judgment cites a bank item.
The bank is labeled **interim** until Reggie's brand guide + newsletter examples land
(issue #6).

## Why

GRILL-LOCK #4 already ruled one real letter beats a guessed brand guide. The brief's
voice test ("reads like we wrote it") needs more than one email to be defensible, and
public content is the only other Vista-authored voice we can touch without internal
access. Gabe stays out of the corpus (GRILL-LOCK #6: no Gabe voice in Vista material).

## Consequences

- Voice check becomes a real validation step: adapter output vs. bank-derived style
  brief, with a human (Barry) as final arbiter, not a similarity score as truth.
- Corpus is public-only; no scraped personal data ships in the pack (ship-bar rule).
- Honesty doc states "voice derived from interim public corpus, not Vista's internal
  brand guide."
