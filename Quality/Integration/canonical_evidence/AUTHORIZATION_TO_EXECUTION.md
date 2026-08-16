# Canonical Evidence — Authorization → Execution

Status: VERIFIED / CONTROLLED_SYNTHETIC
Side effect: false

## Bounded Contract

`Decision/authorization_gate.py` is the authorization authority and returns `AUTHORIZED` with `execution_status=NOT_STARTED` only after explicit approval. `Runtime/Execution/execution_entrypoint.py` is the governed execution handoff and rejects any request without explicit authorization or a source trace before producing a canonical execution trace.

The connected-spine runner is the actual runtime caller and passes the authorization result into the governed execution entrypoint. The current path is explicitly simulated and side-effect-free.

## Test

`Runtime/Execution/test_execution_entrypoint.py` proves authorized execution produces a canonical trace handoff, unauthorized execution is rejected, and missing source trace is rejected.

`Runtime/Execution/test_connected_spine_runner.py` proves the integrated caller path reaches `AUTHORIZED`, `PLAN_READY`, the canonical execution trace, and `side_effect=false`, while missing authorization blocks execution and outcome.

## Trace

`Quality/Integration/canonical_evidence/AUTHORIZATION_TO_EXECUTION_TRACE.json`

The trace records the bounded authorized handoff as controlled synthetic evidence. It does not represent external side effects or autonomous production execution.

## Boundary

This evidence certifies the governed Authorization → Execution handoff only. It does not authorize arbitrary actions, external side effects, or autonomous execution.
