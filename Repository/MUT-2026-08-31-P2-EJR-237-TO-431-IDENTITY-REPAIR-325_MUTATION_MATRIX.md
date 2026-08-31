# MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-237-TO-431-IDENTITY-REPAIR-325
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / DRIFT-PRESERVED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 325-01 | `EJR/EJR-431_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | CREATE | displaced root content with first-H1 identity EJR-431; semantic body/date/chronology preserved | Y | Y |
| 325-02 | `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` | DELETE | old root identity absent in same atomic tree | Y | Y |
| 325-03 | `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` | UPDATE | move semantic evidence references whose referent is root EJR-237 negative-runtime evidence to EJR-431 only | Y | Y |
| 325-04 | `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md` | UPDATE | move root-negative-runtime evidence heading/reference EJR-237 → EJR-431 only | Y | Y |
| 325-05 | `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md` | KEEP | retained earlier allocation byte-for-byte | Y | Y |
| 325-06 | census expected baseline | KEEP | remain 6 during repair; expected drift failure preserved for separate rebaseline | Y | Y |
| 325-R1 | rejected attempt `423170ca485bb8693b23fd1044d573b989e49c9f` | ROLLBACK | controlled rollback restored pre-attempt functional state | Y | Y |
| 325-R2 | compliant reexecution `49680f1eddd29a4a18336261ae5aec594087d3a0` | REEXECUTE | identical bounded repair with this Matrix changed in the same atomic functional commit | Y | Y |

## KEEP REQUIREMENT
The accepted repair preserves the original bounded scope. Memory EJR-237 remains blob `ff85f1270ebb4d30985f9bc9183bcc179ad43021`; baseline remains 6 inside Repair325; historical P2 evidence, 317/318, Runtime implementation, and REP-016 ordering remain unchanged. The rejected first attempt remains evidence only and is not used as closure authority.

## Execution Evidence
Lease323 retained Memory EJR-237. Lease324 run `33426371329` proved EJR-431 VACANT. First attempt `423170ca485bb8693b23fd1044d573b989e49c9f` was governance-rejected because Full-Stack run `33426813721` found protected REP-020 without a Matrix in the same changed-file set. Atomic rollback `0f7273e0b0fdbf155bdf693afa9f746ac186b5d3` restored the functional tree and passed Full-Stack `33427024520`, Internal-ID `33427024464`, Real Mutation Matrix `33427024471`, and Runtime/Integration `33427024517`.

Compliant reexecution `49680f1eddd29a4a18336261ae5aec594087d3a0` changed exactly four paths: root rename/H1, EJR-418 semantic references, REP-020 P322 semantic references, and this Matrix. Full-Stack `33427225861` passed, including current-change Matrix enforcement. Runtime/Integration `33427225759` passed.

Internal-ID `33427225894` passed every stage except MEMORY_TO_ROOT census emission. Artifact `9771215241`, digest `sha256:abf5b10e02459cad33d05944542549e6d3cf33760ea7fb48ab68155487c13df9`, proves expected=6, observed=5, history_complete=true, decision=PARTIAL, incomplete only `__COHORT_COUNT_DRIFT__`, target_ids=EJR-165/EJR-293/EJR-294/EJR-295/EJR-296.

Reusable learning candidate: `PRE-WRITE MATRIX EXISTENCE ≠ SAME-CHANGE-SET MATRIX BINDING FOR PROTECTED CI ENFORCEMENT.` This is recorded without governance promotion.

## Closure
Repair325 is CLOSED / VERIFIED / DRIFT-PRESERVED / RESUME-SAFE. The only next legal continuation from this repair is a separate deterministic baseline normalization 6→5 before selecting another Priority-2 target.
