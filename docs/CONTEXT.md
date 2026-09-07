# Vista Launch Factory

The bounded context for turning one Vista feature-release folder into six review-ready launch artifacts plus a one-release campaign cadence, with Barry as the only copy/creative ship gate.

## Language

**Launch Factory**:
The system that turns one release folder into review-ready launch artifacts. Not a prompt. Not auto-publish.
_Avoid_: pipeline, motion, machine, orchestrator (except as informal talk)

**Release Campaign**:
One campaign object for one feature ship. Holds status, sources, six artifact slots, cadence, Barry queue, HubSpot sandbox state.
_Avoid_: project, job, workflow run

**Claim Ledger**:
The allowed / forbidden / needs-disclaimer list plus evidence spans for one campaign.
_Avoid_: facts list, brand rules, compliance pack

**Claims Lock**:
Barry's once-per-campaign yes on the Claim Ledger. Adapters stay cold until this passes.
_Avoid_: brand check, first review, copy review

**Adapter**:
The cell that drafts one output slot (social video, blog, email, changelog, login animation, in-app popup) from locked claims only.
_Avoid_: generator, writer, skill

**Cadence Binder**:
The one-release schedule that sequences the six outputs across channels (changelog → interrupt email → story video → written social + IG/TikTok).
_Avoid_: campaign calendar, content plan, blast list

**Barry**:
The VP Marketing seat. Only human who Approves copy and creative. Writer is never this seat.
_Avoid_: approver, HITL, marketing lead (when you mean this gate)

**Fixture**:
A labelled fake release used for rehearsal. Placeholders only (`FEATURE_NAME`). Not real Vista product facts.
_Avoid_: mock, sample, demo data (when you mean this labelled pack)

**Held**:
An artifact slot kept empty on purpose, with a reason, instead of inventing a claim or asset.
_Avoid_: skipped, missing, N/A (when a slot is intentionally stopped)

**Kill-switch**:
Armed when an allowed claim has no evidence or forbidden text appears. Factory stops drafting.
_Avoid_: error, fail, block

**Honesty Doc**:
The list of steps that still need a human, shipped with the package.
_Avoid_: limitations, known issues, TODO

**Vista Work**:
The Wed hero feature. Claims come only from the shared Barry email PDF plus the trial brief. Not a full Drive release folder yet.
_Avoid_: FEATURE_NAME, generic social tool, Work (alone)

**Demo Asset**:
A generated mockup/video/example made for the Wed recording so the system looks cool. Not evidence for Claims Lock. Not from Vista internal docs/access.
_Avoid_: fixture (fixture = labelled fake claims pack), real output, production creative

**Pilot MVP**:
What the $1k buys: prove we understand the ask/pain, a clear Launch Factory design, and a cool recorded demo. Not a fully wired production system.
_Avoid_: FTE scope, full automation, production HubSpot

**Close Ask**:
The end of the Wed demo: hire Gabe, fund a deeper build, or take the MVP handoff. Not part of Claims Lock.
_Avoid_: soft CTA, next steps (when you mean this fork)

**Tech Demo (Wed)**:
A mocked/simulated interactive run of the Launch Factory with made-up data for a normie audience. Clips can feed the UGC open. Not Claims Lock evidence.
_Avoid_: production app, live HubSpot, fixture (claims pack)
