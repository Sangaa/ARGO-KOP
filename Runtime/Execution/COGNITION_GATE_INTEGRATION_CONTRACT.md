# Cognition Gate Integration Contract

## Purpose

Define how an unresolved cognition condition controls the connected execution spine.

## Governed Path

```text
Context
  ↓
Conflict Detection
  ↓
Reasoning Hold
  ↓
┌───────────────┐
│ HOLD          │
│               │
│ Decision  ✕   │
│ Auth.     ✕   │
│ Execution ✕   │
└───────────────┘
```

When cognition reports `REQUIRES_REASONING`, the runner must stop the downstream path and return a held result.

## Clear Path

If no unresolved conflict exists, the normal decision/authorization/execution gates remain available according to their own rules.

## Boundary

The cognition gate blocks downstream progress; it does not itself authorize, decide, or execute.
