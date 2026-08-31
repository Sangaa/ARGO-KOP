# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-221

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline: `main@a78bf0dd8760b036656515c39378261a1c0a2a09`
Prewrite: `a17f6109283387a29f1eca79babd8d5d5e41eaaa`
Functional head: `bab2d672773a633e404213d02f6ed9bf458d1c78`
Predecessor: Lease220 EJR-301→EJR-403 identity repair + direct REP-021 consumer rewrite.

## Evidence basis
Lease220 Internal-ID `33357105926` preserved the correct drift failure: expected=33 / observed=32 / history_complete=true / sole incomplete=`__COHORT_COUNT_DRIFT__`; all 32 selected groups were individually complete and EJR-301/EJR-403 were no longer ambiguous.

## Executed mutation
Exactly one semantic constant changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
- `EXPECTED_GROUP_COUNT = 33` → `EXPECTED_GROUP_COUNT = 32`.

Compare `a17f610...` → `bab2d672...` proves exactly one source file changed with one addition and one deletion. Classifier logic, scanner, evidence boundary, drift failure semantics, tests, EJR records, consumers, and REP authority surfaces were unchanged.

## Exact-head verification
At `bab2d672773a633e404213d02f6ed9bf458d1c78`:
- Internal Document-ID Audit `33357346467` — SUCCESS;
- Full-Stack Repository Audit `33357346484` — SUCCESS;
- Runtime Prototype and Integration Tests `33357346422` — SUCCESS;
- M2 Multi-Channel Proposal Training `33357346457` — SUCCESS.

Deterministic census artifact `9745556033`, digest `sha256:f885ecfe13c18ff6cd3dbe11cdbc5e20e2d1350d93547019486fa6d8a3296287`, proves expected=32, observed=32, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[]. Internal-ID artifact `9745553680`, digest `sha256:7097e7b30d585732be801d2344e0627fb21a25fd3be289b6f93d52319667430b`, keeps EJR-301/EJR-403 non-ambiguous.

Real Mutation Matrix did not trigger on the census-only functional diff. This is NOT APPLICABLE to that exact diff, not PASS or FAIL. The closure commit changes governed Matrix surfaces and is the applicable regression point.

## Learning rule
When a bounded identity repair includes its direct governed consumer and legitimately removes one classifier-selected ambiguity group, preserve the drift failure first; rebaseline only afterward from execution-proven post-repair state without weakening guard semantics.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
