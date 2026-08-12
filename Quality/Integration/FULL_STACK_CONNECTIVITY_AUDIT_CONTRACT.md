# ARGO-KOP Full-Stack Connectivity Audit Contract

## Purpose

Provide a repository-wide integration audit that asks whether the built system is actually connected from its entry layer through runtime, trace, feedback, and learning boundaries.

## Audit Layers

```text
Repository / Governance
        ↓
Architecture
        ↓
Knowledge
        ↓
Memory / Context
        ↓
Cognition / Reasoning
        ↓
Decision
        ↓
Authorization
        ↓
Runtime / Execution
        ↓
Trace / Outcome
        ↓
Feedback
        ↓
Learning
        ↓
Memory Observation
```

## Evidence Classes

Every discovered component should eventually be classified as:

- `IMPLEMENTED`
- `TESTED`
- `LINKED`
- `RUNTIME_REACHABLE`
- `DOCUMENTED`
- `ORPHAN_CANDIDATE`
- `UNTESTED_CANDIDATE`
- `BROKEN_REFERENCE`

A candidate is not automatically a defect. Architectural review is required.

## Required Questions

1. Does each important layer have a reachable path from an entry point?
2. Does each output have a defined consumer?
3. Are contracts actually consumed by implementations or tests?
4. Are runtime components covered by executable tests?
5. Does the end-to-end path reach Trace, Outcome, Feedback, and Learning boundaries?
6. Which files/components are present but disconnected?
7. Which paths are documented but not executable?
8. Which executable paths are not represented in the architecture documentation?

## PASS Definition

`PASS` requires more than green unit tests. A complete audit has three levels:

```text
TEST PASS
    ↓
INTEGRATION PASS
    ↓
ARCHITECTURAL CONNECTIVITY PASS
```

The final level must be supported by evidence of cross-layer reachability.

## Safety

The audit is read-only. It discovers and reports candidates; it does not delete, promote, authorize, or execute external actions.
