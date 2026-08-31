# MUTATION MATRIX — Lease228 MEMORY_TO_ROOT cohort baseline 32→31

Status: CLOSED / EXECUTION-VERIFIED
Baseline: `a7434269d28c2f4bf5510497091291a2579feb74`
Prewrite: `2413ec8a164a1551e82043398bef3953f3f9cef2`
Functional: `1972ebe9fd5b32e3eaf5703866e671d697e27975`

| Surface | Authorized change | Result |
|---|---|---|
| cohort census constant | EXPECTED_GROUP_COUNT 32→31 | DONE |
| classifier logic | NONE | UNCHANGED |
| tests/workflows | NONE | UNCHANGED |
| EJR/GOV/REP/Memory | NONE | UNCHANGED |
| Lease227 history | NONE | UNCHANGED |

Evidence: repair-head artifact `9746355744` proved drift 32→31. Successor artifact `9746432334` proved 31/31, complete, CENSUSED. Internal-ID, Full-Stack, Runtime and M2 passed at exact functional head. Real Matrix was NOT APPLICABLE to the census-only diff.
