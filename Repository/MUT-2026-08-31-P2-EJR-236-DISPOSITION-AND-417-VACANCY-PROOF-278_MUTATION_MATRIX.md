# MUTATION MATRIX — EJR-236 DISPOSITION + EJR-417 VACANCY PROOF 278

Status: PREWRITE / EVIDENCE EXECUTION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-236-DISPOSITION-AND-417-VACANCY-PROOF-278
Opening main: `4160c2ba51e1ca886decfa5da947f6eb5f8337e0`
Execution role: HERMUZ

## Selection evidence

The current deterministic MEMORY_TO_ROOT census is 20/20 and CENSUSED. EJR-236 is selected by evidence rather than numeric order: two legitimate distinct members, only two external exact-ID references in the current census, and zero external exact-member-path references.

Chronology evidence is unambiguous: Memory EJR-236 was allocated on 2026-08-14 (`bc106bd24f8edc48a42c729c212fbb7d2916d022`), while root EJR-236 was allocated on 2026-08-17 (`ae1ae7c6da941d2b1efcc04d9074c9dd52e3d86d`). Under the first-valid historical allocation rule, absent stronger contrary evidence, Memory EJR-236 is RETAINED and root EJR-236 is DISPLACED legitimate content.

## Authorized evidence mutation

1. preserve both EJR-236 records unchanged during this lease;
2. create a dedicated complete-history vacancy workflow for candidate EJR-417;
3. checkout with `fetch-depth: 0` and fail if repository history is shallow;
4. run existing fail-closed `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-417`;
5. upload the exact JSON evidence and require `decision == VACANT`;
6. reserve EJR-417 solely for the displaced root EJR-236 only after successful proof.

No EJR identity mutation, baseline normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease278.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
