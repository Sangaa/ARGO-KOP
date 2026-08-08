# ARC-005

---

# ARCHITECTURE RULES

---

Platform

ARGO KOP (Knowledge Operating Platform)

Document ID

ARC-005

Version

1.2.0

Status

Validated / Integrity Hold

Category

Architecture

Repository Development Baseline

3.2.1

Latest Official Release

1.0.0

Last Audit

2026-08-08

---

# Purpose

This document defines architectural control rules for the design, evolution and maintenance of ARGO KOP.

These rules govern architectural relationships without pretending that every historical rule remains permanently correct. Existing rules remain reviewable when current evidence shows a simpler, safer or more accurate control.

# Rules

## Rule 1 — Architecture and Implementation

Architecture defines intended structure and boundaries. Implementation must conform to governed architecture, but implementation evidence may reveal that the architecture itself requires review.

An implementation finding does not silently redefine architecture; it triggers architectural review when the boundary or dependency model is materially affected.

## Rule 2 — Repository Reality

The current repository is the authoritative engineering source for current repository state, subject to higher Constitution, Governance and applicable Release authority.

Conversation memory, historical ZIPs and generated summaries do not override current repository evidence.

## Rule 3 — Ownership and Identity

Every active canonical logical identity must have one clearly established owner and one canonical active path.

Historical, archived and legacy artifacts may preserve older identities when required for traceability, but must not silently compete with active authority.

## Rule 4 — Physical Placement

A physical folder does not by itself establish architectural ownership, authority or layer membership.

Placement must be interpreted together with filename, internal identity, content, references, indexes, governance and dependency relationships.

## Rule 5 — Dependency Direction

Canonical architectural dependencies follow the active Architecture Model and must not introduce reverse dependencies without governed authorization.

A dependency is not valid merely because a path is named; its target, authority, relationship and affected consumers must be verified.

## Rule 6 — Responsibility Boundaries

Each logical component should have a primary responsibility and explicit interfaces, but legitimate cross-domain collaboration is allowed when ownership and dependency semantics remain clear.

Responsibility overlap is a finding requiring review, not an automatic deletion rule.

## Rule 7 — Knowledge Duplication

Avoid unnecessary duplication of authoritative knowledge.

When duplication is required for usability, preserve provenance and identify the authoritative source rather than silently creating competing truth.

## Rule 8 — Architectural Decisions

Material architectural decisions must be documented with reason, evidence, impact, authority and traceability.

A historical decision remains evidence of what was decided at the time; it does not automatically override newer governed decisions.

## Rule 9 — Architectural Modification

Material architectural changes must preserve, or explicitly migrate:

- Repository Integrity
- Traceability
- Version History
- Authority Boundaries
- Affected Dependency Contracts

Post-change re-read and relationship validation are mandatory for affected artifacts.

## Rule 10 — Deletion and Archival

Deletion is not prohibited in every circumstance, but irreversible deletion must not be used to erase historical evidence or bypass migration traceability.

Archive, deprecation or controlled removal should be preferred when historical continuity or recovery matters.

## Rule 11 — Controlled Evolution

Architecture evolves through evidence-backed review.

Structural modifications require architectural review when they affect layer boundaries, dependency direction, ownership, canonical identity or cross-layer contracts.

## Rule 12 — Review Evidence

Every significant architectural review should identify:

- Inspection Scope
- Repository Coverage
- Evidence State
- Confidence / Limitations
- Assessment Type
- Repository Version / Commit
- Affected Relationships
- Post-Change Validation

## Rule 13 — Folder Governance

Major repository folders should maintain an evidence-backed status artifact when the repository structure requires one.

A `_FOLDER_STATUS.md` file is evidence about reviewed scope; it is not proof of completeness by itself.

## Rule 14 — Technology Independence

Platform architecture should remain technology-independent unless a technology is explicitly elevated by a governed architectural decision.

## Rule 15 — Architectural Quality

Architectural artifacts should be understandable, traceable, reviewable, maintainable and version controlled.

## Rule 16 — Evidence Before Normalization

Do not rename, move, merge, duplicate, archive or promote an artifact solely because its filename sequence or folder placement appears inconsistent.

Inspect content, identity, authority and relationships first.

## Rule 17 — Reopen on New Evidence

A previously reviewed architectural domain may be reopened when new repository evidence changes the interpretation of its identity, authority, dependency or status.

---

# Related Documents

- `Core/CORE-003_CONSTITUTION.md`
- `Core/CORE-011_PLATFORM_CHARTER.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

---

# Integrity State

This document is aligned to the current audit model, but Architecture remains under consolidated validation until the active architectural inventory and cross-layer relationships are verified.

---

# Guiding Statement

**Architecture governs structural intent; evidence, governance and review govern how that intent evolves.**

---

End of Document
