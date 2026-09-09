# Engine reference

This is a from-source reference for operating the Launch Factory engine. Every
claim below was checked against the code in this checkout (`run.sh`,
`engine/scripts/*.py`, `engine/local_run/*.py`, `engine/schemas/*.json`, and
the two packages under `packages/`). Where the code and the existing prose
docs (`README.md`, `docs/OPERATE-LAUNCH-FACTORY.md`) disagree, this file
follows the code and calls out the gap.

## 1. Commands

### `run.sh`: the one-command door

```
./run.sh RELEASE_FOLDER
```

No flags. `RELEASE_FOLDER` is a directory containing `release_campaign.json`
(directly, or the script falls back to `engine/fixtures/<folder-name>/`).
Runs five stages in order, `set -euo pipefail`, and stops at the first
failure. `fail()` prints the failed check plus a "safest re-entry" message to
stderr and exits 1. It does not retry.

| Stage | What runs | On failure |
| --- | --- | --- |
| 0 | Creates `.venv/`, installs `requirements.txt` if needed | exits 1 |
| 1 | `init_release.py`, then `validate_record.py` on the fresh record | resumes if a record already exists at `runs/<name>/` |
| 2 | `validate_ledger.py` on the release folder's `claim_ledger.json` | skipped with a warning if no ledger file is found |
| 3 | `validate_campaign.py` on `release_campaign.json` | exits 1 on any missing slot or bad `barry.wip` |
| 4 | `build_package.py` into `packages/<campaign id>/` | exits 1 if an adapter path is missing |

Verified working example: `./run.sh engine/fixtures/vista-work`. Every path
`build_package.py` needs from this fixture (`cadence_binder.json`,
`sources/*`, `claim_ledger.json`, `engine/adapters/02_blog.md`, and
`engine/honesty/still-needs-human.md`) resolves correctly in this checkout.

### `engine/scripts/*.py`: the six STRUCTURAL_INTEGRITY_ONLY scripts

All are plain `python3 script.py ...`. None call a network or publish
anything. Each prints JSON, except `init_release.py`, which prints the
record path. Each uses its exit code as the pass/fail signal.

| Script | Usage | Exit code |
| --- | --- | --- |
| `init_release.py` | `RELEASE_FOLDER [--workspace DIR]` | 0, or a `SystemExit` message |
| `validate_record.py` | `RECORD` | 0 ok / 1 fail |
| `transition_slot.py` | `RECORD SLOT STATUS [--human-confirmed] [--reason TEXT]` | 0 ok / `SystemExit` on refusal |
| `validate_ledger.py` | `LEDGER_PATH` | 0 ok / 1 fail / 2 if kill-switch armed |
| `validate_campaign.py` | `CAMPAIGN_PATH` | 0 ok / 1 fail |
| `build_package.py` | `CAMPAIGN_JSON OUT_DIR [--work-root PATH]` | 0, prints the built path |

What each one does:

- **`init_release.py`**: sha256-hashes every file in `RELEASE_FOLDER`,
  writes `release-record.json` with all 7 slots defaulted to `held` (slots
  1/5/6 get a fixed ADR-0013 hold reason), and refuses to overwrite an
  existing record.
- **`validate_record.py`**: schema-checks the record, then confirms no slot
  is `approved`/`packaged` without a matching Barry `gates` entry, and that
  a `locked_by_barry` claims lock has its own timestamp and gate entry.
  Read-only.
- **`transition_slot.py`**: applies one permitted state transition to one
  slot and rewrites `RECORD` in place; see §3. `SLOT` accepts `1`-`7` or a
  slot name.
- **`validate_ledger.py`**: schema-checks the ledger, then confirms every
  `allowed` claim has a valid evidence span, no `allowed` text contains
  forbidden text, and every evidence `claim_id` resolves. Any failure arms
  `kill_switch.armed` and exits 2.
- **`validate_campaign.py`**: schema-checks the campaign, then confirms all
  7 slots exist with a `path` or `hold_reason`, all 7 artifact types are
  present, `barry.wip == 1`, and both segment lists are non-empty. Also
  exposes `validate_cadence_binder()`, unused by `run.sh`.
- **`build_package.py`**: builds `OUT_DIR/<campaign id>/` with one directory
  per slot, `cadence/` and `provenance/` copies, an `honesty/` stub,
  `MANIFEST.json` (`auto_publish: false` always), and a generated `BARRY.md`
  card. This shape matches neither package checked into `packages/` today;
  see §2.

### `engine/scripts/specialist_route.py`: offline specialist routing

```
python engine/scripts/specialist_route.py {route|validate-result|check-binding} REQUEST.json --workspace DIR [--result RESULT.json]
```

Not called by `run.sh`. Resolves specialist role(s) for a
`deliverable`/`stage` against `engine/specialists/registry.json`, re-hashes
every referenced file, and returns `status: held` with named reasons, or
`status: ready_for_protocol`. `human_approval_granted`,
`generation_authorized`, and `authentication_verified` are `false` in every
code path. Any error prints `{"status": "refused", ...}` and exits 2.

### `engine/local_run/*.py`: the scripts that built `camp_vista_work_public_001`

| Script | Usage | Requires | What it does |
| --- | --- | --- | --- |
| `build_public_demo.py` | no args, from repo root | `ffmpeg`, one live network fetch | Wipes and rewrites the package: sources, claim ledger, two rendered H.264 concept videos, every file in §2 |
| `verify_public_demo.py` | no args | `ffprobe` | Read-only: re-hashes files, checks claim IDs, email distinctness, video codec/duration, popup `<dialog>`, calendar bindings, zero paid calls |

### Package-embedded scripts (not general engine commands)

`packages/camp_tix_launch_001/01_channel_run/serve_review.py --port PORT
[--film PATH] [--animation PATH]` and `verify_package.py [--write-manifest]`
are copied into that one package, hardcode paths relative to it, and are not
reusable across campaigns. The server range-serves two named videos only
after a sha256 check against `review-data.json`'s `approved` entries.

## 2. Package layout (ground truth: `packages/`)

Two packages are checked in, built by two different, incompatible pipelines.
Neither matches the `build_package.py` shape described in §1.

**`packages/camp_vista_work_public_001/`** (built by
`engine/local_run/build_public_demo.py`) is the fuller of the two examples:

```
artifacts/
  blog.md, blog.html
  emails/{lead_smb,lead_agency,lead_reseller_affiliate,customer_smb,customer_agency}.{md,html}
  email_segments.md                      # bundle of all five
  changelog.md, changelog-v2.md, changelog.html
  social/{linkedin,x,threads,tiktok,storyboard}.md
  social/vista-work-social-concept.mp4   # 1080x1920, h264, >=12s
  login/README.md, login/vista-work-login-concept.mp4  # 1920x1080, h264, >=8s
  popup/{copy.md,preview.html,vista-work-popup.svg}
campaign/calendar.json, calendar.csv     # the two-week plan; see §4
claims/claim-ledger.json                 # see §4, does not match the schema
costs/costs.json                         # see §4
events/events.jsonl                      # one JSON object per line
jobs/jobs.json                           # {"jobs": [...]}
reviews/
  delegated-marketing-review-v1.json     # provisional verdict, barry pending
  revision-v2.json                       # before/after sha256 of one revision
  local-recheck-v2.md, local-verification.md
requests/run-brief.md
sources/                                 # captured/copied source files
voice/barry-seed.md, public-vista-work.md
README.md, RUN.md, run.json, review.html, source-manifest.json,
export-manifest.json, recording-pending.md
```

The "six outputs" live under `artifacts/`: social video is
`artifacts/social/`, blog is `artifacts/blog.*`, email is
`artifacts/emails/`, changelog is `artifacts/changelog*`, login animation is
`artifacts/login/`, in-app popup is `artifacts/popup/`. The 7th slot, the
campaign plan, is `campaign/calendar.{json,csv}`.

**`packages/camp_tix_launch_001/`** uses an unrelated, older two-stage
layout: `00_baseline/` (source manifest, claim-ledger.json, voice profile,
`approvals.json`), then `01_channel_run/` (per-channel dirs `blog/`,
`email/`, `changelog/`, `popup/`, `campaign/calendar.{json,csv}`, plus
`bindings/`, `requests/`, `routing/`, `verification/`,
`PACKAGE-MANIFEST.json`, `review.html`, and the §1 package-embedded
scripts). No script here builds this shape; treat it as hand-assembled, not
`build_package.py` output.

## 3. State machine (`engine/scripts/transition_slot.py`)

One `release-record.json` holds 7 slots (`1`-`7`, fixed names
`social_video, blog, email_segments, changelog, login_animation,
in_app_popup, campaign_plan`). Each slot's `state` is one of `held, drafted,
reviewed, approved, packaged`.

| From | To | Extra requirement |
| --- | --- | --- |
| `held` | `drafted` | none, clears `hold_reason` |
| `drafted` | `reviewed` | none |
| `drafted` | `held` | `--reason TEXT` |
| `reviewed` | `approved` | `--human-confirmed` |
| `reviewed` | `held` | `--reason TEXT` |
| `reviewed` | `drafted` | none (request changes) |
| `approved` | `packaged` | `--human-confirmed` |
| `approved` | `reviewed` | none (request changes after approve) |

Every other `(from, to)` pair, including any transition into `held` without
`--reason`, is refused: the script raises `SystemExit("refused: ...")`,
printed to stderr, exit 1, and nothing is written to disk. A transition into
`approved`/`packaged` without `--human-confirmed` refuses the same way; only
Barry, the human, authorizes those two states, and the writer seat never
self-approves.

On success the script always appends one `run_log` entry, and, only for
transitions into `approved`/`packaged`, one `gates` entry
(`decided_by: "barry"`, `decision: "approve"`). This gate entry is what
`validate_record.py` later checks for, and it is written by the CLI flag
alone, not by any identity check (see §5).

`claims_lock.state` (`drafted` to `locked_by_barry`) is a separate record
field that no script in `engine/scripts/` transitions. `validate_record.py`
only checks that, once already `locked_by_barry`, a matching `locked_at`
timestamp and `gates` entry (`gate: "claims_lock"`) both exist.

## 4. Data files

**`claim_ledger.schema.json`** requires `campaign_id, allowed, forbidden,
needs_disclaimer, evidence, kill_switch`. Each `evidence` row's `source`
field is a closed enum: `loom_transcript | github_outline | footage_index`.
Redacted shape:

```json
{
  "campaign_id": "camp_...",
  "allowed": [{ "claim_id": "vw1", "text": "..." }],
  "forbidden": [{ "claim_id": "f1", "text": "...", "reason": "..." }],
  "needs_disclaimer": [{ "claim_id": "d1", "text": "...", "disclaimer": "..." }],
  "evidence": [{ "claim_id": "vw1", "source": "loom_transcript",
                 "path": "sources/...", "span_start": 498, "span_end": 550,
                 "quote": "..." }],
  "kill_switch": { "armed": false, "reason": null }
}
```

`engine/fixtures/vista-work/claim_ledger.json` conforms to this schema. The
shipped `packages/camp_vista_work_public_001/claims/claim-ledger.json` does
not: its `evidence[].source` values (`supplied_email_source_text`,
`repository_source_text`, `public_web_capture`) are not in the schema enum,
so `validate_ledger.py` would fail against that real file.

**`release-record.schema.json`** (`release-record/v1`): a record has
`record_id, release_folder{path,files[]}, ingest{state,at},
claims{allowed,forbidden,held}, claims_lock{state,locked_at}, slots[7],
voice_check, validations[], gates[], package_path, run_log[]`. Each slot is
`{slot,name,state,hold_reason}`; each gate is
`{gate,decision,decided_by,at}` with `decided_by` one of `barry | writer |
orchestrator`.

**`release_campaign.schema.json`**: `id, title, folder_id, status` (13-value
enum), `sources{loom,transcript,github_outline,footage[]}, claim_ledger_ref,
voice_pack_ref, segments{leads,customers,affiliate_rules}, artifacts[7],
cadence_ref, barry{seat,surface,wip}, hubspot_sandbox{draft_ids,status},
still_needs_human[]`. Each artifact is
`{slot,type,version,path,validation,barry_status,held,hold_reason}`.

**`cadence_binder.schema.json`**: `campaign_id, fixture_label, cells[]`,
each cell `{order,channel,artifact_slot,utm{utm_source,utm_medium,
utm_campaign},notes}`. `channel` is one of 8 fixed cadence values
(`changelog, email_interrupt, story_video, linkedin_written, x_written,
threads_written, instagram_video, tiktok_video`).

**`campaign/calendar.csv`** columns, from the real
`camp_vista_work_public_001` file: `week, proposed_day, order, timezone,
channel, audience, asset_id, asset_path, action, review_state`. One real row:

```
1,Mon (proposed),1,America/Sao_Paulo,blog,all social managers,blog-v1,artifacts/blog.html,read linked-task story,delegated_review_pending_barry
```

`campaign/calendar.json` wraps the same rows, plus `scheduled: false`, a
`timezone`, and an `asset_index` mapping every `asset_id` to its file path.

**`costs/costs.json`**, redacted real example:

```json
{
  "currency": "USD",
  "incremental_paid_calls_this_run": 0,
  "observed_usd_this_run": 0,
  "prior_observed_usd": 0.235,
  "prior_provider_credit_usd_unknown": true,
  "ceiling_usd": 500
}
```

**`jobs/jobs.json`** shape: `{"jobs": [{"id","state","provider","paid"}]}`.
Every recorded job in the real package has `"state": "completed"` and
`"paid": false`.

**`events/events.jsonl`**: one JSON object per line, for example
`{"event": "local_package_built", "at": "...", "paid_provider_call": false,
"route": "..."}`.

## 5. What is NOT implemented

The existing prose docs make several claims the code does not back up.
Verified against the actual scripts in this checkout:

- **No retries.** `run.sh`'s `fail()` exits on the first failure; no script
  under `engine/scripts/` loops or retries. The schemas carry a `retries`
  counter and a `retryable_fail` enum value, but nothing increments or acts
  on them. `docs/OPERATE-LAUNCH-FACTORY.md` and `README.md` currently claim
  "Validators retry twice"; not true of this code.
- **No hash-bound approval invalidation.** `transition_slot.py` never reads
  or compares a file hash on approval. Nothing here reopens a gate when an
  approved file's content changes. `README.md` currently claims "An
  approval binds to the asset's hash, so editing an approved file reopens
  its gate"; not implemented.
- **No auto-publish.** True as claimed: `build_package.py` hardcodes
  `"auto_publish": false` always, and nothing under `engine/` calls a send,
  publish, or schedule API.
- **No hosted trigger.** Every entrypoint here is a local CLI script, run
  from a shell or an agent session; no server, webhook, or UI starts a run.
- **No authentication on `--human-confirmed`.** It is a boolean CLI flag,
  not an identity check; anyone who can run the script can pass it.
  `specialist_route.py` says as much about itself, marking every output
  `"authentication_verified": false`.
