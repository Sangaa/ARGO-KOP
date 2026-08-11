# Decision Outcome Feedback Contract

## Purpose

Create a governed boundary between an executed decision outcome and future learning.

## Flow

```text
Decision
   ↓
Execution
   ↓
Outcome
   ↓
Evaluation
   ↓
Learning Eligibility
```

## Rules

1. An outcome must retain both `decision_id` and `execution_id`.
2. An outcome must have an explicit `outcome_id`.
3. `UNASSESSED` outcomes may be recorded but are not learning eligible.
4. Only an explicitly `EVALUATED` outcome can become learning eligible.
5. `learning_eligible=true` is accepted only when evaluation is `EVALUATED`.
6. Missing provenance or invalid evaluation state rejects feedback.

## Boundary

Recording an outcome is not the same as judging a decision correct.

Learning eligibility is a further governed state; the feedback gate does not promote knowledge itself.

## Failure Codes

- `DECISION_ID_REQUIRED`
- `EXECUTION_ID_REQUIRED`
- `OUTCOME_ID_REQUIRED`
- `INVALID_EVALUATION_STATUS`
