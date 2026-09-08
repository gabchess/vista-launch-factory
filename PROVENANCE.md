# Provenance

## Canonical sources

This Augment pack is built from:

1. **Vista Social trial brief** — feature-release folder → launch outputs + Campaign Plan; Barry VP Marketing as HITL gate.
2. **Factory engine (vista/work SHOW-ME spine)** — schemas, validators, adapters, fixtures, barry templates, and honesty notes, consolidated under repo-root `engine/` (Option B single SoT; ADR 0012 moved the pack envelope to the repo root in v0.2.0, and the former repo-root developer spine was deduplicated into `engine/` — hashes compared, one copy kept).
3. **This pack** — customer envelope, skill door, docs, manifests, and honesty surfaces authored for Launch Factory v0.2.0, with the later specialist and recipe additions below.
4. **ADR 0012–0016** (`docs/adr/`) — recorded-run hero + repo-link door, HOLD discipline, one-command door, interim Voice Bank, Campaign Plan as seventh output.
5. **[ADR 0017](docs/adr/0017-specialist-routing-and-current-scope.md)** — specialist routing, selective evidence and voice references, project host entry points, and offline consistency checks. These checks grant no human approval or provider authority.
6. **[UGC App Reveal](engine/specialists/video-production/recipes/ugc-app-reveal/README.md)** — original reusable prompts drawn from one approved production run. The recipe records the actual provider roles and source-adaptation method; private media, credentials, job IDs and review conversation remain outside the portable pack. Third-party source packs informed patterns only; their prose and assets were not copied into these prompts.
7. **[ADR 0018](docs/adr/0018-ugc-app-reveal-preparation.md)** — the n8n preparation subworkflow packages the recipe and source bindings for an operator. **[ADR 0019](docs/adr/0019-testable-app-and-next-milestone.md)** records the next app milestone. This package does not implement an authenticated approval store or unattended media dispatch.

## What this is not derived from

Domain content, personas, knowledge bases, and deal-strategist materials from third-party finished packs are **not** sources for Launch Factory. Only the **package layout and claim-discipline pattern** (install door, dual-host, custody manifests, aligned HITL surfaces) informed the skeleton. Demo packages under repo-root `packages/camp_*` are run outputs, not engine SoT.

## Synthetic / placeholder material

Engine fixtures (`engine/fixtures/demo-release`, `engine/fixtures/vista-work`) are **labelled fixtures** (mock release folders). They do not establish live Vista pricing. The retained v0.2.0 fixtures and archive keep their slot 1/5/6 HOLD records from ADR 0013. Later user-authorized work follows ADR 0017 without rewriting those historical records. ADR 0001 still separates demo assets from the Claims Ledger.

The 25-item corpus at `voice-bank/` and its derived brief are present. They remain **interim voice evidence** under ADR 0015, pending Vista's official brand guide; see [collection provenance](voice-bank/provenance.md). Source facts and product claims require their own evidence.

## Custody note

`maintainer-source/` is for maintainers only and must never ship as customer runtime.
