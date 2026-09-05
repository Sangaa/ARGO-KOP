# P12 Models Transaction B — Unit 18 Corrective Matrix

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Corrective scope: `UNIT18 POST-CLOSURE SEMANTIC-GUARD TRANSITION`
State: `CORRECTIVE / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Trigger

Unit-18 closure-state head `950ecab850ddb1b40cf10df14c781c55db9a3e79` passed M2, Real Matrix and Full-Stack, while Runtime/Integration failed only its integrity job.

Failure evidence:

- Runtime workflow `33978962770`;
- prototype and integration jobs: SUCCESS;
- integrity suite: `257 passed / 3 failed`;
- two failures required historical literal `INTEGRITY HOLD / STAGED RECONSTRUCTION` in the Models folder status;
- one failure required the superseded REP-020 queue checkpoint `P12-B-MODELS-RELATIONSHIP-CONTENT / CANONICAL REP-014 SYNCHRONIZATION`.

## Classification

`STALE PRECLOSURE REPRESENTATION GUARDS / BOUNDED CLOSURE SEMANTICS INTACT / NO MATERIAL REOPEN`.

Direct guard-source review shows the protected invariant behind the first two tests is that bounded Models evidence must not become consolidated domain-canonical or global certification. The stable current representation of that invariant is now:

- `Canonical: Pending consolidated validation`;
- `CLOSED_FOR_PHASE_1 / BOUNDED MODELS PARTITION CERTIFIED / DOWNSTREAM AND GLOBAL HOLDS REMAIN`;
- explicit statement that bounded closure does not promote individual model maturity;
- explicit Global/Phase-1 non-closure boundaries.

The historical `INTEGRITY HOLD / STAGED RECONSTRUCTION` literal is therefore no longer the stable contractual representation after the explicit bounded closure decision.

The REP-020 failure is a direct checkpoint transition: canonical REP-014 v1.2.20 remains unchanged and bound, while the current manifest checkpoint legitimately advances to the same-change-set P12 closure-state/REP-016 v1.3.2 binding.

## Authorized corrective change

Exactly four paths are authorized:

1. `Quality/Integrity/test_models_identity_inventory_alignment.py`
2. `Quality/Integrity/test_models_relationship_bidirectionality.py`
3. `Quality/Integrity/test_models_p12_registry_allocation_plan.py`
4. this corrective Matrix

No Models status/source, REP-014, REP-016, REP-020 or other semantic/control-plane artifact is mutated.

## Repair semantics

- Identity/inventory guard retains filename↔Document-ID alignment and individual `Canonical: Yes` checks, but tests the folder-level nonpromotion boundary through `Canonical: Pending consolidated validation`, bounded closure wording, unchanged individual maturity and Global non-closure.
- Bidirectionality guard retains the two inspected direct relationship checks and tests nonpromotion at the current bounded closure representation.
- Registry allocation guard retains exact REL-001..123 binding, stable-ID corrections and no-edge protection, and advances only its current REP-020 checkpoint expectation to the verified closure-state manifest while continuing to require REP-014 v1.2.20 and Phase 1 OPEN.

`TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`

## Next gate

Require exact-head SUCCESS in M2, Real Matrix, Full-Stack and Runtime/Integration before Matrix-only Transaction-B closure.

---

End of Unit-18 Corrective Matrix
