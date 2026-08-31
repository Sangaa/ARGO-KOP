# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-298

Status: OPEN / NORMALIZATION AUTHORIZED
Opening repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`
Pre-write Matrix298: `60b1487f8280c07dcfbea8a24938ac533a841fa9`
Execution role: HERMUZ

## Trigger

Repair297 removed EJR-246 from the deterministic MEMORY_TO_ROOT ambiguity cohort by retaining the earlier Memory allocation and moving displaced root content to vacancy-proven EJR-423.

Repair-head evidence:
- Full-Stack run `33409682009`: SUCCESS.
- Internal Document-ID run `33409681899`: FAILURE solely at MEMORY_TO_ROOT census.
- census artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`.
- expected=14, observed=13, history_complete=true, sole incomplete group=`__COHORT_COUNT_DRIFT__`.

## Authorized mutation

Change only `EXPECTED_GROUP_COUNT = 14` to `EXPECTED_GROUP_COUNT = 13` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No other functional or identity mutation is authorized. Final verification requires exact-head Full-Stack and Internal Document-ID success plus a CENSUSED 13/13 artifact.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
