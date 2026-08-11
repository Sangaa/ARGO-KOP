# Reasoning Hold and State Behavior

## Purpose

Turn an unresolved cognition condition into governed system behavior.

## State Rule

```text
CONTEXT CONFLICT
      ↓
REQUIRES_REASONING
      ↓
HOLD
      ↓
Decision = BLOCKED
Authorization = BLOCKED
Execution = BLOCKED
```

A `HOLD` is an active system state, not merely a diagnostic message.

## Clear Path

```text
NO CONTEXT CONFLICT
      ↓
CLEAR
      ↓
Decision may proceed
      ↓
Authorization remains separately governed
      ↓
Execution remains separately governed
```

## Safety Principle

A cognition hold can stop downstream progress, but clearing the hold does not grant authorization or execution permission.
