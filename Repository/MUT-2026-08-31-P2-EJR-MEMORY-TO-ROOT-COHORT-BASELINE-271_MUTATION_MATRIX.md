# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 271

Status: PRE-WRITE / OPEN
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-271
Opening main: `ad7fd5642941a398f915dad5c299e009346c38a7`

## Trigger

Repair270 changed the displaced root allocation from EJR-235 to EJR-414 while retaining the earlier Memory EJR-235 allocation unchanged.

Exact repair-head evidence:
- Repair270 functional commit: `ad7fd5642941a398f915dad5c299e009346c38a7`.
- Full-Stack #2390 / run `33380217985`: SUCCESS.
- Internal Document-ID Audit #61 / run `33380217984` completed all identity, vacancy, ambiguity, chronology, namespace-lineage, non-monotonic, and reverse-direction stages successfully; only the MEMORY_TO_ROOT provenance census emission failed.
- Census artifact `9753468588`, digest `sha256:f0897d8869170a12046b836abc5b0ce2c0325402522b41826d455c499e97e6dc` proves `history_complete=true`, `expected_group_count=23`, `observed_group_count=22`, `classification_complete=false`, `decision=PARTIAL`, and `incomplete_group_ids=["__COHORT_COUNT_DRIFT__"]`.
- Current target cohort contains exactly 22 IDs and no member-specific incompleteness.

## Authorized mutation boundary after pre-write validation

Exactly one functional line may change:
`Quality/Integration/ejr_memory_to_root_provenance_census.py`

`EXPECTED_GROUP_COUNT = 23` → `EXPECTED_GROUP_COUNT = 22`.

No classifier logic, membership derivation, tests, workflow logic, EJR, Memory, GOV, REP, consumer, chronology, or Global Integrity state may change.

## Expected verification

After the one-line baseline normalization:
- Internal Document-ID Audit must complete SUCCESS;
- MEMORY_TO_ROOT census must report expected=22 / observed=22 / history_complete=true / classification_complete=true / decision=CENSUSED / incomplete_group_ids=[];
- Full-Stack, Runtime, M2, and applicable Matrix gates must remain green.

## Boundary

This transaction does not reopen Repair270 identity reasoning and does not authorize another identity repair.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
