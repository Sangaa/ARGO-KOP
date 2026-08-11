# Evidence → Decision → Execution Continuity Contract

## Purpose

Ensure that evidence used by a governed proposal remains traceable through authorization and execution.

## Required Chain

```text
Historical Evidence
      ↓
Proposal
      ↓
Authorization
      ↓
Execution
```

The trace identity must survive each boundary.

## Invariants

1. Every evidence trace used by the proposal remains identifiable.
2. Evidence may not silently disappear between Context and Decision.
3. Authorization remains a separate authority boundary.
4. `SIMULATED_ONLY` must remain `side_effect=false`.
5. A simulated execution must identify the evidence trace that informed the proposal.
6. Continuity validation reports a broken chain rather than repairing it silently.

## Failure Codes

- `EVIDENCE_DROPPED_BEFORE_DECISION`
- `AUTHORIZATION_NOT_CONFIRMED`
- `SIMULATION_SIDE_EFFECT_CONFLICT`
- `EXECUTION_PROVENANCE_BROKEN`

## Non-Goals

This contract does not determine whether evidence is true, relevant, or sufficient. Those are Cognition/Decision responsibilities. It only verifies that provenance is not lost after selection.
