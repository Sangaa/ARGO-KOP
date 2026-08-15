# REP-020 — SESSION DELTA — 2026-08-15 — P129

Platform: ARGO KOP  
Checkpoint: P129  
Status: Active / Integrity Hold  
Predecessor: P128

## Work Completed

- Inspected `Learning Readiness → Learning Promotion Gate` as the next actual cross-layer boundary rather than treating `Learning Pipeline → Readiness` composition as a separate seam.
- Confirmed the readiness report explicitly delegates authority to `EXISTING_LEARNING_PROMOTION_GATE` and never claims promotion authority itself.
- Confirmed the Knowledge-layer adapter is the actual boundary into the prototype promotion gate and maps governed evidence into the gate's minimal candidate shape.
- Confirmed the promotion gate is side-effect-free and requires explicit `promotion_authority=True`; without it, valid evidence is held with `PROMOTION_AUTHORITY_MISSING`.
- Added a bounded direct integration test covering both sides of that authority boundary: readiness evidence cannot promote by default, while explicit authority is the only condition that permits `PROMOTION_ELIGIBLE` under otherwise valid evidence.
- No Runtime/Memory mutation was made.

## Finding

`Learning Readiness → Learning Promotion Gate` is a genuine cross-layer boundary with an explicit authority contract. The safe invariant is not "readiness promotes"; it is "readiness remains non-authoritative until an external promotion authority is explicitly supplied." The new test directly proves that boundary.

## Decision

- Keep readiness non-authoritative.
- Do not connect readiness directly to persistence or Memory promotion.
- Validate the new boundary through CI before any Matrix/Registry reconciliation.
- Do not certify the seam from test definition alone.

## Next Highest-Value Work

Observe CI for P129. If green, inspect the existing promotion-gate evidence/trace path and determine whether this boundary has canonical Contract + Test + Trace evidence. If the trace cannot establish the exact boundary, keep it partial and move to the next real cross-layer seam.

## Checkpoint Classification

`PROVISIONAL_CHECKPOINT / EXPLICIT-PROMOTION-AUTHORITY BOUNDARY TEST ADDED`

P129 does not close the Connected Baseline gate.
