# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 295

Status: PREWRITE / NORMALIZATION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-295
Opening repair head: `d5ebe81889edc8b72459f2135ba2603cc32eda0a`
Execution role: HERMUZ

## Trigger evidence

Repair294 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-245 and atomically moving the displaced root allocation to complete-history-vacancy-proven EJR-422.

Repair-head Internal Document-ID run `33402907681` completed FAILURE only at the deterministic MEMORY_TO_ROOT provenance census. Exact census artifact `9761968609`, digest `sha256:3a0614c948c9cb8d133000be54b3292b7d7c03490a802453e13c3a60cf8e1200`, proves:
- expected_group_count=15;
- observed_group_count=14;
- history_complete=true;
- history_scope=`all locally reachable refs`;
- classification_complete=false only because incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`];
- decision=PARTIAL.

Repair-head Full-Stack run `33402907617`: SUCCESS.

## Authorized normalization

Exactly one functional line may change in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 15` → `EXPECTED_GROUP_COUNT = 14`.

No cohort membership rewrite, identity repair, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease295.

## Required final gate

The exact normalization head must satisfy:
- Full-Stack Repository Audit = SUCCESS;
- Internal Document-ID Audit = SUCCESS;
- final MEMORY_TO_ROOT census expected=14 and observed=14;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
