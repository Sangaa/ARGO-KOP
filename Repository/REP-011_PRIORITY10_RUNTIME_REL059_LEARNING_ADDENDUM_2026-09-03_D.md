# REP-011 Priority-10 Runtime REL-059 Learning Addendum — Transaction D

Date: 2026-09-03
Applies to: `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md`
State: `CURRENT BOUNDED REVIEW ADDENDUM / MATERIAL CI PENDING`
Transaction: `MUT-2026-09-03-P10-RUNTIME-REL059-LEARNING-PROMOTION-D`

## Review result

Current source retains `RUN-014 → RUN-011 = VALIDATES`, but executable read-back exposed a real consumer gap: promotion tests synthesized candidates independently instead of consuming the cognitive-loop trace. The gate also omitted RUN-014's governing-conflict scenario and accepted blank required identity/pattern values.

Transaction D adds an explicit trace-to-candidate adapter, uses it in acceptance coverage and fails closed for governing conflict or incomplete identity. Task/session identity, evidence and validation are preserved from the RUN-011 trace. Observed result, pattern, confidence, conflict disposition and promotion authority remain explicit inputs; action authorization is never treated as learning authority.

The first material head preserved a Runtime/integration failure after the gate began requiring an explicit conflict disposition. The tracked `Knowledge/Learning/promotion_gate_adapter.py` consumer still built the earlier candidate shape, so its integration tests reached `CANDIDATE_INCOMPLETE` before the expected authority result. No assertion was weakened. The bounded correction extends that adapter with a separate `governing_conflict` argument, defaults its established interface to no declared conflict, and proves that an explicit conflict remains held even with promotion authority.

## Boundary

`PROMOTION_ELIGIBLE` does not perform knowledge mutation. REL-059 retains its stable ID, direction and `VALIDATES` type. No dependency, consumption, implementation or governance edge is inferred. RUN-011 and RUN-014 remain `Candidate / Integrity Hold`; Runtime Gate 15, Priority 10, Phase 1, the repository-wide graph, Global Connected Baseline and Global Integrity remain open.
