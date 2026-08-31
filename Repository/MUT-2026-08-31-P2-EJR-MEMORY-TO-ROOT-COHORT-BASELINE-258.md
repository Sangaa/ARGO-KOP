# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-258

Status: PREWRITE / SUCCESSOR MUTATION PENDING
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair257.

## Trigger evidence
Repair257 exact head `bd0b833ed006118352dc1139f83de0a4e63a4194` preserved baseline 26. Internal-ID run `33368357858` passed audit/chronology/lineage/provenance stages and failed only at deterministic MEMORY_TO_ROOT census.

Artifact `9749113045`, digest `sha256:354c7181f8b881e302828a3d7a311f7e06c9295ed4a14e2b58b78b19538d9558`, proved:
- expected_group_count=26
- observed_group_count=25
- history_complete=true
- classification_complete=false
- decision=PARTIAL
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`]
- EJR-217 absent from target_ids
- EJR-411 absent from target_ids.

This is legitimate classifier-cardinality drift caused by removal of the final displaced root for EJR-217, not a semantic repair failure.

## Authorized successor
Change only `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 26` → `EXPECTED_GROUP_COUNT = 25`.

No classifier logic, tests, workflow, EJR, Memory, GOV, REP, or history mutation is authorized.

## Verification
Compare prewrite→functional successor must show one file with one-line constant replacement. Exact functional-head Internal-ID must succeed and deterministic artifact must prove expected=25, observed=25, history complete, classification complete, decision=CENSUSED and incomplete=[]. Full-Stack/Runtime/M2 and any other applicable workflows must be classified from exact-head evidence.

Priority 2 remains OPEN; Global Integrity remains HOLD.
