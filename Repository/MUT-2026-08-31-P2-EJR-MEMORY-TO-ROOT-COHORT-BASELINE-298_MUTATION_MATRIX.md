# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 298

Status: PREWRITE / NORMALIZATION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-298
Opening repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`
Execution role: HERMUZ

## Trigger evidence

Repair297 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-246 and atomically moving displaced root allocation to complete-history-vacancy-proven EJR-423.

Repair-head evidence:
- Full-Stack run `33409682009`: SUCCESS.
- Internal Document-ID run `33409681899`: FAILURE solely at the deterministic MEMORY_TO_ROOT provenance census.
- census artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`.
- expected_group_count=14;
- observed_group_count=13;
- history_complete=true;
- classification_complete=false only because incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`];
- decision=PARTIAL.

## Authorized normalization

Exactly one functional line may change in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 14` → `EXPECTED_GROUP_COUNT = 13`.

No cohort membership rewrite, identity repair, consumer rewrite, governance promotion, REP promotion, or Global Integrity change is authorized in Lease298.

## Required final gate

The exact normalization head must satisfy:
- Full-Stack Repository Audit = SUCCESS;
- Internal Document-ID Audit = SUCCESS;
- final MEMORY_TO_ROOT census expected=13 and observed=13;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
