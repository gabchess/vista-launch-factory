# Vista Launch Factory

One feature-release folder in. A review-ready launch package out. A person approves every word before anything leaves.

Hand your AI agent this repository and one release folder: a Loom transcript, a feature outline, raw screen and social footage. It returns six launch assets and a campaign plan. Every product claim traces to a quoted source. Every asset waits for the reviewer's decision. Nothing publishes, sends, or schedules.

First ask, in Claude Code or Codex from this folder:

```
Run Launch Factory on this release folder.
```

## What comes out

| # | Output | What you get |
| --- | --- | --- |
| 1 | Social video | A short cut with burned-in captions, plus the IG/TikTok script and shot plan. |
| 2 | Blog post | Markdown and HTML for vistasocial.com/insights, with images. |
| 3 | Email announcement | Five variants: SMB, agency, and reseller/affiliate leads; SMB and agency customers. |
| 4 | Changelog post | A short versioned entry for suggestions.vistasocial.com/changelog. |
| 5 | Login animation | A short looping motion piece for vistasocial.com/login. |
| 6 | In-app popup | Graphic, copy, and a working dialog preview. |
| 7 | Campaign plan | A two-week calendar across email, popup, blog, LinkedIn, X, Threads, and IG/TikTok, with a human gate on every row. |

## Two runs you can open now

| Run | Source | Media | Open |
| --- | --- | --- | --- |
| Tix | Gabe's own product, run by an engineer from Claude Code with local tools | 55-second product film and 10-second login animation, both approved creative | [review page](packages/camp_tix_launch_001/01_channel_run/review.html) |
| Vista Work | Vista's public Insights article plus one Barry email, 4 grounded claims | Concept previews only, because no private Vista footage was available | [review page](packages/camp_vista_work_public_001/review.html) |

Tix media, playable in the browser: [product film](packages/camp_tix_launch_001/media/tix-product-film-v3.mp4) and [login animation](packages/camp_tix_launch_001/media/tix-login-animation.mp4). Tix package guide: [01_channel_run/README.md](packages/camp_tix_launch_001/01_channel_run/README.md).

Vista Work outputs, readable without a server: [blog](packages/camp_vista_work_public_001/artifacts/blog.md), [emails](packages/camp_vista_work_public_001/artifacts/emails/), [changelog](packages/camp_vista_work_public_001/artifacts/changelog-v2.md), [social drafts](packages/camp_vista_work_public_001/artifacts/social/), [popup copy](packages/camp_vista_work_public_001/artifacts/popup/copy.md), [calendar](packages/camp_vista_work_public_001/campaign/calendar.csv), [claim ledger](packages/camp_vista_work_public_001/claims/claim-ledger.json).

## How a run works

| Stage | What happens | Who decides |
| --- | --- | --- |
| Ingest | Every source file is hashed into one release record. | System |
| Ground | Claims are extracted with a file, offset, and quote each; voice is checked against 25 items of Vista's own published writing. | System |
| Claims Lock | Allowed, forbidden, and held claims are confirmed once. | Barry |
| Create | Twelve specialist roles draft each asset from locked claims only. | System |
| Review | Four gates run: accuracy, voice, completeness, authority. | System, then Barry spot-check |
| Package | A review page, honesty note, and campaign plan are assembled. | Barry approves |
| Stop | Publishing, sending, and scheduling stay with a person. | Human |

## Where the checks live

- A claim without an evidence span arms the kill-switch before any drafting starts.
- Barry locks claims before fan-out, the cheapest point to stop a wrong promise.
- The first blog draft gets a spot-check before the other assets are written.
- An approval binds to the asset's hash, so editing an approved file reopens its gate.
- The writer role can never approve; moving a slot to approved needs a `--human-confirmed` flag from a person.
- Validators retry twice, then print the failed check and the safest re-entry point.

## Run it

```bash
git clone https://github.com/gabchess/vista-launch-factory.git
cd vista-launch-factory
./run.sh engine/fixtures/vista-work
```

`run.sh` creates a virtual environment on first use, then runs ingest, validation, and packaging with stage banners. The same spine runs from a chat prompt in Claude Code or Codex.

Open the Tix review with its media:

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
python3 packages/camp_tix_launch_001/01_channel_run/serve_review.py --port 8770 \
  --film packages/camp_tix_launch_001/media/tix-product-film-v3.mp4 \
  --animation packages/camp_tix_launch_001/media/tix-login-animation.mp4
```

Then open `http://127.0.0.1:8770/01_channel_run/review.html`. The server binds to loopback and checks each video against its approved SHA-256.

## Verify

```bash
.venv/bin/pytest -q
.venv/bin/python engine/local_run/verify_public_demo.py
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/verify_package.py
```

Expected: 77 tests pass; 124 checks pass on the Vista Work package with 0 paid provider calls; 94 checks pass on the Tix package.

## What still needs a human

| Job | Why |
| --- | --- |
| Claims Lock | Only Barry knows what Vista may promise. |
| Final voice call | The voice bank flags drift; taste decides. |
| Video, animation, and popup art | Real footage and creative judgment are required. |
| Publish, send, schedule | Never automated in v1, by design. |
| Which feature, which week | The factory runs launches; it does not choose them. |

## Status and limits

- Barry has not approved any output; every asset is a review-ready draft.
- Vista Work media is a concept preview because no private Vista footage, UI recording, or Loom was shared.
- Today an engineer runs the media lane from Claude Code or Codex; the hosted app where marketing clicks a button is the next phase.
- Two n8n workflows prepare work packets; they do not yet dispatch a provider worker.
- License is not yet set; see [LICENSE-STATUS.md](LICENSE-STATUS.md).

## Layout

| Path | Role |
| --- | --- |
| `engine/` | Schemas, validators, specialist protocols, fixtures, and the package builder. |
| `codex/launch-factory/` | The operator skill an agent reads first. |
| `.claude/`, `.agents/`, `.codex/` | Native entry points for Claude Code and Codex. |
| `packages/` | The two built review packages. |
| `voice-bank/` | 25 items of Vista's public writing and the derived tone brief. |
| `barry/` | The three human review cards: claims lock, spot-check, pack approve. |
| `automation/n8n/` | Two importable preparation workflows. |
| `handoff/` | The engineer handoff and marketer run checklist. |
| `docs/` | Operating guide, first run, troubleshooting, and decision records. |

Read [START-HERE.md](START-HERE.md) next, then the [engineer handoff](handoff/ENGINEER-START-HERE.md).
