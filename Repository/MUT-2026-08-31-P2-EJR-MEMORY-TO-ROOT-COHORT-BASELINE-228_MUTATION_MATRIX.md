# MUTATION MATRIX — Lease228 MEMORY_TO_ROOT cohort baseline 32→31

Status: OPEN / PREWRITE
Baseline: `a7434269d28c2f4bf5510497091291a2579feb74`

| Surface | Authorized change |
|---|---|
| cohort census constant | `EXPECTED_GROUP_COUNT = 32` → `31` |
| classifier logic | NONE |
| tests/workflows | NONE |
| EJR/GOV/REP/Memory | NONE |
| Lease227 repair history | NONE |

Evidence authority: run `33359946109`, artifact `9746355744`, digest `sha256:5cf5e30dc15fbd91dadddf810bb102e352ece47e99d4a9b2572435ef6ef05c51` proved complete deterministic cohort 31 after Lease227.

Verification: bounded compare plus exact-head Internal-ID census, Full-Stack, Runtime, M2. Real Matrix non-trigger from a census-only diff is NOT APPLICABLE.
