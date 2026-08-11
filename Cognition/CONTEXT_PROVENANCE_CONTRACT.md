# Cognition Context Provenance Contract

## Purpose

Define what Cognition receives when current facts and historical evidence are combined.

## Required Separation

```text
CURRENT FACTS
    ↓
Current Context

HISTORICAL EVIDENCE
    ↓
Historical Context
    ↓
Explicit provenance
```

Historical evidence must remain identifiable as historical. Retrieval does not make it current.

## Rules

1. Cognition receives provenance with historical evidence.
2. Historical evidence cannot silently become an active fact.
3. Missing history remains empty; it is never inferred.
4. Promotion is outside the basic loader and requires a governed process.

## Safety Boundary

This loader prepares context for reasoning. It does not make decisions, grant authorization, or execute actions.
