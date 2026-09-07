# Barry review card — camp_demo_001

**Campaign:** camp_demo_001 — FIXTURE — FEATURE_NAME launch
**Seat:** Barry VP Marketing (writer ≠ Barry)
**Surface:** Notion + Drive pack
**Package status:** `packaged`
**Campaign status:** `drafting`
**Claims Lock:** RECORDED (campaign past claims_gate)
**First real (non-HELD) spot-check:** O1 social_video
**Fixture label:** `LABELLED_FIXTURE_NOT_REAL_VISTA_PRODUCT`

## Honesty

Claims Lock is recorded on the campaign; proceed to pack-approve gates.

## Slots

| Slot | Type | Package path | Spot-check | State |
|---|---|---|---|---|
| 1 | social_video | 01_social_video | required first (first real non-HELD slot) | real draft |
| 2 | blog | 02_blog | after first-real spot-check | real draft |
| 3 | email_segments | 03_email_segments | after first-real spot-check | real draft |
| 4 | changelog | 04_changelog | after first-real spot-check | real draft |
| 5 | login_animation | 05_login_animation | after first-real spot-check | real draft |
| 6 | in_app_popup | 06_in_app_popup | after first-real spot-check | real draft |
| 7 | campaign_plan | 07_campaign_plan | after first-real spot-check | real draft |
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
