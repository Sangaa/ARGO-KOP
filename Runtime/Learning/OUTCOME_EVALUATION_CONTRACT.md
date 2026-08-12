# Outcome Evaluation Contract

## Purpose

Classify a recorded decision outcome before any learning promotion is considered.

## Required Chain

```text
Decision
  ↓
Execution
  ↓
Outcome Evidence
  ↓
Outcome Evaluation
  ↓
Learning Eligibility
  ↓
Existing Learning Promotion Gate
```

## Result Classes

- `SUCCESS` — intended result achieved according to the available evaluation evidence.
- `PARTIAL` — meaningful result achieved, but the intended result was only partly achieved.
- `FAILURE` — the evaluated result did not achieve the intended outcome.
- `INCONCLUSIVE` — available evidence is insufficient to classify the outcome reliably.

## Rules

1. Evaluation must retain `decision_id` and `execution_id`.
2. Evaluation must retain `outcome_id`.
3. Evaluation must retain at least one outcome evidence trace.
4. Unknown result classes are rejected.
5. `INCONCLUSIVE` is evaluated but is not learning eligible.
6. `SUCCESS`, `PARTIAL`, and `FAILURE` may become learning eligible for review; they are not automatically promoted.
7. This evaluator does not determine truth outside the supplied evaluation evidence.
8. This evaluator does not replace the existing Learning Promotion Gate.

## Boundary

```text
Outcome Classification
        ≠
Knowledge Promotion
```

A failure can be valuable learning material. A success can still contain a bad decision path. Promotion remains a separate governed step.
