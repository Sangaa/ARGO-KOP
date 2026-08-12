# Learning Pipeline Integration Contract

## Purpose

Provide one auditable upstream path from an executed decision outcome to promotion review.

## Pipeline

```text
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

## Rules

1. Invalid outcomes stop at Evaluation.
2. Weak feedback quality stops the pipeline before readiness.
3. `INCONCLUSIVE` outcomes are not learning-ready.
4. A readiness report is not a promotion action.
5. This integration MUST NOT promote knowledge itself.
6. The existing Learning Promotion Gate remains the only downstream promotion authority.

## Result States

- `NOT_READY` with stage `EVALUATION` — outcome classification failed.
- `NOT_READY` with stage `QUALITY` — feedback quality validation failed.
- `READY_FOR_PROMOTION_REVIEW` with stage `READINESS` — upstream checks passed.

## Boundary

Pipeline integration coordinates existing validators. It does not replace their contracts or bypass governance.
