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
2026-09-01
Review Type
Repository Re-Audit / Exact Core Local Inventory Reconciliation P336

---

# Purpose

This file is the inventory index for the `Core/` folder.

It records known Core artifacts as they exist in the repository. It is an index, not an authority override for the artifacts it lists.

A listed artifact must still be evaluated using its own identity, status, authority, version and validation evidence.

# Current Repository Inventory

The member list below is the exact current top-level `Core/` file inventory excluding this self-index file (`Core.md`) by design.

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
- `CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`
- `_FOLDER_STATUS.md`

# Inventory Rules

1. This inventory reflects repository paths, not inferred names.
2. A filename in this index does not prove the artifact is canonical, current or validated.
3. A missing numbered Core document is not evidence that a new document should be created.
4. Renames, moves, additions or deletions require identity and relationship revalidation.
5. The index itself must be revalidated when Core inventory changes materially.
6. `Core.md` excludes itself from the member list so equality can be tested against the physical top-level inventory minus this single self-index path.

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

# P336 Current Inventory Reconciliation — 2026-09-01

Direct exact current-repository enumeration established 18 top-level files in `Core/`: this self-index plus the 17 members listed above.

`CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` is now represented locally after its legitimate 2026-08-18 migration from a colliding CORE-011 identity to the unique CORE-012 identity.

`CORE-000_PLATFORM_IDENTITY.md` remains listed because it is physically present, but its own metadata remains `Canonical: No / Legacy / Superseded`; listing it does not promote it or create a second active CORE-000 authority.

This reconciliation is deliberately local. Current REP-001/REP-002/REP-013 control-plane representation and cross-layer Governance/Architecture relationships require separate controlled review. No Core certification is implied.

# Historical and Review Provenance

A historical audit date records an actual completed review event. It shall not be advanced merely because another Core artifact was reviewed.

The previous targeted inventory audit on 2026-08-10 remains historical evidence. This index itself was re-audited on 2026-09-01 by P336 against the exact current top-level Core repository inventory.

The review confirms local inventory synchronization only; it does not certify the entire Core folder.

# Integrity Status

Core remains under `INTEGRITY HOLD` until control-plane inventory representation, remaining cross-layer relationships, consumers/dependencies and certification criteria are reconciled.

---

End of Document
