# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-295

Status: OPEN / NORMALIZATION AUTHORIZED
Opening repair head: `d5ebe81889edc8b72459f2135ba2603cc32eda0a`
Pre-write Matrix295: `1d69a47271979cb5ccf21256cea4e7bd45fd9ef2`
Execution role: HERMUZ

## Trigger

Repair294 removed EJR-245 from the deterministic MEMORY_TO_ROOT ambiguity cohort by retaining the earlier Memory allocation and moving displaced root content to vacancy-proven EJR-422.

Repair-head evidence:
- Full-Stack run `33402907617`: SUCCESS.
- Internal Document-ID run `33402907681`: FAILURE solely at MEMORY_TO_ROOT census.
- census artifact `9761968609`, digest `sha256:3a0614c948c9cb8d133000be54b3292b7d7c03490a802453e13c3a60cf8e1200`.
- expected=15, observed=14, history_complete=true, sole incomplete group=`__COHORT_COUNT_DRIFT__`.

## Authorized mutation

Change only `EXPECTED_GROUP_COUNT = 15` to `EXPECTED_GROUP_COUNT = 14` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No other functional or identity mutation is authorized. Final verification requires exact-head Full-Stack and Internal Document-ID success plus a CENSUSED 14/14 artifact.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
