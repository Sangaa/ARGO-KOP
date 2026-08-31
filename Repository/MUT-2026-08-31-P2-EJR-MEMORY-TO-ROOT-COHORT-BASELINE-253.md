# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-253

Status: PREWRITE / SUCCESSOR MUTATION PENDING
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair252.

## Trigger evidence
Repair252 exact head `2d17e029701e0a670cf45c08921bc9eb0e71a4df` preserved baseline 27. Internal-ID run `33365725799` passed the audit/chronology/lineage/provenance stages and failed only at the deterministic MEMORY_TO_ROOT census.

Artifact `9748220566`, digest `sha256:719cde8a93ef85cc23be9d3482c22b1f0e4a1bca5e24330a4f13ca214fdb86ca`, proved:
- expected_group_count=27
- observed_group_count=26
- history_complete=true
- classification_complete=false
- decision=PARTIAL
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`]
- EJR-215 absent from target_ids
- EJR-410 absent from target_ids.

This is legitimate classifier-cardinality drift caused by removal of the final displaced root for EJR-215, not a semantic repair failure.

## Authorized successor
Change only `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 27` → `EXPECTED_GROUP_COUNT = 26`.

No classifier logic, tests, workflow, EJR, Memory, GOV, REP, or history mutation is authorized.

## Verification
Compare prewrite→functional successor must show one file with one-line constant replacement. Exact functional-head Internal-ID must succeed and its deterministic artifact must prove expected=26, observed=26, history complete, classification complete, decision=CENSUSED and incomplete=[]. Full-Stack/Runtime/M2 and any other applicable triggered workflows must be classified from exact-head evidence.

Priority 2 remains OPEN; Global Integrity remains HOLD.
