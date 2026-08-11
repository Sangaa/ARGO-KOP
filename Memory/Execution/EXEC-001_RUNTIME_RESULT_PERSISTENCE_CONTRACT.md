# EXEC-001 — Runtime Result Persistence Contract

## Purpose

Define how an execution result becomes reusable cross-session evidence without turning the experimental runtime into an uncontrolled memory writer.

## Persistence Boundary

```text
Runtime Result
     ↓
Normalize Trace
     ↓
Evidence Record
     ↓
Persist
     ↓
Re-read
     ↓
Available for future Context loading
```

## Required Identity

Every persisted execution result must retain, where available:

- task identity;
- session identity;
- project identity;
- execution status;
- authorization identity;
- action/plan identity;
- evidence references;
- timestamp;
- side-effect status;
- source runtime result.

## Prototype Safety Rules

1. The mock executor may produce a persistence candidate but must not silently mutate canonical Memory.
2. Persistence requires an explicit adapter/boundary.
3. `SIMULATED_ONLY` is evidence of a simulation, not evidence that an external action occurred.
4. A persisted result must remain distinguishable from a user fact, decision, or promoted knowledge.
5. Re-reading the persisted artifact is required before it is treated as available cross-session context.

## State Model

```text
SIMULATED_ONLY
      ↓
PERSISTENCE_CANDIDATE
      ↓
PERSISTED
      ↓
RE_READ
      ↓
CONTEXT_ELIGIBLE
```

A failure at persistence or re-read leaves the result non-context-eligible.

## Authority Boundary

This contract governs runtime-result persistence only. It does not promote results into Knowledge, alter Constitution, or grant execution authority.
