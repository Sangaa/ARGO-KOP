# MUTATION MATRIX — EJR-246 DISPOSITION + EJR-423 VACANCY PROOF 296

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-246-DISPOSITION-AND-423-VACANCY-PROOF-296
Opening main: `98c81b0920425b2dc9a14baf5026c72ddf46b56e`
Execution role: HERMUZ

## Selection evidence

Current MEMORY_TO_ROOT cohort baseline is 14 after closed Repair294 and Lease295 normalization. EJR-246 is selected by evidence, not numeric order: final census artifact `9762099086` shows only 3 external exact-ID references, all confined to prior cohort-governance records, and zero external exact-member-path consumers for either current EJR-246 member.

Chronology:
- Memory EJR-246 allocation commit `899924bf6916129db59ef2a5eb035c5f969ea5c7` at 2026-08-15T07:35:51Z.
- Root EJR-246 allocation commit `35ec18ca6a0444ecc945e72fe10ac4374713dbdd` at 2026-08-17T18:54:52Z.

Both current records were directly read and are semantically legitimate independent records. The Memory record is a P65 session-closure record; the root record is M2 proposal-write reusable-learning evidence. Neither invalidates the other. Under the first-valid historical allocation rule, absent stronger contradictory evidence, Memory EJR-246 is RETAINED and root EJR-246 is DISPLACED legitimate content.

Current search absence for EJR-423 is discovery only and is not vacancy proof.

## Authorized evidence mutation

1. preserve both EJR-246 records unchanged;
2. create a dedicated complete-history vacancy workflow for candidate EJR-423;
3. checkout with `fetch-depth: 0` and fail if shallow;
4. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-423`;
5. upload exact JSON and require `decision == VACANT`;
6. reserve EJR-423 solely for displaced root EJR-246 only after successful proof.

No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease296.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
