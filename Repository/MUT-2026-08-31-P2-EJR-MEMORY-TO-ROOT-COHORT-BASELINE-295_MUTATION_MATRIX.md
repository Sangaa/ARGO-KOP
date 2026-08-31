# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 295

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-295
Opening repair head: `d5ebe81889edc8b72459f2135ba2603cc32eda0a`
Execution role: HERMUZ
Functional normalization head: `f0875f4b0ee68dadfddb585530451669929832ed`

## Trigger evidence

Repair294 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-245 and atomically moving the displaced root allocation to complete-history-vacancy-proven EJR-422.

Repair-head Internal Document-ID run `33402907681` failed only at the deterministic MEMORY_TO_ROOT census. Artifact `9761968609`, digest `sha256:3a0614c948c9cb8d133000be54b3292b7d7c03490a802453e13c3a60cf8e1200`, proves expected=15, observed=14, history_complete=true, decision=PARTIAL, with sole incomplete group `__COHORT_COUNT_DRIFT__`.

Repair-head Full-Stack run `33402907617`: SUCCESS.

## Executed mutation

Exactly one line changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 15` → `EXPECTED_GROUP_COUNT = 14`.

Exact compare from Lease295 open head `24d5f5156a37ca980cfcbc0ae74abbea9c3a6a09` to normalization head `f0875f4b0ee68dadfddb585530451669929832ed` shows one modified file with one addition and one deletion.

## Final verification

- Full-Stack run `33403240740`: SUCCESS.
- Internal Document-ID run `33403240765`: SUCCESS.
- final census artifact `9762099086`, digest `sha256:8fd78bcb0fa025989cd16bd30c74d54a9bdc29429ea3d6e44df69b91e5966193`.
- expected=14, observed=14, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No other mutation was authorized or executed by Matrix295.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
