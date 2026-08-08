# ARC-006

---

# DEPENDENCY MODEL

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

ARC-006

Version

1.2.0

Status

Validated / Integrity Hold

Category

Architecture

Development Baseline

3.2.1

Latest Official Release

1.0.0

Last Audit

2026-08-08

---

# Purpose

This document defines the dependency model of ARGO KOP and is aligned with `Architecture/ARC_MAP.md` and `Architecture/ARC-004_LAYER_MODEL.md`.

It governs dependency direction, not physical folder layout.

---

# Canonical Dependency Direction

Identity / Core

↓

Governance

↓

Architecture

↓

Repository

↓

Knowledge / Specifications / Standards

↓

Memory

↓

Cognition / Engine

↓

Runtime / Services / AI

↓

Projects / Applied Artifacts

Dependencies must not reverse this direction unless explicitly approved by an architectural decision.

---

# Allowed Dependencies

## Core

Depends on: None.

## Governance

May depend on: Core.

## Architecture

May depend on: Core, Governance.

## Repository

May depend on: Core, Governance, Architecture.

## Knowledge / Specifications / Standards

May depend on: Repository, Architecture, applicable Governance rules.

## Memory

May depend on: Knowledge, Repository, applicable Governance rules.

## Cognition / Engine

May depend on: Knowledge, Memory, Repository, Architecture interfaces.

## Runtime / Services / AI

May depend on: Core, Repository, Memory, Cognition / Engine, and approved service interfaces.

## Projects / Applied Artifacts

May depend on approved platform capabilities and documented interfaces. Projects MUST NOT redefine platform architecture or governance.

---

# Dependency Qualification

Every dependency MUST be:

- Necessary
- Explicitly documented
- Traceable to a current repository artifact or interface
- Owned
- Architecturally justified
- Free of circular dependency

A reference to a file path alone does not prove an architectural dependency.

---

# Prohibited Dependencies

The following are prohibited:

- Lower layers rewriting higher-layer authority.
- Projects redefining Core, Governance, or Architecture.
- Repository artifacts silently overriding Governance or Constitution.
- Memory rewriting Architecture without a governed decision.
- Undocumented cross-component dependencies.
- Circular dependencies.
- Using folder placement as implicit authority.

---

# Repository Principle

The repository is the canonical storage source. Repository documents may reference one another, but references MUST respect architectural ownership and authority boundaries.

---

# Validation

A new dependency requires review of:

1. Layer Direction
2. Ownership
3. Traceability
4. Canonicality of referenced artifact
5. Circularity
6. Compatibility with `ARC-004_LAYER_MODEL.md`
7. Compatibility with `ARC_MAP.md`

---

# Related Documents

- `Architecture/ARC_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

---

# Guiding Statement

Explicit, traceable dependencies produce stable architecture.

---

End of Document
