# MUTATION MATRIX — P6 QUALITY / INTEGRATION EXACT-PATH IMPACT MAPPING 016

Transaction ID: `MUT-2026-08-29-P6-QI-MAPPING-016`  
Protocol: GOV-014 v1.0.1  
Lease: `R71-20260829-P6-QI-MAPPING-016`  
Pre-write baseline: `397adb88136d453094fc44610d07615a89626f92`

> This pre-write record does not authorize semantic promotion. The protected REP-020 mutation must still be committed with this Matrix visible in the same CI changed-file set. If packaging separates the Matrix from the protected mutation, the transaction remains HOLD.

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| QI-MAP-016-01 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | Add exact-path evidence mapping for `Quality/Integration/test_run010_eng006_handoff_contract.py` to the existing bounded RUN-010 → ENG-006/SRV-009 impact boundary; preserve `PARTIALLY_VERIFIED`, non-universal routing boundary, and non-authority status | N | N |
| QI-MAP-016-02 | `Quality/Integration/test_ci_impact_correlation.py` | UPDATE | Add canonical-repository regression proving the exact test path resolves `IN_SCOPE → MAPPED → NO_AUTO_PROMOTION` using current REP-020/REP-014/P6 scope artifacts | N | N |

## KEEP REQUIREMENT

All other repository content and all existing REP-020 relationship states are `KEEP`.

Specifically this transaction MUST NOT:

- promote `PARTIALLY_VERIFIED` to `VERIFIED`;
- infer universal RUN-010 → SRV-009 routing;
- create reverse SRV-009 → RUN-010 dependency;
- claim runtime reachability from test mapping;
- change P6 scope eligibility;
- close the global Connected Baseline.

## Execution Evidence

- Pre-write authority/scope review completed against `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` v1.1.0.
- Existing bounded impact evidence reviewed in `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` v0.2.3.
- Functional verification, same-change-set packaging verification, read-back, and exact-head CI are pending.
- Unexpected Changes = 0 at pre-write stage.

## Closure

`MUT-2026-08-29-P6-QI-MAPPING-016 = PRE-WRITE / NOT YET VERIFIED`.
