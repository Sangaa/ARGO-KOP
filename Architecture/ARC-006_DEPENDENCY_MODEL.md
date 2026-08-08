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

1.3.0

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

Defines the dependency model of ARGO KOP. It governs logical dependency direction, ownership and qualification rather than physical folder layout.

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

Dependencies must not reverse this direction unless explicitly authorized by a governed architectural decision.

# Allowed Dependencies

## Core

Depends on: None at the architectural layer level.

## Governance

May depend on: Core.

## Architecture

May depend on: Core, Governance.

## Repository

May depend on: Core, Governance, Architecture.

## Knowledge / Specifications / Standards

May depend on: Repository, Architecture and applicable Governance rules.

## Memory

May depend on: Knowledge, Repository and applicable Governance rules.

## Cognition / Engine

May depend on: Knowledge, Memory, Repository and approved Architecture interfaces.

## Runtime / Services / AI

May depend on: approved lower-level platform interfaces and the applicable runtime contracts. AI providers do not acquire platform authority through integration.

## Projects / Applied Artifacts

May depend on approved platform capabilities and documented interfaces. Projects MUST NOT redefine platform architecture or governance.

# Dependency Qualification

Every claimed architectural dependency MUST be:

- necessary;
- explicitly documented;
- traceable to a current canonical artifact or interface;
- owned;
- architecturally justified;
- free of circular dependency;
- compatible with the current layer model.

A textual reference to a file path does not by itself establish an architectural dependency.

# Authority Rule

A dependency does not transfer authority.

A lower layer may consume an approved contract from a higher layer but cannot use that dependency to rewrite or redefine the higher layer.

# Prohibited Dependencies

- Lower layers rewriting higher-layer authority.
- Projects redefining Core, Governance or Architecture.
- Repository artifacts silently overriding Constitution or Governance.
- Memory rewriting Architecture without a governed decision.
- Undocumented cross-component dependencies.
- Circular dependencies.
- Using folder placement as implicit authority.

# Validation

A new or materially changed dependency requires review of:

1. Layer direction.
2. Ownership.
3. Traceability.
4. Canonicality of referenced artifact.
5. Circularity.
6. Compatibility with `ARC-004_LAYER_MODEL.md`.
7. Compatibility with `ARC_MAP.md`.
8. Compatibility with Repository and Governance authority.

Validation failure blocks acceptance until corrected or explicitly dispositioned by the applicable authority.

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
