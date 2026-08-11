# Historical Context Bridge Contract

## Purpose

Combine current facts with historical execution evidence without silently promoting history into current truth.

## Contract

- `current_facts` are current-session inputs.
- `historical_evidence` is explicitly historical.
- `historical_is_active_context` defaults to `false`.
- Historical evidence requires explicit promotion before becoming active context.
- Promotion does not grant authorization and does not execute an action.

## Flow

```text
Current Facts ─────────┐
                      ├→ Context Package → Cognition
Historical Evidence ──┘
          │
          └→ remains HISTORICAL_ONLY unless explicitly promoted
```

## Failure Behavior

No matching historical evidence must remain explicit rather than being inferred or fabricated.
