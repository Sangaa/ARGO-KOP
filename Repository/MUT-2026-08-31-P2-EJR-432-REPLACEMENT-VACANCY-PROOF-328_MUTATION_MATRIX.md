# MUT-2026-08-31-P2-EJR-432-REPLACEMENT-VACANCY-PROOF-328 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-432-REPLACEMENT-VACANCY-PROOF-328
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 328-01 | vacancy proof record | CREATE | candidate-only EJR-432 complete-history gate; no allocation | Y | Y |
| 328-02 | `.github/workflows/ejr-432-vacancy-proof-328.yml` | CREATE | full-history execution of existing vacancy gate | Y | Y |
| 328-03 | EJR-293 members / cohort | KEEP | no identity repair or baseline change until VACANT is execution-verified | Y | Y |
| 328-04 | `p2_ejr432_vacancy_trigger.txt` | CREATE | one-time execution trigger | Y | Y |

## KEEP REQUIREMENT
No EJR-432 identity content was created under this proof lease. EJR-293 members and semantic references remain unchanged; baseline remains 5; Runtime, REP-016, and Priority ordering remain unchanged. The workflow reused `Quality/Integration/ejr_allocation_vacancy_gate.py`; no vacancy logic was added.

## Execution Evidence
Lease327 dispositioned root EJR-293 as the displacement candidate and retained Memory EJR-293. Workflow `EJR-432 Vacancy Proof 328`, run `33428317233` at `a3985e3d507a043debea7969cf1f9767190a9fa8`, completed SUCCESS after a non-shallow checkout and reported candidate=EJR-432, current_claims=[], historical_claims=[], history_complete=true, history_scope=`all locally reachable refs`, occupied=false, vacant=true, decision=VACANT. Artifact `9771588196`, digest `sha256:4a72f53c58c9387f5cae065ca12b78b99590b2180e9eb635659ad20894312060` preserves the evidence. Exact trigger head also ran M2 successfully.

## Closure
Lease328 is CLOSED / VERIFIED / RESUME-SAFE. One bounded root EJR-293→EJR-432 identity repair may now be opened under a separate pre-write matrix. Priority 2 remains OPEN.
