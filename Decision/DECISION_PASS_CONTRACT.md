# Decision Pass Contract

## Purpose

Convert a traceable reasoning result into a governed proposal without executing an action.

## Rules

1. Incomplete reasoning produces `HOLD`.
2. Unresolved questions produce `REVIEW_REQUIRED`.
3. Clear reasoning may produce `PROPOSAL_READY`.
4. A proposal is not authorization.
5. Execution remains `NOT_REQUESTED` at this layer.

## Flow

```text
Reasoning
   ↓
Rule Evaluation
   ↓
┌─────────────────────┐
│ Unresolved Evidence │ → REVIEW_REQUIRED
└─────────────────────┘
           │
           ↓
┌─────────────────────┐
│ Sufficient Reasoning│ → PROPOSAL_READY
└─────────────────────┘
           ↓
   Authorization Boundary
           ↓
      Execution
```

## Governance Boundary

The Decision Pass may recommend what should happen next. It may not perform the action or imply that authorization has already been granted.
