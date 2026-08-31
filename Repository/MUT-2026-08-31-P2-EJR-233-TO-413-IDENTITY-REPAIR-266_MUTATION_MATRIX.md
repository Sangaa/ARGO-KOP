# MUTATION MATRIX — EJR-233 → EJR-413 IDENTITY REPAIR 266

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-233-TO-413-IDENTITY-REPAIR-266
Functional repair head: `a47c20d9b065533107f47cecc1e82e92bf8847f6`
Normalized successor: Lease267 / `338732cd880a8f6d1a12672aa2e2980c26b49fa6`

| Surface | Before | Final verified state |
|---|---|---|
| Memory EJR-233 | earlier retained allocation | unchanged / retained |
| Root old path | displaced EJR-233 | removed |
| Root successor path | vacancy-proven EJR-413 | created as EJR-413 |
| Root H1 | EJR-233 | EJR-413 |
| Root semantic body/date/chronology | source state | preserved except H1 identity |
| Historical footer | `End of EJR-233` | preserved |
| Historical disposition/path refs | provenance evidence | unchanged |
| Direct executable consumers | zero established | zero rewrites |
| MEMORY_TO_ROOT baseline at repair head | 24 | preserved inside Repair266 |
| Repair-head observed cohort | 23 | deterministic drift only |
| Successor baseline Lease267 | 24 | 23 |
| Final observed cohort | 23 | 23 |
| History complete | true | true |
| Classification complete | false at repair head | true after Lease267 |
| Decision | PARTIAL at repair head | CENSUSED after Lease267 |
| Classifier logic/tests/workflows | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Repair266 artifact: `9751379903` / `sha256:4d71b41256ea0d308769d61f10145efecb1ba07eee6067218f77f7f1c055abf8`.
Lease267 final artifact: `9751501145` / `sha256:d83115ddec53c17e030f985affe8d7b251db38432d18037ebb77dcce2a4330b1`.

Lease267 final gates: Internal-ID #60 SUCCESS; Full-Stack #2375 SUCCESS; Runtime #2149 SUCCESS; M2 #1032 SUCCESS.

Closure reconciliation is documentation-only. No EJR, Memory, census code, tests, workflows, GOV/REP, history, or Global Integrity state is modified by this closure.