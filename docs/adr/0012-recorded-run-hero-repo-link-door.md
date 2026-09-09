# ADR 0012: Wed hero: recorded run first, pack as handoff proof

Date: 2026-09-07. Status: accepted (Gabe, grill round 1).

## Decision

Wednesday's presentation leads with the recorded end-to-end run: raw release folder in,
six outputs + campaign cadence out, Barry gates visible, nothing auto-published. The
installable workflow pack follows as the handoff artifact, distributed as a **repo link**
(not a ZIP as primary): any host agent (Claude Code, ChatGPT, Codex, Cursor)
receives the URL plus "install this workflow pack" and self-installs from README + START-HERE.

## Why

Reggie's brief says "show the recorded video of the run." The brief also says the
evaluation is judgment over tooling. A recorded run shows judgment; the repo-link pack
shows a stranger can keep it. Supersedes the old lock where the workflow pack was the hero and
schemas were inside it; the machine and its evidence lead, the envelope carries it home.

## Consequences

- Repo root README becomes an install door for agents, not marketing prose.
- ZIP stays as the Claude-host door inside `claude/` (repo root, since v0.2.0).
- The recorded run must be pre-baked (DESIGN-LOCK §3 stands): no live generation waits.
