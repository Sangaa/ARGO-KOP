# ARCHITECTURE MAP

---

Document ID
ARC-001

Version
1.2.0

Status
Validated / Integrity Hold
Category
Architecture
Owner
ARGO Foundation
Repository Development Baseline
3.2.1
Latest Official Release
1.0.0
Last Audit
2026-08-08

---

# Purpose

Defines the current logical architecture of ARGO KOP and its dependency boundaries.

This document is an architectural authority for structure and dependency semantics only. It does not override the Constitution, Governance, Repository Index, or Release authority.

# Design Principles

1. Separation of Concerns.
2. Single Source of Truth.
3. Layered responsibility and explicit dependency direction.
4. Repository Reality First.
5. No Reverse Dependency without governed architectural authorization.
6. Physical folder placement does not create architectural authority.

# Canonical Architectural Layers

1. Identity / Core
2. Governance
3. Architecture
4. Repository
5. Knowledge / Specifications / Standards
6. Memory
7. Cognition / Engine
8. Runtime / Services / AI
9. Projects / Applied Artifacts

`Archive` is a repository preservation domain, not an active dependency layer.

`Standards`, `Specifications`, `Models`, `Engine`, `Services`, and `AI` are domains/groupings unless an explicit architectural decision establishes a distinct layer.

# Dependency Direction

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

Reverse dependency is prohibited unless explicitly authorized by a governed architectural decision.

# Canonicality Rule

A document is architecturally canonical only when:

- its current repository path is verified;
- its filename and internal identity agree where an ID is assigned;
- its authority is established by the applicable repository/governance rules;
- its version is compatible with the active development baseline;
- its required references resolve or are explicitly recorded as unresolved.

A status file alone cannot create architectural authority.

# Change Rule

Any material change to layer boundaries, dependency direction, ownership or canonical architectural relationships requires architectural review and synchronized repository/index updates.

# Integrity State

Architecture remains **INTEGRITY HOLD** until component maps, folder status, dependency references and cross-layer identity validation are completed.

# Related Authority

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Release/VERSION.md`

---

End of Document
