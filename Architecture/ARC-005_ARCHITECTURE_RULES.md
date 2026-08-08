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

1.1.0

Status

Approved

Category

Architecture

---

# Purpose

This document defines the mandatory architectural rules governing the design, evolution and maintenance of ARGO KOP.

These rules ensure consistency across the entire platform.

---

# Rule 1

Architecture precedes implementation.

Implementation shall never redefine architecture.

---

# Rule 2

The Repository is the Single Source of Truth.

Conversation memory shall never override repository content.

---

# Rule 3

Every document shall have one primary owner.

Duplicate ownership is prohibited.

---

# Rule 4

Every document shall belong to exactly one architectural component.

Cross references are allowed.

Duplicate documents are prohibited.

---

# Rule 5

Dependencies shall always point downward.

Higher layers never depend on lower implementation details.

---

# Rule 6

Each architectural component shall have one clearly defined responsibility.

Responsibility overlap is prohibited.

---

# Rule 7

Knowledge duplication is prohibited.

Reference.

Do not copy.

---

# Rule 8

Every architectural decision shall be documented.

Undocumented architectural decisions are invalid.

---

# Rule 9

Every architectural modification shall preserve:

- Repository Integrity
- Knowledge Integrity
- Traceability
- Version History

---

# Rule 10

Deletion is prohibited.

Archive replaces deletion.

Repository history shall remain recoverable.

---

# Rule 11

Architecture evolves through controlled change.

Structural modifications require architectural review before implementation.

---

# Rule 12

Every repository review shall include:

- Inspection Scope
- Repository Coverage
- Confidence Level
- Assessment Type
- Repository Version

---

# Rule 13

Folder governance is mandatory.

Each major repository folder shall maintain:

_FOLDER_STATUS.md

containing:

- Review Status
- Current Version
- Outstanding Work
- Next Action
- Folder Approval

---

# Rule 14

Platform knowledge shall remain technology independent.

Technologies may change.

Architecture remains stable.

---

# Rule 15

Every architectural artifact shall be:

- Understandable
- Traceable
- Reviewable
- Maintainable
- Version Controlled

---

# Related Documents

CORE-003_CONSTITUTION

CORE-011_PLATFORM_CHARTER

GOV-006_REVIEW_STANDARD

GOV-009_REPOSITORY_POLICY

GOV-010_GOVERNANCE_MODEL

ARC-001_PLATFORM_ARCHITECTURE

ARC-002_COMPONENT_ARCHITECTURE

ARC-004_LAYER_MODEL

---

# Guiding Statement

Architecture governs change.

Governance protects architecture.

Repository preserves both.

---

End of Document