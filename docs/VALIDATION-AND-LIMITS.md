# Validation and limits

## Claim ceilings (v0.2.0)

- Every claim must trace to release-folder source (outline, transcript, approved brand doc).
- **No invent pricing.** No invent features, limits, or competitive claims.
- **Validate ≤2** — at most two validation/repair loops before escalating to a human with a clear gap list.
- Do not claim “all six review-ready” while slots 1/5/6 are HOLD.
- Structural scripts prove package mechanics, not marketing judgment or brand quality.
- **Barry HITL cards** live under product-root `barry/` (Claims Lock → spot-check → pack approve). Slack thumbs ≠ approve.

## Verified in this release (A3)

- Pack tree and custody files present (inspection).
- HITL / non-goals text aligned across START-HERE, SKILL, capability-and-authority, TRUST, VALIDATION, HOST-MATRIX, skill README.
- Explicit exclusions: auto-publish, auto-send, invent claims.
- **A5 Barry HITL** product-root cards: `barry/{README,claims-lock,spot-check,pack-approve}.md` (coexist with `engine/barry-templates/` generator templates).
- **Engine Option B present** under `engine/` (schemas, `validate_ledger` / `validate_campaign` / `build_package`, adapters, fixtures). Local Python prove: validators OK on `engine/fixtures/vista-work`; repo-root `.venv/bin/pytest -q` 22 passed (13 spine + 9 record/plan).
- `codex/launch-factory/schemas/` is pointer-only — one canonical schema set.

## Not verified

- Fresh-host discovery or automatic activation (Codex or Claude).
- Semantic fan-out quality for blog/email/changelog (adapters present; judgment not scored).
- Live HubSpot, CMS, or social behavior (excluded).
- Grok-crew host behavior.
- Accessibility or formal compliance testing.
- A7/A8 encode/assets for slots 1/5/6 (HOLD).

See also [HOST-MATRIX.md](../HOST-MATRIX.md) and [engine/README.md](../engine/README.md).
