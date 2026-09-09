# Operate Launch Factory

## Runtime spine

1. **Marketer run.** Point the operator at a release folder.
2. **Ingest and retrieve.** Read the Loom transcript, outline, footage, and brand
   references.
3. **Voice pack.** Check drafts against Vista's actual voice, not generic AI tone.
4. **Claims Lock (Barry, once).** See `barry/claims-lock.md`. Every claim must trace to a
   source. Never invent pricing, features, or limits.
5. **Draft the first real adapter.** That's the blog post (slot 2). Don't wait on a held
   slot to start.
6. **Spot-check that artifact.** See `barry/spot-check.md`. The order is always: draft the
   first real output, then Barry spot-checks it, then draft the rest. Never spot-check
   before a draft exists.
7. **Draft the remaining adapters.** Email (3) and changelog (4). Skip any held slot for
   now; see the slot map below.
8. **Validate, at most twice.** Run the structural and claim-ceiling checks. If a check
   still fails after one fix-and-retry, stop and escalate to a human instead of looping
   forever.
9. **Barry approves the pack.** See `barry/pack-approve.md`, the copy-and-creative gate.
10. **Package and write the honesty note.** Name every held slot. Send an email through
    the HubSpot sandbox only as a draft, only last, and only after Barry's approval and
    authorized tooling.

Keep one campaign in progress at a time. Drafting is not the same as Barry's approval.
Nothing in this spine auto-publishes.

## Skipping held slots

A slot marked held is skipped for now, not blocked forever:

- Don't wait on a held slot to finish a run.
- Write an honesty note for each held slot, and keep going.
- The first real adapter is the blog post (slot 2), then email (3) and changelog (4).
- Never fake a held output to make the package look complete.

## Slot map (v0.2.0)

Slot 7 is the Campaign Plan (see [ADR 0016](adr/0016-orchestrator-and-campaign-plan.md)):
a day-by-day, multi-channel sequence drafted from the same locked claims.
`cadence_binder.json` is its data shape.

| Slot | Output | Status | Rule |
|---|---|---|---|
| 1 | Social video + burned captions | Approved creative for Tix; concept preview only for Vista Work (no private footage) | Skip when held |
| 2 | Blog | First real adapter | Draft this first |
| 3 | Email (segments) | Real adapter | After blog |
| 4 | Changelog | Real adapter | After blog |
| 5 | Login animation | Approved creative for Tix; concept preview only for Vista Work (no private footage) | Skip when held |
| 6 | In-app popup | Real adapter | Draft after email and changelog |
| 7 | Campaign Plan | Adapter `07_campaign_plan.md` | One-release scope only; approved in the pack gate |

## Engine

The canonical schemas, validators, and adapters live under `engine/`. Don't fork a second
schema tree elsewhere.

## Scripts

All executable helpers live under `engine/scripts/`: `init_release.py`,
`validate_record.py`, `transition_slot.py`, `validate_ledger.py`, `validate_campaign.py`,
and `build_package.py`. They validate structure only. They never publish, and moving a
slot to `approved` or `packaged` requires Barry's recorded decision
(`--human-confirmed`). The one-command door is `./run.sh RELEASE_FOLDER` (see
[ADR 0014](adr/0014-one-command-one-prompt.md)). Any scripts under
`codex/launch-factory/scripts/` follow the same rule.
