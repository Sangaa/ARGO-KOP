# MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325
Protocol: GOV-013 / GOV-014A
Status: OPEN / REEXECUTION PREWRITE / SAME-CHANGE-SET BINDING
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 325-01 | `EJR/EJR-431_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | CREATE | displaced root content with first-H1 identity EJR-431; semantic body/date/chronology preserved | N | N |
| 325-02 | `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | DELETE | old root identity absent in same atomic tree | N | N |
| 325-03 | `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` | UPDATE | move semantic evidence references whose referent is root EJR-237 negative-runtime evidence to EJR-431 only | N | N |
| 325-04 | `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md` | UPDATE | move root-negative-runtime evidence heading/reference EJR-237 → EJR-431 only | N | N |
| 325-05 | `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md` | KEEP | retained earlier allocation byte-for-byte | Y | N |
| 325-06 | census expected baseline | KEEP | remain 6 during repair; expected drift failure must be preserved for separate rebaseline | Y | Y |
| 325-R1 | rejected attempt `423170ca485bb8693b23fd1044d573b989e49c9f` | ROLLBACK | controlled rollback restored pre-attempt functional state | Y | Y |
| 325-R2 | compliant reexecution | REEXECUTE | identical bounded repair with this Matrix changed in the same atomic functional commit | N | N |

## KEEP REQUIREMENT
Preserve the original bounded repair scope. The rejected first attempt is historical evidence only. Rollback head `0f7273e0b0fdbf155bdf693afa9f746ac186b5d3` restored the functional tree and passed Full-Stack `33427024520`, Internal-ID `33427024464`, Real Mutation Matrix `33427024471`, and Runtime/Integration `33427024517`. Reexecute only the same root rename/H1 and the two already-identified live semantic consumer rewrites. Include this Matrix in the same functional commit because the current-change CI gate evaluates only that changed-file set. Preserve Memory EJR-237 byte-for-byte, baseline 6, historical P2 evidence, 317/318, Runtime implementation, and REP-016 ordering.

## Execution Evidence
Lease323 retained Memory EJR-237; Lease324 run `33426371329` proved EJR-431 VACANT. First attempt `423170ca485bb8693b23fd1044d573b989e49c9f` was semantically bounded but governance-rejected because Full-Stack run `33426813721` reported `protected_changes=1`, `mutation_matrices=0` for protected REP-020. Atomic rollback `0f7273e0b0fdbf155bdf693afa9f746ac186b5d3` restored all functional surfaces; compare against pre-attempt head leaves only this Matrix changed, and rollback verification passed.

Reusable learning candidate: `PRE-WRITE MATRIX EXISTENCE ≠ SAME-CHANGE-SET MATRIX BINDING FOR PROTECTED CI ENFORCEMENT.`

## Closure
Do not close until the compliant reexecution passes current-change Matrix enforcement and Full-Stack. Inspect Internal-ID independently. If it fails only at MEMORY_TO_ROOT expected=6/observed=5 with `__COHORT_COUNT_DRIFT__`, preserve that failure and rebaseline only in a separate lease. Any other failure is a HARD HOLD.
