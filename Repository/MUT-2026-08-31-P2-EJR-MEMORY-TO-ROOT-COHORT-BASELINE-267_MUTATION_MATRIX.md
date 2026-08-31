# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 267

Status: PREWRITE / FUNCTIONAL MUTATION PENDING

| Surface | Before | Authorized after |
|---|---:|---:|
| EXPECTED_GROUP_COUNT | 24 | 23 |
| Observed deterministic cohort | 23 at Repair266 head | 23 |
| History complete | true | true |
| Classification complete | false only due cohort drift | true if no other defect appears |
| Classifier logic | unchanged | unchanged |
| Tests/workflows | unchanged | unchanged |
| EJR/Memory/GOV/REP/history | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Authority: Repair266 exact-head Internal-ID run `33374581005` passed every identity/chronology/lineage/provenance stage and failed only at MEMORY_TO_ROOT census. Artifact `9751379903`, digest `sha256:4d71b41256ea0d308769d61f10145efecb1ba07eee6067218f77f7f1c055abf8`, proves expected=24, observed=23, history_complete=true, classification_complete=false, decision=PARTIAL, incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`], with EJR-233 and EJR-413 absent from target_ids.

This lease authorizes one deterministic one-line constant update only. Any additional failure is a HARD HOLD and is not authorized for opportunistic repair here.