# MUT-2026-08-31-P2-EJR-432-REPLACEMENT-VACANCY-PROOF-328 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-432-REPLACEMENT-VACANCY-PROOF-328
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / EXECUTION-PENDING
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 328-01 | vacancy proof record | CREATE | candidate-only EJR-432 complete-history gate; no allocation | Y | N |
| 328-02 | `.github/workflows/ejr-432-vacancy-proof-328.yml` | CREATE | full-history execution of existing vacancy gate | Y | N |
| 328-03 | EJR-293 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | N |
| 328-04 | `p2_ejr432_vacancy_trigger.txt` | CREATE LATER | one-time trigger only after workflow and record are re-readable | N | N |

## KEEP REQUIREMENT
No EJR-432 identity content is created under this proof lease. EJR-293 members and semantic references remain unchanged; baseline remains 5; Runtime, REP-016, and Priority ordering remain unchanged. The workflow reuses `Quality/Integration/ejr_allocation_vacancy_gate.py` and does not introduce new vacancy logic.

## Execution Evidence
Lease327 dispositioned root EJR-293 as the displacement candidate and retained Memory EJR-293. Current indexed search returned no EJR-432 result; this is bounded discovery evidence only. Complete-history execution remains mandatory.

## Closure
Do not close until the workflow reports history_complete=true and decision=VACANT and the artifact digest is recorded. Any OCCUPIED, incomplete-history, or workflow failure is a HARD HOLD for EJR-432 allocation.
