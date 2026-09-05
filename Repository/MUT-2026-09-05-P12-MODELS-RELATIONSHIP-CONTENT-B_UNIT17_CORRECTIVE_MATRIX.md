# P12 Models Transaction B — Unit 17 Corrective Matrix

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Corrective scope: `UNIT17 PRE-CLOSURE STATUS GUARD REPAIR`
State: `CORRECTIVE / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Trigger

Unit-17 head `9607e7bfa6e6f1a6b8d5ab570d959967c26412e8` passed M2, Real Matrix and Full-Stack, while Runtime/Integration failed only its integrity job.

Failure evidence:

- Runtime workflow `33978409297`;
- 255 tests passed / 1 failed;
- failing guard: `test_p12_models_status_preserves_open_relationship_boundary`;
- sole stale assertion required literal phrase `relationship/content graph` from an earlier Transaction-A-era status representation.

## Classification

`STALE HISTORICAL WORDING GUARD / CURRENT STATUS SEMANTICS CORRECT / NO MATERIAL REOPEN`.

The failing assertion did not protect a stable contractual representation. The stable invariants are:

- exact seven-path inventory and digest;
- allocation remains non-authoritative;
- Transaction A remains closed;
- Priority 12 remains OPEN before explicit closure;
- Models remains INTEGRITY HOLD / STAGED RECONSTRUCTION before explicit closure;
- canonical relationship synchronization is complete at REP-014 v1.2.20;
- bounded material completion is distinct from transaction/priority closure.

## Authorized change

Exactly two paths:

1. `Quality/Integrity/test_models_p12_exact_inventory_allocation.py`
2. this corrective Matrix

No Models status/source, registry, queue, manifest or other semantic/control-plane artifact is changed.

## Repair

Replace the obsolete free-text phrase assertion with current semantic-contract assertions for:

- `MATERIAL RECONCILIATION COMPLETE / CLOSURE REVIEW PENDING`;
- REP-014 v1.2.20 synchronization complete;
- `CLOSED_FOR_PHASE_1` still absent;
- all pre-existing exact inventory/allocation/Transaction-A/open-P12/HOLD invariants retained.

`TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`

## Next gate

Require exact-head success in all four workflow families before any closure-state binding.

---

End of Corrective Matrix
