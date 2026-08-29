# MUT-2026-08-29 — P6 EJR SCOPE GOVERNANCE RESOLUTION — 009

State: CLOSED / EXECUTION-VERIFIED
Lease: R71-20260829-P6-EJR-SCOPE-009
Baseline: a661fcd63662fb979c027cc6ad21ae95a300566f
Functional SHA: 0ea193655f1c0b2448c39b18872ef7598eb0cfde
Issue: #15 — CLOSED / COMPLETED
Scope: P6 eligibility policy + canonical regression only

## Decision

Classify `EJR/**` as `OUT_OF_SCOPE` for **direct P6 implementation/relationship impact correlation**.

This is deliberately narrower than `EJR is irrelevant`.

Engineering Journal artifacts remain valid provenance, failure/learning evidence, session transfer evidence, and candidate inputs to later governed promotion.

## Authority basis

- GOV-013 separates evidence/relationship state and forbids unsupported promotion.
- GOV-015 states documentation is not evidence and learning requires a governed promotion chain.
- GOV-016 states failure/learning records do not gain governance/runtime/relationship authority by existence.
- Issue #15 forbids adding REP-020 mappings or classifier exceptions merely to turn EJR documentation changes green.

## Mutation Matrix

| Target | Before | After | Authority effect |
|---|---|---|---|
| Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md | EJR/** = UNRESOLVED | EJR/** = OUT_OF_SCOPE for direct P6 correlation | policy resolution only; no relationship/runtime promotion |
| Quality/Integration/test_p6_canonical_repository.py | asserts POLICY_UNRESOLVED | asserts NOT_APPLICABLE + NO_AUTO_PROMOTION + mixed-path independence | regression protection |

## Exact-head proof

At `0ea193655f1c0b2448c39b18872ef7598eb0cfde`:

- Full-Stack Repository Audit run `33239636423` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests run `33239636402` — SUCCESS; prototype, integrity and integration jobs all passed.
- M2 Multi-Channel Proposal Training run `33239636453` — SUCCESS.
- P6 canonical repository boundary regression — SUCCESS inside Full-Stack.
- Mixed-path independence is regression-covered: EJR `NOT_APPLICABLE` cannot hide an independent in-scope path.

Issue #15 was closed as `completed` only after exact-head verification.

## Non-claims

- No REP-020 mapping added.
- No relationship promoted.
- No runtime semantics changed.
- No EJR evidence discarded.
- No Connected Baseline global closure implied.

## Continuous-improvement learning

A documentation/evidence surface should not be forced into an implementation impact graph merely because a correlation mechanism accepts paths. Scope eligibility must be decided before correlation, and `OUT_OF_SCOPE` must preserve independent provenance/learning duties rather than mean `ignored`.

## Closure

`P6-EJR-DIRECT-IMPACT-SCOPE = CLOSED / OUT_OF_SCOPE / EXECUTION-VERIFIED`.
