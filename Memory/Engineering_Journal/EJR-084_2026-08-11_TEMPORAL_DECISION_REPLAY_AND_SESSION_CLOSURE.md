# EJR-084 — TEMPORAL DECISION REPLAY AND SESSION CLOSURE

Date: 2026-08-11
Session Type: Decision / Time / Replay / Reassessment / Closure
Status: CLOSED CHECKPOINT

## Objective

Separate reconstruction of a historical decision from evaluation of the same evidence under a newer ruleset.

## Work Completed

- Added `Runtime/Decision/decision_temporal_replay.py`.
- Added `Runtime/Decision/test_decision_temporal_replay.py`.
- Added `Runtime/Decision/DECISION_TEMPORAL_REPLAY_CONTRACT.md`.

## Verified Cases

### Same evidence + same ruleset

Result: `HISTORICAL_REPLAY` / `SAME_DECISION_BASIS`.

### Same evidence + changed ruleset

Result: `CURRENT_RULE_REASSESSMENT` / `RULESET_CHANGED`.

This is explicitly treated as a new assessment, not a reconstruction of the old decision.

### Changed evidence

Result: `RECONSTRUCTION_BLOCKED` / `EVIDENCE_CHANGED`.

The prototype refuses to call this an exact historical replay.

## Architectural Result

ARGO now has an explicit temporal distinction:

```text
Past Decision
     ↓
Historical Replay
     │
     └── same evidence + same rules

Past Evidence
     ↓
Current Rules
     ↓
Current Reassessment
```

This prevents current knowledge or rules from silently rewriting historical decisions.

## Closure

Temporal replay boundary implemented and negatively tested. Session closed at EJR-084.
