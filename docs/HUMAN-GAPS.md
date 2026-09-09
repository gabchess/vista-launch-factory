# Human work and unfinished implementation

Current assessment: the Tix package has reviewable blog, five emails, changelog and popup drafts, plus a proposed campaign. Two separate media masters match the recorded creative hashes. The system still needs an operator for source intake and provider execution. The recipient app, persistent approval events and complete recorded run remain unfinished. See the [SDS trial audit](audits/sds-trial-2026-09-09/REPORT.md) and [engineer handoff](../handoff/ENGINEER-START-HERE.md).

## Human decisions retained by design

Barry approves Vista copy and creative against the exact rendered version. The product owner resolves source conflicts and confirms release availability. Marketing maps real audience segments and judges whether each message fits its reader. These responsibilities continue after automation works.

## Engineering work still required

A non-engineer must be able to supply the release folder and start generation. The worker must save outputs and job state, bound retries and costs, and resume after interruption. Review must identify the authorized reviewer, preserve the version and input bindings, and invalidate affected decisions after revision. Export must use the reviewed bytes. Version 1 has no automatic publishing.

Social placement and login integration need their own checks. Capture a complete run on one real feature release, including a revision and the review-ready six-output package. Then have a new operator repeat the process. Present the observed limits with that recording.

## Historical v0.2.0 fixture assessment

The retained text below describes the original fixture route. Its stub labels do not describe the later Tix creative and popup files. Historical approvals and HOLD records remain intact.

# Original human gaps

Launch Factory v0.2.0 is an installable workflow pack with a **wired Option B engine**. Be explicit about what still needs a human and what is held.

## Barry-required

- Claims Lock approval (once) before fan-out.
- Final pack approve for copy + creative.
- Any publish or send decision (outside this pack).

## HOLD: slots 1 / 5 / 6

| Slot | Output | Honesty |
|---|---|---|
| 1 | Social video + burned captions | **HOLD**: stub only; no zoom-on-still as “video”; real encode later |
| 5 | Login animation | **HOLD**: stub only; no inventing motion copy without source |
| 6 | In-app popup | **HOLD**: stub only; no mock-as-proof |

Do **not** claim Wed or trial success as “all six review-ready” while these are held. Name the HOLD in every package and recording note.

## Engine (Option B, A3 wired)

`engine/` is the live Option B SoT: schemas, validators (`validate_ledger` / `validate_campaign` / `build_package`), adapters, fixtures, barry templates, honesty. Structural scripts are **STRUCTURAL_INTEGRITY_ONLY**: they validate/package; they are not brand or legal judgment and they never publish.

Still human: Claims Lock, pack approve, publish/send decisions. Slots **1 / 5 / 6** remain HOLD (ADR 0001: Demo Assets ≠ Claim Ledger).

## Dual-host

Claude ZIP is present (`claude/launch-factory-v0.2.0.zip`) with Codex skill door. Fresh-host activation remains unverified, see HOST-MATRIX. Folder/ZIP visible ≠ workflow pack active. Claude ZIP must not fork a second schema tree; canonical schemas stay under `engine/`.

## Still human for good reasons

- Brand taste above claim ceiling.
- Legal/security-sensitive wording.
- Segment strategy judgment beyond template email slots.
- Whether a release is ready to launch at all.
