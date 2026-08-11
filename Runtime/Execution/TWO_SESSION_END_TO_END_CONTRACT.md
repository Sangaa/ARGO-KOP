# Two-Session End-to-End Contract

## Purpose

Prove continuity across sessions without collapsing historical evidence into current facts or bypassing authorization.

## Required Cycle

```text
SESSION 1
Runtime
  ↓
Execution Trace
  ↓
Historical Memory

SESSION 2
Historical Memory
  ↓
Scoped Selection
  ↓
Context Rehydration
  ↓
Reasoning / Proposal
  ↓
Authorization
  ↓
Execution Adapter
```

## Invariants

1. Session 1 identity remains attached to recovered historical evidence.
2. Session 2 identity is not overwritten by Session 1 identity.
3. Historical evidence remains labeled as historical evidence.
4. Authorization must be explicit in Session 2.
5. Execution remains simulated and side-effect-free in the prototype.
6. Unrelated historical evidence remains excluded.

## Failure Boundary

If Session 2 lacks authorization, the cycle stops before execution.

If no scoped historical evidence exists, the cycle must not manufacture evidence; the proposal remains review-required.

## Result

Success means continuity of evidence and provenance, not automatic trust or automatic action.
