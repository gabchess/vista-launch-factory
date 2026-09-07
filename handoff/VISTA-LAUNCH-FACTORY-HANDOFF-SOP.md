---
document_id: VISTA-LF-HANDOFF-001
title: Vista Social Launch Factory — Marketer Handoff SOP
version: "0.1.1"
status: "Working Draft"
owner: "UNRESOLVED — propose Gabe (process sponsor) pending Reggie (COO) ops ownership confirmation"
approver: "UNRESOLVED — Barry VP Marketing is ship gate for packs; SOP distribution approver UNRESOLVED (Gabe/Reggie)"
effective_date: ""
review_date: "2026-09-16"
risk_tier: "Tier 2 Enhanced"
canonical_source: "VISTA-LAUNCH-FACTORY-HANDOFF-SOP.md"
supersedes: ""
audience: "Vista marketing operator who clicks Run; Barry (HITL); Gabe/Reggie owners for access and cut-order"
---

# Vista Social Launch Factory — Marketer Handoff SOP

## Operational foreground

- **Current state:** Scope B + recorded-factory HOW are Gabe-approved (2026-09-07). Working tree under `vista/work/` uses a **labelled fixture** until Reggie shares the real release folder. This SOP is a **Working Draft** — not approved for distribution. v0.1.1 repairs reviewer R3–R7 only; does not invent live automation or close Reggie/owner gaps.
- **Next consequential action:** Fresh review packet to `sop-reviewer` for v0.1.1; Gabe/Reggie decide process owner + Reggie access gates before any operator uses this as live procedure on real Vista claims.
- **Active blockers or uncertainty:** G1–G10 Reggie access/judgment; G11 process-owner / distribution-approver seats; G12 durable post-Wed Run trigger. Notion **Run launch** is a **demo leave-behind** (not evidenced as a live clickable control). Local validators/package scripts are **crew-run / manual demo** capabilities — not a marketer terminal path and not claimed live automation.
- **Authority currently required:** Gabe/Reggie for access and ownership; Barry for Claims Lock / O1 spot-check / pack approve; Gabe for cut-order fall-back to thin C; Tom advises cut-order order only (D7).


## Terms (first use)

| Term | Meaning at first use |
|---|---|
| recorded factory (HOW) | Locked delivery method: pre-bake path; no live-wait generation in the room |
| package stop (STOP) | Final procedure halt after Barry-ready package (+ optional sandbox drafts) |
| human-in-the-loop (HITL) | Barry ship gate: Claims Lock, O1 spot-check, pack approve |
| work in progress (WIP) | Max one campaign in `awaiting_barry` (`barry_wip=1`) |
| Email service provider (ESP) | Outbound email platform for Vista send — never Customer.io in this path |
| Customer.io (CIO) | Crew-only tool — never Vista ESP |
| Small and medium business (SMB) | Email segment label in cadence / O3 |
| Campaign tracking parameters (UTM) | Tracking stubs on cadence cells |
| Vice President (VP) | Barry title: VP Marketing |
| Chief Operating Officer (COO) | Reggie title |
| content management system (CMS) | Final post surface — humans publish out of band |
| User interface (UI) | Login/popup format details from Reggie |
| Instagram (IG) / LinkedIn (LI) | Cadence cell channels |
| JavaScript Object Notation (JSON) | Ledger and campaign source of truth (SoT) files |
| HyperBots agent stack (STACK) | Builder-side only — not marketer Run |
| explicit okay (OK) | Labelled human-gap posture is acceptable when honesty notes it |
| Document filenames | DESIGN-LOCK, GABE-SCOPE, and handoff readme (README) are document names, not process acronyms; design document prefix (DESIGN); design lock file (LOCK); Gabe scope file (GABE); scope document (SCOPE) |

## Purpose and outcome

This standard turns one Vista **release folder** (Loom + GitHub outline + footage) into a **Barry-ready package**: six review-ready outputs plus a one-release campaign cadence binder, with a visible claims ledger and honest human-gaps list — without inventing product claims and without auto-publishing.

**Observable done:** campaign status is `packaged` (or `sandbox_exported` if HubSpot draft beat ran); Drive package + honesty doc frozen; `auto_publish: false` in MANIFEST; humans still own CMS/changelog/login/in-app/HubSpot send out of band.

## Trigger

Marketing needs a Barry-reviewable launch pack for a named Vista feature release, **or** the team is rehearsing the Wed recorded E2E on the labelled fixture.

**Start only when** a Notion Campaign row exists (or fixture campaign `camp_demo_001` is in use) and the operator knows whether sources are **fixture** or **Reggie-real**.

## Scope and boundaries

**Included:**

- Scope **B**: outputs O1–O6 + full one-release cadence binder (tier blast cells + UTM stubs).
- HOW = **recorded factory** (pre-bake path); same spine for live operator runs after Wed.
- Claims Lock → adapters → Barry HITL → package → optional HubSpot **sandbox draft last**.
- Fixture-labelled operation until Reggie access.
- Re-run of **named** artifact slot(s) after Request Changes.
- Cut-order contingency labelling (not silent scope change).

**Excluded / routed elsewhere:**

- Auto-publish or production HubSpot send → humans out of band; refuse in this SOP.
- Customer.io as Vista ESP → never; CIO is crew-only.
- Temporal / multi-tenant SaaS orchestration → out.
- Live-wait generation in a customer room → forbidden (HOW lock).
- Inventing Vista pricing, limits, partner language, competitor compares → forbidden.
- Decision C thin spine as hero → only with explicit Gabe yes + “bonus partial” label.
- Builder maintenance of HyperBots STACK / marketplace bots → builder role, not marketer Run.
- Final CMS publish, changelog post, login asset deploy, in-app ship → human publish list (`still-needs-human.md`).

## Prerequisites and stop conditions

| Requirement | Ready condition | Evidence / location | If unavailable |
|---|---|---|---|
| Source folder | Drive folder contains Loom (or transcript), GitHub outline, footage index; **or** fixture folder with `FIXTURE_LABEL.md` | `folder_id` on Campaign; fixture at `work/fixtures/demo-release/` | Stop Run; escalate to Gabe/Reggie for folder share. Do not invent sources. |
| Fixture vs real | `fixture_label` non-empty **or** explicitly cleared after Reggie swap | Notion `fixture_label`; `FIXTURE_LABEL.md` | If unclear, treat as fixture and label every artifact. |
| Claims seed | Forbidden list present; allowed claims cite evidence spans | `claim_ledger.json` / Drive ledger link | Do not start adapters. Hold at Claims Lock. |
| Voice pack | Style guide / past newsletters bound or honesty-noted as human gap | `voice_pack_ref` | Continue only with honesty entry “voice pack encode still needs human”; do not invent voice. |
| Barry seat | Writer seat ≠ Barry seat; Barry surface known (default Notion + Drive pack) | Campaign `barry.seat`, `barry.surface` | Pause at Claims Lock / pack queue until surface confirmed. |
| WIP gate | Zero other campaigns in `awaiting_barry` (WIP=1) | Notion `barry_wip` / campaign statuses | Do not advance a second pack into `awaiting_barry`. |
| HubSpot sandbox (optional last) | Reggie sandbox invite; draft-only confirmed; Barry pack already approved | `hubspot/sandbox-checklist.md` | Skip sandbox beat; set `hubspot_sandbox.status=skipped`. Never use production. |
| Kill switch | `kill_switch.armed=false` before draft/export | Ledger | If armed → status `needs_source_fix`; adapters cold; no HubSpot. |
| Run trigger surface | Operator knows whether **demo leave-behind**, **manual rehearsal**, or **evidenced live** trigger applies | Campaign comment / row note: `trigger_used` | If Notion button not clickable / not demonstrated → use **manual rehearsal fallback** (step 3). Do **not** call path marketer-live until one demonstrated trigger + proof on row (G12). |
| Validate / package capability | Crew (or builder) available to run local `validate_*.py` / `build_package.py` **or** documented pass/fail already on the Campaign row | `work/scripts/`; validator logs | Marketer does **not** open a terminal. If crew absent and no pass recorded → hold before pack (E5). Never claim unattended automation live. |

**Hard stop conditions (do not continue):** kill-switch armed; invented claim detected; attempt to publish/send; CIO presented as Vista ESP; Slack emoji treated as Barry approve; second campaign entering `awaiting_barry` while one waits.

## Roles and decision rights

| Role | Executes | Decides / approves | Verifies | Escalation boundary |
|---|---|---|---|---|
| **Marketer (Run operator)** | Uses Notion Campaign row after trigger is available (or follows manual rehearsal); confirms folder/fixture; watches status; submits pack to Barry; confirms package after crew build; optional HubSpot draft | When to start Run / rehearsal; when to skip optional sandbox | Folder present; WIP=1; honesty doc attached; `trigger_used` noted | Does **not** open a terminal; cannot approve Claims Lock or pack; cannot publish; cannot invent a live Run button |
| **Writer / adapters (crew or tools)** | Draft O1–O6 + cadence from ledger + voice pack | None on ship | Validation scripts pass/fail | Never Barry; never silent rewrite-as-approve |
| **Barry (VP Marketing)** | Claims Lock once; O1 spot-check; pack approve / Request Changes | Allowed/forbidden claims; creative+copy ship gate | Provenance beside copy; WIP=1 | Slack thumbs ≠ approve; cannot auto-publish |
| **Gabe** | Access chase; cut-order / thin-C yes; process sponsor until ops owner named | Fall back to thin C; reopen Scope B | — | Authority for contingency labels |
| **Reggie (COO / sponsor)** | Folder/perms, brand samples, HubSpot sandbox invite, feature pick, format rules, off-limits claims | Real-feature intake; off-limits claim list | — | Blanks = keep fixture label |
| **Builder (crew)** | Schemas, validators, leave-behinds, recording bake; runs local validators/package for demos until a non-terminal path is evidenced | Implementation design inside locks | Tests / validators | **Builder ≠ maintainer** of day-to-day Run; hand maintainership to marketing ops after owner approval of this SOP |
| **Tom (contingency adviser)** | Advises cut-order drop sequence when clock slips (D7 / E7) | Advises order only — does **not** approve thin-C fall-back; does **not** reopen Scope A/B/C | Cut-order note accuracy vs `decision.md` | Thin C / scope fall-back requires **Gabe yes** + “bonus partial” label; Tom advice ≠ target scope |
| **Writer lead / Scribe** | Leads adapter draft quality; owns E5 hold decision when validate hard-fails or >2 retries; Scribe is the evidenced crew drafting / yes-gate seat for O2–O4 briefs (eggbot wire; questions-for-reggie Scribe draft) | Hold vs fix-and-retry on validation hard fail (E5); not ship gate | Validator errors + `hold_reason` on record | Never Barry; never silent rewrite-as-approve; cannot clear Claims Lock |
| **Human publishers** | CMS, changelog, login, in-app, production email send | Final live publish | Post-Barry package | Outside this SOP |

## Systems, inputs, and records

| Item | Purpose | Source of truth | Sensitivity / access | Record retained |
|---|---|---|---|---|
| Notion Campaign row | Status, Barry queue; **Run launch** = demo leave-behind Button (template + leave-behind doc) — **not evidenced** as a live clickable control in a production Notion database | Pilot SoT status (intended) | Internal | Status transitions; `barry_wip=1`; `trigger_used` note |
| Drive release folder | Blobs: sources, adapters, package | Files | Client/product material | Package zip/folder + MANIFEST |
| Claim ledger JSON | Allowed / forbidden / evidence / kill_switch | Schema `claim_ledger.schema.json` | Claim-sensitive | Ledger version + Barry Claims Lock decision |
| ReleaseCampaign JSON | Six artifacts + cadence refs + HubSpot sandbox fields | `release_campaign.schema.json` | Internal | Validated campaign file in package |
| Cadence binder JSON | One-release tier-blast cells | `cadence_binder.schema.json` | Internal | In package; same `campaign_id` |
| Validators | `validate_ledger.py`, `validate_campaign.py` — **crew-run / manual demo** local scripts (marketer has no terminal path) | Local `work/scripts/` | — | Pass/fail logs; retry count ≤2; result surfaced on Campaign row |
| `build_package.py` | Frozen package + honesty — **crew-run / manual demo** until non-terminal path evidenced | Drive package path | — | MANIFEST with `auto_publish: false` |
| HubSpot sandbox | Optional draft emails last | Reggie sandbox only | Credentials — operator only | `draft_ids[]`; status `draft_only` |
| Customer.io | Crew internal only | Not Vista ESP | — | Do not appear in Vista demo path |
| Gumloop / Drive label | Leave-behind Run triggers (same brain pickup; not Wed hero) | Documented leave-behinds only | — | Handoff note; record `trigger_used` if used |
| Honesty doc | Still-needs-human table | `work/honesty/still-needs-human.md` | Client-facing honesty | Copy in every package |

## Standard path

### A. Intake and Run

1. **Confirm fixture vs real sources.** Marketer opens the Campaign row. If `fixture_label` is non-empty or `FIXTURE_LABEL.md` applies, label the run “fixture until Reggie folder” on every artifact and on camera for recordings. If Reggie real folder is in use, confirm `fixture_label` cleared only after sources swapped and Claims Lock will be re-run. If unclear, follow [E2](#exceptions-and-escalation).

2. **Check WIP=1.** Marketer lists campaigns in `awaiting_barry`. If any other campaign is waiting, do not Run a second pack into Barry — follow [E3](#exceptions-and-escalation).

3. **Start Run or manual rehearsal.** Notion **Run launch** is the **demo leave-behind** (campaign-template Button + `notion-run-leavebehind.md`) — **not evidenced** as a live clickable control. Do **not** call this marketer-live until a trigger has been demonstrated once and proof is on the Campaign row (G12).  
   - **If a demonstrated Notion / Gumloop / Drive trigger is available:** Marketer uses that control. Observable result: status moves toward `ingested` / checklist comment with `folder_id`, claim_ledger link, WIP check. Record `trigger_used` on the row.  
   - **Manual rehearsal fallback (current honest path):** Crew (builder/orchestrator) drives ingest from the labelled fixture or shared folder **without** requiring a marketer terminal; marketer confirms folder/fixture + WIP on the row and records `trigger_used=manual_rehearsal`.  
   - Marketer does **not** open a terminal. Local validators/package remain crew-run. **Never claim unattended automation is live.**

4. **Confirm ingest + retrieve.** Marketer verifies Loom transcript, GitHub outline, and footage index are present for this `campaign_id`. If any required source missing → [E1](#exceptions-and-escalation).

5. **Bind voice pack.** Marketer confirms `voice_pack_ref` points to style guide / past newsletters **or** honesty lists “voice pack encode” as still-needs-human. Do not invent brand voice.

### B. Claims Lock (Barry once)

6. **Present ledger for Claims Lock.** Writer/crew places claim ledger on the Barry surface (Notion approve card + linked ledger). Status `claims_gate`. Every **allowed** claim shows evidence span (transcript or outline). Forbidden list present. No pricing/limits invention.

7. **Barry decides Claims Lock.** Barry selects **Approve Claims Lock** (adapters may run) **or** **Reject / kill-switch** (fix source; do not draft). Slack thumbs do not count.  
   - Approve → continue to step 8.  
   - Reject → status `needs_source_fix`; `kill_switch.armed=true` with reason; follow [E4](#exceptions-and-escalation).

### C. Draft adapters (writer ≠ Barry)

8. **Run adapter O1 (social video + burned captions).** Writer produces O1 only. Validation: cut + captions present; claims ⊆ ledger; length bounds. Status drafting for slot 1.

9. **Barry O1 spot-check.** Barry reviews O1 creative + copy with provenance visible.  
   - Pass → continue.  
   - Request Changes on slot 1 only → regenerate named slot (step 16 pattern); do not treat as pack approve.

10. **Run remaining adapters O2–O6 + cadence binder.** Writer produces: blog; email ×5 segments (leads SMB/Agency/Reseller·Affiliate + customers SMB/Agency, or explicit N/A); changelog (feature bullets only); login animation (Lottie/MP4/still or labelled mock); in-app popup (graphic + copy); cadence binder tier blast (changelog floor → interrupt email → story video → written social LI/X/Threads + IG/TikTok cells + UTM stubs) under the **same** `campaign_id`. Login/video/popup may stay honesty-labelled human-gap if Reggie formats pending — mark `held` + `hold_reason` when holding.

11. **Validate (≤2 retries).** **Crew** (builder/Writer lead path) runs local `validate_campaign.py` + `validate_ledger.py` from `work/scripts/` — these are **crew-run / manual demo** capabilities, not a marketer terminal step and not claimed live automation. Marketer confirms pass/fail (or hold) on the Campaign row. On retryable fail → Writer/crew fixes and re-validates (count ≤2). On hard fail → status `held`; follow [E5](#exceptions-and-escalation). Do not advance to Barry pack with hard fail.

12. **Submit pack (WIP=1).** Move campaign to `awaiting_barry` only if no other campaign is awaiting Barry. Attach all six slots (or held with reason) + cadence + ledger + provenance.

### D. Barry pack approve

13. **Barry pack approve (copy + creative).** Barry uses approve-pack template. Prerequisite: Claims Lock approved; O1 spot-check done; validate ≤2 done.  
   - **Approve pack** → status `approved`.  
   - **Request Changes** → list **named** artifact slot(s) only; regenerate those slots (step 16); return to validate; do not silent-rewrite-as-approve; do not HubSpot export yet.

### E. Package, honesty, optional sandbox, stop

14. **Build package + honesty doc.** After approve, **crew** runs `build_package.py` (crew-run / manual demo — marketer does not open a terminal). Include MANIFEST with `auto_publish: false`, six outputs/held reasons, cadence binder, ledger, honesty table (`still-needs-human.md`). Marketer confirms package contents on the row. Status `packaged`.

15. **Optional HubSpot sandbox draft last.** Only if Barry approved **and** email artifacts approved **and** sandbox invite exists: create **draft** emails only; record `draft_ids[]`; set `hubspot_sandbox.status=draft_only`; status may become `sandbox_exported`. **Do not** publish, marketing-send, or touch production lists. Say aloud on any recording: “sandbox draft; humans send later.” If skipping → `skipped`. Never demo Customer.io as Vista ESP ([E6](#exceptions-and-escalation)).

16. **STOP.** Humans publish out of band. Factory procedure ends at review-ready package (+ optional sandbox drafts). Marketer does not click production publish from this path.

### F. Re-run one output (after Request Changes or defect)

17. **Re-run named slot only.** Marketer/writer notes Barry’s named slot number(s) (1–6) or `cadence`. Regenerate **only** those artifacts from current ledger (do not reopen Claims Lock unless claims themselves changed). Bump artifact `version`. Re-validate affected slots. Resubmit pack with WIP=1. If claims text must change → return to Claims Lock (step 6) before adapters.

### G. Builder ≠ maintainer

18. **Separate builder from Run maintainer.** Builder (crew) may change schemas, bots, leave-behinds. Day-to-day **who clicks Run** = marketing. After this SOP is owner-approved, maintenance of operator steps lives with the named process owner — not the original builder — unless owner reassigns.

## Decision points

| Decision ID | Cue / question | Authorized decider | Route | Evidence retained |
|---|---|---|---|---|
| D1 | Fixture or real Reggie folder? | Marketer + Reggie access | Fixture → label; Real → clear label only after swap + re-Claims Lock | `fixture_label` |
| D2 | Claims Lock approve or kill? | Barry | Approve → adapters; Reject → E4 | Claims Lock card |
| D3 | O1 spot-check pass? | Barry | Pass → O2–O6; Changes → re-run slot 1 | Spot-check note |
| D4 | Validation pass within ≤2 retries? | Crew runs validators; Writer lead on hard fail (E5); marketer confirms row | Pass → awaiting_barry; Hard fail → E5 | Validator log |
| D5 | Pack approve or Request Changes? | Barry | Approve → package; Changes → named slots only | Pack card |
| D6 | Run HubSpot sandbox beat? | Marketer (optional) | Yes only post-approve + invite; else skip | `hubspot_sandbox.status` |
| D7 | Cut-order live (<24h / blocking)? | Gabe (thin C); Tom advises order | Label bonus partial; never quiet thin C | Cut-order note on package |
| D8 | Advance second pack while one awaits Barry? | Marketer | **No** — E3 | Status list |

## Exceptions and escalation

| ID | Trigger | Contain / continue | Decision owner and channel | Response window | Re-entry or closure | Evidence |
|---|---|---|---|---|---|---|
| E1 | Missing Loom / outline / footage | Pause at ingest; no Claims Lock | Gabe → Reggie folder share | Before next Run | Re-enter step 1 when folder complete | Campaign comment |
| E2 | Fixture/real unclear | Treat as fixture; label all outputs | Marketer; Reggie to confirm | Immediate | Step 1 after confirmation | `fixture_label` forced on |
| E3 | WIP>1 attempted | Do not set second `awaiting_barry` | Marketer; Barry if conflict | Immediate | Wait until first leaves awaiting_barry | Status screenshot/log |
| E4 | Claims Lock reject / kill-switch armed | Adapters cold; no HubSpot; status `needs_source_fix` | Barry + source owner (Reggie/Gabe) | Before any draft | Fix source → new Claims Lock (step 6) | Ledger kill_switch |
| E5 | Validate hard fail or >2 retries | Status `held`; hold artifact on record with reason | Writer lead; Barry notified | Before pack submit | Fix → validate → step 12 | Validator errors + hold_reason |
| E6 | Publish / CIO-as-ESP / production HubSpot pressure | **Stop.** Refuse action | Marketer stops; escalate Gabe/Reggie | Immediate | Resume only at step 14/15 lawful path | Incident note on campaign |
| E7 | Clock slip / cut-order | Keep six + claims + Barry + recorded path; drop Threads/X first → TikTok if IG exists → extra email beyond required → login/popup polish; label bonus partial | Gabe for thin-C fall-back | <24h to present | Package with explicit deferred list | decision.md cut-order cite |
| E8 | Claim missing mid-draft | Hold that artifact (`held` + reason); do not invent | Barry / Reggie off-limits | Before pack | Reliability on next feature; pack may proceed with hold | hold_reason |

## Completion and verification

The procedure is complete only when:

1. Campaign status is `packaged` or `sandbox_exported` (or `held` with documented hold if intentionally stopped), **and**
2. Package contains ledger, six slots or holds, cadence binder, honesty doc, MANIFEST with `auto_publish: false`, **and**
3. Barry Claims Lock + pack approve records exist (unless stopped earlier at E4/E5), **and**
4. No production publish / CIO-as-ESP occurred.

Marketer verifies package contents. Barry verifies ship-gate decisions. Interrupted work resumes from the last Campaign `status` checkpoint (do not skip Claims Lock or Barry after interruption into drafting).

## Evidence basis and open items

| Claim / gap ID | State | Basis | Consequence | Owner / next evidence |
|---|---|---|---|---|
| C1 Scope B + HOW recorded factory | Human decision | DESIGN-LOCK; GABE-SCOPE; design.md | Wrong HOW → live-wait failure | Locked — do not reopen without Gabe |
| C2 Spine + Barry HITL sequence | Human decision | DESIGN-LOCK §1–§2; barry templates | Skipping Claims Lock → false claims | Locked |
| C3 No auto-publish; HubSpot draft-only last; CIO ≠ ESP | Human decision | design §4–§9; hubspot checklist | Brand/trust breach | Locked |
| C4 Fixture labelled until Reggie | Evidence-backed fact + rule | FIXTURE_LABEL.md; questions-for-reggie.md | Invented product facts | Reggie access answers |
| C5 Who clicks Run = marketing | Human decision | design §5–§6; trigger leave-behind | Role drift to eng/builder | Confirm on owner approval |
| C6 Builder ≠ maintainer | Human decision | design handoff must-names | Orphaned procedure | Name maintainer at approval |
| C7 Notion Run = demo leave-behind (not evidenced live clickable) | Bounded assumption | trigger leave-behind; campaign-template Button; reconstruction (marketers not yet day-to-day) | Calling path marketer-live without proof | Manual rehearsal until demonstrated trigger; G12 durable pick post-Wed |
| C8 Barry surface = Notion + Drive pack | Bounded assumption | templates; Reggie Q4 unanswered | Wrong queue | Reggie answer |
| G1–G10 Reggie questionnaire | Unresolved fact | questions-for-reggie.md blank | Block real-feature swap | Gabe sends; Reggie replies |
| G11 SOP process owner / distribution approver | Unresolved fact | No named ops owner in evidence | Cannot leave Working Draft for distribution | Gabe/Reggie decide |
| G12 Durable post-Wed Run trigger (Notion vs Gumloop vs Drive) | Unresolved fact | design leave-behinds; no evidenced live clickable Run | Marketer may lack a real Run control | Gabe/Reggie/ops pick + demonstrate once; proof on row before “live” |

## Governance

- **Review cadence:** Within 7 days after Wed Sep 9 recorded E2E (target review_date 2026-09-16); then after each material factory change or quarterly if stable.
- **Change triggers:** Scope/HOW lock change; Barry HITL sequence change; new publish system; Reggie off-limits claims change; trigger UI change; schema status enum change; exception rate on E4/E5/E6; process owner change.
- **Feedback route:** Marketer and Barry → named process owner (UNRESOLVED) → Gabe for lock conflicts.
- **Retirement criteria:** Factory retired; replaced SOP Approved for Distribution; or Vista launch process moves to a different controlled system with supersession link.

## References and related artifacts

- Source register: `source-register.csv` (this folder; workspace mirror `../../sop-workspace/companions/source-register.csv`)
- Assumption and gap log: `assumption-and-gap-log.csv` (this folder; workspace mirror `../../sop-workspace/companions/assumption-and-gap-log.csv`)
- Risk assessment: `risk-assessment.yaml` (this folder; workspace mirror `../../sop-workspace/companions/risk-assessment.yaml`)
- Operator checklist: `marketer-run-checklist.md` (this folder; workspace mirror `../../sop-workspace/companions/marketer-run-checklist.md`)
- Design lock: `../../DESIGN-LOCK.md`
- Design: `../../2026-09-07-vista-launch-factory-design.md`
- Plan: `../../2026-09-07-vista-launch-factory-plan.md`
- Honesty: `../honesty/still-needs-human.md`
- Barry templates: `../barry/`
- Recording shot list: `../recording/shot-list.md`
- HubSpot checklist: `../hubspot/sandbox-checklist.md`
- Trigger leave-behind: `../trigger/notion-run-leavebehind.md`
- Prep gates: `../prep/tue-wed-checklist.md`
- Fixture label: `../fixtures/demo-release/FIXTURE_LABEL.md`
- Local validators / package (crew-run): `../scripts/validate_ledger.py`, `../scripts/validate_campaign.py`, `../scripts/build_package.py`

## Change history

| Version | Date | Change and reason | Authorized by | Supersedes |
|---|---|---|---|---|
| 0.1.0 | 2026-09-07 | Initial evidence-led Working Draft from Gabe-approved design lock + work tree | sop-builder (Morgan Bridger voice); not owner-approved | None (replaces handoff stub README only as pointer) |
| 0.1.1 | 2026-09-07 | Repair pass per review-report R3–R7: companion paths; Tom + Writer lead/Scribe roles; crew-run validate/package + Notion demo leave-behind + manual rehearsal; Terms table; G12 label aligned to durable trigger. G1–G11 unchanged unresolved | sop-builder repair; not owner-approved | 0.1.0 |

