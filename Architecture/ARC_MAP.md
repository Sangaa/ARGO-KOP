# ARCHITECTURE MAP

---

Document ID

ARC-001

Version

1.1.0

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

This document defines the current logical architecture of the ARGO KOP repository and its dependency boundaries.

It is an architectural authority for structure only. It does not override the Constitution, Governance, Repository Index, or release authority.

---

# Design Principles

1. **Separation of Concerns** — each document has one primary responsibility.
2. **Single Source of Truth** — authoritative information has one canonical active location.
3. **Layered Knowledge** — dependencies flow from governing foundations toward implementation and project artifacts.
4. **Repository Reality First** — the map must describe the actual repository, not a historical structure.
5. **No Reverse Dependency** — lower layers must not require higher-layer implementation details.

---

# Current Repository Layers

The repository currently contains more operational layers than the original Foundation architecture. The active baseline is therefore represented as follows:

**Governance**

Defines rules, authority, identity, review, naming, and repository policy.

↓

**Repository / Core**

Defines canonical storage, platform identity, constitution, and foundational constraints.

↓

**Architecture**

Defines structural relationships, component boundaries, and dependency models.

↓

**Standards / Specifications / Models**

Define reusable rules, expected behavior, document models, and structured specifications.

↓

**Engine / Runtime / Services / AI**

Define cognitive processing, runtime behavior, validation, service boundaries, and AI integration.

↓

**Projects / Decision / Knowledge / Docs**

Contain applied work, decisions, reusable knowledge, and explanatory documentation.

↓

**Archive**

Preserves superseded or historical evidence and is not an active dependency layer.

---

# Dependency Rule

The intended dependency direction is:

Governance

↓

Core / Repository

↓

Architecture

↓

Standards / Specifications / Models

↓

Engine / Runtime / Services / AI

↓

Projects / Applied Knowledge

Reverse dependency is forbidden unless explicitly authorized by a higher-level architectural decision.

---

# Canonicality Rule

A document is architecturally canonical only when:

- its path exists in the current repository;
- its filename and internal identity agree where an ID is assigned;
- its canonical status is verified;
- its version is compatible with the active development baseline;
- its references resolve to current repository artifacts.

---

# Integrity State

Architecture has been partially re-aligned with the current repository baseline.

The repository remains under **INTEGRITY HOLD** until the Architecture layer, its folder statuses, component maps, and cross-layer references complete the repository-wide audit.

---

# Related Authority

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Release/VERSION.md`

---

End of Document
