# ARCHITECTURE MAP

---

Platform
ARGO KOP (Knowledge Operating Platform)

Artifact Type
Architecture Map / Navigation Artifact

Version
1.3.2

Status
Validated / Integrity Hold

Category
Architecture / Repository Navigation

Canonical
Yes — as the Architecture Map artifact

Repository Development Baseline
3.2.1

Latest Official Release
1.0.0

Last Audit
2026-08-13

---

# Identity Boundary

This file is a **map artifact**, not `ARC-001`.

`ARC-001` is reserved for `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`.

The map intentionally has no numeric `ARC-NNN` Document ID so that it cannot create a duplicate architectural identity with the canonical platform architecture document.

# Purpose

Defines the current logical architecture of ARGO KOP and its dependency boundaries.

This map is an architectural navigation and relationship artifact. It does not override the Constitution, Governance, Repository Index, or Release authority.

# Design Principles

1. Separation of Concerns.
2. Single Source of Truth.
3. Layered responsibility and explicit dependency direction.
4. Repository Reality First.
5. No Reverse Dependency without governed architectural authorization.
6. Physical folder placement does not create architectural authority.
7. A map describes relationships; it does not create authority merely by listing a node.
8. Legacy draft content does not become canonical merely because it occupies a mapped domain.
9. Rebuilt domains must be connected to the canonical model only after their current content and relationships are validated.

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

`Standards`, `Specifications`, `Models`, `Engine`, `Services`, and `AI` are domains/groupings unless an explicit architectural decision establishes a distinct architectural layer.

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

A status file or map alone cannot create architectural authority.

# Legacy / Reconstruction Rule

Existing draft, primitive, incomplete or historically speculative domain files may be retained for provenance but MUST NOT be treated as authoritative merely because they exist.

When a domain is rebuilt after the foundation is stable, the preferred process is:

**Read Existing Material → Extract Useful Evidence → Classify Facts / Assumptions / Draft Ideas → Discard Invalid Structure → Rebuild Canonical Content → Validate Identity / Authority / Relationships → Connect to Active Map**

Rewriting from first principles is permitted and preferred when the previous domain was an early sketch whose structure no longer reflects current ARGO knowledge.

The original material must remain recoverable through governed Archive/history when it has migration value.

# Change Rule

Any material change to layer boundaries, dependency direction, ownership or canonical architectural relationships requires architectural review and synchronized repository/index updates.

# Integrity State

Architecture remains **INTEGRITY HOLD** until active architectural artifacts, folder status, dependency references and cross-layer identity validation are completed.

---

# Related Authority

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Release/VERSION.md`

---

End of Document
