# MUTATION MATRIX — EJR-239 DISPOSITION + EJR-419 VACANCY PROOF 284

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-239-DISPOSITION-AND-419-VACANCY-PROOF-284
Opening main: `cd4ae1ff080d2f27f0166c9d8bc989253fdccaea`
Execution role: HERMUZ

## Selection evidence

Current deterministic MEMORY_TO_ROOT census is 18/18 CENSUSED. EJR-239 is selected by evidence, not numeric order: two legitimate distinct members, two external exact-ID references, and zero external exact-member-path references.

Chronology: Memory EJR-239 allocation commit `33dac661bd794043ddd651605351c56a5c037119` (2026-08-15) predates root EJR-239 allocation commit `6d1f6b28088feac82d3eba669b4a3542e5baf338` (2026-08-17). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-239 is RETAINED and root EJR-239 is DISPLACED legitimate content.

Fresh exact search for `EJR/EJR-239_2026-08-17_P1_MUTATION_MATRIX_PREFLIGHT.md` returned zero current consumers.

## Authorized evidence mutation

1. preserve both EJR-239 records unchanged;
2. create a dedicated complete-history vacancy workflow for candidate EJR-419;
3. checkout with `fetch-depth: 0` and fail if shallow;
4. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-419`;
5. upload exact JSON and require `decision == VACANT`;
6. reserve EJR-419 solely for displaced root EJR-239 only after successful proof.

No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease284.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
