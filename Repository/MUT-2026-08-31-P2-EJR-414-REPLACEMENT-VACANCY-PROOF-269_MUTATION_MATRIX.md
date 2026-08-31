# MUTATION MATRIX — EJR-414 REPLACEMENT VACANCY PROOF 269

Status: PREWRITE / VACANCY PROOF PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-414-REPLACEMENT-VACANCY-PROOF-269
Opening main: `9c12a6b78f79b4502ae9b7cab46683b6c23048da`

## Trigger

Lease268 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and retains the earlier Memory EJR-235 while classifying the later root EJR-235 displaced.

Current code search returns no EJR-414 claim. This is candidate discovery only and is not vacancy evidence.

## Authorized proof scope

| Surface | Current state | Authorized state |
|---|---|---|
| Candidate | EJR-414 | EJR-414 only |
| Current-tree search | no claim surfaced | signal only |
| Complete reachable history | unproven | execute dedicated proof |
| EJR-414 allocation | none authorized | none |
| EJR-235 repair | not authorized here | unchanged |
| EJR/Memory content | current | unchanged |
| Census baseline | 23 | unchanged |
| Global integrity | HOLD | HOLD |

A dedicated workflow must checkout complete history (`fetch-depth: 0`), verify the repository is non-shallow, execute `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-414`, upload the JSON evidence, and enforce `decision == VACANT`.

No rename, allocation, delete, content rewrite, consumer rewrite, cohort-baseline update, or integrity promotion is authorized in Lease269.