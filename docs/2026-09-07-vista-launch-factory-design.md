# Vista Social — Launch Factory Design
**Date:** 2026-09-07  
**Status:** SPEC APPROVED by Gabe 2026-09-07; writing-plans invoked  
**Present:** Wednesday September 9, 2026 (paid trial = the eval)  
**Sponsor:** Reggie Azevedo (COO) · **Ship gate:** Barry, VP Marketing  
**Author:** Nova (fold of Egdod / Marlowe / Holloway / Apiana / Omnara / Tom / Matt / Lingxi)

**SPEC APPROVED by Gabe 2026-09-07; writing-plans invoked.** Implementation follows the plan (still no auto-publish / no inventing claims).

---

## 0. Problem & success

Every Vista feature ship rebuilds the same launch package by hand. Raw material is always Loom + GitHub outline + footage. Missing: the machine that turns that into a Barry-ready pack.

**Wed success**
- Recorded E2E: release folder → six review-ready outputs + one-release campaign cadence binder/cells
- Visible claims ledger + Barry HITL (copy + creative)
- Non-engineer trigger
- Honest human-gaps write-up
- HubSpot sandbox email draft last (optional), no auto-publish
- Handoff SOP a marketer can run next week

**Not success:** live-wait generation in the room; inventing Vista claims; CIO as their ESP; six orphan assets with no cadence story; Decision C email-pack as hero.

---

## 1. Scope & HOW (locked)

| Lock | Value |
|---|---|
| Scope | **B** — all six required outputs + full one-release campaign cadence (quality risk accepted) |
| HOW | **Recorded factory** — pre-bake; room is Q&A |
| Cut-order | Contingency only (`decision.md`) — never quiet revert to thin spine; label bonus partial |
| Engine | Grok-crew brain; Gumloop/Notion/Drive = trigger leave-behind; Temporal OUT |

---

## 2. Spine (§1 approved)

```text
Marketer Run
  → Release folder ingest
  → Retrieve (Loom transcript + GitHub outline + footage index)
  → Voice pack bind (past newsletters / style guide)
  → Claims Lock (Barry once) ──fail──► kill switch / fix source
  → pass → adapter₁ → Barry spot-check
  → remaining five + cadence binder (tier blast)
  → Validate / retry ≤2 (hard fail → hold)
  → Barry pack approve (copy + creative)
  → Package + honesty doc
  → HubSpot sandbox email draft last (optional)
  → STOP (humans publish out of band)
```

**Non-negotiables:** writer ≠ Barry; WIP=1 in `awaiting_barry`; no draft→published without Barry; no auto-publish.

---

## 3. Six outputs + cadence (§2 approved)

| # | Output | Wed posture | Validation before Barry |
|---|---|---|---|
| 1 | Social video + burned captions | First-pass cut; taste in honesty | Cut + captions; claims in ledger; length bounds |
| 2 | Blog → vistasocial.com/insights/ | Review-ready draft | H1, sections, CTA; claims cited; voice pack |
| 3 | Email ×5 segments | Draft pack | leads SMB/Agency/Reseller·Affiliate + customers SMB/Agency; N/A explicit OK |
| 4 | Changelog → suggestions.vistasocial.com/changelog | Thin draft | Feature bullets only; no pricing invention |
| 5 | Login animation | Lottie/MP4 or labelled mock | Asset + brief; no new claims — weakest LLM cell |
| 6 | In-app popup | Graphic + copy | CTA; claims gated; size/placement from Reggie |

**Cadence binder (same `campaign_id`):** one-release channel cells — not a multi-week calendar product.  
**Tier blast:** changelog floor → interrupt email → story video → written social (LI/X/Threads) + IG/TikTok cells + UTM stubs.

**Barry HITL**
- Claims Lock once → O1 spot-check → pack approve (v1 default)
- One queue (Notion + Drive pack; Planable-class if access)
- Slack thumbs ≠ approve; no “one click to ship”
- Request Changes regenerates named artifact(s), not silent rewrite-as-approve

---

## 4. Recording contract (§3 approved)

Pre-bake everything. No live-wait. Live = architecture + artifact Qs.

**Shot list**
1. Marketer clicks Run  
2. Folder ingest visible  
3. Claims ledger on screen → Claims Lock  
4. O1 → Barry spot-check beat  
5. Jump-cut O2–O6 + cadence binder  
6. Pack approve → frozen package + honesty doc  
7. HubSpot sandbox draft last (optional ~10s) → stop  

**Must show:** provenance next to copy; WIP=1; writer ≠ Barry.  
**Must not:** token stream; auto-publish; CIO as Vista ESP; invented facts; six orphans.  
**If claim missing:** hold one artifact on camera (reliability on next feature).

---

## 5. Integrations (§4 approved)

| System | Wed role | Claim hygiene |
|---|---|---|
| Drive | Release-folder ingest | Once Reggie shares |
| Notion | Campaign SoT + Barry queue | One campaign row |
| Gumloop | Non-engineer Run leave-behind | Trigger only — not brain |
| HubSpot | Their sandbox email after Barry | Draft only; no /publish; not “we own Vista HubSpot” |
| Customer.io | Ours only | Never demo as Vista ESP |
| Resend | Internal preview fallback | Never customer send |
| Temporal | OUT | — |
| n8n | Optional later leave-behind | Not Wed hero |

**Need from Reggie (Gabe sends `questions-for-reggie.md`):** folder link/perms, brand samples ETA, HubSpot sandbox invite, Barry surface, Wed feature, Loom/outline locs, login/popup formats, channel priority, off-limits claims.

---

## 6. Human-gaps + handoff (§5 approved)

**Still needs a human**
- Source folder quality  
- Claims Lock seed (forbidden list)  
- Voice pack encode  
- Social video taste  
- Login animation (designer/Lottie)  
- Popup graphic taste / placement  
- Final publish (CMS, changelog, login, in-app)  
- Segment / affiliate legal  

**Handoff SOP must name**
- Who clicks Run (marketing)  
- WIP=1 awaiting_barry  
- Claims Lock + kill switch  
- Forbidden publish transitions  
- Builder ≠ maintainer  
- Where Barry Approves / Request Changes  
- How to re-run one output  
- Cut-order if clock slips (labelled bonus partial)  

Full SOP via `sop-builder` after this spec is accepted.

---

## 7. SoT sketch (pilot)

```text
ReleaseCampaign
  id, title, folder_id, status
  sources { loom, transcript, github_outline, footage[] }
  claim_ledger { allowed[], forbidden[], needs_disclaimer[], evidence[] }
  voice_pack_ref
  segments { leads[], customers[], affiliate_rules }
  artifacts[1..6] { type, version, path, validation, barry_status }
  cadence[]
  barry { seat, surface }
  hubspot_sandbox { draft_ids[], status }
  still_needs_human[]
```

Pilot SoT = Notion + Drive blobs. Dex may harden later.

---

## 8. Research grounding (do not reopen)

- Omnara: Makrly / AnnounceKit / Falkster / CloudStudio twins; complaints = voice drift, fake claims, autopost; recorded E2E wins  
- Newsletters: Descript×HubSpot 1→55 HITL; MilkKarten approval kills ideas; Resend changelog packs  
- Marlowe/PIST/PoP: Claims Lock + serial Barry + cadence binder required; P1 ship vs pack, P2 rewrite tax — don’t pitch Vista end-user G2 pain  
- Holloway: Barry queue bottleneck; marketer Run  
- Apiana: connector claim hygiene; HubSpot sandbox last  

See `OVERVIEW-FOLD.md`, `research-omnara.md`, `overview-*.md`.

---

## 9. Out of scope (Wed)

- Auto-publish / production HubSpot send  
- Swap Vista ESP to Customer.io  
- Temporal / 200-tenant SaaS  
- Support triage / sales ops (later role work)  
- Decision C deck/MVP as hero  
- Live generation in the room  

---

## 10. Next after Gabe reviews this file

1. Spec self-review nits fixed inline (below)  
2. Gabe yes on written spec  
3. Invoke **writing-plans** → implementation plan  
4. **sop-builder** → handoff SOP  
5. Matt retitles Notion board to Vista tasks  
6. Build toward recorded E2E (after Reggie access where needed)

---

## Spec self-review (2026-09-07)

| Check | Result |
|---|---|
| Placeholders | None intentional except Reggie answers TBD |
| Contradictions | Scope B vs Tom thin C resolved: C = contingency only |
| Ambiguity | Trigger pick (Notion vs Gumloop vs Drive) left as “pick one for demo, document all three” — OK for plan phase |
| Scope creep | Explicit outs in §9 |
| Claims Lock vs Claims gate naming | Both mean Barry-once ledger approve before adapters |

