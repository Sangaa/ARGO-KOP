# End-to-End Traceability Contract

## Purpose

Ensure one execution attempt remains traceable from its originating task and context through cognition, reasoning, decision, authorization, plan, and execution.

## Required Identity

The execution trace must preserve:

- `task_id`
- `project_id`
- `session_id` when supplied by context
- authorization identity when authorization exists
- final execution status

## Evidence Continuity

The trace must not silently replace the originating task identity while moving between stages.

## Prototype Rule

A synthetic trace may prove continuity of identity and state. It must not be interpreted as production observability.

## State Boundary

```text
Task
 ↓
Context
 ↓
Cognition / Reasoning
 ↓
Decision
 ↓
Authorization
 ↓
Plan
 ↓
Execution
 ↓
Trace
```

A `HOLD` remains traceable as a blocked attempt rather than disappearing from the trace.
