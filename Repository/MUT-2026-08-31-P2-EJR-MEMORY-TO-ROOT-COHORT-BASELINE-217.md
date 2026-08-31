# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-217

Status: OPEN / PREWRITE AUTHORITY
Baseline: `main@0b67b706de7b7a8d54b7f4decc0fa51820e6add6`
Predecessor repair: Lease216 — root `EJR-219` re-identified to vacancy-proven `EJR-402`.

## Evidence basis
Lease216 exact-head Internal Document-ID Audit run `33355206134` failed only at the deterministic memory-to-root provenance census after all tests and prior analyzers passed. Artifact `9744912199` proves:
- expected_group_count = 34;
- observed_group_count = 33;
- history_complete = true;
- classification_complete = false;
- decision = PARTIAL;
- incomplete_group_ids = [`__COHORT_COUNT_DRIFT__`].

Internal-ID artifact `9744909922` shows neither `EJR-219` nor `EJR-402` remains in `ambiguous_duplicate_records`. Full-Stack, Runtime/Integration, M2, and Real Mutation Matrix all passed on the Lease216 repair head.

## Allowed functional mutation
Exactly one semantic constant in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
- `EXPECTED_GROUP_COUNT = 34` → `EXPECTED_GROUP_COUNT = 33`.

No classifier, scanner, evidence boundary, failure semantics, tests, EJR record, REP authority surface, or unrelated file may be changed except this Lease and its Mutation Matrix/closure evidence.

## Required verification
At the exact functional head:
1. Internal Document-ID Audit must SUCCESS.
2. Deterministic memory-to-root census must report 33/33, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].
3. `EJR-219` and `EJR-402` must remain non-ambiguous.
4. Full-Stack Repository Audit, Runtime Prototype/Integration, M2 Multi-Channel Proposal Training, and Real Mutation Matrix Regression must SUCCESS.

## Learning rule
When a separately authorized identity repair legitimately removes one classifier-selected ambiguity group, preserve the drift failure as evidence; rebaseline only afterward from the proven post-repair cohort and never weaken the guard.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
