# MUTATION MATRIX — EJR-217 → EJR-411 IDENTITY REPAIR 257

Status: PREWRITE / FUNCTIONAL MUTATION PENDING

| Surface | Before | Authorized after |
|---|---|---|
| Memory EJR-217 | earlier valid allocation | unchanged / retained |
| Root EJR-217 | displaced later allocation | removed from old path |
| Root EJR-411 | absent / vacancy-proven | created with preserved body/date/chronology |
| Root H1 | EJR-217 | EJR-411 |
| Exact-ID consumers | zero established | no rewrite |
| Exact-path consumers | zero established | no rewrite |
| MEMORY_TO_ROOT baseline | 26 | 26 inside repair |
| Classifier logic/tests/workflows | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Functional completion requires exact diff/readback and post-mutation CI/artifact evidence.
