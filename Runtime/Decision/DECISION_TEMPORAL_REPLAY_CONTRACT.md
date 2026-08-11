# Decision Temporal Replay Contract

## Purpose

Prevent historical decision reconstruction from being silently mixed with reassessment under newer rules.

## Modes

### HISTORICAL_REPLAY

Used when the recorded evidence set and recorded ruleset are unchanged.

Purpose: reconstruct the decision basis as it existed at the time.

### CURRENT_RULE_REASSESSMENT

Used when the evidence is unchanged but the current ruleset differs from the recorded ruleset.

Purpose: explicitly evaluate the old evidence under current rules. This is a new assessment, not a replay of the historical decision.

### RECONSTRUCTION_BLOCKED

Used when the evidence set has changed.

The system must not claim to have reconstructed the historical decision because its evidence basis is no longer identical.

## Invariant

```text
Historical Replay ≠ Current Reassessment
```

A changed ruleset must never overwrite the historical basis.

A changed evidence set must never be presented as an exact replay.

## Boundary

This mechanism compares decision inputs. It does not determine whether a historical or current decision is correct.
