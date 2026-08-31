# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 274

Status: PREWRITE / EXECUTION NOT AUTHORIZED YET
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-274
Opening repair head: `24cb04ef430316c2fb9b9f6ab6af7eaf82bbe5df`
Execution role: HERMUZ

## Trigger evidence

Repair273 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-212 and moving the displaced root allocation to vacancy-proven EJR-415.

Exact repair-head evidence:
- Full-Stack #2405 / run `33381941006`: SUCCESS;
- Internal Document-ID Audit #64 / run `33381940680`: all test and report stages through reverse-direction provenance succeeded; MEMORY_TO_ROOT census alone failed;
- census artifact `9754096972`, digest `sha256:f6d40232ae5ee20b428e95b3fc5706ceca638c928afb03718510bbf68cffda1b`;
- artifact proves `history_complete=true`, `expected_group_count=22`, `observed_group_count=21`, `classification_complete=false`, `decision=PARTIAL`, and sole `incomplete_group_ids=["__COHORT_COUNT_DRIFT__"]`.

Therefore the only justified normalization is deterministic expected cohort count 22→21.

## Authorized mutation

Change exactly one line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:

`EXPECTED_GROUP_COUNT = 22` → `EXPECTED_GROUP_COUNT = 21`

## Exclusions

No changes to cohort membership derivation, classifier logic, tests, workflows, EJR, Memory, Repository history records other than this Matrix/Lease evidence, GOV/REP authority, consumers, or Global Integrity.

## Verification contract

After the one-line change:
- exact compare must show only the expected constant replacement plus governed Lease274 evidence updates;
- Internal Document-ID Audit must succeed and emit MEMORY_TO_ROOT census;
- final census must prove expected=21, observed=21, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[];
- Full-Stack must succeed on the normalized head;
- only then may Repair273 and Lease274 close.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
