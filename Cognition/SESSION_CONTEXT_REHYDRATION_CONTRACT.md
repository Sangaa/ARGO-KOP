# Session Context Rehydration Contract

## Purpose

Define the controlled transition from persisted historical Runtime evidence into a new session's Cognition Context.

## Flow

```text
Persisted Historical Evidence
          ↓
Scoped Memory Selection
          ↓
Context Rehydration
          ↓
CONTEXT_READY
```

## Boundaries

- Current facts remain current facts.
- Historical records remain historical evidence.
- Only task- or project-scoped history may be selected by the current prototype.
- Rehydration does not promote evidence into Knowledge.
- Rehydration does not create authorization.
- Rehydration does not trigger execution.

## Rehydration Output

The resulting context must expose:

- current facts;
- selected historical evidence;
- excluded history;
- provenance requirement;
- explicit `rehydrated=true` state;
- `historical_is_active_context=false`.

## Future Extension

Semantic relevance, temporal weighting, contradiction detection, and confidence scoring may refine selection later. They must operate after the structural scope boundary and must not erase provenance.
