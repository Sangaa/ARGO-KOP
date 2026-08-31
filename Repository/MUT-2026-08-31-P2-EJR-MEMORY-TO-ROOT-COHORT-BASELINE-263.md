# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-263

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair262.

## Chain

- Repair262 head: `5bbfd61df063024824091c74c8597f89eb9b8bf2`.
- Pre-write Matrix263: `d8cb01864687dba1227d18867688e2b024f29020`.
- Lease263 open: `131a190d7d370385485c16828adf451673e6a87d`.
- Functional successor: `b2843dc2aa43c9a3110988873afa880ef855ffe2`.
- Matrix263 closure: `74b49fa23ddec991dd7f9378a16a8579f9db66d8`.

## Trigger evidence

Repair262 resolved one MEMORY_TO_ROOT ambiguity while preserving baseline 25. Its exact-head Internal-ID evidence failed only at the deterministic census with expected=25 / observed=24 and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Repair262 artifact: `9750192824`, digest `sha256:0761f442a253813426fcdebe4290b0b3895337abd339b85628dda853d8e189e4`.

## Executed successor

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:

`EXPECTED_GROUP_COUNT = 25` → `EXPECTED_GROUP_COUNT = 24`.

Exact compare from `131a190d7d370385485c16828adf451673e6a87d` to `b2843dc2aa43c9a3110988873afa880ef855ffe2` proved one modified file with one-line replacement (`+1/-1`). No classifier logic, tests, workflows, EJR records, Memory records, GOV/REP records, history, or Global Integrity state changed.

## Exact-head verification

- Internal Document-ID Audit #58 / run `33373341560`: SUCCESS, including MEMORY_TO_ROOT census.
- Full-Stack Repository Audit #2358 / run `33373341575`: SUCCESS.
- ARGO Runtime Prototype and Integration #2133 / run `33373341571`: SUCCESS.
- M2 #1015 / run `33373341543`: SUCCESS.

Final census artifact `9750922890`, digest `sha256:1948d5e7ea91d7dc416a88d99180e4f04ad0ef4426c66178da7f645d577a29be`, proves:
- expected_group_count=24
- observed_group_count=24
- history_complete=true
- classification_complete=true
- decision=CENSUSED
- incomplete_group_ids=[]

## Learning / transfer disposition

No new governance rule is required. The observed behavior is an additional execution-confirmed instance of the existing Repair → separate deterministic cohort-baseline successor pattern already proven by Lease258. Reuse the existing pattern; do not duplicate it as a new permanent rule.

## Boundary and resume

The new deterministic MEMORY_TO_ROOT baseline is 24. Repair262 → Lease263 is closed as an execution-verified chain.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Resume by re-discovering live main, validating this closure commit, then selecting the next Priority-2 target from the current 24-group census using fresh risk/consumer evidence. Do not assume the next identity from historical ordering alone.