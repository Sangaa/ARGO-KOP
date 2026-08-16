# EJR-181 — HERMUZ Bootstrap, Control-Plane Reconciliation & Content-Preservation Learning

Date: 2026-08-16
Session: HERMUZ Session Build / P297 closure
Status: Recorded / Canonical Learning Evidence

## 1. Root Failure That Initiated This Learning

The session initially continued from historical conversation/checkpoint context before proving the repository's current ARGO KOP bootstrap state. This caused the working state to be interpreted from handoff memory rather than from repository reality.

The critical distinction is:
- historical checkpoint ≠ current repository state
- conversation handoff ≠ bootstrap proof
- documented relationship ≠ executable relationship
- test capability ≠ test result
- execution connectivity ≠ governed mutation coupling
- negative search result ≠ repository absence
- missing CI evidence ≠ CI failure or PASS

## 2. Corrective Control

GOV-013A — HERMUZ Bootstrap Integrity Gate was introduced as a canonical addendum to GOV-013.

Required sequence:
BOOTSTRAP PROVEN → CHECKPOINT RECONCILED → SAFE CONTINUATION → MUTATION

Structural mutation must not begin when repository reality has not been established.

Evidence priority:
Repository Evidence > Historical Handoff > Conversation Memory > Assumption

If mutation is discovered to have started before bootstrap proof, stop, establish repository reality, reconcile the mutation history, and only then continue.

## 3. Control-Plane Lessons

The session demonstrated that a repository state can be physically ahead of one or more navigation/control-plane views. Therefore:
- REP-014 relationship state must not be inferred from REP-016 queue state alone.
- REP-015 bootstrap evidence and audit freshness must be distinguished from physical file presence.
- REP-016 checkpoint state must preserve the full queue/history; checkpoint correction must never truncate repository content.
- REP-011/012 are protected registries and must only be mutated with complete-content preservation.
- REP-013 inventory reconciliation must preserve all existing inventory entries.
- REP-020 is the session evidence ledger, not a substitute for canonical registries.

## 4. Mutation Safety Learning

P291/P293 exposed a repeatable failure mode: a mutation that intends to change one registry field can accidentally replace the file with a shortened reconstruction.

New operational rule:
FULL READ → MINIMUM EDIT → WRITE → FULL RE-READ → PROMOTE

If full-content preservation cannot be guaranteed, do not mutate the canonical registry. Record the binding lag and continue only with safe work.

## 5. Runtime / Executable Boundary Learning

The presence of connected_spine_runner → execution_entrypoint proved execution connectivity, but the inspected plan used SIMULATED_REVIEW with side_effect=false. Therefore the spine is connected without proving governed mutation coupling to SRV-009.

GOVERNED_WRITE_DISPATCH exists as executable infrastructure and has tests, but its existence does not prove that ENG-006/RUN-010 invokes SRV-009 through it.

Required distinction remains:
DOCUMENTED → CONTRACTUAL → CONNECTED → EXECUTED → TESTED → VERIFIED

No state may be promoted without evidence for that state.

## 6. Evidence / Search Learning

GitHub/code-search returned negative results for items that were demonstrably present when accessed directly or through commit history. Therefore negative search results are classified as Search/Index Evidence Defect unless independently corroborated.

Likewise, absence of current CI status/workflow runs is classified as NO_CURRENT_CI_EVIDENCE, not PASS and not FAIL.

## 7. Governance Learning

GOV-013A is canonical but is an addendum, not a replacement of GOV-013. It must be represented in navigation/control-plane inventories without inventing unsupported relationship types.

A relationship must use an existing controlled relationship type; if the correct authority/type is unknown, record the gap instead of creating a new semantic type merely to close reconciliation.

## 8. Session-Level Learning

The correct objective is not to maximize the number of mutations. It is to maximize verified progress while preserving repository integrity.

A session may legitimately produce several evidence-only checkpoints when mutation is unsafe.

Never close a gap by weakening the evidence boundary.

## 9. Carry-Forward Rule

At every future session opening:
1. Prove current ARGO KOP bootstrap state from repository reality.
2. Load GOV-013 and GOV-013A.
3. Reconcile current HEAD against the last checkpoint.
4. Verify canonical registry freshness before mutation.
5. Protect long registries from lossy replacement.
6. Treat negative search and absent CI as evidence limitations until corroborated.
7. Continue only after the above gates pass.

## 10. Closure

This learning is recorded specifically to prevent recurrence of the initial bootstrap misunderstanding and the later content-preservation regressions.
