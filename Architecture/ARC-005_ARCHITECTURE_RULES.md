# ARC-005

---

# ARCHITECTURE RULES

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

ARC-005

Version

1.0.0

Status

Approved

Category

Architecture

---

# Purpose

This document defines the mandatory architectural rules that govern the design, evolution, and maintenance of the ARGO KOP platform.

These rules ensure consistency, maintainability, traceability, and long-term architectural integrity.

Every component, document, service, and future extension shall comply with these rules.

---

# Architectural Laws

## Law 1 — Architecture Before Implementation

Architecture shall always be defined before implementation begins.

No implementation shall establish architecture.

Architecture guides implementation.

---

## Law 2 — Single Responsibility

Every architectural component shall have one primary responsibility.

Multiple unrelated responsibilities shall never be assigned to the same component.

---

## Law 3 — Clear Ownership

Every document belongs to one primary component.

Every component owns its knowledge.

Ownership shall always be explicit.

---

## Law 4 — No Duplicate Knowledge

Knowledge shall exist only once.

If the same information is required elsewhere, it shall be referenced rather than duplicated.

The repository is the single source of truth.

---

## Law 5 — Traceability

Every important architectural decision shall be traceable.

The following shall be identifiable:

• Decision

• Reason

• Author

• Date

• Related Components

• Impact

---

## Law 6 — Controlled Dependencies

Dependencies shall always be intentional.

Every dependency shall be:

Documented

Understandable

Necessary

Maintainable

Circular dependencies are prohibited.

---

## Law 7 — Layer Integrity

Architectural layers shall never be bypassed.

Communication between layers shall occur only through documented interfaces.

---

## Law 8 — Simplicity

Architectural complexity shall never be introduced without measurable value.

Whenever two solutions exist, the simpler architecture shall be preferred unless a more complex solution provides significant long-term benefits.

---

## Law 9 — Technology Independence

Architecture shall describe concepts rather than implementations.

Technologies may change.

Architecture shall remain stable.

---

## Law 10 — Evolution Without Disruption

Platform evolution shall extend the architecture rather than replace it.

Existing structures shall remain valid whenever possible.

Breaking changes require formal architectural review.

---

# Architectural Constraints

The platform shall avoid:

Duplicated responsibilities

Hidden dependencies

Undocumented interfaces

Repository fragmentation

Technology lock-in

Temporary architectural shortcuts

---

# Architecture Review

Every significant architectural modification shall answer the following questions:

Why is the change required?

Which components are affected?

Which documents must be updated?

Will existing repositories remain compatible?

Can the change be traced in the future?

---

# Exception Policy

Exceptions are permitted only when:

The architectural benefit is clearly documented.

The impact is understood.

The change has been reviewed.

The exception itself becomes part of the architectural history.

---

# Compliance

Every repository component shall comply with these rules.

Non-compliance shall be treated as an architectural issue requiring review.

---

# Success Criteria

Architecture is considered healthy when:

Responsibilities remain clear.

Dependencies remain controlled.

Knowledge remains organized.

Repository evolution remains predictable.

Platform identity remains preserved.

---

# Related Documents

ARC-001_PLATFORM_ARCHITECTURE

ARC-004_LAYER_MODEL

ARC-006_DEPENDENCY_MODEL

ARC-009_ARCHITECTURE_DECISIONS

GOV-001_DOCUMENT_STANDARD

GOV-010_GOVERNANCE_MODEL

---

# Guiding Statement

Architecture is not documentation.

Architecture is discipline.

---

End of Document
