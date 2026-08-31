# MUT-2026-08-31-P2-EJR-431-REPLACEMENT-VACANCY-PROOF-324 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-431-REPLACEMENT-VACANCY-PROOF-324
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / EVIDENCE-ONLY
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 324-01 | vacancy proof record | CREATE | candidate-only EJR-431 complete-history gate; no allocation | N | N |
| 324-02 | `.github/workflows/ejr-431-vacancy-proof-324.yml` | CREATE | full-history execution of existing vacancy gate | N | N |
| 324-03 | EJR-237 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |
| 324-04 | `p2_ejr431_vacancy_trigger.txt` | CREATE | one-time trigger only after workflow and record are re-readable | N | N |

## KEEP REQUIREMENT
Do not create EJR-431 identity content, rename EJR-237, rewrite consumers, change baseline 6, reopen 317/318, or treat search absence as vacancy.

## Execution Evidence
Lease323 closed the EJR-237 disposition: Memory allocation retained; later root allocation is the displacement candidate. Direct repository search for `EJR-431` returned no result, but this is candidate discovery only and is not vacancy authority.

## Closure
Close only if a complete-history Actions run executes `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-431`, records `history_complete=true`, zero current/historical claims, and `decision=VACANT`. Any OCCUPIED/HISTORY_INCOMPLETE result blocks repair.
