# Human gaps (honesty first-class)

Launch Factory v0.1.0 is an installable Augment with a **wired Option B engine**. Be explicit about what still needs a human and what is held.

## Barry-required

- Claims Lock approval (once) before fan-out.
- Final pack approve for copy + creative.
- Any publish or send decision (outside this pack).

## HOLD — slots 1 / 5 / 6

| Slot | Output | Honesty |
|---|---|---|
| 1 | Social video + burned captions | **HOLD** — stub only; no zoom-on-still as “video”; real encode later |
| 5 | Login animation | **HOLD** — stub only; no inventing motion copy without source |
| 6 | In-app popup | **HOLD** — stub only; no mock-as-proof |

Do **not** claim Wed or trial success as “all six review-ready” while these are held. Name the HOLD in every package and recording note.

## Engine (Option B — A3 wired)

`engine/` is the live Option B SoT: schemas, validators (`validate_ledger` / `validate_campaign` / `build_package`), adapters, fixtures, barry templates, honesty. Structural scripts are **STRUCTURAL_INTEGRITY_ONLY** — they validate/package; they are not brand or legal judgment and they never publish.

Still human: Claims Lock, pack approve, publish/send decisions. Slots **1 / 5 / 6** remain HOLD (ADR 0001: Demo Assets ≠ Claim Ledger).

## Dual-host

Claude ZIP is present (`claude/launch-factory-v0.1.0.zip`) with Codex skill door. Fresh-host activation remains unverified — see HOST-MATRIX. Folder/ZIP visible ≠ Augment active. Claude ZIP must not fork a second schema tree; canonical schemas stay under `engine/`.

## Still human for good reasons

- Brand taste above claim ceiling.
- Legal/security-sensitive wording.
- Segment strategy judgment beyond template email slots.
- Whether a release is ready to launch at all.
