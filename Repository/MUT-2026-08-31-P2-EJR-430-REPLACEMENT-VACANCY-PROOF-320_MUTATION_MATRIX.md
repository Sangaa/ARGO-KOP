# MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320
Protocol: GOV-013 / GOV-014A
Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 320-01 | `Repository/MUT-2026-08-31-P2-EJR-430-REPLACEMENT-VACANCY-PROOF-320.md` | CREATE | candidate-only EJR-430 complete-history gate; no allocation | Y | Y |
| 320-02 | `.github/workflows/ejr-430-vacancy-proof-320.yml` | CREATE | full-history execution of existing vacancy gate | Y | Y |
| 320-03 | EJR-240 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |
| 320-04 | `p2_ejr430_vacancy_trigger.txt` | CREATE | one-time trigger for vacancy proof; no identity content | Y | Y |

## KEEP REQUIREMENT
EJR-240 members and baseline 7 were preserved through the proof. No EJR-430 allocation or identity repair occurred under Lease320. 317/318 remain unchanged.

## Execution Evidence
Run `33422684323` on `eb4407cf280074a223d4efe0e90826257ac4428b` completed SUCCESS with complete history. Artifact `ejr-430-vacancy-proof` ID `9769515369` reported `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `occupied=false`, `vacant=true`, `decision=VACANT`. The one-time trigger path prevents stale post-allocation enforcement.

## Closure
PASS. EJR-430 vacancy is execution-verified for Lease320. Separate bounded identity repair is now legally eligible under Lease319 disposition + Lease320 vacancy proof. Priority 2 remains OPEN.