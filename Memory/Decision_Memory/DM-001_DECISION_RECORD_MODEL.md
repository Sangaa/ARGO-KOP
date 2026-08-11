# DM-001 — DECISION RECORD MODEL

Version: 1.0.0
Status: 🟡 BUILD-01 / INTEGRITY HOLD

## Purpose

Define the canonical structure for a Decision Memory record without creating governance authority by itself.

## Required Fields

| Field | Requirement |
|---|---|
| Decision ID | Unique and stable |
| Decision | Exact decision statement |
| Context | Situation in which the decision was made |
| Scope | Systems, files, domains or time boundaries affected |
| Facts | Evidence-backed facts available at decision time |
| Assumptions | Explicit non-verified assumptions |
| Alternatives | Material alternatives considered |
| Rationale | Reason the selected option was preferred |
| Consequences | Expected and observed consequences |
| Dependencies | Conditions or artifacts the decision depends on |
| Evidence | Sources supporting the decision |
| Validation | Evidence that tests the decision after execution |
| Review Trigger | Conditions requiring reassessment |
| Status | Candidate / Accepted / Validated / Superseded / Retired |
| Provenance | Source, authoring context and traceability |

## Decision Discipline

A decision must not silently convert an assumption into a fact. If later evidence contradicts the decision, the record is updated through a traceable revision or a superseding decision rather than silently rewritten.

## Relationship Expectations

Decision records may link to:

- Engineering Journal events
- Governance rules
- Architecture decisions
- Memory artifacts
- Project artifacts
- Evidence records
- Superseding decisions

## Boundary

This model defines record structure. It does not authorize mutation of protected repository layers.

---

End of DM-001
