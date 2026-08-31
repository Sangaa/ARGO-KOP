# Mutation Matrix — Lease217

Status: OPEN / PREWRITE
Lease: `Repository/MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-217.md`
Baseline: `0b67b706de7b7a8d54b7f4decc0fa51820e6add6`

| Surface | Before | Authorized after | Boundary |
|---|---|---|---|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | `EXPECTED_GROUP_COUNT = 34` | `EXPECTED_GROUP_COUNT = 33` | one-line rebaseline only |
| classifier-derived target membership | 33 observed groups | unchanged | dynamic membership preserved |
| drift failure semantics | fail when observed != expected | unchanged | must remain fail-closed |
| EJR identity records | Lease216 post-repair state | unchanged | no EJR mutation |
| tests / scanner / workflow logic | current | unchanged | no weakening |

Exit requires exact-head Internal-ID + Full-Stack + Runtime/Integration + M2 + Real Mutation Matrix SUCCESS and inspected deterministic 33/33 census evidence.
