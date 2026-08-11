# Trace Inspection and Promotion Contract

## Purpose

Retrieve historical execution traces without contaminating current runtime context.

## Default Rule

Inspection is read-only. A retrieved trace is `HISTORICAL_ONLY` by default.

## Explicit Promotion

Historical information may become active context only through an explicit promotion request represented by `promote=True` in the prototype.

Promotion is a separate governance event; retrieval itself never promotes data.

## Boundary

```text
Historical Trace
      ↓
    Inspect
      ↓
HISTORICAL_ONLY
      │
      └── explicit promotion → PROMOTED → Active Context
```

## Safety

A trace containing a previous authorization or simulated action does not carry forward authorization into a new session.

Historical execution evidence can inform future reasoning only after a separate governed promotion decision.
