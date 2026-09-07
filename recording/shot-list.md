# Recording shot list — Vista Launch Factory v0.2.0 (refreshed 2026-09-07, post-restructure)

**HOW:** Recorded factory. Pre-bake everything. Live call = architecture + artifact Qs only.
**Story:** Demo first (GRILL-LOCK #6 override), spine second. Win the room, then show the machine.
**Run command for every factory beat:** `./run.sh engine/fixtures/vista-work` (Quorum Desk / Vista Work fixture, labeled on screen).

## Part 1 — The cool open (~30% of runtime)
1. **UGC-with-product open** (per GRILL-LOCK #7): the approval-queue pain scene. Sheets ↔ Drive ↔ Canva ↔ email, cut fast. On-camera line: "I made these assets to show how the system would work, since I don't have internal access to your files."
2. **Tech Demos clip** (per Q13 lock): the mocked normie run, clickable mini-app screen-recorded, labeled simulated.
3. Product Educator beat is LIVE on the call (Gabe), not recorded.

## Part 2 — The spine, recorded (~60%)
4. **One command:** terminal, `./run.sh engine/fixtures/vista-work` — the marker-run door. Show the stage banners scroll: ingest → record created.
5. **Release record on screen:** `runs/*/release-record.json` — input file hashes, claims with evidence spans, statuses.
6. **Claims Lock (Barry, once):** fill `barry/claims-lock.md` card; show writer ≠ Barry; lock recorded in the record.
7. **O2 blog draft** → Barry spot-check beat (first real draft, direction approved before fan-out).
8. **Jump-cut O3 emails (5 segments) + O4 changelog + O7 Campaign Plan** (day-by-day, one source of truth — the bonus, say it out loud).
9. **Slots 1/5/6 HOLD beat:** show the HELD stubs + reason on camera. Line: "held beats invented."
10. **Validation + run log:** validators pass ≤2 retries; run log shows inputs, outputs, failures, gates.
11. **Pack approve** → frozen package + honesty doc → **STOP.** Nothing publishes.
12. Optional ~10s: HubSpot sandbox draft-only, after Barry, then stop again.

## Part 3 — The handoff (~10%)
13. **Repo-link install door:** paste the GitHub URL into a fresh agent (Claude Code or Codex), "install this Augment," agent reads README top section and self-installs. One take, no cuts.
14. **Voice Bank flash:** 25-item corpus + 12 voice rules — "voice is checked against your own words, not a guess."
15. **Mini-roadmap slide:** support triage → sales ops → lifecycle (Reggie's own lined-up list), n8n/Gumloop as phase-2 trigger layer, AskVista-shaped.
16. **Close (three slides, pick live per Q10 lock):** hire-me (first 30 days owning AI ops) / deeper build (fixed-scope phase 2) / graceful handoff (maintainer onboarding week).

## Must show
- Provenance next to copy · WIP=1 in awaiting_barry · Writer ≠ Barry · the run log · HOLD honesty

## Must not
- Token stream · auto-publish · invented facts/pricing · six orphans with no campaign story · Victor/Stunspot brand anywhere · live generation waits

## If claim missing
Hold one artifact on camera (reliability on the next feature) — label `held` + reason.

## Cut-order contingency (not the target)
If clock slips: Part 1 → beats 4/6/11/13 → close. Label Campaign Plan partial; never quiet-ship a thin cut without Gabe yes.
