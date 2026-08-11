# Decision Context Contract

## Purpose

Ensure the Decision layer consumes explicit cognitive state and evidence instead of treating reasoning as an opaque input.

## Required Decision Inputs

A decision proposal must be derived from:

- current facts
- assumptions
- known knowledge references
- unresolved questions
- evidence map
- governance rules
- cognition state

## Decision Safety Rules

1. `HOLD` cognition state must not reach `PROPOSAL_READY`.
2. Any unresolved question remains visible to the decision layer.
3. Evidence must remain traceable to its basis.
4. A decision proposal is not authorization.
5. Authorization is not execution.

## State Flow

```text
Cognition State
      ↓
Evidence + Context
      ↓
Decision Evaluation
      ↓
PROPOSAL_READY / REVIEW_REQUIRED / HOLD
      ↓
Authorization Gate
      ↓
Execution Gate
```
