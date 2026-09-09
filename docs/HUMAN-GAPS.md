# What still needs a human, and why

This is the honest accounting for Launch Factory. It says what a human must do, what
is genuinely unfinished, and why each gap exists. Read this before you judge the two
built packages under `packages/`.

## Human decisions the factory will never make

These stay with a person by design, not by accident.

- **Claims Lock.** Only Reviewer (or the product owner, for internal test runs) knows what a
  company may promise. The factory extracts candidate claims with evidence; a human
  decides which ones ship.
- **Final voice call.** The voice bank flags drift from the product's own published writing,
  but a similarity score is not truth. A human decides whether a draft sounds right.
- **Video, animation, and popup art.** Real footage and creative judgment are required.
  The factory can draft scripts and copy around them, not replace them.
- **Publish, send, schedule.** Nothing in this repository publishes a page, sends an
  email, or schedules a post. That line is intentional, not a missing feature.
- **Which feature, which week.** The factory runs a launch someone has already chosen. It
  does not decide what ships or when.

## What is built and working today

- The claim-evidence pipeline: every allowed claim in the two shipped packages traces to
  a file, an offset, and a quote. `engine/scripts/validate_ledger.py` enforces this and
  arms a kill-switch when it fails.
- The approval state machine: `engine/scripts/transition_slot.py` only allows the
  transitions listed in its own docstring, and refuses `approved` or `packaged` without a
  `--human-confirmed` flag. `engine/scripts/validate_record.py` separately refuses to
  accept either state unless a matching Reviewer decision is recorded. Neither script lets
  the writer role approve its own work.
- Twelve specialist roles (`.claude/agents/`, `.codex/agents/`) that draft one output each
  from locked claims only.
- A review package you can open today: [the internal test-product run](../packages/camp_tix_launch_001/01_channel_run/review.html).

## What is not built yet

**The non-engineer trigger is Phase B.** Today, an engineer runs the pipeline from Claude
Code or Codex, one command or one chat prompt at a time. A hosted app where a marketer
submits a release folder, watches progress, and downloads a package without an engineer
in the loop does not exist yet. That is the next phase of work, not a hidden feature of
this repository.

**End-to-end pipeline packaging is still being closed.** The two packages under
`packages/` were hand-assembled: an engineer ran ingest, the specialist roles, and the
package scripts step by step, then reviewed the result. There is no single command today
that takes a raw release folder and produces a finished, six-output package unattended.
The pieces exist (`run.sh`, the specialist protocol, the validators) and are wired
together for the demonstrated runs; they have not yet been proven on a fresh source folder
with no engineer touching intermediate steps.

**The two n8n workflows prepare work packets only.** `automation/n8n/channel-production/`
and `automation/n8n/ugc-app-reveal/` validate a request and return a structured packet.
Neither dispatches a provider job, waits on a callback, or writes an approval record. The
worker that would take a packet and actually call a video or text provider is unbuilt.

**No persistent, authenticated approval store exists.** `--human-confirmed` is a CLI flag
a person passes by hand. It proves intent in this repository's structural sense; it does
not authenticate who typed it. A production system needs a real login and an approval
event tied to an exact artifact version, not a flag.

**Recovery and retry are manual.** Nothing in `engine/scripts/` retries automatically.
When a validator fails, `run.sh` prints the failed check and stops. A person decides the
next step. There is no bounded-retry, cost-capped job queue yet.

## Historical fixture note

Earlier v0.2.0 planning treated slots 1 (social video), 5 (login animation), and 6 (in-app
popup) as held stubs. That plan changed for the internal test-product package, which now
has real creative approved by the product owner for that test run (a 55-second product film
and a 10-second login animation). A package built for a real client product would instead use
concept previews when no private footage is available. Neither approach carries Reviewer's
final approval on its own; both are review-ready drafts until Reviewer signs off.

## Where to verify this yourself

```bash
.venv/bin/pytest -q
.venv/bin/python packages/camp_tix_launch_001/01_channel_run/verify_package.py
```
