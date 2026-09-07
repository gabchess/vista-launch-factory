# Provenance

## Canonical sources

This Augment pack is built from:

1. **Vista Social trial brief** — feature-release folder → launch outputs + Campaign Plan; Barry VP Marketing as HITL gate.
2. **Factory engine (vista/work SHOW-ME spine)** — schemas, validators, adapters, fixtures, barry templates, and honesty notes, consolidated under repo-root `engine/` (Option B single SoT; ADR 0012 moved the pack envelope to the repo root in v0.2.0, and the former repo-root developer spine was deduplicated into `engine/` — hashes compared, one copy kept).
3. **This pack** — customer envelope, skill door, docs, manifests, and honesty surfaces authored for Launch Factory v0.2.0.
4. **ADR 0012–0016** (`docs/adr/`) — recorded-run hero + repo-link door, HOLD discipline, one-command door, interim Voice Bank, Campaign Plan as seventh output.

## What this is not derived from

Domain content, personas, knowledge bases, and deal-strategist materials from third-party finished packs are **not** sources for Launch Factory. Only the **package layout and claim-discipline pattern** (install door, dual-host, custody manifests, aligned HITL surfaces) informed the skeleton. Demo packages under repo-root `packages/camp_*` are run outputs, not engine SoT.

## Synthetic / placeholder material

Engine fixtures (`engine/fixtures/demo-release`, `engine/fixtures/vista-work`) are **labelled fixtures** (mock release folders). They do not invent live Vista pricing. Slots 1/5/6 remain HOLD honesty stubs (ADR 0013). ADR 0001: Demo Assets ≠ Claim Ledger. The Voice Bank brief is an **interim placeholder** (ADR 0015) until the corpus at `voice-bank/` lands.

## Custody note

`maintainer-source/` is for maintainers only and must never ship as customer runtime.
