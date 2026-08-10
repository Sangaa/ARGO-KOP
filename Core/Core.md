# CORE INDEX

Document ID
CORE-INDEX
Version
1.1.0
Status
Validated for inventory / Integrity Hold
Category
Core Registry
Canonical
Yes
Last Audit
2026-08-10
Review Type
Repository Re-Audit / Targeted Core Inventory Review

---

# Purpose

This file is the inventory index for the `Core/` folder.

It records known Core artifacts as they exist in the repository. It is an index, not an authority override for the artifacts it lists.

A listed artifact must still be evaluated using its own identity, status, authority, version and validation evidence.

# Current Repository Inventory

- `ARGO_KERNEL.md`
- `CORE-000_PLATFORM_ARCHITECTURE.md`
- `CORE-000_PLATFORM_IDENTITY.md`
- `CORE-000A_PLATFORM_GLOSSARY.md`
- `CORE-001_ARGO_MANIFEST.md`
- `CORE-002_ARGO_IDENTITY.md`
- `CORE-003_CONSTITUTION.md`
- `CORE-004_CORE_PRINCIPLES.md`
- `CORE-005_COGNITIVE_MODEL.md`
- `CORE-006_SYSTEM_PHILOSOPHY.md`
- `CORE-007_DESIGN_PRINCIPLES.md`
- `CORE-008_ARCHITECTURAL_LAWS.md`
- `CORE-009_PLATFORM_LIFECYCLE.md`
- `CORE-010_PLATFORM_ROADMAP.md`
- `CORE-011_PLATFORM_CHARTER.md`
- `_FOLDER_STATUS.md`

# Inventory Rules

1. This inventory reflects repository paths, not inferred names.
2. A filename in this index does not prove the artifact is canonical, current or validated.
3. A missing numbered Core document is not evidence that a new document should be created.
4. Renames, moves, additions or deletions require identity and relationship revalidation.
5. The index itself must be revalidated when Core inventory changes materially.

# Identity / Path Boundary

The following are distinct claims and must not be conflated:

```text
Listed in Index
      ↓
Path Exists
      ↓
File Read
      ↓
Document Identity Verified
      ↓
Authority Verified
      ↓
Relationship Classified
      ↓
Validated State
```

An index entry establishes an inventory claim only. It does not establish the later states in this chain.

# Registry Boundary

`Core.md` is the inventory layer.

Detailed authority, dependency, relationship, lifecycle and validation claims belong to their applicable registries and canonical artifacts.

This prevents the Core index from becoming an accidental second source of truth.

# Historical and Review Provenance

A historical audit date records an actual completed review event. It shall not be advanced merely because another Core artifact was reviewed.

This index was specifically re-audited on 2026-08-10 against the current repository inventory.

The review confirms inventory synchronization only; it does not certify the entire Core folder.

# Integrity Status

Core remains under `INTEGRITY HOLD` until the remaining canonical Core artifacts and relevant cross-layer relationships are revalidated.

---

End of Document
