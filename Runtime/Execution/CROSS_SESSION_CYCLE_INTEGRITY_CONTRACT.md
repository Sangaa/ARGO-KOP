# CROSS-SESSION CYCLE INTEGRITY CONTRACT

## Purpose

Define the invariants that must remain true when historical evidence from one session is rehydrated into a later session and used in a governed decision path.

## Required Invariants

1. Historical evidence retains its historical role and provenance.
2. Session 1 identity is not confused with Session 2 identity.
3. Historical evidence may inform a proposal but does not grant authorization.
4. Authorization belongs to the current session/decision context.
5. Execution remains bounded by the current execution adapter.
6. `SIMULATED_ONLY` must remain distinguishable from external execution.
7. `side_effect=false` must remain explicit in the prototype.

## Integrity Path

```text
Session 1
   ↓
Runtime Trace
   ↓
Historical Memory
   ↓
Session 2 Selection
   ↓
Historical Evidence
   ↓
Current Proposal
   ↓
Current Authorization
   ↓
Current Plan
   ↓
Simulation Boundary
```

## Failure Conditions

The cycle is invalid if:

- historical evidence is relabeled as a current fact;
- authorization identity is lost before execution;
- execution crosses the simulation boundary;
- an external side effect is represented as simulation;
- session identities are conflated.

## Scope

This is a prototype integrity contract. It does not provide production security, cryptographic provenance, or external authorization enforcement.
