# Traceable Reasoning Contract

## Purpose

Turn a classified cognition packet into a traceable analysis object without crossing into decision or execution authority.

## Input

- Facts
- Assumptions
- Known Knowledge references
- Unresolved Questions

## Processing

The reasoning pass preserves the original categories and creates an evidence map showing whether each item comes from runtime context or a promoted knowledge record.

## Output

```text
REASONED
 ├── observations
 ├── evidence_map
 ├── decision_status = NOT_EVALUATED
 └── execution_status = NOT_REQUESTED
```

## Governance Boundary

Reasoning may organize, connect and explain available evidence. It must not silently convert an assumption into a fact, a knowledge reference into a new fact, or an analysis into an authorized action.

## Fail-Closed Rule

Incomplete classified input produces `HOLD`.
