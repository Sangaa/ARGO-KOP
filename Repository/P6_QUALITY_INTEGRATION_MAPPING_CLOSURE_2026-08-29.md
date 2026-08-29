# P6 Quality / Integration Exact-Path Mapping — Closure

Date: 2026-08-29  
Lease: `R71-20260829-P6-QI-MAPPING-016`  
Role: HERMUZ  
Functional evidence SHA: `c01113447bf5688165ad390d072ef4849c65de79`

## Objective

Close the observed P6 CI-impact `UNMAPPED` result for:

`Quality/Integration/test_run010_eng006_handoff_contract.py`

without inventing relationship authority or widening RUN-010 → ENG-006/SRV-009 semantics.

## Implemented boundary

`Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` classifies `Quality/Integration/**` as `IN_SCOPE`.

The exact test path is now present in `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` only as discoverable impact evidence for the existing bounded RUN-010 / ENG-006 / SRV-009 seam.

The matrix still states `PARTIALLY_VERIFIED`; ordinary connected-spine routing remains non-universal and unproven.

## Verification

Exact functional change set:

`1f92593bd736371cc93e837644ec0aad6ad4932c → c01113447bf5688165ad390d072ef4849c65de79`

Changed together:

- `Quality/Integration/test_ci_impact_correlation.py`
- `Repository/MUT-2026-08-29-P6-QUALITY-INTEGRATION-MAPPING-016_MUTATION_MATRIX.md`
- `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md`

Evidence:

- Full-Stack run `33244385018` — SUCCESS.
- Mutation Matrix preflight — PASS with one protected change and one Matrix in the same diff.
- P6 CI-impact regression — PASS, including the current-repository assertion that the target exact path is `IN_SCOPE`, `MAPPED`, and `NO_AUTO_PROMOTION`.
- Full-Stack candidate audit — `gap_count=0`.
- Runtime/Integration run `33244385021` — SUCCESS.
- M2 run `33244385032` — SUCCESS.

## Separate policy gap

The exact-head correlator classified some files belonging to this transaction itself as unresolved/unmapped. That is a distinct **control-surface self-correlation policy** problem. It does not reverse the target-path proof because the target path is tested directly against current canonical repository sources.

## Failure-to-learning record

An unintended temporary staging file was created during preparation and immediately removed before the protected mutation. The event is preserved in Git history and in the transaction Matrix. Rule learned: when preparing a multi-file protected transaction, do not use repository file creation as a scratch buffer; use the Git tree transaction directly.

## Non-claims

- Exact-path mapping is not relationship verification.
- Exact-path mapping is not runtime reachability.
- `PARTIALLY_VERIFIED` is not promoted.
- Global Connected Baseline remains open.
- Provider-authentication and later IGT trust states remain on their existing holds.

## Closure

`CI-IMPACT-QUALITY-INTEGRATION-MAPPING = CLOSED / EXECUTION-VERIFIED / EXACT-TARGET-PATH`
