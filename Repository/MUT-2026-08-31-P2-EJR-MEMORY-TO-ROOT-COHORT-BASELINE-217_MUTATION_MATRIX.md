# Mutation Matrix — Lease217

Status: CLOSED / EXECUTION-VERIFIED
Lease: `Repository/MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-217.md`
Baseline: `0b67b706de7b7a8d54b7f4decc0fa51820e6add6`
Functional head: `f0262431402c953d1138e74f2f4ac6845ca3ef1a`

| Surface | Before | Executed after | Result |
|---|---|---|---|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | `EXPECTED_GROUP_COUNT = 34` | `EXPECTED_GROUP_COUNT = 33` | exact one-line rebaseline |
| classifier-derived target membership | 33 observed groups | unchanged | preserved |
| drift failure semantics | fail when observed != expected | unchanged | preserved fail-closed |
| EJR identity records | Lease216 post-repair state | unchanged | no EJR mutation |
| tests / scanner / workflow logic | current | unchanged | no weakening |

Functional-head evidence: Internal-ID `33356597214` SUCCESS; Full-Stack `33356597201` SUCCESS; Runtime `33356597204` SUCCESS; M2 `33356597202` SUCCESS; artifact `9745333997` proves 33/33 CENSUSED with no incomplete groups.

Real Mutation Matrix did not match the census-only functional diff; this closure/matrix synchronization commit is the applicable Real Matrix regression surface and must be checked before session close.
