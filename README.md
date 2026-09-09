# Launch Factory

One feature-release folder in. A review-ready launch package out. A person approves every word before anything leaves.

Hand your AI agent this repository and one release folder: a transcript, a feature outline, raw screen or product footage, a link, a repo, whatever you have. It returns six launch assets and a campaign plan. Every product claim traces to a quoted source. Every asset waits for a human decision. Nothing publishes, sends, or schedules.

It runs two ways:

- **From an agent.** Open this repository in Claude Code or Codex, then ask, in plain language: `Run Launch Factory on this release folder.` The operator reads the release folder, drafts each asset, and stops at every gate below for a human decision.
- **From the command line.** Run `./run.sh RELEASE_FOLDER` for the same ingest, validate, and package steps, no agent required.

## What comes out

| # | Output | What you get |
| --- | --- | --- |
| 1 | Social video | A short cut with burned-in captions, plus the IG/TikTok script and shot plan. |
| 2 | Blog post | Markdown and HTML, ready for your own blog, with images. |
| 3 | Email announcement | Five variants, segmented by audience: you define the segments, the run fills them. |
| 4 | Changelog post | A short versioned entry for your own changelog. |
| 5 | Login animation | A short looping motion piece for your own login or site. |
| 6 | In-app popup | Graphic, copy, and a working dialog preview. |
| 7 | Campaign plan | A two-week calendar across email, popup, blog, LinkedIn, X, Threads, and IG/TikTok, with a human gate on every row. |

## A run you can open now

| Run | Source | Media | Open |
| --- | --- | --- | --- |
| Tix | A real product release, run by an engineer from Claude Code with local tools | Two accepted video renditions, each referenced by exact hash | [review page](packages/camp_tix_launch_001/01_channel_run/review.html) |

Both finished videos ship in this repository and play in the browser: [product film](packages/camp_tix_launch_001/media/tix-product-film-v3.mp4) and [login animation](packages/camp_tix_launch_001/media/tix-login-animation.mp4).

Tix outputs, readable without a server: [blog](packages/camp_tix_launch_001/01_channel_run/blog/article.md), [emails](packages/camp_tix_launch_001/01_channel_run/email/), [changelog](packages/camp_tix_launch_001/01_channel_run/changelog/entry.md), [popup copy](packages/camp_tix_launch_001/01_channel_run/popup/copy.md), [calendar](packages/camp_tix_launch_001/01_channel_run/campaign/calendar.csv), [claim ledger](packages/camp_tix_launch_001/00_baseline/claim-ledger.json). Package guide: [01_channel_run/README.md](packages/camp_tix_launch_001/01_channel_run/README.md).

## How a run works

| Stage | What happens | Who decides |
| --- | --- | --- |
| Ingest | Every source file is hashed into one release record. | System |
| Ground | Claims are extracted with a file, offset, and quote each, and an optional voice bank checks drafts against the product's own writing. | System |
| Claims Lock | Allowed, forbidden, and held claims are confirmed once. | Reviewer |
| Create | Twelve specialist roles draft each asset from locked claims only. | System |
| Review | Scripts check evidence, slot completeness, and approval authority; a specialist checks voice and Reviewer makes the final call. | System, then Reviewer spot-check |
| Package | A review page, honesty note, and campaign plan are assembled. | Reviewer approves |
| Stop | Publishing, sending, and scheduling stay with a person. | Human |

## Where the checks live

- A claim without an evidence span arms the kill-switch before any drafting starts.
- Reviewer locks claims before fan-out, the cheapest point to stop a wrong promise.
- The first blog draft gets a spot-check before the other assets are written.
- The writer role can never approve. Moving a slot to `approved` or `packaged` needs a `--human-confirmed` flag from a person, and `validate_record.py` refuses to accept either state unless a matching Reviewer decision is recorded.
- Each validator runs once. On failure, `run.sh` prints the failed check and the safest re-entry point, then stops. Nothing retries automatically.

## Run it

```bash
git clone https://github.com/gabchess/launch-factory.git
cd launch-factory
./run.sh engine/fixtures/demo-release
```

`run.sh` creates a virtual environment on first use, then runs ingest, validation, and packaging with stage banners. `engine/fixtures/` also has `mock-gtm-ship` (a fuller sample release) and `specialist-demo` (routing only, no packaging). The same spine runs from a chat prompt in Claude Code or Codex.

Open the Tix review:

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt
python3 packages/camp_tix_launch_001/01_channel_run/serve_review.py --port 8770 \
  --film packages/camp_tix_launch_001/media/tix-product-film-v3.mp4 \
  --animation packages/camp_tix_launch_001/media/tix-login-animation.mp4
```

Then open `http://127.0.0.1:8770/01_channel_run/review.html`. The server binds to loopback and checks each video against its recorded SHA-256 before serving it. Drop both flags and the four drafted outputs (blog, email, changelog, popup) still render on their own.

## Verify

```bash
.venv/bin/pytest -q
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/verify_package.py
```

Expected: every test passes, and the Tix package verifier prints `"status": "pass"` with no human approval recorded yet.

## What still needs a human

| Job | Why |
| --- | --- |
| Claims Lock | Only Reviewer knows what the product may promise. |
| Final voice call | A voice bank flags drift; taste decides. |
| Video, animation, and popup art | Real footage and creative judgment are required. |
| Publish, send, schedule | Never automated in v1, by design. |
| Which feature, which week | The factory runs launches; it does not choose them. |

## Status and limits

- Reviewer has not approved any output; every asset is a review-ready draft.
- Today an engineer runs the media lane from Claude Code or Codex. A hosted app where a non-engineer clicks a button and gets a package back is the next phase (Phase B), not built yet.
- The built package under `packages/` was hand-assembled by an engineer running the scripts and specialists step by step. The single command that ingests a folder and packages six outputs end to end, unattended, is still being closed.
- Two n8n workflows prepare work packets; they do not yet dispatch a provider worker.
- No voice-bank corpus ships with this repository. Bring your own if you want the voice check; the pipeline runs without one.

Full detail on what still needs a human and why: [docs/HUMAN-GAPS.md](docs/HUMAN-GAPS.md).

## License

MIT. See [LICENSE](LICENSE). Fork it, change it, ship it commercially; keep the copyright notice, and expect no warranty. What the grant does not cover (runtimes, provider accounts, your own inputs and outputs) is set out in [LICENSE-STATUS.md](LICENSE-STATUS.md).

## Layout

| Path | Role |
| --- | --- |
| `engine/` | Schemas, validators, specialist protocols, fixtures, and the package builder. |
| `codex/launch-factory/` | The operator skill an agent reads first. |
| `.claude/`, `.agents/`, `.codex/` | Native entry points for Claude Code and Codex. |
| `packages/` | The one built review package (Tix). |
| `voice-bank/` | Where a voice-bank corpus and its derived tone brief go, if you provide one. |
| `reviewer/` | The three human review cards: claims lock, spot-check, pack approve. |
| `automation/n8n/` | Two importable preparation workflows. |
| `handoff/` | The engineer handoff; start at `handoff/ENGINEER-START-HERE.md`. |
| `docs/` | Operating guide, first run, troubleshooting, decision records, and the [engine reference](docs/REFERENCE.md). |

Read [START-HERE.md](START-HERE.md) next, then the [engineer handoff](handoff/ENGINEER-START-HERE.md).
