# P6 Quality / Integration Exact-Path Mapping — Closure Candidate

Date: 2026-08-29  
Lease: `R71-20260829-P6-QI-MAPPING-016`  
Role: HERMUZ

## Objective

Close the observed P6 CI-impact `UNMAPPED` result for:

`Quality/Integration/test_run010_eng006_handoff_contract.py`

without inventing relationship authority or widening RUN-010 → ENG-006/SRV-009 semantics.

## Authority boundary

`Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` explicitly classifies `Quality/Integration/**` as `IN_SCOPE` for P6 direct impact correlation.

`Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` already records the bounded RUN-010 / ENG-006 / SRV-009 evidence boundary as `PARTIALLY_VERIFIED`, with ordinary connected-spine routing remaining non-universal and unproven.

Therefore the permitted repair is exact-path evidence discoverability only.

## Required mutation

1. Add the exact test path to the existing bounded REP-020 impact evidence.
2. Preserve all existing relationship states and semantic boundaries.
3. Add a regression that reads current canonical P6 scope, REP-020, and REP-014 and proves:
   `IN_SCOPE → MAPPED → NO_AUTO_PROMOTION` for the exact test path.
4. Keep the Mutation Matrix visible in the same changed-file set as the protected REP-020 update.

## Verification status

`PENDING SAME-CHANGE-SET MUTATION + READ-BACK + EXACT-HEAD CI`

## Non-claims

- Exact-path mapping is not relationship verification.
- Exact-path mapping is not runtime reachability.
- This does not promote `PARTIALLY_VERIFIED`.
- This does not close the global Connected Baseline.
- This does not alter provider-authentication or IGT trust-state holds.
