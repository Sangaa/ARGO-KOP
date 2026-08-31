# MUT-2026-08-31-P2-EJR-431-REPLACEMENT-VACANCY-PROOF-324 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-431-REPLACEMENT-VACANCY-PROOF-324
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 324-01 | vacancy proof record | CREATE | candidate-only EJR-431 complete-history gate; no allocation | Y | Y |
| 324-02 | `.github/workflows/ejr-431-vacancy-proof-324.yml` | CREATE | full-history execution of existing vacancy gate | Y | Y |
| 324-03 | EJR-237 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |
| 324-04 | `p2_ejr431_vacancy_trigger.txt` | CREATE | one-time trigger only after workflow and record are re-readable | Y | Y |

## KEEP REQUIREMENT
No EJR-431 identity content was created under this proof lease; EJR-237 members and consumers were unchanged, baseline remained 6, and 317/318 remained untouched.

## Execution Evidence
Lease323 closed the EJR-237 disposition. Workflow run `33426371329` at `7db1eaa45d0a86b64a19cc1b9f693d0eb02b1808` completed SUCCESS and proved: candidate=EJR-431, current_claims=[], historical_claims=[], history_complete=true, history_scope=`all locally reachable refs`, occupied=false, vacant=true, decision=VACANT. Artifact `9770873918`, digest `sha256:2316b9f56376531d5248ea676326cc5d2bd374db5206d1427c7677421b8f3d12` preserves the evidence.

## Closure
Lease324 is CLOSED / VERIFIED / RESUME-SAFE. One bounded EJR-237→EJR-431 identity repair may now be opened under a separate pre-write matrix. Priority 2 remains OPEN.
