# P6 Control-Surface Self-Correlation Policy — Closure

Date: 2026-08-29  
Lease: `R71-20260829-P6-CONTROL-CORRELATION-017`  
Role: HERMUZ  
Functional evidence SHA: `667ec201940a09107706dafa469dbe34c2510d71`

## Closed problem

The P6 changed-path correlator previously produced self-referential noise for its own control transaction: P6 control surfaces could be `UNMAPPED`, while Mutation Matrix paths could become `POLICY_UNRESOLVED`, even though Mutation Matrices already have independent GOV-014 gates.

## Implemented boundary

- `Repository/MUT-*_MUTATION_MATRIX.md` is `OUT_OF_SCOPE` for direct P6 implementation/relationship impact correlation only.
- Mutation Matrix GOV-014, preflight, semantics, provenance, read-back, and closure duties remain mandatory.
- `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md`, `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md`, and `Quality/Integration/test_ci_impact_correlation.py` are explicitly discoverable as bounded P6 control evidence.
- Policy remains in the canonical scope registry; no special-case policy was hard-coded into `ci_impact_correlation.py`.
- All paths retain `NO_AUTO_PROMOTION`.

## Exact-head execution proof

Full-Stack run `33244552680` on exact functional SHA succeeded.

Actual changed-set correlation:

- `overall = MAPPED`
- `mapped_path_count = 3`
- `not_applicable_path_count = 1`
- `unmapped_path_count = 0`
- `policy_unresolved_path_count = 0`
- `promotion = NO_AUTO_PROMOTION`

The Matrix path resolved `OUT_OF_SCOPE / NOT_APPLICABLE`; the three P6 control surfaces resolved `IN_SCOPE / MAPPED`.

Additional evidence:

- P6 CI-impact regression PASS.
- P6 canonical repository scope regression PASS.
- Mutation Matrix preflight PASS: one protected REP-020 change and one Matrix in the same change set.
- Full-Stack candidate audit: `gap_count=0`.
- Runtime/Integration run `33244552683` SUCCESS.
- M2 run `33244552693` SUCCESS.
- Real Mutation Matrix Regression run `33244552686` SUCCESS.

## Learning

A governance/control artifact can be mandatory for a transaction while still being not applicable to a different direct-impact classifier. The two dimensions must not be collapsed. Applicability belongs in explicit policy; mandatory validation remains enforced by the artifact's own governance gates.

## Non-claims

- No runtime or relationship state was promoted.
- Mutation Matrices were not exempted from GOV-014.
- Unknown path families remain unresolved unless separately governed.
- Global Connected Baseline remains open.
- Provider authentication remains blocked by the external trust-anchor hold.
- Cognitive improvement remains unproven.

## Closure

`P6-CONTROL-SURFACE-SELF-CORRELATION-POLICY = CLOSED / EXECUTION-VERIFIED / NO AUTO-PROMOTION`
