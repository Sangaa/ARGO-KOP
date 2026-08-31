# MUTATION MATRIX — Lease226 EJR-405 Vacancy Proof

Status: OPEN / PREWRITE
Baseline: `2af2ccd9f982e5b9e8ccfc735c6d7d09f3b9c9e4`

| Surface | Authorized change |
|---|---|
| Lease226 | create vacancy-proof authority/evidence record |
| Vacancy workflow | create dedicated complete-history EJR-405 proof workflow |
| EJR-302 target root | NONE |
| GOV-013B | NONE |
| Memory EJR-302 | NONE |
| census/analyzers/tests | NONE |

Verification: complete-history checkout + `ejr_allocation_vacancy_gate.py EJR-405` + uploaded deterministic artifact + enforced `VACANT` decision. No allocation or repair in this lease.
