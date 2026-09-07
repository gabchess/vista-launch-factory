---
name: launch-factory
description: "Vista Social GTM launch pack — release folder to review-ready package with Barry HITL."
---

# Launch Factory

Vista Social GTM launch operations Augment.

Turn a feature release folder into a gated, review-ready launch package. Retrieve from source materials, lock claims with Barry, fan out adapters, validate ≤2, and package with honesty. This is launch ops support, not a publisher.

## Trust / Do-not

**Do:**

- Trace every claim to release-folder evidence (outline, transcript, approved docs).
- Stop for **Claims Lock (Barry once)** before generators fan out.
- Keep Writer / adapters separate from Barry approval.
- Name HOLD stubs for slots 1 / 5 / 6 in every package.
- Prefer validate ≤2 then escalate with a gap list.

**Do not:**

- Auto-publish to CMS, changelog, login, in-app, or social.
- Auto-send email or HubSpot campaigns.
- Invent features, limits, pricing, or competitive claims.
- Treat CIO / orchestration tools as Vista’s ESP.
- Treat folder presence as “Augment active.”
- Ship `maintainer-source` behaviors as runtime.
- Claim all six outputs are review-ready while 1/5/6 are held.

## Run spine

1. Ingest release folder.
2. Retrieve + voice.
3. **Claims Lock (Barry once).**
4. Adapters: real path for blog / email / changelog when engine live; **HOLD stubs** for social video, login animation, in-app popup.
5. Cadence binder (bonus) from same Claims Lock — still no publish.
6. Validate ≤2.
7. Barry pack approve.
8. Package + honesty. HubSpot sandbox only last, only with authorized tooling after Barry.

## Engine

Canonical SoT is sibling `engine/` at product root (**Option B — A3 wired**):

- `engine/schemas/` — claim ledger, release campaign, cadence binder
- `engine/scripts/` — `validate_ledger.py`, `validate_campaign.py`, `build_package.py` (**STRUCTURAL_INTEGRITY_ONLY**; no publish)
- `engine/adapters/`, `engine/fixtures/`, `engine/barry/`, `engine/honesty/`

This skill's `schemas/` directory is a **thin pointer** only — do not create a divergent third schema set. When Python is available, Run may invoke engine structural validators; Claims Lock honesty and Barry HITL still apply. Slots 1/5/6 remain HOLD.

## Never publish

Drafting is not publishing. Packaging is not sending. Barry (or delegated authorized human) remains the gate.
