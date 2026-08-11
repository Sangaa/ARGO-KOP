# Execution State Transition Contract

## Purpose

Make the connected execution spine explicit about the state transition caused by Cognition.

## State Model

```text
CONTEXT_READY
     ↓
COGNITION_ANALYZED
     ↓
 ┌───────────────┐
 │ conflict?     │
 └───────┬───────┘
     no  │  yes
         │
         ↓
      CLEAR ─────────────→ REQUIRES_REASONING → HOLD
         │                                      │
         ↓                                      ├→ Decision BLOCKED
      DECISION                                ├→ Authorization BLOCKED
         ↓                                      └→ Execution BLOCKED
      AUTHORIZATION
         ↓
      EXECUTION
```

## Governance Rules

1. `HOLD` is terminal for the current execution attempt.
2. A `HOLD` does not imply that the historical evidence is correct or incorrect.
3. Clearing a `HOLD` does not grant authorization or execution permission.
4. External side effects remain outside the experimental runner.
5. Every transition must remain traceable to the preceding state and evidence.

## Current Scope

This contract describes the experimental connected spine. It is not a production workflow engine.
