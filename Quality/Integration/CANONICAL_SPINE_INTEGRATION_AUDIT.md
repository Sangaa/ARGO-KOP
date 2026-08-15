# Canonical Spine Integration Audit

## Purpose

Run one repository-wide audit against the canonical ARGO KOP spine and expose every seam that is not supported by sufficient evidence.

## Evidence Policy

The audit is deliberately conservative.

A keyword or file-name match can produce only:

- `PARTIAL`
- `MISSING`

It cannot produce `CONNECTED`.

A seam becomes `CONNECTED` only when an explicit verified seam record is supplied from an integration contract or executable/synthetic integration test.

## Canonical Seams

1. Memory / Context → Cognition
2. Cognition → Reasoning
3. Reasoning → Decision
4. Decision → Authorization
5. Authorization → Execution
6. Execution → Execution Trace
7. Execution → Outcome
8. Execution Trace → Outcome Evaluation
9. Outcome Evaluation → Feedback Quality
10. Feedback Quality → Learning Readiness
11. Learning Readiness → Learning Pipeline

The canonical seam count is **11** and must remain aligned with `Quality/Integration/canonical_spine_gap_map.py`.

## Output

The audit returns:

- total seam count
- evidence state for every seam
- gap map
- number of explicitly verified connections

## Principle

`Repository presence ≠ connectivity proof`.

`Local test pass ≠ global integration pass`.

`CONNECTED` is an evidence-backed claim, not a discovery guess.
