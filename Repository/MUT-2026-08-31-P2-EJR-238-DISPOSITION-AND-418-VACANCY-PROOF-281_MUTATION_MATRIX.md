# MUTATION MATRIX — EJR-238 DISPOSITION + EJR-418 VACANCY PROOF 281

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-238-DISPOSITION-AND-418-VACANCY-PROOF-281
Opening main: `5b3d9fefc199755fdb284488dd61c2a8b7f40177`
Execution role: HERMUZ

## Selection evidence

The current deterministic MEMORY_TO_ROOT census is 19/19 and CENSUSED. EJR-238 is selected by evidence rather than numeric order: two legitimate distinct members, two external exact-ID references in the current census, and zero external exact-member-path references.

Chronology is unambiguous: Memory EJR-238 was allocated on 2026-08-15 (`e299765f029939b8798a41cbe561872f0a2ea741`), while root EJR-238 was allocated on 2026-08-17 (`1898e3b7e31fb599f42ae33af0efa5880480b2fd`). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-238 is RETAINED and root EJR-238 is DISPLACED legitimate content.

Fresh exact search for `EJR/EJR-238_2026-08-17_P322_RECONCILIATION_UPDATE.md` returned zero current consumers.

## Authorized evidence mutation

1. preserve both EJR-238 records unchanged during this lease;
2. create a dedicated complete-history vacancy workflow for candidate EJR-418;
3. checkout with `fetch-depth: 0` and fail if repository history is shallow;
4. run existing fail-closed `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-418`;
5. upload exact JSON evidence and require `decision == VACANT`;
6. reserve EJR-418 solely for the displaced root EJR-238 only after successful proof.

No EJR identity mutation, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease281.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
