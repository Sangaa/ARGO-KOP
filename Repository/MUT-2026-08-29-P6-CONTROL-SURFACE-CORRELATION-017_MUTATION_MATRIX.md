# MUTATION MATRIX — P6 CONTROL-SURFACE SELF-CORRELATION POLICY 017

Transaction ID: `MUT-2026-08-29-P6-CONTROL-CORRELATION-017`  
Protocol: GOV-014 v1.0.1  
Lease: `R71-20260829-P6-CONTROL-CORRELATION-017`  
Baseline: `d257d6c23151207f24b3110d0378585a8b2fa60b`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P6-CTRL-017-01 | `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` | UPDATE | Classify Mutation Matrix direct P6 impact as OUT_OF_SCOPE while retaining GOV-014 controls | Y | N |
| P6-CTRL-017-02 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | Add exact control-surface evidence paths for REP-020, P6 scope registry, and CI correlator regression; no relationship promotion | Y | N |
| P6-CTRL-017-03 | `Quality/Integration/test_ci_impact_correlation.py` | UPDATE | Canonically prove mapped control surfaces and NOT_APPLICABLE Mutation Matrix policy | Y | N |

## KEEP REQUIREMENT

All runtime, relationship, provider-authentication, IGT, and Connected-Baseline states are `KEEP`.

This transaction MUST NOT:

- promote any relationship state;
- exempt Mutation Matrices from GOV-014 or Matrix CI gates;
- hard-code policy in the correlator;
- classify unknown path families by analogy;
- claim global integrity.

## Execution Evidence

- Policy source remains the canonical P6 scope registry.
- REP-020 remains provisional/not authority.
- Same-change-set Matrix packaging is present for the protected REP-020 mutation.
- Read-back and exact-head CI pending.
- Unexpected Changes = 0.

## Closure

`MUT-2026-08-29-P6-CONTROL-CORRELATION-017 = APPLIED / VERIFICATION PENDING`.
