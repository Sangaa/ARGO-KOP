# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.0  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Development Baseline: 3.2.1  
Last Audit: 2026-08-13

## Purpose

Provide a repository-wide lookup and impact surface that identifies:

`Artifact → Relationship → Consumer/Dependency → Revalidation Scope`

This matrix exists to reduce repeated repository rediscovery while preserving the full evidence and authority checks required by the governing standards and registries.

**The matrix does not grant authority.** Canonical authority remains with the applicable governed artifact.

## Governing Model

```text
Changed Artifact
      ↓
Matrix Lookup
      ↓
Direct Relationships
      ↓
Reverse Relationships
      ↓
Consumers + Dependencies
      ↓
Authority / Content Contract
      ↓
Impact Set
      ↓
Targeted Revalidation
      ↓
Re-read
      ↓
Matrix Update
```

## Node Schema

| Field | Requirement |
|---|---|
| Artifact ID | Current internal identity where applicable |
| Path | Current repository path |
| Folder | Physical folder |
| Domain | Logical domain |
| Authority | Canonical authority source, if applicable |
| Version | Current artifact version |
| Baseline | Current development baseline |
| Status | Repository/review state |
| Freshness | Current / stale / unknown |
| Last Verified | Date/time |
| Verification Commit | Commit/checkpoint |
| Provenance | Historical or derived origin |

## Edge Schema

| Field | Requirement |
|---|---|
| Relationship ID | Stable relationship identifier |
| Source | Source artifact |
| Target | Target artifact |
| Type | Controlled relationship type |
| Direction | Source → Target |
| Authority Basis | Rule/document authorizing relationship |
| Evidence | Evidence location/reason |
| State | Verification state |
| Consumers | Known downstream consumers |
| Dependencies | Known upstream dependencies |
| Impact | Mutation impact |
| Last Verified | Date/time |
| Checkpoint | Commit/checkpoint evidence |
| Revalidation Trigger | Mutation/change that invalidates edge |

## Relationship States

`NOT_CHECKED` · `OBSERVED` · `PARTIALLY_VERIFIED` · `VERIFIED` · `REVALIDATION_REQUIRED` · `STALE` · `CONFLICT` · `UNAVAILABLE`

`VERIFIED` is an evidence claim, not a value inferred from the presence of a row.

## Initial Control-Plane Seed

The following seed is populated from current `REP-013` inventory and `REP-014` relationship evidence. It is intentionally limited and must expand only from inspected repository evidence.

| ID | Source | Target | Type | Direction | State | Impact / Revalidation |
|---|---|---|---|---|---|---|
| MX-001 | REP-001 | REP-002 | REFERENCES | → | VERIFIED within control-plane scope | Revalidate if master index/map changes |
| MX-002 | REP-002 | REP-001 | REFERENCES | → | VERIFIED within control-plane scope | Revalidate if map/index changes |
| MX-003 | REP-001 | REP-013 | DEPENDS_ON | → | VERIFIED within control-plane scope | Revalidate if content inventory changes |
| MX-004 | REP-002 | REP-013 | DEPENDS_ON | → | VERIFIED within control-plane scope | Revalidate if content tree changes |
| MX-005 | REP-013 | REP-011 | DEPENDS_ON | → | VERIFIED within control-plane scope | Review-state impact |
| MX-006 | REP-013 | REP-012 | DEPENDS_ON | → | VERIFIED within control-plane scope | Allocation-state impact |
| MX-007 | REP-013 | REP-014 | DEPENDS_ON | → | VERIFIED within control-plane scope | Relationship graph impact |
| MX-008 | REP-014 | REP-011 | DEPENDS_ON | → | VERIFIED within control-plane scope | Evidence/review impact |
| MX-009 | REP-014 | REP-012 | DEPENDS_ON | → | VERIFIED within control-plane scope | Allocation/checkpoint impact |
| MX-010 | REP-015 | REP-011 | DEPENDS_ON | → | VERIFIED within control-plane scope | Bootstrap evidence impact |
| MX-011 | REP-015 | REP-012 | DEPENDS_ON | → | VERIFIED within control-plane scope | Allocation/recovery impact |
| MX-012 | REP-015 | REP-013 | DEPENDS_ON | → | VERIFIED within control-plane scope | Inventory impact |
| MX-013 | REP-015 | REP-014 | DEPENDS_ON | → | VERIFIED within control-plane scope | Relationship impact |
| MX-014 | REP-015 | REP-016 | DEPENDS_ON | → | VERIFIED within control-plane scope | Work-queue impact |
| MX-015 | REP-016 | REP-011 | DEPENDS_ON | → | VERIFIED within control-plane scope | Review evidence impact |
| MX-016 | REP-016 | REP-012 | DEPENDS_ON | → | VERIFIED within control-plane scope | Allocation/recovery impact |
| MX-017 | REP-016 | REP-013 | DEPENDS_ON | → | VERIFIED within control-plane scope | Inventory impact |
| MX-018 | REP-016 | REP-014 | DEPENDS_ON | → | VERIFIED within control-plane scope | Relationship impact |
| MX-019 | REP-016 | REP-015 | CONSUMES | → | VERIFIED within current control-plane scope | Bootstrap/work-queue impact |
| MX-020 | REP-012 | DIAG-001 | DOCUMENTS | → | PROVISIONAL / provenance-linked | Revalidate/regenerate when REP-012 changes |
| MX-021 | DIAG-001 | REP-012 | DERIVED_FROM | → | PROVISIONAL / provenance-linked | Stale if source registry changes |

## Current Artifact Inventory Seed

The current content tree explicitly identifies the following control-plane artifacts:

```text
Repository/
├── REP-011_REVIEW_TRACEABILITY_LEDGER.md
├── REP-012_REPOSITORY_ALLOCATION_REGISTRY.md
├── REP-013_REPOSITORY_CONTENT_TREE.md
├── REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md
├── REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md
└── REP-016_PHASE1_PARTITION_WORK_QUEUE.md
```

`REP-013` confirms this set as physically present and states that allocation, review and relationship records remain subject to cross-registry reconciliation.

## Baseline Control

Current development baseline: **3.2.1**.

Any matrix row or node declaring another baseline must be treated as a drift finding until reconciled against `Release/VERSION.md` and the applicable authority.

## Mutation Impact Contract

A material mutation to any matrix node must trigger lookup of:

1. outgoing edges;
2. incoming/reverse edges;
3. direct consumers;
4. direct dependencies;
5. canonical authority;
6. content contract;
7. derived/provenance artifacts;
8. session/audit records requiring synchronization.

The resulting set becomes the minimum targeted revalidation scope. Discovery of a new relationship expands the scope.

## Session Closure Contract

At every session closure, once this matrix is governed for operational use, record:

- timestamp;
- repository HEAD;
- session ID;
- node changes;
- edge changes;
- impacted consumers/dependencies;
- revalidation completed;
- revalidation pending;
- contradictions/findings;
- new engineering knowledge;
- next recovery point.

## Limitations / Open Work

- This is a Phase-1 seed, not an exhaustive repository graph.
- Wildcard/partial inventory entries remain unresolved until physically enumerated.
- Bidirectional validation is not globally complete.
- Domain semantic relationships outside the inspected control plane remain open.
- `REP-020` must not be used as an authority substitute for `REP-014`, `REP-011`, `REP-012`, `REP-013`, `REP-015`, `REP-016`, `STD-003`, or other canonical authorities.

## Integrity State

`INTEGRITY HOLD`

## Evidence Basis

- `REP-013` — physical content inventory and state rules.
- `REP-014` — relationship schema and current relationship evidence.
- `STD-003` — cross-reference verification contract.
- `Release/VERSION.md` — current development baseline.
- `ROADMAP.md` F-004 — pre-existing Dependency & Consumer Impact Matrix candidate.

## Design Principle

> **Optimize lookup, not proof.**

End of Document
