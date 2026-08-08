# REP-003

---

# REPOSITORY STANDARDS

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

REP-003

Version

1.2.0

Status

Approved / Revalidated

Category

Repository

Canonical

Yes

Last Audit

2026-08-08

---

# Purpose

This document defines the mandatory standards governing every artifact stored inside the ARGO KOP repository.

These standards ensure repository consistency, maintainability, traceability and long-term scalability.

---

# Objectives

Repository Standards shall:

- Standardize repository structure.
- Standardize document quality.
- Eliminate ambiguity.
- Preserve evidence boundaries.
- Improve navigation.
- Preserve repository integrity.
- Prevent architecture from being inferred from incomplete evidence.

---

# Repository Principles

The repository is the Single Source of Truth.

Repository content has priority over conversation memory.

Architecture governs organization.

Governance governs standards.

Knowledge remains reusable.

Current repository evidence outranks historical copies, session memory, model confidence and undocumented assumptions.

---

# Evidence-First Verification Standard

A repository artifact or relationship shall not be considered verified merely because:

- its filename appears in an index;
- a folder is expected to contain it;
- another document references it;
- a previous session reported it;
- a model remembers it;
- a similarly named artifact exists elsewhere.

Verification follows this minimum chain:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read**

Where practical, critical relationships shall be checked in both directions.

If any required evidence is unavailable, the result is **UNRESOLVED**, not PASS.

An equivalent document elsewhere may not silently replace a missing canonical artifact. Replacement requires content, authority, ownership and relationship analysis.

---

# Evidence States

Repository review shall distinguish at minimum:

- VERIFIED — directly supported by inspected current repository evidence.
- PARTIAL — only part of the required evidence was inspected.
- INFERRED — interpretation derived from available evidence but not directly established.
- UNRESOLVED — required evidence is missing, inaccessible or contradictory.
- CONFLICT — multiple verified artifacts or relationships materially disagree.
- BLOCKED — work cannot safely proceed without resolving an evidence or authority gap.

A status document must not promote PARTIAL, INFERRED or UNRESOLVED evidence to VERIFIED without new evidence.

---

# Mandatory Document Structure

Every repository document shall include, as applicable:

Document Title

Platform

Document ID

Version

Status

Category

Purpose

Content

Related Documents

Guiding Statement

---

# Naming Standard

Every canonical document shall follow:

PREFIX-NNN_NAME.md

Examples

CORE-001_ARGO_MANIFEST.md

ARC-006_DEPENDENCY_MODEL.md

REP-003_REPOSITORY_STANDARDS.md

Supporting files such as `README.md` and `_FOLDER_STATUS.md` are governed by their folder-level role and are not evidence of canonical artifact existence by filename alone.

---

# Ownership Standard

Every canonical document shall have:

One Owner

One Folder

One Canonical Version

Duplicate ownership is prohibited.

Physical location alone does not establish logical ownership.

---

# Repository Organization

Repository organization follows responsibility.

Technology shall never determine repository structure.

A folder shall not be treated as a complete logical layer until its relevant contents, identities and relationships have been inspected.

---

# Repository Integrity

Repository integrity requires:

No unintended Duplicate Documents

No Duplicate Ownership

No Hidden Components

No Undefined Critical Dependencies

No Unresolved Critical References

No Unexplained Orphan Documents

No Stale or Over-Claiming Status Declarations

No Unbounded Global Completion Claims

---

# Version Control

Every repository modification shall:

- Increment Version when appropriate.
- Preserve Traceability.
- Record Architectural Impact when material.
- Update Related Documents when required.
- Re-read every mutated artifact.
- Revalidate affected references, consumers, indexes and status entries.
- Update Folder Status only to the evidence-supported state.

A successful write operation proves only that the requested mutation was accepted; it does not prove surrounding repository integrity.

---

# Review Standard

Every repository review shall verify, within its declared scope:

Repository Structure

Navigation

Ownership

Dependencies

Naming

Version Alignment

Folder Status

Canonical References

Evidence Coverage

Cross-Layer Relationships

Conflict Propagation

Post-Mutation Consistency

The scope of a PASS must always be stated. A local PASS shall never be promoted automatically to repository-wide PASS.

---

# Folder Standard

Every major folder should contain:

README.md

_FOLDER_STATUS.md

The Folder Status document records:

Current State

Evidence Coverage

Completed Reviews

Outstanding Work

Known Conflicts

Approval Status

Next Actions

A Folder Status document is a status record, not proof of the existence or integrity of the files it lists.

If the folder contents change materially, its status must be revalidated.

---

# Canonical Reference Standard

A reference is not a validated dependency until its target has been:

1. Located.
2. Read.
3. Identity-checked.
4. Authority-checked.
5. Relationship-validated.
6. Checked for downstream consumer impact where material.

Broken, stale, ambiguous or conflicting references shall remain explicitly marked until resolved.

---

# Repository Lifecycle

Create

↓

Review

↓

Verify

↓

Approve

↓

Release

↓

Maintain

↓

Revalidate

↓

Archive

Deletion is prohibited.

Archive replaces deletion.

---

# Review Reopening Rule

A previously reviewed domain may be reopened whenever new evidence changes the interpretation of its identity, ownership, dependency, authority, status or cross-layer relationship.

Review completion is therefore evidence-bounded, not permanently sacred.

---

# Related Documents

CORE-003_CONSTITUTION

GOV-003_NAMING_STANDARD

GOV-006_REVIEW_STANDARD

GOV-009_REPOSITORY_POLICY

ARC-008_REPOSITORY_LAYOUT

REP-001_MASTER_INDEX

REP-002_REPOSITORY_MAP

PROJECT_STATUS

---

# Guiding Statement

**A reliable repository is not one where every expected file merely exists; it is one where the critical artifacts, authorities, references, consumers and status claims agree with verified current evidence.**

---

End of Document
