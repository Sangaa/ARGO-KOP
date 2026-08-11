# Historical Context Bridge Contract

## Purpose

Allow Cognition/Context loading to retrieve relevant historical execution evidence without silently converting history into active state.

## Contract

```text
Historical Trace
      ↓
Task/Session Filter
      ↓
Historical Evidence
      ↓
Context Loader
      ↓
ACTIVE_CONTEXT = false
```

## Promotion Boundary

Historical evidence may be promoted only by an explicit governed process. Retrieval alone never grants current-state authority, decision authority, or execution authorization.

## Required Labels

- `record_type = EXECUTION_TRACE`
- `promotion_status = NOT_PROMOTED`
- `active_context = false`

## Failure Behavior

No matching trace returns `NO_HISTORY` rather than an inferred or fabricated result.
