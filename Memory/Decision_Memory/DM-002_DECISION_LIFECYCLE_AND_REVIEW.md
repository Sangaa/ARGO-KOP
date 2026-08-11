# DM-002 — DECISION LIFECYCLE AND REVIEW

Version: 1.0.0
Status: 🟡 BUILD-01 / INTEGRITY HOLD

## Lifecycle

Decision Memory follows a controlled lifecycle:

```text
Candidate
  ↓
Reviewed
  ↓
Accepted
  ↓
Executed / Observed
  ↓
Validated
  ↓
Maintained
  ├── Superseded
  └── Retired
```

## Review Principle

A decision remains valid only within its evidence, scope and assumptions. New evidence may trigger review even when the original decision was reasonable when made.

## Review Triggers

Examples include:

- contradictory evidence;
- changed repository architecture;
- changed governance constraints;
- failed expected outcome;
- changed scope or dependency;
- discovery of a material omitted alternative;
- repeated operational exceptions.

## Supersession

When a decision is replaced, the original record remains preserved. The new decision explicitly references the superseded decision and records why the replacement became necessary.

## Validation

Validation must distinguish:

- decision was implemented;
- decision produced the expected result;
- result was caused by the decision;
- result remains valid under current conditions.

These are separate claims and should not be collapsed into one status.

## Governance Boundary

Decision review cannot bypass higher-authority governance or architecture controls. Decision Memory is evidence-bearing memory, not an authority escalation mechanism.

---

End of DM-002
