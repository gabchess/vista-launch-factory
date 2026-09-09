# Validation and limits

## Claim ceilings (v0.2.0)

- Every claim must trace to a release-folder source: an outline, a transcript, or an
  approved brand document.
- Never invent pricing, features, limits, or competitive claims.
- Validate, fix, and retry at most twice. After that, stop and hand the reviewer a clear
  gap list instead of looping.
- Don't claim every output is review-ready while any slot is held.
- The structural scripts prove package mechanics. They don't judge marketing quality or
  brand fit.
- Barry's human-review cards live under `barry/` (Claims Lock, then spot-check, then pack
  approve). A thumbs-up in Slack doesn't count as approval.

## Verified in this release

- The pack tree and custody files are present (checked by inspection).
- The "who reviews what" and "what this doesn't do" language stays aligned across
  START-HERE, the skill file, `capability-and-authority.md`, TRUST, VALIDATION, and
  HOST-MATRIX.
- Explicit exclusions: no auto-publish, no auto-send, no invented claims.
- Barry's human-review cards exist under `barry/` (`README.md`, `claims-lock.md`,
  `spot-check.md`, `pack-approve.md`), alongside the generator templates in
  `engine/barry-templates/`.
- The engine is present under `engine/`: schemas, `validate_ledger.py`,
  `validate_campaign.py`, `build_package.py`, and adapters. The validators pass locally
  against `engine/fixtures/vista-work`, and `.venv/bin/pytest -q` passes.
- `codex/launch-factory/schemas/` is a pointer only; there is one canonical schema set.

## Not verified

- Fresh-host discovery or automatic activation, on either Codex or Claude Code.
- Copy quality for blog, email, and changelog drafts. The adapters exist; nobody has
  scored their writing quality independently.
- Live HubSpot, CMS, or social behavior. Excluded by design in v1.
- Accessibility or formal compliance testing.

See also [HOST-MATRIX.md](../HOST-MATRIX.md) and [engine/README.md](../engine/README.md).
