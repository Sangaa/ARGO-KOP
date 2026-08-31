# MUTATION MATRIX — EJR-243 DISPOSITION + EJR-420 VACANCY PROOF 287

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-243-DISPOSITION-AND-420-VACANCY-PROOF-287
Opening main: `bd0ba60c65c957a90026b390513d0c40be329ea6`
Execution role: HERMUZ

## Selection evidence

Current MEMORY_TO_ROOT cohort is 17 after the previous closed repair. EJR-243 is selected by evidence, not numeric order: two legitimate distinct members, two external exact-ID references, and zero external exact-member-path references in the last verified census.

Chronology: Memory EJR-243 allocation commit `3b4853da0da0e21891b59ad21625f1ed7460396e` (2026-08-15T07:21:12Z) predates root EJR-243 allocation commit `7fbe379e0960499a13e381d2b3d9dca8bec78c8c` (2026-08-17T18:27:22Z). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-243 is RETAINED and root EJR-243 is DISPLACED legitimate content.

Both current records were directly read and are semantically legitimate independent session/engineering records. Current census evidence reports zero exact-member-path consumers for both members.

## Authorized evidence mutation

1. preserve both EJR-243 records unchanged;
2. create a dedicated complete-history vacancy workflow for candidate EJR-420;
3. checkout with `fetch-depth: 0` and fail if shallow;
4. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-420`;
5. upload exact JSON and require `decision == VACANT`;
6. reserve EJR-420 solely for displaced root EJR-243 only after successful proof.

Current search absence for EJR-420 is discovery only and is not vacancy proof.

No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease287.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
