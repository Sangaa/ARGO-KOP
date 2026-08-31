# MUTATION MATRIX — EJR-244 DISPOSITION + EJR-421 VACANCY PROOF 290

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-244-DISPOSITION-AND-421-VACANCY-PROOF-290
Opening main: `34bade3b130d54f827dd4abea99d6c83d4132429`
Execution role: HERMUZ

## Selection evidence

Current MEMORY_TO_ROOT cohort is 16 after the previous closed repair. EJR-244 is selected by evidence, not numeric order: two legitimate distinct members, two external exact-ID references, and zero external exact-member-path references in the verified census artifact from Internal Document-ID Audit run `33394963190`.

Chronology: Memory EJR-244 allocation commit `82ccbdda485297ed8a206c5dad960ce44f076cbc` (2026-08-15T07:27:45Z) predates root EJR-244 allocation commit `1510161a687a336e8efa52b522ed8ea8aea942a4` (2026-08-17T18:36:56Z). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-244 is RETAINED and root EJR-244 is DISPLACED legitimate content.

Both current records were directly read and are semantically legitimate independent session/engineering records. Current census evidence reports zero exact-member-path consumers for both members.

## Authorized evidence mutation

1. preserve both EJR-244 records unchanged;
2. create a dedicated complete-history vacancy workflow for candidate EJR-421;
3. checkout with `fetch-depth: 0` and fail if shallow;
4. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-421`;
5. upload exact JSON and require `decision == VACANT`;
6. reserve EJR-421 solely for displaced root EJR-244 only after successful proof.

Current search absence for EJR-421 is discovery only and is not vacancy proof.

No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease290.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
