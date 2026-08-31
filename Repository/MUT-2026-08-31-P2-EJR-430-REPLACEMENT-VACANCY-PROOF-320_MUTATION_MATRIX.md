# MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / EVIDENCE-ONLY
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 320-01 | `Repository/MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320.md` | CREATE | candidate-only EJR-430 complete-history gate; no allocation | Y | Y |
| 320-02 | `.github/workflows/ejr-430-vacancy-proof-320.yml` | CREATE | full-history execution of existing vacancy gate | Y | Y |
| 320-03 | EJR-240 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |
| 320-04 | `p2_ejr430_vacancy_trigger.txt` | CREATE | one-time trigger for vacancy proof; no identity content | N | N |

## KEEP REQUIREMENT
Do not create EJR-430, rename EJR-240, rewrite consumers, change the census baseline, or treat search absence as vacancy. Preserve 317/318 unchanged. The workflow is lifecycle-bounded by a one-time trigger path so later allocation does not re-run the historical VACANT assertion.

## Execution Evidence
Lease319 closed the EJR-240 disposition: Memory allocation retained; later root allocation is the displacement candidate. Direct repository search for `EJR-430` returned no result, but this is candidate discovery only and is not vacancy authority. Lease320 and the dedicated workflow are present and re-readable on current main before the trigger write.

## Closure
Close only if a complete-history Actions run executes `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-430`, records `history_complete=true`, zero current/historical claims, and `decision=VACANT`. Any OCCUPIED/HISTORY_INCOMPLETE result blocks repair.