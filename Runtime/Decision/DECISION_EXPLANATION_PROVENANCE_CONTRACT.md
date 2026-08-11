# Decision Explanation & Provenance Contract

## Purpose

Provide a readable reconstruction of a recorded decision without silently reassessing it under current rules.

## Required Provenance Chain

```text
Context
  ↓
Evidence
  ↓
Ruleset
  ↓
Decision
  ↓
Authorization
  ↓
Execution Trace
```

## Explanation Mode

The prototype uses `RECORDED_PROVENANCE`.

It reports what was recorded and how the decision path is identified. It does not invent missing reasoning or infer undocumented facts.

## Boundary

A provenance explanation is not:

- proof that the decision was correct;
- a new decision;
- a current-rule reassessment;
- authorization to execute;
- permission to repair missing records silently.

## Integrity Rule

`is_reassessment` must remain `false` for a recorded-provenance explanation.

Current-rule evaluation belongs to the explicit temporal reassessment path.

## Missing Evidence

If future integrations discover missing provenance, the explanation layer should report the gap rather than silently filling it from current Context.
