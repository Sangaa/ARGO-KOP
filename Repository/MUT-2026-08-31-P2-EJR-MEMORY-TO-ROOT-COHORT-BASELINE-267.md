# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-267

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair266.

## Chain

- Repair266 head: `a47c20d9b065533107f47cecc1e82e92bf8847f6`.
- Pre-write Matrix267: `1205a010fa032cfe7486a12bf9334690bbcccc74`.
- Lease267 open: `3df51d4354bdd633bce1d36f43629bc895c61b64`.
- Functional successor: `338732cd880a8f6d1a12672aa2e2980c26b49fa6`.
- Matrix267 closure: `9468d81b4a7e5b22c29e20dec2d91222e6c11017`.

## Trigger evidence

Repair266 resolved the displaced root EJR-233 identity to vacancy-proven EJR-413 while preserving baseline 24. Its exact-head Internal-ID evidence passed every identity/chronology/lineage/provenance stage and failed only at the deterministic MEMORY_TO_ROOT census.

Repair266 census artifact `9751379903`, digest `sha256:4d71b41256ea0d308769d61f10145efecb1ba07eee6067218f77f7f1c055abf8`, proved expected=24, observed=23, history_complete=true, classification_complete=false, decision=PARTIAL, and sole incompleteness `__COHORT_COUNT_DRIFT__`.

## Executed successor

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:

`EXPECTED_GROUP_COUNT = 24` → `EXPECTED_GROUP_COUNT = 23`.

Exact compare from `3df51d4354bdd633bce1d36f43629bc895c61b64` to `338732cd880a8f6d1a12672aa2e2980c26b49fa6` proved one modified file with one-line replacement (`+1/-1`). No classifier logic, tests, workflows, EJR records, Memory records, GOV/REP records, history, Repair266 records, or Global Integrity state changed.

## Exact-head verification

- Internal Document-ID Audit #60 / run `33374897233`: SUCCESS, including MEMORY_TO_ROOT census.
- Full-Stack Repository Audit #2375 / run `33374897260`: SUCCESS.
- ARGO Runtime Prototype and Integration #2149 / run `33374897257`: SUCCESS.
- M2 #1032 / run `33374897254`: SUCCESS.

Final census artifact `9751501145`, digest `sha256:d83115ddec53c17e030f985affe8d7b251db38432d18037ebb77dcce2a4330b1`, proves:
- expected_group_count=23
- observed_group_count=23
- history_complete=true
- classification_complete=true
- decision=CENSUSED
- incomplete_group_ids=[]

Verified target_ids: EJR-165, EJR-174, EJR-212, EJR-218, EJR-234, EJR-235, EJR-236, EJR-237, EJR-238, EJR-239, EJR-240, EJR-241, EJR-243, EJR-244, EJR-245, EJR-246, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296, EJR-297.

## Learning / transfer disposition

No new governance rule is required. Lease267 is a third execution-confirmed application of the already established Repair → separate deterministic cohort-baseline successor pattern proven by Leases258 and 263. Reuse that pattern; do not duplicate it as a new permanent rule.

## Boundary and resume

The new deterministic MEMORY_TO_ROOT baseline is 23. Lease267 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Repair266 closure should now record this normalized successor. After the entire chain is closed and its closure commit validated, select the next Priority-2 target from the current 23-group census using fresh consumer/risk/chronology evidence; do not assume historical ordering.