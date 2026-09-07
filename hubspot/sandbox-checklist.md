# HubSpot sandbox — last step checklist (Apiana hygiene)

**Order:** only after Barry pack approve on email artifacts.
**Account:** Reggie sandbox invite — not production.
**CIO:** ours only — never demo as Vista ESP.

## Before opening HubSpot
- [ ] Campaign status is `approved` or `packaged` (not `awaiting_barry`)
- [ ] Email adapter (O3) claims ⊆ ledger
- [ ] Segments mapped: leads SMB/Agency/Reseller_Affiliate + customers SMB/Agency (or explicit N/A)
- [ ] MANIFEST.json has `auto_publish: false`

## In sandbox
- [ ] Create **draft** emails only
- [ ] Record `draft_ids[]` on campaign `hubspot_sandbox`
- [ ] Set `hubspot_sandbox.status` = `draft_only`
- [ ] **Do not** call publish / marketing send / production lists

## Recording
- Optional ~10s beat showing draft UI → STOP
- Say on camera: “sandbox draft; humans send later”

## Refuse
- Production HubSpot send in trial recording
- Claiming we own Vista HubSpot
- Swapping Vista ESP to Customer.io
- Export while kill-switch armed
