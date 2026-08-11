# DM-004 — DECISION TRACEABILITY AND CONSUMER LINKS

Version: 1.0.0
Status: 🟡 BUILD-01 / INTEGRITY HOLD

## Purpose

Ensure decisions remain connected to the artifacts and outcomes they influence.

## Traceability Chain

```text
Evidence / Context
      ↓
Decision
      ↓
Implementation / Action
      ↓
Observed Outcome
      ↓
Validation
      ↓
Revision / Reuse
```

## Consumer Links

A decision may be consumed by Governance, Architecture, Runtime, Projects, Memory, Knowledge or operational workflows. A consumer reference does not automatically make the decision authoritative for that domain.

## Impact Discipline

When a decision changes materially, affected consumers should be identified and reviewed. If a consumer depends on an obsolete decision, the relationship must be repaired or explicitly marked unresolved.

## Relationship Integrity

Decision relationships should identify at minimum:

- source decision;
- target artifact or consumer;
- relationship type;
- scope;
- evidence;
- validation state;
- whether the relationship is active, superseded or unresolved.

## Boundary

This artifact defines traceability expectations for Decision Memory. Cross-registry relationships remain subject to REP-014 and broader Control Plane reconciliation.

---

End of DM-004
