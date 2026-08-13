# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.1  
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

## Phase-1 Service Node Seed

The Services folder was physically inspected during this audit. `_FOLDER_STATUS.md` confirms the declared inventory as `SRV-001` through `SRV-010`, plus `README.md` and the folder status file, while explicitly keeping the folder on `INTEGRITY HOLD`. `Services/README.md` enumerates the exact ten service filenames.

| Node ID | Artifact | Baseline | State | Directly evidenced relationships / consumers |
|---|---|---|---|---|
| SVC-001 | Services/SRV-001_SERVICE_ARCHITECTURE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED | References SRV-002, CORE-003, RUN-010; defines service-layer intent |
| SVC-002 | Services/SRV-002_REPOSITORY_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED | References SRV-001, SRV-003, RUN-001, RUN-004; repository operation contract |
| SVC-003 | Services/SRV-003_MEMORY_SERVICE.md | not declared in artifact | OBSERVED / REVALIDATION_REQUIRED | References SRV-001, SRV-002, SRV-004, RUN-004; memory continuity contract |
| SVC-004 | Services/SRV-004_KNOWLEDGE_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED | References MOD-001 and SPEC-001; direct specification existence re-read |
| SVC-005 | Services/SRV-005_VALIDATION_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD | Consumer of ENG-004; references CORE-003, REP-001/002, RUN-007 |
| SVC-006 | Services/SRV-006_SEARCH_SERVICE.md | not declared in artifact | OBSERVED / REVALIDATION_REQUIRED | References SRV-001/002/005/007 and PROJECT_BOOTSTRAP |
| SVC-007 | Services/SRV-007_LOGGING_SERVICE.md | not declared in artifact | OBSERVED / REVALIDATION_REQUIRED | References SRV-001/005/006/008 and RUN-007 |
| SVC-008 | Services/SRV-008_INDEX_SERVICE.md | not declared in artifact | OBSERVED / REVALIDATION_REQUIRED | References SRV-001/006/007/009; indexing/relationship role |
| SVC-009 | Services/SRV-009_UPDATE_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD | Controlled mutation service consumed by ENG-006; depends on SRV-005/007/008 |
| SVC-010 | Services/SRV-010_SERVICE_REFERENCE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD | Navigation/reference artifact; selected relationships only |

**Important:** `OBSERVED / REVALIDATION_REQUIRED` means the physical artifact and declared relationships were inspected; it does not certify implementation, runtime execution, or global integration.

## Phase-1 Service Relationship Edges

| ID | Source | Target | Type | State | Impact / Revalidation |
|---|---|---|---|---|---|
| SVC-E01 | SRV-001 | SRV-002 | REFERENCES | OBSERVED | Revalidate if service architecture changes |
| SVC-E02 | SRV-002 | SRV-003 | REFERENCES | OBSERVED | Memory/repository contract impact |
| SVC-E03 | SRV-003 | SRV-004 | REFERENCES | OBSERVED | Memory/knowledge boundary impact |
| SVC-E04 | SRV-004 | MOD-001 | DEPENDS_ON | OBSERVED | Revalidate model identity/content |
| SVC-E05 | SRV-004 | SPEC-001-KNOWLEDGE-ORGANIZATION | DEPENDS_ON | PARTIALLY_VERIFIED | Specification existence and identity verified; full bidirectional validation remains open |
| SVC-E06 | ENG-004 | SRV-005 | CONSUMES | VERIFIED within inspected scope | Validation gate impact; revalidate on engine/service contract changes |
| SVC-E07 | SRV-005 | ENG-004 | CONSUMES / IMPLEMENTS RESPONSIBILITY | VERIFIED within inspected scope | Reverse validation required on ENG-004 changes |
| SVC-E08 | SRV-006 | SRV-007 | REFERENCES | OBSERVED | Search/logging integration impact |
| SVC-E09 | SRV-007 | SRV-008 | REFERENCES | OBSERVED | Logging/index impact |
| SVC-E10 | SRV-008 | SRV-009 | REFERENCES | OBSERVED | Index/update synchronization impact |
| SVC-E11 | ENG-006 | SRV-009 | CONSUMES | VERIFIED within inspected scope | Mutation-control impact |
| SVC-E12 | SRV-009 | SRV-005 | DEPENDS_ON | OBSERVED | Mutation validation dependency |
| SVC-E13 | SRV-009 | SRV-007 | DEPENDS_ON | OBSERVED | Mutation traceability dependency |
| SVC-E14 | SRV-009 | SRV-008 | DEPENDS_ON | OBSERVED | Index/status synchronization impact |
| SVC-E15 | RUN-010 | Services | RUNTIME_REFERENCE | PARTIALLY_VERIFIED | Runtime/service boundary exists; does not prove every service path |

## Initial Control-Plane Seed

The control-plane seed remains as previously established from `REP-013` inventory and `REP-014` relationship evidence, including MX-001 through MX-021. It is intentionally limited and must expand only from inspected repository evidence.

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
- `SRV-003`, `SRV-006`, `SRV-007`, and `SRV-008` do not explicitly declare a Development Baseline in their inspected documents; this is a metadata completeness finding, not permission to infer a baseline.
- Bidirectional validation is not globally complete.
- Domain semantic relationships outside the inspected control plane and service boundary remain open.
- `REP-020` must not be used as an authority substitute for canonical authorities.

## Integrity State

`INTEGRITY HOLD`

## Evidence Basis

- `Services/README.md` — exact service inventory.
- `Services/_FOLDER_STATUS.md` — bounded folder status and audit boundary.
- `SRV-001` through `SRV-010` — inspected service contracts and declared relationships.
- `REP-013` / `REP-014` — control-plane inventory and relationship contract.
- `STD-003` — cross-reference verification contract.
- `Release/VERSION.md` — current development baseline.

## Design Principle

> **Optimize lookup, not proof.**

End of Document
