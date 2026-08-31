# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-263

Status: OPEN / EXECUTION-PENDING
Scope: Separate deterministic MEMORY_TO_ROOT cohort successor after Repair262.
Opening repair head: `5bbfd61df063024824091c74c8597f89eb9b8bf2`.
Pre-write Matrix263 commit: `d8cb01864687dba1227d18867688e2b024f29020`.

## Trigger evidence

Repair262 exact head preserved `EXPECTED_GROUP_COUNT = 25` while resolving one MEMORY_TO_ROOT ambiguity. Exact-head Internal-ID run `33371361058` passed all identity, vacancy, ambiguity, chronology, namespace-lineage, non-monotonic and reverse-provenance stages, and failed only at the deterministic MEMORY_TO_ROOT census.

Artifact `9750192824`, digest `sha256:0761f442a253813426fcdebe4290b0b3895337abd339b85628dda853d8e189e4`, established the bounded drift condition: expected=25, observed=24, history_complete=true, classification_complete=false, decision=PARTIAL, with sole incompleteness `__COHORT_COUNT_DRIFT__`.

This is the same governed successor pattern proven by Lease258 after Repair257.

## Pre-write validation

Matrix263 passed before this lease opened:
- Full-Stack Repository Audit #2356: SUCCESS
- ARGO Runtime Prototype and Integration #2131: SUCCESS
- Real Mutation Matrix Regression #199: SUCCESS
- M2 Multi-Channel Proposal Training #1013: SUCCESS

## Authorized mutation

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` may change:

`EXPECTED_GROUP_COUNT = 25` → `EXPECTED_GROUP_COUNT = 24`.

No classifier logic, tests, workflows, EJR records, Memory records, GOV/REP documents, historical evidence, or Global Integrity state may change.

## Hard gate

Immediately before execution, re-discover main and re-read the census source. Abort if main is not this lease commit or if the source constant/blob has drifted.

After execution require exact one-line diff/readback and Internal-ID evidence showing expected=24, observed=24, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Any additional failure is a HARD HOLD and is outside this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.