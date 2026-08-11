# Context Conflict Handling Contract

## Purpose

Detect disagreement between current facts and historical evidence without silently resolving the disagreement.

## Rule

Detection is not resolution.

When a contradiction is detected, Cognition must emit a reasoning requirement rather than selecting a winner automatically.

```text
Current Fact
     +
Historical Evidence
     ↓
Conflict Detection
     ↓
REQUIRES_REASONING
     ↓
Reasoning / Evidence Validation
```

## Safety

The detector does not promote history, change facts, make decisions, authorize actions, or execute anything.

## Important Limitation

The current detector uses exact claim matching as a minimal synthetic mechanism. It is an integration contract, not a semantic contradiction engine.
