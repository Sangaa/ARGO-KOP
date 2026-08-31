# MUTATION MATRIX — EJR-215 DISPOSITION AUTHORIZATION 250

Status: PREWRITE / AUTHORIZATION ONLY

| Surface | Before | Authorized disposition | Mutation in this lease |
|---|---|---|---|
| Memory EJR-215 | earlier valid allocation | RETAIN | NONE |
| Root EJR-215 | later reused allocation | DISPLACED | NONE |
| Replacement ID | unallocated | separate complete-history vacancy proof required | NONE |
| Exact consumers | deterministic census = zero ID/path consumers | recheck before repair | NONE |
| MEMORY_TO_ROOT baseline | 27 | preserve | NONE |
| Global integrity | HOLD | HOLD | NONE |

Exit condition: a replacement candidate may be considered only after this authorization is committed and live `main` is rechecked. Candidate discovery is not vacancy proof.
