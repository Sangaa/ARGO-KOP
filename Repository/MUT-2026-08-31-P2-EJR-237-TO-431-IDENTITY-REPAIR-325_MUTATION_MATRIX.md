# MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325
Protocol: GOV-013 / GOV-014A
Status: OPEN / CI-HARD-HOLD / CONTROLLED ROLLBACK
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 325-01 | `EJR/EJR-431_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | CREATE | displaced root content with first-H1 identity EJR-431; semantic body/date/chronology preserved | N | N |
| 325-02 | `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | DELETE | old root identity absent in same atomic tree | N | N |
| 325-03 | `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` | UPDATE | move semantic evidence references whose referent is root EJR-237 negative-runtime evidence to EJR-431 only | N | N |
| 325-04 | `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md` | UPDATE | move root-negative-runtime evidence heading/reference EJR-237 → EJR-431 only | N | N |
| 325-05 | `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md` | KEEP | retained earlier allocation byte-for-byte | Y | N |
| 325-06 | census expected baseline | KEEP | remain 6 during repair; expected drift failure must be preserved for separate rebaseline | Y | Y |
| 325-R1 | first functional attempt `423170ca485bb8693b23fd1044d573b989e49c9f` | ROLLBACK | restore all three functional surfaces to pre-attempt state because protected REP-020 changed without a Matrix in the same CI diff | N | N |

## KEEP REQUIREMENT
Preserve the original repair scope and evidence. The first functional attempt is not accepted as closure evidence because Full-Stack run `33426813721` failed at current-change Mutation Matrix enforcement: `protected_changes=1`, `mutation_matrices=0`, protected path `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md`. The pre-write Matrix existed in the parent, but the CI gate requires a Matrix inside the same changed-file set. No semantic or runtime failure was observed. Roll back the root rename and both semantic consumer rewrites atomically, with this Matrix changed in the same rollback commit, before re-executing the identical bounded repair with the Matrix in that same functional commit.

## Execution Evidence
Lease323 retained Memory EJR-237. Lease324 run `33426371329` proved EJR-431 VACANT. First functional attempt `423170ca485bb8693b23fd1044d573b989e49c9f` had the intended exact semantic diff and P4 safety gates passed, but Full-Stack run `33426813721` HARD-HOLD failed solely at `Enforce Mutation Matrix on current change set`. This is classified as a same-change-set governance binding defect, not a semantic repair defect.

## Closure
Do not close Repair325. First complete and verify the atomic rollback, then re-execute the same bounded repair with this Matrix included in the same functional commit. Preserve baseline 6 throughout. Any non-Matrix failure blocks continuation.
