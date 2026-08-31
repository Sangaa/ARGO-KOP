# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-217

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline: `main@0b67b706de7b7a8d54b7f4decc0fa51820e6add6`
Prewrite: `545b325b7967e8d73cc55eab533e28f37660c72c`
Functional head: `f0262431402c953d1138e74f2f4ac6845ca3ef1a`
Predecessor repair: Lease216 — root `EJR-219` re-identified to vacancy-proven `EJR-402`.

## Evidence basis
Lease216 exact-head Internal Document-ID Audit run `33355206134` failed only at the deterministic memory-to-root provenance census after all tests and prior analyzers passed. Artifact `9744912199` proved expected=34, observed=33, history_complete=true, and sole incomplete=`__COHORT_COUNT_DRIFT__`. Internal-ID artifact `9744909922` showed neither `EJR-219` nor `EJR-402` remained ambiguous. The four other Lease216 workflows passed.

## Executed mutation
Exactly one semantic constant changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
- `EXPECTED_GROUP_COUNT = 34` → `EXPECTED_GROUP_COUNT = 33`.

Compare `545b325...` → `f026243...` proves the functional diff contains only that file with one addition and one deletion. Classifier logic, scanner, evidence boundary, failure behavior, tests, EJR records, and REP authority surfaces were unchanged.

## Exact functional-head verification
At `f0262431402c953d1138e74f2f4ac6845ca3ef1a`:
- Internal Document-ID Audit `33356597214` — SUCCESS;
- Full-Stack Repository Audit `33356597201` — SUCCESS;
- Runtime Prototype and Integration Tests `33356597204` — SUCCESS;
- M2 Multi-Channel Proposal Training `33356597202` — SUCCESS.

Deterministic census artifact `9745333997`, digest `sha256:2218b68129f8f84244848558a9e6065363ecc7a0c39eaee8b5ef32010970398b`, proves expected=33, observed=33, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[]. Internal-ID remains clean for `EJR-219` / `EJR-402`.

## Workflow applicability note
Real Mutation Matrix Regression did not trigger on the census-only functional commit because that diff did not match its path filter. This is neither PASS nor FAIL and is not rewritten as one. The closure commit synchronizes the governed Mutation Matrices and therefore requires Real Mutation Matrix Regression on that closure head.

## Learning rule
When a separately authorized identity repair legitimately removes one classifier-selected ambiguity group, preserve the drift failure as evidence; rebaseline only afterward from the proven post-repair cohort and never weaken the guard. Path-filtered workflow non-trigger must be recorded as NOT APPLICABLE to that exact diff, not fabricated into a result.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
