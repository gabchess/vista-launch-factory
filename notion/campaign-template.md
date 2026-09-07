# Notion — Campaign DB field map (pilot SoT)

One row per `ReleaseCampaign`. Drive holds blobs; Notion holds status + Barry queue.

| Notion property | Type | Maps to | Notes |
|---|---|---|---|
| Name | Title | `title` | e.g. FIXTURE — FEATURE_NAME launch |
| campaign_id | Rich text | `id` | `camp_demo_001` |
| folder_id | URL / text | `folder_id` | Drive folder once Reggie shares |
| status | Select | `status` | idle → … → closed (see schema enum) |
| fixture_label | Rich text | `fixture_label` | Non-empty = labelled fixture |
| claim_ledger | Files / URL | `claim_ledger_ref` | JSON in Drive |
| voice_pack_ref | Text | `voice_pack_ref` | |
| cadence_ref | Text / URL | `cadence_ref` | |
| artifact_1..6 | Files | `artifacts[].path` | Or linked Drive subfolder |
| barry_seat | Text | `barry.seat` | const Barry VP Marketing |
| barry_surface | Select | `barry.surface` | Notion + Drive pack (v1) |
| barry_wip | Number | `barry.wip` | **Must be 1** |
| hubspot_sandbox_status | Select | `hubspot_sandbox.status` | not_started / draft_only / blocked_no_barry / skipped |
| still_needs_human | Multi-select / text | `still_needs_human[]` | Honesty list |
| Run launch | Button | trigger | See `trigger/notion-run-leavebehind.md` |

**WIP rule:** only one campaign in `awaiting_barry` at a time (`barry.wip=1`).

**Not in Notion:** Customer.io as ESP; production HubSpot publish; Temporal run ids.
