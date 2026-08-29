# MUTATION MATRIX — P6 CONTROL-SURFACE SELF-CORRELATION POLICY 017

Transaction ID: `MUT-2026-08-29-P6-CONTROL-CORRELATION-017`  
Protocol: GOV-014 v1.0.1  
Lease: `R71-20260829-P6-CONTROL-CORRELATION-017`  
Baseline: `d257d6c23151207f24b3110d0378585a8b2fa60b`  
Functional evidence SHA: `667ec201940a09107706dafa469dbe34c2510d71`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P6-CTRL-017-01 | `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` | UPDATE | Classify Mutation Matrix direct P6 impact as OUT_OF_SCOPE while retaining GOV-014 controls | Y | Y |
| P6-CTRL-017-02 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | Add exact control-surface evidence paths for REP-020, P6 scope registry, and CI correlator regression; no relationship promotion | Y | Y |
| P6-CTRL-017-03 | `Quality/Integration/test_ci_impact_correlation.py` | UPDATE | Canonically prove mapped control surfaces and NOT_APPLICABLE Mutation Matrix policy | Y | Y |

## KEEP REQUIREMENT

All runtime, relationship, provider-authentication, IGT, and Connected-Baseline states are `KEEP`.

This transaction MUST NOT:

- promote any relationship state;
- exempt Mutation Matrices from GOV-014 or Matrix CI gates;
- hard-code policy in the correlator;
- classify unknown path families by analogy;
- claim global integrity.

## Execution Evidence

Exact functional change set: `d257d6c23151207f24b3110d0378585a8b2fa60b → 667ec201940a09107706dafa469dbe34c2510d71`.

- Full-Stack run `33244552680` = SUCCESS.
- P6 CI-impact regression = PASS.
- P6 canonical repository scope regression = PASS.
- Mutation Matrix preflight = PASS with `changed_files=4`, `protected_changes=1`, `mutation_matrices=1`.
- Actual changed-set correlation = `overall=MAPPED`, `mapped_path_count=3`, `not_applicable_path_count=1`, `unmapped_path_count=0`, `policy_unresolved_path_count=0`, `promotion=NO_AUTO_PROMOTION`.
- The Matrix path resolved `OUT_OF_SCOPE → NOT_APPLICABLE` while REP-020, P6 scope registry, and CI correlator regression resolved `IN_SCOPE → MAPPED`.
- Full-Stack repository audit = `gap_count=0`, no orphan/untested/broken-reference candidates.
- Runtime/Integration run `33244552683` = SUCCESS across integration, prototype, and integrity jobs.
- M2 run `33244552693` = SUCCESS.
- Real Mutation Matrix Regression run `33244552686` = SUCCESS.
- Read-back confirms policy lives in the canonical P6 scope registry; the correlator implementation itself was not hard-coded.
- Unexpected Changes = 0.

## Learning

A control-plane correlator can create recursive noise when it treats its transaction-control artifacts as ordinary implementation impact. The safe boundary is not to suppress those artifacts in code, but to classify their direct-impact applicability in the governing scope registry while retaining their independent governance gates.

## Closure

`MUT-2026-08-29-P6-CONTROL-CORRELATION-017 = CLOSED / EXECUTION-VERIFIED / NO AUTO-PROMOTION`.
