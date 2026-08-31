# MUTATION MATRIX — EJR-210 TO EJR-408 IDENTITY REPAIR 242

Status: OPEN / PREWRITE

| Surface | Before | Authorized after |
|---|---|---|
| Memory EJR-210 | valid earlier allocation | unchanged / retained |
| Root EJR-210 | displaced later reuse | removed |
| Root EJR-408 | absent / vacancy-proven | created from displaced root |
| Exact-ID consumers | 0 | no rewrite |
| Exact-path consumers | 0 | no rewrite |
| Semantic body | legitimate engineering evidence | preserved |
| MEMORY_TO_ROOT baseline | 29 | preserve during repair |
| Global integrity | HOLD | HOLD |

Post-repair verification must inspect exact-head Internal-ID artifact. Any legitimate cohort drift requires a separate successor lease.
