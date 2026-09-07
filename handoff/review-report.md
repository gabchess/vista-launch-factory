# Independent SOP review report

## Reviewed state

- **SOP / document ID:** Vista Social Launch Factory — Marketer Handoff SOP / `VISTA-LF-HANDOFF-001`
- **Version or SHA-256:** `0.1.0` / SHA-256 `efc1351d4792d488c3424e56bc52d34b99ac61f10be261c85d1846b71a5bb4d5` (independently re-hashed 2026-09-07; matches packet bind)
- **Status and risk tier:** Working Draft; Tier 2 Enhanced (R=36 in supplied `risk-assessment.yaml`; S4×O3×V3)
- **Target operator and intended use:** Vista marketing Run operator (clicks Run); Barry HITL ship gate; Gabe/Reggie for access, ownership, cut-order. Intended use = release folder → Barry-ready package (+ optional HubSpot sandbox drafts); stop before publish. Fixture-labelled path until Reggie real sources.
- **Evidence set supplied:**
  - Canonical SOP: `work/handoff/VISTA-LAUNCH-FACTORY-HANDOFF-SOP.md`
  - `source-register.csv`, `assumption-and-gap-log.csv`, `risk-assessment.yaml`, `marketer-run-checklist.md`, `REVIEW-PACKET.md`, `lint-report.json` (handoff copies)
  - Workspace: `vista/sop-workspace/` (companions, governance, reconstruction `current-state-vs-canonical.md`, evidence working copies + `source-manifest.json`, checks, builder-closeout)
  - Referenced operating companions confirmed present under `vista/work/` (Barry templates, honesty, HubSpot checklist, trigger leave-behind, fixture + FIXTURE_LABEL, validators/package scripts, schemas)
- **Deterministic checks supplied or run:**
  - Supplied `lint-report.json`: 0 errors, 0 warnings
  - Independent re-run: `scripts/lint_sop.py` on the bound SOP → **0 errors, 0 warnings** (JSON written to reviewer temp; agrees with supplied report)
  - Independent SHA-256 verification: match to packet bind
- **Capabilities not exercised:** DOCX/PDF render; link-crawler beyond manual relative-path spot-check; live Notion/Drive/HubSpot execution simulation; operator walkthrough with real credentials; qualified legal/domain claim audit of Vista product facts (fixture only)

**Credit rule applied:** Only reviewed files, declared capabilities, and context an operator/approver will possess. Crew tribal knowledge, unsent Reggie answers, and unwired UI are **not** credited as available.

## Verdict

**Conditional pass**

**Authority:** Recommendation on readiness for owner approval; not operational approval or authorization to distribute.

**Basis:** For Tier 2, this exact Working Draft encodes Gabe-locked Scope B / recorded HOW / Barry HITL / no-publish / CIO≠ESP / fixture-until-Reggie with visible gaps, decision rights, exceptions with re-entry, checklist, and clean independent lint. It is **not** a Fail: the fixture path is operable as a labelled procedure design, and material uncertainties are declared rather than laundered into false certainty. It is **not** a clean Pass: process owner and distribution approver remain UNRESOLVED (G11); Reggie G1–G10 (especially G10 off-limits) block real-feature use; and several operator-facing seams (Notion Run wiring, who runs local validators/package without a terminal, broken companion relative paths, unnamed Writer lead / Tom in tables) remain as bounded conditions. **Not Approved for Distribution. Not Ready for Owner Review** until conditions below are disposed or explicitly accepted in a bounded owner decision object.

## Findings

| ID | Classification | Review evidence | Operational consequence | Required disposition | Owner | Observable closure |
|---|---|---|---|---|---|---|
| R1 | Owner decision | Frontmatter `owner` / `approver` UNRESOLVED; Evidence basis G11; risk-assessment `process_owner` / `approval_authority` UNRESOLVED; gap log G11 open | No named custody for feedback, maintenance, or distribution approval; status cannot honestly advance to Ready for Owner Review / Approved for Distribution | Name process owner + SOP distribution approver (or explicit interim sponsor with expiry) before seeking distribution approval | Gabe / Reggie | Metadata and gap G11 show named seats; approval-record can bind version+hash to those names |
| R2 | Unavailable evidence | Gap log G1–G10 open; `questions-for-reggie.md` unanswered / do-not-send; reconstruction: fixture remains labelled; G10 critical for off-limits claims | Real Reggie folder / brand / sandbox / feature / Barry surface / formats / off-limits list unavailable; inventing would breach Claims Lock controls | Keep fixture-labelled path only until answers land; seed forbidden list before any real Claims Lock; treat live swap as re-Claims Lock gate | Gabe (send) / Reggie (answer); Barry for claims seed | G1–G10 closed or explicitly deferred with fixture_label forced; G10 forbidden list present for real ledger |
| R3 | Specification / authority ambiguity | SOP: marketer “does not open a terminal”; Systems table lists local `validate_*.py` / `build_package.py`; step 11 “Operator/crew”; leave-behind: orchestrator (crew) picks up Notion | Alone, the named marketer cannot complete validate/package steps as written without crew/automation the packet does not prove is live | Document the runnable handoff: which actor runs validators/package, from which surface, when crew is absent; or wire non-terminal Run→validate→package path | Process owner (once named); Builder implements | Checklist/SOP name a non-terminal verify path **or** an on-call crew role with channel; marketer dry-run completes without undocumented help |
| R4 | Unavailable evidence | `notion-run-leavebehind.md` + campaign-template describe demo Button; reconstruction: marketers not yet day-to-day operators; no evidence of live Notion DB with working Run launch | Operator may not find a clickable Run control; “demo default” may be aspirational | Confirm durable trigger (Notion vs Gumloop vs Drive — G12) exists for the rehearsal audience before calling the path marketer-executable | Gabe / Reggie / ops | Campaign row (or alt trigger) demonstrated once; trigger used recorded on row |
| R5 | Implementation defect | References section paths `../sop-workspace/companions/*` from `work/handoff/` do not resolve (needs `../../sop-workspace/…`); handoff-folder copies of companions do exist | Reviewer/operator following SOP-relative companion links from handoff lands on missing path; relies on “also under handoff/” aside | Fix relative links in a later draft **or** point only to same-folder companions | Builder (editorial) | From `work/handoff/`, every References path resolves; re-lint |
| R6 | Authority ambiguity | Decision D7 cites “Tom advises order”; exception E5 cites “Writer lead”; neither appears in Roles and decision rights table | Escalation/advice may dead-end or invent a seat under time pressure | Add Tom / Writer lead to Roles with boundaries, or retarget D7/E5 to named existing roles | Process owner / Gabe | Roles table includes every decider named in Decision/Exception tables |
| R7 | Non-blocking improvement | Terms (first use) is a single dense paragraph mixing HOW/STOP/HITL/WIP/ESP/CIO and document-name glosses; older lint warnings on DESIGN/STOP were cleared in this version (independent lint 0/0) | Scan cost and first-use friction for a new marketer under interruption | Optional glossary table in a later editorial pass; do not reopen control design for this alone | Builder | Operator can locate term definitions without reading one mega-paragraph |
| R8 | Non-blocking improvement | Effective date blank; feedback route → UNRESOLVED owner; approval-record blank supplied in workspace only | Expected for Working Draft; blocks controlled distribution, not fixture rehearsal design review | Fill on owner approval event; do not fake dates | Named approver at decision time | Approval record binds version/hash, scope, audience, accepted uncertainty, conditions |

## Conditions and unresolved boundaries

**Bounded conditions for advancing toward owner approval (not distribution):**

1. **G11 / R1:** Gabe/Reggie name SOP process owner and distribution approver (or time-boxed interim sponsor).
2. **G1–G10 / R2:** Reggie/Gabe gaps remain **conditions on live/real Vista claims**. Fixture-labelled rehearsal may proceed under existing stop rules; real-folder swap requires answered access gates + re-Claims Lock; **G10 forbidden-list seed is mandatory before real Claims Lock**.
3. **R3–R4:** Before asserting marketer-solo day-to-day Run, confirm (a) who runs validate/package without terminal tribal knowledge, and (b) which Run trigger is actually available to the operator.
4. **R5–R6:** Repair companion relative paths and align Roles with D7/E5 actors in the next builder pass (may be same revision that satisfies R1 metadata).

**Explicitly out of scope / not credited:** Live product claim truth beyond fixture; HubSpot production; CMS publish; DOCX/PDF derivatives; unsent Reggie questionnaire as answered.

**Ready for Owner Review:** **No** (Conditional pass with open ownership and Reggie/live-path conditions; status remains Working Draft).

**Approved for Distribution:** **No** — reviewer has no authority to grant; conditions unmet.

## Verdict validity

This verdict applies only to reviewed version **0.1.0** / SHA-256 **`efc1351d4792d488c3424e56bc52d34b99ac61f10be261c85d1846b71a5bb4d5`**, the evidence set listed above, dependencies in `vista/work/` companions referenced by the SOP, and declared capabilities (lint performed; render/execution simulation **not** performed).

Reopen affected review claims when: process logic or Barry HITL sequence changes; evidence basis or Reggie answers materially change live-path controls; risk/control design changes; approval scope/audience changes; operator-facing Run/validate/package instructions change; or SHA-256 of the canonical Markdown changes. Editorial-only glossary/path fixes that cannot alter execution need not reopen the whole verdict if R1–R4 dispositions are otherwise unchanged — but any ownership, trigger, or claims-control edit **does** reopen.

Reviewer did **not** rewrite the SOP and does **not** approve distribution.
