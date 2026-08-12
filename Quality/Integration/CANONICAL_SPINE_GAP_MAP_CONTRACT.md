# Canonical Spine Gap Map Contract

## Purpose

Provide an explicit, executable representation of every seam in the canonical ARGO operational spine.

## Seam States

- `CONNECTED` — required source, destination, contract, and evidence are present.
- `PARTIAL` — some required integration evidence exists, but the seam is incomplete.
- `MISSING` — no sufficient integration evidence has been established.
- `BLOCKED_BY_GOVERNANCE` — the seam is intentionally prevented by a governance boundary.
- `INTENTIONALLY_ISOLATED` — the component is outside the operational spine by design.

## Rule

Missing evidence defaults to `MISSING`. The audit must not infer `CONNECTED` from file existence or individual test success.

## Canonical Seams

```text
Memory / Context → Cognition
Cognition → Reasoning
Reasoning → Decision
Decision → Authorization
Authorization → Execution
Execution → Execution Trace
Execution Trace → Outcome Evaluation
Outcome Evaluation → Feedback Quality
Feedback Quality → Learning Readiness
Learning Readiness → Learning Pipeline
```

## Safety

The gap map is diagnostic. It does not modify architecture, delete files, grant authorization, or enable external execution.
