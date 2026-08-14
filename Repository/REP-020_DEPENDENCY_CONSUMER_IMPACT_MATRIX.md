# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.2  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Development Baseline: 3.2.1  
Last Audit: 2026-08-14

## Purpose

Provide a repository-wide lookup and impact surface that identifies:

`Artifact → Relationship → Consumer/Dependency → Revalidation Scope`

The matrix reduces repeated repository rediscovery while preserving evidence and authority checks. **The matrix does not grant authority.**

## Governing Model

`Changed Artifact → Matrix Lookup → Direct + Reverse Relationships → Consumers + Dependencies → Authority / Content Contract → Impact Set → Targeted Revalidation → Re-read → Matrix Update`

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

`VERIFIED` is an evidence claim, not a value inferred from row presence.

## Service Node Seed

The Services folder inventory is exact: SRV-001 through SRV-010 plus README and `_FOLDER_STATUS`. Services remain `INTEGRITY HOLD`.

| Node | Artifact | Baseline | State |
|---|---|---|---|
| SVC-001 | SRV-001_SERVICE_ARCHITECTURE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-002 | SRV-002_REPOSITORY_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-003 | SRV-003_MEMORY_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-004 | SRV-004_KNOWLEDGE_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-005 | SRV-005_VALIDATION_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |
| SVC-006 | SRV-006_SEARCH_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-007 | SRV-007_LOGGING_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-008 | SRV-008_INDEX_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-009 | SRV-009_UPDATE_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |
| SVC-010 | SRV-010_SERVICE_REFERENCE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |

## Reverse-Edge Validation — Documentation Boundary

| ID | Relationship | Evidence | State | Revalidation |
|---|---|---|---|---|
| REV-001 | SRV-003 ↔ SRV-002 | SRV-003 names SRV-002; reverse declaration remains incomplete | OBSERVED | Required |
| REV-002 | SRV-003 ↔ SRV-004 | SRV-003 names SRV-004; reverse declaration remains incomplete | OBSERVED | Required |
| REV-003 | SRV-006 ↔ SRV-007 | Both service documents name the other | PARTIALLY_VERIFIED | Runtime/implementation evidence required |
| REV-004 | SRV-007 ↔ SRV-008 | Both service documents name the other | PARTIALLY_VERIFIED | Runtime/implementation evidence required |
| REV-005 | SRV-008 ↔ SRV-009 | Both service documents name the other | PARTIALLY_VERIFIED | Runtime/implementation evidence required |
| REV-006 | SRV-009 → SRV-005 | SRV-009 declares Validation Service dependency | OBSERVED | Reverse consumer evidence required |
| REV-007 | SRV-009 → SRV-007 | SRV-009 declares Logging Service dependency | OBSERVED | Reverse consumer evidence required |
| REV-008 | SRV-009 → SRV-008 | SRV-009 declares Index Service dependency | OBSERVED | Reverse consumer evidence required |

**Interpretation rule:** reciprocal documentation is stronger than a one-sided declaration but does not prove operational/runtime coupling. Therefore reciprocal documentation is `PARTIALLY_VERIFIED` until implementation/runtime evidence exists.

## Current High-Value Impact Surface

`SRV-006 → SRV-007 → SRV-008 → SRV-009 → SRV-005` forms a high-value documentation dependency chain. A material change to one node should trigger targeted inspection of downstream consumers, reverse edges, validation, logging, indexing, and update controls.

`SRV-003 → SRV-004` forms the Memory → Knowledge boundary and requires separate bidirectional validation before promotion.

## Baseline Control

Current development baseline: **3.2.1**. Any conflicting declared baseline is a drift finding until reconciled against `Release/VERSION.md` and the applicable authority. Missing baseline metadata remains `UNDECLARED`; it is never inferred.

## Mutation Impact Contract

For every material mutation, lookup:

1. outgoing edges;
2. incoming/reverse edges;
3. direct consumers;
4. direct dependencies;
5. canonical authority;
6. content contract;
7. derived/provenance artifacts;
8. session/audit records requiring synchronization.

The resulting set is the minimum targeted revalidation scope; discovery of a new relationship expands it.

## Limitations / Open Work

- Phase-1 seed; not exhaustive.
- SRV-003/006/007/008 baseline metadata unresolved.
- Bidirectional validation is incomplete.
- Runtime/implementation coupling is not proven by documentation reciprocity.
- Services → Runtime Consumers → Repository/Index expansion remains open.
- REP-020 is not an authority substitute.

## Integrity State

`INTEGRITY HOLD`

## Design Principle

> **Optimize lookup, not proof.**

> **Inspect once → capture node → capture edges → capture impact → continue.**

End of Document
