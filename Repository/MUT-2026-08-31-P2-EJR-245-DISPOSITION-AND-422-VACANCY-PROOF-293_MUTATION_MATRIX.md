# MUTATION MATRIX — EJR-245 DISPOSITION + EJR-422 VACANCY PROOF 293

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-245-DISPOSITION-AND-422-VACANCY-PROOF-293
Opening main: `6e00c2a0ca138918ae7c2c9bf02fd97da8f57f41`
Execution role: HERMUZ

## Selection evidence

Current MEMORY_TO_ROOT cohort baseline is 15 after the closed EJR-244 -> EJR-421 repair and Lease292 normalization. EJR-245 is selected by evidence, not numeric order: two legitimate distinct current members, low external exact-ID exposure, and zero external exact-member-path consumers in the last verified census evidence.

Chronology: Memory EJR-245 allocation commit `99e8d80c033da324f0e20dcd2b521cf7d0603d88` (2026-08-15T07:34:09Z) predates root EJR-245 allocation commit `499e90d71a6daadc124b6709910842e24b521795` (2026-08-17T18:41:14Z). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-245 is RETAINED and root EJR-245 is DISPLACED legitimate content.

Both current records were directly read and are semantically legitimate independent engineering/session records. Current search absence for EJR-422 is discovery only and is not vacancy proof.

## Authorized evidence mutation

1. preserve both EJR-245 records unchanged;
2. create a dedicated complete-history vacancy workflow for candidate EJR-422;
3. checkout with `fetch-depth: 0` and fail if shallow;
4. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-422`;
5. upload exact JSON and require `decision == VACANT`;
6. reserve EJR-422 solely for displaced root EJR-245 only after successful proof.

No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease293.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
