# MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / EVIDENCE-ONLY
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 320-01 | vacancy proof record | CREATE | candidate-only EJR-430 complete-history gate; no allocation | N | N |
| 320-02 | `.github/workflows/ejr-430-vacancy-proof-320.yml` | CREATE | full-history execution of existing vacancy gate | N | N |
| 320-03 | EJR-240 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |

## KEEP REQUIREMENT
Do not create EJR-430, rename EJR-240, rewrite consumers, change the census baseline, or treat search absence as vacancy. Preserve 317/318 unchanged.

## Execution Evidence
Lease319 closed the EJR-240 disposition: Memory allocation retained; later root allocation is the displacement candidate. Direct repository search for `EJR-430` returned no result, but this is candidate discovery only and is not vacancy authority.

## Closure
Close only if a complete-history Actions run executes `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-430`, records `history_complete=true`, zero current/historical claims, and `decision=VACANT`. Any OCCUPIED/HISTORY_INCOMPLETE result blocks repair.