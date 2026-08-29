# MUT-2026-08-29 — P6 EJR SCOPE GOVERNANCE RESOLUTION — 009

State: APPLIED / PENDING EXACT-HEAD CI
Lease: R71-20260829-P6-EJR-SCOPE-009
Baseline: a661fcd63662fb979c027cc6ad21ae95a300566f
Issue: #15
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

## Required proof

- EJR-only changed path returns `OUT_OF_SCOPE / NOT_APPLICABLE / NO_AUTO_PROMOTION`.
- Injected mapping/relationship text cannot promote EJR to mapped.
- Unknown paths remain `UNRESOLVED / POLICY_UNRESOLVED`.
- Mixed EJR + in-scope implementation paths are evaluated independently.
- Runtime/Integration, Full-Stack and M2 must be green at the exact functional SHA before Issue #15 closes.

## Non-claims

- No REP-020 mapping added.
- No relationship promoted.
- No runtime semantics changed.
- No EJR evidence discarded.
- No Connected Baseline global closure implied.
