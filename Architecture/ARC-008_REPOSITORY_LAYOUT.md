# ARC-008

---

# REPOSITORY LAYOUT

---

Platform

ARGO KOP (Knowledge Operating Platform)

Document ID

ARC-008

Version

1.2.0

Status

Validated / Integrity Hold

Category

Architecture / Repository Layout

Repository Development Baseline

3.2.1

Latest Official Release

1.0.0

Last Audit

2026-08-08

---

# Purpose

Defines the architectural principles for physical repository organization without treating physical placement as automatic proof of logical architecture or authority.

# Repository Philosophy

The repository is organized to preserve responsibility, traceability and navigation.

Physical structure supports architecture, but physical folder placement does not by itself create architectural authority.

The repository must therefore be read as a relationship graph as well as a storage tree.

# Canonical Relationship

The active architecture is represented by:

`Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`

and navigated through:

`Architecture/ARC_MAP.md`

Repository storage authority is represented by:

`Repository/REP-001_MASTER_INDEX.md`

`Repository/REP-002_REPOSITORY_MAP.md`

The map/index documents must agree with current repository evidence.

# Repository Structure Model

The current architectural model is:

Core / Identity

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

Other physical domains such as Models, Interfaces, Quality, Intelligence, Decision, Release, Logs, Examples and Future are repository domains/groupings whose architectural role must be established by their contents and relationships rather than by folder name alone.

Archive is a preservation domain and is not an active dependency layer.

# Folder Responsibilities

Folders should have understandable purposes and evidence-backed ownership.

A folder is not required to contain a particular filename pattern merely because another folder does.

Where a `_FOLDER_STATUS.md` exists, it records reviewed scope and known state; it does not create authority or certify uninspected content.

# Document Organization

For artifacts with assigned Document IDs, the expected relationship is:

`Filename Identity ↔ Internal Document ID ↔ Canonical Path ↔ Repository Registration`

Exceptions such as navigation maps or README/status artifacts must be explicitly identifiable as such and must not reuse another document's identity.

# Naming Rules

Assigned canonical documents should follow the applicable Governance naming standard.

Numeric sequence gaps are findings, not permission to invent missing artifacts.

Legacy and historical identities may be preserved when needed for traceability, but they must not silently compete with active canonical identities.

# Repository Integrity

Repository layout integrity requires evidence for:

- identity uniqueness;
- canonical path uniqueness;
- content/placement consistency;
- navigation coverage;
- reference resolution;
- authority alignment;
- status/index consistency;
- preservation of required historical traceability.

A directory listing alone cannot establish these conditions.

# Repository Evolution

The repository may evolve through governed changes, new domains, migrations, archival transitions and capability additions.

When physical layout changes affect architectural boundaries, dependencies, ownership or canonical identity, the change requires architectural review and synchronized index/status updates.

# Repository Validation

Reviews should verify together:

- physical paths;
- filenames;
- internal identities;
- content and purpose;
- ownership and authority;
- indexes and maps;
- cross-references;
- affected consumers and dependencies;
- post-change state.

# Related Documents

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC_MAP.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Core/CORE-003_CONSTITUTION.md`

---

# Integrity State

This layout model is aligned with the current repository-first audit method. The complete repository remains under connected-baseline validation until active domains and their relationships are verified.

---

# Guiding Statement

**The repository is a physical home for ARGO's knowledge; its architecture is established by verified relationships, not by the walls alone.**

---

End of Document
