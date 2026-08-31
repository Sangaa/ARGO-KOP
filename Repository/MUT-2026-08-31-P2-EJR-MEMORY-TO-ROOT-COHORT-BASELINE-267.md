# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-267

Status: OPEN / EXECUTION-PENDING
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair266.
Repair266 head: `a47c20d9b065533107f47cecc1e82e92bf8847f6`.
Pre-write Matrix267: `1205a010fa032cfe7486a12bf9334690bbcccc74`.

## Trigger evidence

Repair266 resolved the displaced root EJR-233 identity to vacancy-proven EJR-413 while intentionally preserving `EXPECTED_GROUP_COUNT = 24`.

Exact-head Internal-ID run `33374581005` passed all identity, vacancy, ambiguity, chronology, namespace-lineage, non-monotonic and reverse-provenance stages, and failed only at MEMORY_TO_ROOT census.

Artifact `9751379903`, digest `sha256:4d71b41256ea0d308769d61f10145efecb1ba07eee6067218f77f7f1c055abf8`, proves:
- expected_group_count=24
- observed_group_count=23
- history_complete=true
- classification_complete=false
- decision=PARTIAL
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`]
- EJR-233 absent from target_ids
- EJR-413 absent from target_ids

This is the execution-confirmed Repair → separate cohort-baseline successor pattern already proven by Leases258 and 263.

## Pre-write validation

Matrix267 commit `1205a010fa032cfe7486a12bf9334690bbcccc74` passed:
- Full-Stack Repository Audit #2373 / run `33374696203`: SUCCESS
- ARGO Runtime Prototype and Integration #2147 / run `33374696170`: SUCCESS
- Real Mutation Matrix Regression #207 / run `33374696180`: SUCCESS
- M2 #1030 / run `33374696197`: SUCCESS

## Authorized mutation

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` may change:

`EXPECTED_GROUP_COUNT = 24` → `EXPECTED_GROUP_COUNT = 23`.

No classifier logic, tests, workflows, EJR records, Memory records, GOV/REP documents, historical evidence, Repair266 records, or Global Integrity state may change.

## Hard gate

Immediately before execution, re-discover main and re-read the census source. Abort if main is not this lease commit or if the source constant/blob has drifted.

After execution require:
- exact one-file, one-line diff;
- read-back `EXPECTED_GROUP_COUNT = 23`;
- Internal-ID evidence with expected=23, observed=23, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[];
- Full-Stack/Runtime/M2 success.

Any additional failure is a HARD HOLD outside this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.