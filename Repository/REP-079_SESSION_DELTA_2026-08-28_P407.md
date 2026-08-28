# P407 — Exact-Head Reconciliation and Caller Boundary Inventory

Date: 2026-08-28
Status: `CLOSED / EXECUTION-VERIFIED / CALLER-UNPROVEN / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## Re-entry
Reviewed P406 and prior learning before action. Applied: exact-head attribution, NO RUN ≠ PASS, repair-only-on-observed-failure, and the rule that an inferred execution gap does not itself authorize runtime mutation.

## Live state
PR #64 currently points to exact HEAD `68ed8d6bea6b7cc991dfc7fe5e3880cbd93d5916`.
Two pull-request workflows completed successfully on that exact HEAD:
- ARGO Runtime Prototype and Integration Tests: `33172894344`
- Full-Stack Repository Audit: `33172894355`

The Full-Stack audit completed all listed gates successfully, including current-change Mutation Matrix enforcement, P391 regression, repository-wide audit, runtime evidence and execution identity. Runtime/Integration completed integrity, prototype and integration jobs successfully.

## Caller boundary inventory
Current repository evidence establishes the canonical RUN-010 execution pipeline and explicitly describes `Authorization -> Processing/Execution -> External Execution` plus the conditional relationship `Decision Candidate -> Validation -> Authorization -> ENG-006 Execution -> SRV-009 Controlled Mutation -> Post-Write Validation / Re-read`. RUN-010 also states that this relationship is descriptive and does not claim every runtime operation follows it.

The existing `run010_handoff_contract.py` is a pure contract builder. It validates already-supplied execution provenance and authorization and produces a `ProductionExecutionCandidate`; it performs no dispatch and no repository I/O.

The existing `ENG006_SRV009_PRODUCTION_ADAPTER.py` is a governed adapter. It requires a caller to supply an already-authorized `ProductionExecutionCandidate` and a connector. Its presence therefore proves the downstream callable surface, not upstream RUN-010 reachability.

Search of the current repository evidence did not identify an existing governed RUN-010 caller that supplies the required authorization/provenance into that adapter. Therefore the live caller remains `UNPROVEN`.

## Decision
No runtime caller was invented. No connected-spine wiring was modified. No production connector was invoked. No authorization or provenance source was fabricated. The correct action is to retain the negative boundary and await an existing governed caller/source or a separately authorized design decision.

## Learning disposition
No new learning claimed. This checkpoint consolidates existing knowledge into an explicit inventory: downstream callable evidence does not imply upstream reachability; exact-head CI proves execution of the tested seam, not existence of an untested caller.

## Close
`P407 CLOSED / EXACT-HEAD VERIFIED / CALLER-UNPROVEN / NO RUNTIME MUTATION / NO PROMOTION`

## Next checkpoint
Only inspect/design against an identified governed authorization/provenance source. If none exists, remain at the negative boundary rather than manufacturing a caller.
