# ARCHITECTURAL LAWS

Document ID
CORE-008
Version
1.2.0
Status
Validated / Integrity Hold
Category
Core
Canonical
Yes
Last Audit
2026-08-08

---

# Laws

## LAW 01 — Single Responsibility

Every component has one primary responsibility.

## LAW 02 — Knowledge Integrity

Canonical knowledge has one authoritative source. Derived representations must remain traceable to that source.

## LAW 03 — Source Traceability

Everything persisted as knowledge or a decision references its source or supporting evidence where applicable.

## LAW 04 — Governed Dependencies

Dependencies follow the approved Architecture and dependency model. Numeric naming alone does not establish dependency authority.

## LAW 05 — Architecture Governs Implementation

Implementation conforms to Canonical Architecture.

## LAW 06 — Implementation Cannot Silently Change Architecture

An implementation change that materially affects architecture requires the applicable architectural review and governed update.

## LAW 07 — Ownership

Every canonical artifact has identifiable ownership and authority.

## LAW 08 — History Preservation

Material engineering history and decisions remain traceable and recoverable according to repository policy.

## LAW 09 — Architectural Review

Major architectural changes require architectural review before becoming canonical.

## LAW 10 — Documentation

Canonical behavior and material decisions are documented sufficiently for human review and machine interpretation.

## LAW 11 — Validation Gate

A change must be validated against applicable Governance, Architecture and Repository constraints before it becomes accepted state.

## LAW 12 — Authority Boundary

Lower layers and implementation mechanisms cannot silently override higher-authority Constitution, Governance or Canonical Architecture.

---

# Enforcement

These laws are architectural constraints. Runtime execution and repository operations enforce them through applicable validation gates.

---

End of Document
