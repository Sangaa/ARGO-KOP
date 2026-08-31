# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-258

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair257.

## Trigger evidence
Repair257 exact head `bd0b833ed006118352dc1139f83de0a4e63a4194` preserved baseline 26. Internal-ID run `33368357858` passed audit/chronology/lineage/provenance stages and failed only at the deterministic MEMORY_TO_ROOT census.

Artifact `9749113045`, digest `sha256:354c7181f8b881e302828a3d7a311f7e06c9295ed4a14e2b58b78b19538d9558`, proved expected=26, observed=25, history_complete=true, classification_complete=false, decision=PARTIAL, and sole incompleteness `__COHORT_COUNT_DRIFT__`, with EJR-217/EJR-411 absent from target_ids.

## Executed successor
Prewrite: `e9f2f6eaacb92916b0e94ab23a8f8ded5847b375`.
Functional successor: `e6111ec33574601d3e979451dedcb3e44d4a0c65`.

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:
`EXPECTED_GROUP_COUNT = 26` → `EXPECTED_GROUP_COUNT = 25`.
Compare proved one modified file with one-line constant replacement. Classifier logic, tests, workflows, EJR, Memory, GOV, REP and history were unchanged.

## Exact-head verification
- Internal-ID `33368587229`: SUCCESS
- Full-Stack `33368587218`: SUCCESS
- Runtime `33368587225`: SUCCESS
- M2 `33368587254`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to census-only diff.

Artifact `9749193758`, digest `sha256:6d3886048bed192173aab7f8a6edacf565af83501691e8305caca6026c303c5f`, proved:
- expected_group_count=25
- observed_group_count=25
- history_complete=true
- classification_complete=true
- decision=CENSUSED
- incomplete_group_ids=[]
- EJR-217 absent from target_ids
- EJR-411 absent from target_ids.

## Boundary
The new deterministic MEMORY_TO_ROOT baseline is 25. Priority 2 remains OPEN; Phase 1 remains OPEN; Global Integrity remains HOLD.
