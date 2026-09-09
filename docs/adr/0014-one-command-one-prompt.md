# ADR 0014: One command, one chat prompt, one spine

Date: 2026-09-07. Status: accepted (Gabe, grill round 1).

## Decision

The operator surface is two doors over the same spine:

1. `./run.sh <release-folder>`: venv, ingest, brief, Claims Lock draft, adapters,
   validation, Barry package, run log. Non-engineers never open code.
2. A chat-prompt door: "Run Launch Factory on this release folder" inside any host
   agent, backed by the installed skill; when Python/engine is unavailable it falls back
   to the chat-only Claims Lock draft shape, fail closed (already documented).

## Why

The brief: "marketing, dev, or product should all be able to trigger it." One spine,
two triggers, means the gates (Claims Lock, spot-check, pack approve) are identical no
matter which door runs, so Barry reviews the same artifact shapes.

## Consequences

- The run log (ADR 0016 material) is written by both doors.
- HOST-MATRIX must state which door was verified on which host.
