# B2 control structure and C1 human review

## System boundary

Release materials enter a local campaign workspace. The canonical router checks selected source bytes and spans. n8n preparation produces work packets. An operator runs selected prompts through separately available tools and writes drafts/media. The review page loads those artifacts and saves local intent. An eventual service must own generation state, assigned-reviewer events and exact-version export. External publishing remains excluded in v1.

| Loop | Controller → actuator → process → sensor → feedback | Process-model variables | Actions and allowed triggers | Blind spot / operating context |
| --- | --- | --- | --- | --- |
| L-01 source preparation | Operator → Python loader/router → source-bound packet → validation result → operator | PM-01 source revision; PM-02 selected fact spans; PM-03 voice context | ACT-01 prepare when required source and voice inputs exist | A valid span does not prove the rendered claim follows from it. Local filesystem, manual selection, missing or changed source. |
| L-02 generation and retry | Operator / future worker → provider tool → generated artifact → job receipt plus decoded output → operator | PM-04 provider state; PM-05 attempt count; PM-06 budget; PM-07 artifact hash | ACT-02 dispatch after actual authority and provider setup; ACT-03 retry only an affected asset within the bound | Current n8n packet has no provider-state sensor or durable attempt store. Network timeout and desktop-session loss matter at the future seam. |
| L-03 review | Gabe for Tix / Barry for Vista → UI note or human decision → review state → version, source and note display → reviewer | PM-08 artifact version; PM-09 current input digest; PM-10 intent versus applied approval | ACT-04 request changes with feedback; ACT-05 record review against exact bytes | Browser notes survive reload but do not authenticate the reviewer or drive backend state. Cross-browser transfer requires export. |
| L-04 final package | Operator / future service → export builder → package → current binding and approval readback → operator | PM-11 complete output inventory; PM-12 approval matches final bytes | ACT-06 export reviewed version; publishing excluded | Current full-runtime export authorization and recovery were not exercised. A historical fixture flag cannot supply the missing decision. |

## Human roles and feedback

The builder controls local preparation and tool dispatch, with immediate validation output but provider latency outside the tested scope. The reviewer can inspect and annotate an exact asset; feedback is immediate in the local UI. The recipient engineer must configure accounts, storage and worker routing before others can generate. Reggie decides whether the demonstrated trial meets the engagement; no inspected acceptance resolves that decision.

| Role / task | Actual state and likely perception | Cognitive risk / severity | Mitigation and acceptance signal |
| --- | --- | --- | --- |
| Reviewer sees green creative badges | Recorded Gabe creative acceptance exists. The social and login placements still have separate work. | Placement or factual readiness inferred from creative approval / high | Keep the scope note visible with the media and distinguish missing rendition checks in the final package. |
| Marketing starts a new release | Existing page previews a prebuilt campaign; the engineer guide requires several commands and paths. | Assumes a generation service is connected / high | Show setup versus runnable state; test one new operator submitting a real source folder. |
| Reviewer is interrupted | Saved changes survive browser reload; unsaved typing has no verified recovery. | Lost intent or ambiguous handoff / medium | Save explicit feedback; export it for cross-device handoff. Backend must retain authenticated events. |
| Engineer verifies relocated package | Builder route SHA changes with absolute paths. | Treats valid content as corrupt and rewrites provenance / medium | Corrected interface recomputes the route and portable context; relocation regression passes. |
| Operator recovers uncertain render | Future worker lacks observed durable job reconciliation. | Duplicate spend or duplicate versions / high | Reconcile provider job ID before retry; pause a campaign on uncertain status. Test restart before enabling dispatch. |

The current recipient procedure requires tracking workspace path, Python environment, packet paths, reviewer, provider account, media hashes and local feedback export. This exceeds the skill's five-variable working-memory heuristic for routine operation. A non-engineer trial has not measured actual operator effort. Move setup into engineering configuration and expose the next action with retained state.

Alarm review: empty change requests produce an actionable prompt; local-storage failure instructs the reviewer to download notes. The UI has no provider alarms because provider execution is absent. In the future worker, group a failure under its campaign and asset, report the failed step and safe recovery action, and show pending/unknown status until output is observed. Do not show successful generation on a request acknowledgement.

Reversibility: local review intent can be cleared, which was exercised. That action cannot substitute for revoking a server-side approval or cancelling a render. Version 1's absent publishing connection limits current external effects. Proposed interlocks: source change reopens dependent review; untrusted generated HTML must not execute with review-store privileges; backend export checks the assigned human and the current artifact digest. These are future runtime clauses, with deployment evidence still required.
