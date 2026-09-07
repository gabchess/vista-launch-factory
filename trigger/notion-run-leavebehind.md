# Non-engineer Run trigger — leave-behind

**Demo default:** Notion button on Campaign row → “Run launch”.
**Brain:** Grok-crew (not Gumloop, not Temporal).
**Gumloop / Drive:** document for handoff; do not require for Wed hero.

## Notion (demo)
1. Property `Run launch` button on campaign row (`notion/campaign-template.md`).
2. Button sets status `ingested` and posts a checklist comment: folder_id, claim_ledger link, WIP check.
3. Orchestrator (crew) picks up from Notion/Drive — marketer does not open a terminal.
4. Status visible on same row through `awaiting_barry`.

## Gumloop (leave-behind)
- Form: folder URL in → status out.
- Trigger only — not the claims brain.
- Install path already available; wire after Notion demo path is solid.

## Drive label (leave-behind)
- Label/tag on release folder watched by crew routine.
- No Temporal watcher.

## Handoff must name
- Who clicks Run (marketing)
- Where Barry Approves / Request Changes
- How to re-run one output
- Builder ≠ maintainer
