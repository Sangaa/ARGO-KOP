# Task Context Envelope

## Purpose

Bound knowledge retrieval to the context of the task instead of treating the entire knowledge repository as equally relevant.

## Context Fields

- `task_id`
- `session_id`
- `project_id`
- `domain`
- `active_state`
- `claim`
- `allowed_scope`

## Retrieval Principle

```text
Task Context
    ↓
Context Filters
    ↓
Promoted Knowledge
    ↓
Relevant Knowledge
```

## Safety

Missing context must reduce retrieval confidence rather than silently widening the search scope.

A record outside `allowed_scope` is not eligible for reuse merely because its text looks similar.
