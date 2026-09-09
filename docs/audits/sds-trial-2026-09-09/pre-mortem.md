# A2: mode confusion across preparation, generation and approval

Horizon: twelve months after a team accepts this repository and expands it into a shared service. This is a hypothetical failure analysis of the current build boundaries.

## Illusion of health

Every source packet has a hash, tests stay green and the review screen shows accepted creative. The team starts treating a prepared packet as a completed workflow. Staff routinely move files and approve browser notes by convention. A new maintainer assumes that the UI and backend share the same approval state because their campaign IDs agree.

## Failure timeline

1. Latent pathogen: preparation, generated output and human intent use neighboring status concepts without a tested shared runtime. CL-03 assumes the complete handoff satisfies the trial.
2. Trigger: a source document changes while an older media render is still pending. The operator starts another attempt after a timeout.
3. Propagation: the provider completes the first job late; a callback replaces the visible artifact while a prior approval remains associated with its logical ID. A caller-supplied attempt count resets the retry budget.
4. Impact: the team exports an old claim or unreviewed rendition and incurs duplicate render cost. Customer trust and the maintainer's credibility suffer.
5. Operator interaction: staff see a prepared status and a green badge, then manually export the package. A missing observed-state check lets that misunderstanding cross the human boundary.
6. Observability paradox: schema, source-hash and prompt tests pass throughout. None observes the final provider artifact against the assigned human's exact decision.

## Failure mechanisms

| ID | Mechanism / archetype | Boundary and misleading signal | Missing signal / tripwire | Violated assumption and detection gap | Recovery / cost / design impact |
| --- | --- | --- | --- | --- | --- |
| FM-01 | Prepared status treated as execution / Mode Confusion | L-02 packet to worker; `ready_for_operator` sounds complete | Persisted job ID, state and output hash; any absent receipt prevents completion | CL-03 load-bearing; tests inspect preparation only | Pause campaign and reconcile job / moderate; require explicit state separation before service acceptance |
| FM-02 | Old human intent survives changed render / Mode Confusion | L-03 to L-04; green creative badge beside a changed artifact | Reviewer, version and source/output digests at export; any mismatch holds export | CL-03 load-bearing; local note checks do not cover backend ordering | Invalidate affected review and return latest asset / moderate; export interface must enforce the binding |
| FM-03 | Source hash masks an unsupported claim / Mode Confusion | L-01 to L-03; exact citation is mistaken for meaning | Statement-level support and simulated/planned/current classification; one unsupported product claim holds its asset | CL-05 load-bearing; no calibrated semantic review result | Revise claim or obtain product evidence / moderate; preserve semantic review independently of file checks |
| FM-04 | Retry restarts an already-submitted job / Mode Confusion | L-02 provider to operator; local request times out | Durable attempt ledger, cost ceiling and reconciliation result; unknown prior submission blocks retry | CL-03 load-bearing; worker not integrated | Pause, query job state, retain completed output / potentially expensive; add durable idempotency before dispatch |

## Preventative actions

| Action | Category / targets | Minimal implementation detail | Acceptance signal |
| --- | --- | --- | --- |
| System must keep prepared, submitted, pending, rendered, reviewed and exported states distinct. | Interface / FM-01 | Persist transitions and provider job ID per artifact | A submitted request never displays rendered without a readable artifact |
| System must check the assigned human's exact subject at export. | Constraint / FM-02 | Bind identity, artifact version/hash and input digest; commit state atomically | Changed source or callback cannot export using an old approval |
| System must hold unsupported product claims even when citation bytes match. | Verification / FM-03 | Preserve explicit claim-to-span review including image and speech claims | Adversarial valid-span/unsupported-claim example is held |
| System must reconcile uncertain jobs before retrying them. | Control / FM-04 | Durable attempts, job idempotency, agreed cost bound and manual recovery state | Duplicate callback and restart tests produce one accepted artifact without duplicate dispatch |

## Apply these changes

- **Constraints:** v1 stays without automatic publication. Unknown execution status holds further paid dispatch. Each client asset needs its assigned reviewer before release.
- **Verification:** run a complete six-output campaign, then change a source, replay a callback and restart the worker. Falsification: old approval passes, a duplicate render dispatches, or source-to-package lineage breaks.
- **Interfaces:** adopt the job-state and export clauses above; IF-ARTICLE-VERIFIER-CONTEXT governs the local portability fix. Runtime critical interfaces remain unimplemented and need contract review before implementation.
- **Observability:** show job ID and last observed provider state. Missing output or approval-binding mismatch immediately holds the affected asset. Stop the campaign if a retry's prior result is unknown.
- **Rollback:** safe state is paused dispatch and blocked export with artifacts and decisions preserved. Reconcile jobs, restore the last known release, and reopen affected review. Test this procedure on the recipient worker; no operational rollback test was possible in this audit.
- **Readiness:** require a new operator run, exact six-output inventory, recorded full run and tested recovery before full-trial completion.
- **Decision note:** keep the current preparation layer as the starting point. Reopen the approach if the chosen app host cannot retain state, background jobs and reviewer decisions through restart. No executive waiver was requested or recorded.

Commitment gate: the future worker needs observable provider state and exact-version export checks before it can make irreversible calls. The audit PR can proceed with these blockers retained. The local regression tests address FM-01's verification confusion at one file boundary; they do not clear the system-level recovery gate.
