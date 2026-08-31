# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 267

Status: CLOSED / EXECUTION-VERIFIED

| Surface | Before | Final verified state |
|---|---:|---:|
| EXPECTED_GROUP_COUNT | 24 | 23 |
| Observed deterministic cohort | 23 | 23 |
| History complete | true | true |
| Classification complete | false at Repair266 head | true |
| Decision | PARTIAL at Repair266 head | CENSUSED |
| Classifier logic | unchanged | unchanged |
| Tests/workflows | unchanged | unchanged |
| EJR/Memory/GOV/REP/history | unchanged | unchanged |
| Global integrity | HOLD | HOLD |

Functional successor: `338732cd880a8f6d1a12672aa2e2980c26b49fa6`.
Exact compare from lease-open commit `3df51d4354bdd633bce1d36f43629bc895c61b64` proved exactly one modified file with one-line replacement (`+1/-1`). Read-back proved `EXPECTED_GROUP_COUNT = 23`.

Exact-head verification:
- Internal Document-ID Audit #60 / run `33374897233`: SUCCESS
- Full-Stack Repository Audit #2375 / run `33374897260`: SUCCESS
- ARGO Runtime Prototype and Integration #2149 / run `33374897257`: SUCCESS
- M2 #1032 / run `33374897254`: SUCCESS

Final census artifact: `9751501145` / `sha256:d83115ddec53c17e030f985affe8d7b251db38432d18037ebb77dcce2a4330b1`.
Artifact evidence: expected=23, observed=23, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

The verified target_ids are: EJR-165, EJR-174, EJR-212, EJR-218, EJR-234, EJR-235, EJR-236, EJR-237, EJR-238, EJR-239, EJR-240, EJR-241, EJR-243, EJR-244, EJR-245, EJR-246, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296, EJR-297.