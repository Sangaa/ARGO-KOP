# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 263

Status: PREWRITE / FUNCTIONAL MUTATION PENDING

| Surface | Before | Authorized after |
|---|---:|---:|
| EXPECTED_GROUP_COUNT | 25 | 24 |
| Observed deterministic cohort | 24 at Repair262 head | 24 |
| History complete | true | true |
| Classification complete | false only due cohort drift | true if no other defect appears |
| Classifier logic | unchanged | unchanged |
| Tests/workflows | unchanged | unchanged |
| EJR/Memory/GOV/REP/history | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Authority: Repair262 exact-head Internal-ID evidence showed only `__COHORT_COUNT_DRIFT__` with expected=25 and observed=24 after EJR-232 root identity was repaired to EJR-412.

This lease authorizes one deterministic one-line constant update only. Any additional failure is a HARD HOLD and is not authorized for opportunistic repair here.