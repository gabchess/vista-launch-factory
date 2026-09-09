# Barry review card — camp_vista_work_001

**Campaign:** camp_vista_work_001 — Vista Work — Wed hero (Barry email seed)
**Seat:** Barry VP Marketing (writer ≠ Barry)
**Surface:** Notion + Drive pack (Email example 2 seed)
**Package status:** `review_ready_pre_claims_lock`
**Campaign status:** `claims_gate`
**Claims Lock:** NOT DONE — campaign still at claims_gate / pre-Claims-Lock
**First real (non-HELD) spot-check:** O2 blog
**Fixture label:** `barry-email-seed`

## Honesty

This package is a **pre-Claims-Lock review bundle**. Barry Claims Lock is still required before pack-approve.

## Slots

| Slot | Type | Package path | Spot-check | State |
|---|---|---|---|---|
| 1 | social_video | 01_social_video/HELD.txt | skip (HELD) | HELD — NO video — no real Loom/UI footage; Demo Assets must not enter Claim Ledger (ADR 0001) |
| 2 | blog | 02_blog | required first (first real non-HELD slot) | real draft |
| 3 | email_segments | 03_email_segments | after first-real spot-check | real draft |
| 4 | changelog | 04_changelog | after first-real spot-check | real draft |
| 5 | login_animation | 05_login_animation/HELD.txt | skip (HELD) | HELD — No real login footage/Lottie source — held for claim-safety |
| 6 | in_app_popup | 06_in_app_popup/HELD.txt | skip (HELD) | HELD — No real popup graphic/copy source — held for claim-safety |
| 7 | campaign_plan | 07_campaign_plan/HELD.txt | skip (HELD) | HELD — Campaign Plan drafts from the same Claims Lock — Barry Claims Lock not yet recorded (ADR 0016) |
| 7 | campaign_plan | 07_campaign_plan/ | in pack-approve gate | Campaign Plan |
| — | cadence binder (Campaign Plan data shape) | cadence/ | after pack spot-check | binder |

## Review links (real drafts)

- Blog (slot 2): `02_blog/`
- Email segments (slot 3): `03_email_segments/`
- Changelog (slot 4): `04_changelog/`
- Claim ledger + sources: `provenance/`
- Honesty table: `honesty/still-needs-human.md`
- Pack-approve template: repo `barry/approve-pack-template.md`
- Claims Lock template: repo `barry/claims-lock-template.md`

## Decision

- [ ] **Claims Lock approve** (once per campaign) — required before adapters are treated as ship-gated
- [ ] **Approve pack** — only after Claims Lock + first-real-slot spot-check
- [ ] **Request changes** — name artifact slot(s) only (no silent rewrite-as-approve)

## Forbidden

- Slack thumbs / emoji as Claims Lock or pack approve
- Auto-publish / one-click ship
- HubSpot send (sandbox draft-only only after Barry pack approve)
- Inventing pricing, seats, or dollar-savings claims
