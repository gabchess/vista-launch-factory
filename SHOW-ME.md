# SHOW-ME — Vista Launch Factory (camp_vista_work_001)

ELI5 end-to-end. **Video/demo PAUSED.** No auto-publish. No HubSpot send. No pricing invent.

## What this is

One release folder in → six review-ready artifact slots + cadence binder out → **STOP**. Humans publish out of band.

Barry (VP Marketing) is the only copy/creative ship gate. Writer ≠ Barry.

## Pipeline (ingest → STOP)

```
1. INGEST
   Marketer Run drops a release folder (Loom/transcript, outline, footage index).
   Here: fixtures/vista-work/ seeded from demo/ Barry email + outline.

2. CLAIMS
   claim_ledger.json = allowed / forbidden / needs-disclaimer + evidence spans.
   validate_ledger.py → kill-switch arms if allowed claim has no evidence or
   forbidden text leaks into allowed. Adapters stay COLD until Claims Lock passes.
   Status today: claims_gate (Barry once-per-campaign yes still needed).

3. ADAPTERS (six slots)
   From locked claims only — never invent features/limits/$.
   Slot 1 social_video     → HELD (no real footage; Demo Assets ≠ ledger)
   Slot 2 blog             → adapters/02_blog.md      (real)
   Slot 3 email_segments   → adapters/03_email_segments.md (real)
   Slot 4 changelog        → adapters/04_changelog.md (real)
   Slot 5 login_animation  → HELD
   Slot 6 in_app_popup     → HELD

4. CADENCE
   cadence_binder.json sequences channels for one release
   (changelog → email interrupt → story video HELD → written social → IG/TikTok HELD).

5. PACKAGE
   build_package.py copies real adapters + HELD.txt + provenance + honesty + cadence
   into packages/<campaign_id>/. Writes MANIFEST.json with auto_publish: false.

6. STOP
   Review-ready Drive pack. Barry pack-approve later. HubSpot sandbox = draft only,
   after Barry. Final publish = human CMS/email — never this factory.
```

## Package tree (this run)

```
packages/camp_vista_work_001/
├── MANIFEST.json
├── 01_social_video/HELD.txt
├── 02_blog/02_blog.md
├── 03_email_segments/03_email_segments.md
├── 04_changelog/04_changelog.md
├── 05_login_animation/HELD.txt
├── 06_in_app_popup/HELD.txt
├── cadence/cadence_binder.json
├── honesty/still-needs-human.md
└── provenance/
    ├── barry_email_transcript.txt
    ├── vista_work_outline.md
    └── claim_ledger.json
```

MANIFEST highlights: `status=packaged`, `auto_publish=false`, `barry_seat=Barry VP Marketing`, note = **STOP — humans publish out of band**.

## How to re-run (from work/)

```bash
cd /home/box/shared/handoffs/reggie-pilot/vista/work
source .venv/bin/activate   # or use .venv/bin/python

# 1) Validate Claim Ledger (kill-switch)
python scripts/validate_ledger.py fixtures/vista-work/claim_ledger.json

# 2) Validate Release Campaign (six slots exist-or-held)
python scripts/validate_campaign.py fixtures/vista-work/release_campaign.json

# 3) Build Drive-ready package
python scripts/build_package.py fixtures/vista-work/release_campaign.json packages
# optional if fixture depth ever differs:
# python scripts/build_package.py fixtures/vista-work/release_campaign.json packages --work-root .

# 4) Tests
pytest -q
```

`work_root` default = `campaign_json.parents[2]` → for `fixtures/vista-work/*.json` that is `work/`. Adapter paths resolve as `work/adapters/...`.

## Hard stops (do not)

- Invent pricing, seats, or $ savings
- Encode / ship video (slot 1 held; Demo Assets out of Claim Ledger — ADR 0001)
- HubSpot send / auto-publish
- Treat Demo Assets as product evidence
- Push to Forge / remote without Gabe

## Design locks (review copies)

See `docs/DESIGN-LOCK.md`, `docs/GRILL-LOCK.md`, `docs/CONTEXT.md`, plus design + plan markdown in `docs/`.
