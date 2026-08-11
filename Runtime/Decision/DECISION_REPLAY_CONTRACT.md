# Decision Replay Contract

## Purpose

Provide a deterministic integrity check for reconstructing a previously governed decision from its recorded evidence, ruleset, authorization state, and execution mode.

## Replay Inputs

```text
Evidence IDs
Ruleset ID
Proposal
Authorization
Execution Result
```

## Replay Principle

Replay does not invent a new decision and does not execute anything. It checks whether the recorded decision path is internally consistent with the supplied reconstruction inputs.

## Match Conditions

A replay is `REPLAY_MATCH` only when:

1. the evidence set is identical;
2. the proposal references the same ruleset;
3. authorization remains `AUTHORIZED`;
4. execution mode is `SIMULATED_ONLY` for this prototype.

Otherwise the replay is `REPLAY_MISMATCH` and reports the broken invariant.

## Failure Codes

- `EVIDENCE_SET_MISMATCH`
- `RULESET_MISMATCH`
- `AUTHORIZATION_MISMATCH`
- `EXECUTION_MODE_MISMATCH`

## Boundary

Replay validates integrity and provenance. It does not establish truth, replace Cognition, grant authority, or perform real-world execution.
