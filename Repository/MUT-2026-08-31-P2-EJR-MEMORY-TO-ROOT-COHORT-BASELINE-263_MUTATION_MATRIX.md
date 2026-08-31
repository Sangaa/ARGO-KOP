# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 263

Status: CLOSED / EXECUTION-VERIFIED

| Surface | Before | Final verified state |
|---|---:|---:|
| EXPECTED_GROUP_COUNT | 25 | 24 |
| Observed deterministic cohort | 24 | 24 |
| History complete | true | true |
| Classification complete | false at Repair262 head | true |
| Decision | PARTIAL at Repair262 head | CENSUSED |
| Classifier logic | unchanged | unchanged |
| Tests/workflows | unchanged | unchanged |
| EJR/Memory/GOV/REP/history | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Functional successor: `b2843dc2aa43c9a3110988873afa880ef855ffe2`.
Exact compare from lease-open commit proved exactly one modified file with one-line replacement (`+1/-1`).

Exact-head verification:
- Internal Document-ID Audit #58 / run `33373341560`: SUCCESS
- Full-Stack Repository Audit #2358 / run `33373341575`: SUCCESS
- ARGO Runtime Prototype and Integration #2133 / run `33373341571`: SUCCESS
- M2 #1015 / run `33373341543`: SUCCESS

Final census artifact: `9750922890` / `sha256:1948d5e7ea91d7dc416a88d99180e4f04ad0ef4426c66178da7f645d577a29be`.
Artifact evidence: expected=24, observed=24, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].