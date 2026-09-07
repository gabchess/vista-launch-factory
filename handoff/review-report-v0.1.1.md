# Independent SOP review report

## Reviewed state

- **SOP / document ID:** Vista Social Launch Factory — Marketer Handoff SOP / `VISTA-LF-HANDOFF-001`
- **Version or SHA-256:** `0.1.1` / SHA-256 `c38f1603c8de2b80c78229ecf2af234264bb6da5bd7346974ef03ecb093169e0` (independently re-hashed 2026-09-07; matches packet bind and `risk-assessment.yaml`)
- **Status and risk tier:** Working Draft; Tier 2 Enhanced (R=36 in supplied `risk-assessment.yaml`; S4×O3×V3; unchanged)
- **Target operator and intended use:** Vista marketing Run operator (clicks Run / confirms rehearsal); Barry HITL ship gate; Gabe/Reggie for access, ownership, cut-order. Intended use = release folder → Barry-ready package (+ optional HubSpot sandbox drafts); stop before publish. Fixture-labelled path until Reggie real sources.
- **Evidence set supplied:**
  - Canonical SOP: `work/handoff/VISTA-LAUNCH-FACTORY-HANDOFF-SOP.md` (v0.1.1)
  - Same-folder companions: `source-register.csv`, `assumption-and-gap-log.csv`, `risk-assessment.yaml`, `marketer-run-checklist.md`, `REVIEW-PACKET.md`, `lint-report.json`, `README.md`
  - Workspace: `vista/sop-workspace/` (companions mirrors, reconstruction `current-state-vs-canonical.md`, evidence working copies + `source-manifest.json`)
  - Operating companions under `vista/work/` (Barry templates, honesty, HubSpot checklist, trigger leave-behind, fixture + FIXTURE_LABEL, validators/package scripts) — relative paths from handoff spot-checked as present
  - Prior review (context only; void for this SHA): `review-report.md` (0.1.0 / prior SHA)
- **Deterministic checks supplied or run:**
  - Supplied `lint-report.json`: 0 errors, 0 warnings
  - Independent re-run: `scripts/lint_sop.py` on the bound SOP → **0 errors, 0 warnings** (agrees with supplied report)
  - Independent SHA-256 verification: match to packet bind
  - Relative References path resolution from `work/handoff/`: same-folder companions, `../../sop-workspace/companions/*` mirrors, and `../` work-tree refs all resolve (prior R5 broken `../sop-workspace/...` pattern absent)
- **Capabilities not exercised:** DOCX/PDF render; automated link-crawler beyond manual relative-path spot-check; live Notion/Drive/HubSpot execution simulation; operator walkthrough with real credentials; qualified legal/domain claim audit of Vista product facts (fixture only)

**Credit rule applied:** Only reviewed files, declared capabilities, and context an operator/approver will actually possess. Crew tribal knowledge, unsent Reggie answers, and unwired UI are **not** credited as available.

## Verdict

**Conditional pass**

**Authority:** Recommendation on readiness for owner approval; not operational approval or authorization to distribute.

**Basis:** For Tier 2, this exact Working Draft still encodes Gabe-locked Scope B / recorded HOW / Barry HITL / no-publish / CIO≠ESP / fixture-until-Reggie with visible gaps, decision rights, exceptions with re-entry, checklist, and clean independent lint. **v0.1.1 repairs for prior R3–R7 actually landed** (see credit block below) and remove the prior operator-facing path/roles/terms defects as open implementation findings. It is **not** a Fail: the fixture + manual-rehearsal path is operable as a labelled procedure design, and material uncertainties remain declared rather than laundered into false certainty. It is **not** a clean Pass: process owner and distribution approver remain UNRESOLVED (G11); Reggie G1–G10 (especially G10 off-limits) still block real-feature use; G12 durable post-Wed trigger remains undemonstrated (honest manual rehearsal is documented until proof). **Not Approved for Distribution. Not Ready for Owner Review** until remaining conditions are disposed or explicitly accepted in a bounded owner decision object that names custody.

### Credit — prior R3–R7 repairs (closed for this SHA)

| Prior ID | Landed in 0.1.1? | Review evidence |
|---|---|---|
| R3 no-terminal vs validators | **Yes** | Prerequisites row “Validate / package capability”; Systems table labelled crew-run/manual demo; steps 3/11/14 assign crew run + marketer row confirm; checklist Ready/Execute/Close; “Never claim unattended automation live”; gap A4 `closed-editorial-0.1.1` |
| R4 Notion Run wiring | **Yes (honesty + fallback)** | Notion labelled demo leave-behind / not evidenced live; step 3 demonstrated-trigger vs `manual_rehearsal` fallback; `trigger_used` record; C7 + G12 proof gate before “live”; reconstruction aligned. **Residual:** G12 durable pick still open (condition, not reopened as path-ambiguity defect) |
| R5 companion paths | **Yes** | References point to same-folder companions + resolving `../../sop-workspace/companions/*`; all listed refs from handoff resolve; broken single-up `../sop-workspace/` pattern gone |
| R6 Tom / Writer lead | **Yes** | Roles table adds Tom (D7 contingency adviser, bounds) and Writer lead/Scribe (E5); D4/D7/E5 name those seats; gap A5 `closed-editorial-0.1.1` |
| R7 Terms density | **Yes** | Terms replaced dense paragraph with glossary table; no scope drift observed; independent lint remains 0/0 |

## Findings

| ID | Classification | Review evidence | Operational consequence | Required disposition | Owner | Observable closure |
|---|---|---|---|---|---|---|
| R1 | Owner decision | Frontmatter `owner` / `approver` UNRESOLVED; Evidence basis G11; risk-assessment `process_owner` / `approval_authority` UNRESOLVED; gap log G11 open; Governance feedback route → UNRESOLVED owner | No named custody for feedback, maintenance, or distribution approval; status cannot honestly advance to Ready for Owner Review / Approved for Distribution | Name process owner + SOP distribution approver (or explicit interim sponsor with expiry) before seeking distribution approval | Gabe / Reggie | Metadata and gap G11 show named seats; approval-record can bind version+hash to those names |
| R2 | Unavailable evidence | Gap log G1–G10 open; `questions-for-reggie.md` unanswered / do-not-send; reconstruction: fixture remains labelled; G10 critical for off-limits claims | Real Reggie folder / brand / sandbox / feature / Barry surface / formats / off-limits list unavailable; inventing would breach Claims Lock controls | Keep fixture-labelled path only until answers land; seed forbidden list before any real Claims Lock; treat live swap as re-Claims Lock gate | Gabe (send) / Reggie (answer); Barry for claims seed | G1–G10 closed or explicitly deferred with fixture_label forced; G10 forbidden list present for real ledger |
| R3 | Unavailable evidence / owner decision | G12 open in gap log + Evidence basis; Notion Run still not evidenced live; reconstruction: marketers not yet day-to-day operators | Path may be called “live” without a demonstrated durable trigger; marketer-solo day-to-day Run remains aspirational | Keep manual rehearsal as honest default until one trigger demonstrated once with `trigger_used` proof; Gabe/Reggie/ops pick durable post-Wed surface | Gabe / Reggie / ops | Demonstrated trigger + row proof; durable Notion vs Gumloop vs Drive pick recorded; G12 closed or time-boxed |
| R4 | Non-blocking improvement | Effective date blank; feedback route → UNRESOLVED owner; approval-record blank in workspace assets only; minor G12 state-label mismatch (gap log “Bounded assumption” vs Evidence basis “Unresolved fact”) — both treat as open | Expected for Working Draft; blocks controlled distribution, not fixture rehearsal design review | Fill on owner approval event; optionally align G12 state label; do not fake dates | Named approver at decision time | Approval record binds version/hash, scope, audience, accepted uncertainty, conditions |

## Conditions and unresolved boundaries

**Bounded conditions remaining (expected):**

1. **G11 / R1:** Gabe/Reggie name SOP process owner and distribution approver (or time-boxed interim sponsor).
2. **G1–G10 / R2:** Reggie/Gabe gaps remain **conditions on live/real Vista claims**. Fixture-labelled rehearsal may proceed under existing stop rules; real-folder swap requires answered access gates + re-Claims Lock; **G10 forbidden-list seed is mandatory before real Claims Lock**.
3. **G12 / R3:** Durable post-Wed Run trigger unresolved. Manual rehearsal + demo-leave-behind honesty in 0.1.1 is acceptable for Working Draft; do not assert marketer-live until demonstrated trigger + proof on row.

**Closed vs prior 0.1.0 review (do not reopen as defects unless prose regresses):** prior R3 (validate/package actor), R4 path-honesty (Notion demo + fallback), R5 companion paths, R6 Roles alignment, R7 Terms table.

**Explicitly out of scope / not credited:** Live product claim truth beyond fixture; HubSpot production; CMS publish; DOCX/PDF derivatives; unsent Reggie questionnaire as answered; unattended automation as live.

**Ready for Owner Review:** **No** (Conditional pass with open ownership G11 and Reggie/live-trigger conditions; status remains Working Draft).

**Approved for Distribution:** **No** — reviewer has no authority to grant; conditions unmet; do not distribute.

## Verdict validity

This verdict applies only to reviewed version **0.1.1** / SHA-256 **`c38f1603c8de2b80c78229ecf2af234264bb6da5bd7346974ef03ecb093169e0`**, the evidence set listed above, dependencies in `vista/work/` companions referenced by the SOP, and declared capabilities (lint performed; render/execution simulation **not** performed). Prior 0.1.0 verdict in `review-report.md` is **void** for this SHA.

Reopen affected review claims when: process logic or Barry HITL sequence changes; evidence basis or Reggie answers materially change live-path controls; risk/control design changes; approval scope/audience changes; operator-facing Run/validate/package instructions change; or SHA-256 of the canonical Markdown changes. Editorial-only glossary/path tweaks that cannot alter execution need not reopen the whole verdict if R1–R3 dispositions above are otherwise unchanged — but any ownership, trigger, or claims-control edit **does** reopen.

Reviewer did **not** rewrite the SOP and does **not** approve distribution.
