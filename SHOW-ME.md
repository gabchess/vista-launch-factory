# SHOW-ME — Vista Launch Factory (camp_vista_work_001)

ELI5 end-to-end. **Video/demo PAUSED.** No auto-publish. No HubSpot send. No pricing invent.

## What this is

One release folder in → six artifact slots (exists-or-held) + Campaign Plan out → **STOP**. Humans publish out of band.

Barry (VP Marketing) is the only copy/creative ship gate. Writer ≠ Barry. All run state lives in one release record (`runs/<folder>/release-record.json`).

## Loop (Ingest → STOP)

```
1. INGEST
   ./run.sh drops a release folder (Loom/transcript, outline, footage index)
   into a workspace; init_release.py hashes every input file into the record.
   Here: engine/fixtures/vista-work/ seeded from the Barry email + outline.

2. GROUND + CLAIMS
   claim_ledger.json = allowed / forbidden / held + evidence spans, each claim
   status-labelled (observed/source_stated/inferred/assumed/unknown).
   validate_ledger.py → kill-switch arms if an allowed claim has no evidence or
   forbidden text leaks into allowed. Adapters stay COLD until Claims Lock passes.
   Status today: claims_gate (Barry's once-per-campaign yes still needed).

3. CREATE (seven slots)
   From locked claims only — never invent features/limits/$.
   Slot 1 social_video     → HELD (no real footage; Demo Assets ≠ ledger)
   Slot 2 blog             → engine/adapters/02_blog.md      (real)
   Slot 3 email_segments   → engine/adapters/03_email_segments.md (real)
   Slot 4 changelog        → engine/adapters/04_changelog.md (real)
   Slot 5 login_animation  → HELD
   Slot 6 in_app_popup     → HELD
   Slot 7 campaign_plan    → engine/adapters/07_campaign_plan.md (ADR 0016;
                             cadence_binder.json is its data shape)

4. REVIEW
   Four gates recorded in the record: claims/accuracy, voice/composition
   (interim Voice Bank brief, ADR 0015), completeness (exists-or-held),
   authority (writer never Barry; approved/packaged need --human-confirmed).

5. PACKAGE
   build_package.py copies real adapters + HELD.txt + provenance + honesty +
   cadence into packages/<campaign_id>/. MANIFEST.json: auto_publish: false.
   BARRY.md review card is filled from campaign state.

6. STOP
   Review-ready Drive pack. Barry pack-approve later. HubSpot sandbox = draft
   only, after Barry. Final publish = human CMS/email — never this factory.

7. LEARN
   Outcomes Barry reports go back into the record's run log. Supplied results
   only; no fabricated metrics.
```

## Package tree (this run)

```
packages/camp_vista_work_001/
├── MANIFEST.json
├── BARRY.md
├── 01_social_video/HELD.txt
├── 02_blog/02_blog.md
├── 03_email_segments/03_email_segments.md
├── 04_changelog/04_changelog.md
├── 05_login_animation/HELD.txt
├── 06_in_app_popup/HELD.txt
├── 07_campaign_plan/          (Held pre-Claims-Lock in this fixture)
├── cadence/cadence_binder.json
├── honesty/still-needs-human.md
└── provenance/
    ├── barry_email_transcript.txt
    ├── vista_work_outline.md
    └── claim_ledger.json
```

MANIFEST highlights: `status=review_ready_pre_claims_lock`, `auto_publish=false`, `fixture_label=barry-email-seed`, `barry_seat=Barry VP Marketing`, note = **STOP — pre-Claims-Lock review bundle; Barry Claims Lock still required before pack-approve**. Package root also has filled `BARRY.md`.

## How to re-run (from repo root)

```bash
cd <repo-root>

# One command (ADR 0014)
./run.sh engine/fixtures/vista-work

# Or stage by stage
.venv/bin/python engine/scripts/init_release.py engine/fixtures/vista-work
.venv/bin/python engine/scripts/validate_record.py runs/vista-work/release-record.json
.venv/bin/python engine/scripts/validate_ledger.py engine/fixtures/vista-work/claim_ledger.json
.venv/bin/python engine/scripts/validate_campaign.py engine/fixtures/vista-work/release_campaign.json
.venv/bin/python engine/scripts/build_package.py engine/fixtures/vista-work/release_campaign.json packages --work-root engine

# Tests
.venv/bin/pytest -q     # 22 passed
```

`build_package`'s `work_root` default = `campaign_json.parents[2]` → for `engine/fixtures/vista-work/*.json` that is `engine/`. Adapter paths resolve as `engine/adapters/...`.

## Hard stops (do not)

- Invent pricing, seats, or $ savings
- Encode / ship video (slot 1 held; Demo Assets out of Claim Ledger — ADR 0001)
- HubSpot send / auto-publish
- Treat Demo Assets as product evidence
- Move a slot to approved/packaged without a recorded Barry decision
- Push to Forge / remote without Gabe

## Design locks (review copies)

See `docs/DESIGN-LOCK.md`, `docs/GRILL-LOCK.md`, `docs/CONTEXT.md`, ADRs 0012–0016 in `docs/adr/`, plus design + plan markdown in `docs/`.
