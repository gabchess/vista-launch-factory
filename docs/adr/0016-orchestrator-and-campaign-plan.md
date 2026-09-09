# ADR 0016: Orchestrator front door; Campaign Plan promoted to seventh output

Date: 2026-09-07. Status: accepted (Gabe, grill round 1).

## Decision

Launch Factory gets an **orchestrator seat**: one agent at the front door.
Whatever arrives, a topic, a file dump, a release folder, a one-line ask, the
orchestrator routes it. Its first move on a bare topic is the content-plan expansion
(angles, opinions, stories, FAQs, myths, mistakes, case studies, tips → pieces adapted
per channel without repetition). Its first move on a release folder is the existing
spine (ingest → Claims Lock → adapters → validate → Reviewer).

The **Campaign Plan** (cadence binder promoted) is the seventh output: a day-by-day
multi-channel sequence: emails, social posts (IG/TikTok video, LinkedIn/X/Threads
written), blog, changelog, popup, all drawn from one locked source of truth, approved
by Reviewer as part of the pack.

## Why

The brief's bonus "counts for a lot": a campaign, not six disconnected assets. And the
orchestrator is what makes the system feel like the thing the brief described (a machine
you drop material into) rather than a folder of scripts. One topic in, weeks of plan
out, is the same motion as one folder in, one launch out.

## Consequences

- CONTEXT.md gains: Orchestrator, Campaign Plan, Voice Bank, Run Log (glossary deltas
  staged with this ADR set).
- The old cadence_binder schema becomes the Campaign Plan's data shape; "one-release
  cells" constraint stands (no invented future features).
- Reviewer approves the Campaign Plan inside the same pack-approve gate; WIP=1 unchanged.
- Adapters stay dumb on purpose: the orchestrator decides sequence and channel, adapters
  only draft slots from locked claims.
