# Learning Pipeline Integration Contract

## Purpose

Provide one auditable upstream path from an executed decision outcome to promotion review while preserving evidence provenance from execution into the outcome.

## Pipeline

```text
Decision
  ↓
Execution
  ↓
Execution Trace
  ↓
Outcome
  ↓
Outcome Evaluation
  ↓
Feedback Quality
  ↓
Learning Readiness Report
  ↓
Existing Learning Promotion Gate
```

## Evidence Rules

1. Invalid outcomes stop at Evaluation.
2. Every evaluated outcome must contain outcome evidence.
3. Every evaluated outcome must identify the execution trace IDs associated with the producing execution.
4. Every outcome evidence trace must belong to the declared execution trace set.
5. Orphaned outcome evidence stops evaluation with `OUTCOME_PROVENANCE_BROKEN`.
6. Weak feedback quality stops the pipeline before readiness.
7. `INCONCLUSIVE` outcomes are not learning-ready.
8. A readiness report is not a promotion action.
9. This integration MUST NOT promote knowledge itself.
10. The existing Learning Promotion Gate remains the only downstream promotion authority.

## Result States

- `NOT_READY` with stage `EVALUATION` — outcome classification or provenance validation failed.
- `NOT_READY` with stage `QUALITY` — feedback quality validation failed.
- `READY_FOR_PROMOTION_REVIEW` with stage `READINESS` — upstream checks passed.

## Boundary

Pipeline integration coordinates existing validators. It does not replace their contracts or bypass governance.
