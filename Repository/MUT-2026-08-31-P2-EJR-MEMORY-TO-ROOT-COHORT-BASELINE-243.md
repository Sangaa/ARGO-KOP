# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-243

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort successor after Repair242.

Repair-head artifact `9747340901` proved legitimate cohort drift from expected 29 to observed 28 with complete history and no incomplete group except `__COHORT_COUNT_DRIFT__`.

Prewrite `3fde3dae61e92b7656214747145c776db230b1d1`. Functional successor `9749752230c7168c45eb915b752926a16054f534` changed only `EXPECTED_GROUP_COUNT = 29` to `28` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`. Compare proved one file, one addition, one deletion.

Exact functional-head verification:
- Internal-ID `33363248873`: SUCCESS
- Full-Stack `33363248793`: SUCCESS
- Runtime `33363248796`: SUCCESS
- M2 `33363248807`: SUCCESS
- Real Matrix: NOT APPLICABLE to census-only diff

Final census artifact `9747405796`, digest `sha256:fb511ebad6ce5ac4a645aa69a1e1ffc7ab535be162b9a66689d5aa6f22c92083`, proved expected=28, observed=28, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[]. EJR-210 and EJR-408 are absent from the target cohort.

Lease243 is CLOSED / EXECUTION-VERIFIED. Current governed MEMORY_TO_ROOT baseline is 28.
