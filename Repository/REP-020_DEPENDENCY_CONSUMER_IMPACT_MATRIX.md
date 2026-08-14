# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.3  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Development Baseline: 3.2.1  
Last Audit: 2026-08-14

## Purpose

Repository-wide lookup surface:
`Artifact → Relationship → Consumer/Dependency → Revalidation Scope`

The matrix narrows rediscovery. It does **not** grant authority or prove runtime coupling.

## Relationship States

`NOT_CHECKED` · `OBSERVED` · `PARTIALLY_VERIFIED` · `VERIFIED` · `REVALIDATION_REQUIRED` · `STALE` · `CONFLICT` · `UNAVAILABLE`

## Service Nodes

| Node | Artifact | Baseline | State |
|---|---|---|---|
| SVC-001 | Services/SRV-001_SERVICE_ARCHITECTURE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-002 | Services/SRV-002_REPOSITORY_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-003 | Services/SRV-003_MEMORY_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-004 | Services/SRV-004_KNOWLEDGE_SERVICE.md | 3.2.1 | OBSERVED / REVALIDATION_REQUIRED |
| SVC-005 | Services/SRV-005_VALIDATION_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |
| SVC-006 | Services/SRV-006_SEARCH_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-007 | Services/SRV-007_LOGGING_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-008 | Services/SRV-008_INDEX_SERVICE.md | UNDECLARED | METADATA GAP / REVALIDATION_REQUIRED |
| SVC-009 | Services/SRV-009_UPDATE_SERVICE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |
| SVC-010 | Services/SRV-010_SERVICE_REFERENCE.md | 3.2.1 | REVALIDATED / INTEGRITY HOLD |

## Service Reverse Edges

| ID | Relationship | State | Evidence / Impact |
|---|---|---|---|
| REV-001 | SRV-003 ↔ SRV-002 | OBSERVED | Reverse declaration incomplete |
| REV-002 | SRV-003 ↔ SRV-004 | OBSERVED | Reverse declaration incomplete |
| REV-003 | SRV-006 ↔ SRV-007 | PARTIALLY_VERIFIED | Reciprocal documentation; runtime proof open |
| REV-004 | SRV-007 ↔ SRV-008 | PARTIALLY_VERIFIED | Reciprocal documentation; runtime proof open |
| REV-005 | SRV-008 ↔ SRV-009 | PARTIALLY_VERIFIED | Reciprocal documentation; runtime proof open |
| REV-006 | SRV-009 → SRV-005 | OBSERVED | Validation dependency; reverse consumer proof open |
| REV-007 | SRV-009 → SRV-007 | OBSERVED | Logging dependency; reverse consumer proof open |
| REV-008 | SRV-009 → SRV-008 | OBSERVED | Index dependency; reverse consumer proof open |

## Runtime Consumer Expansion

`RUN-010_RUNTIME_REFERENCE.md` is a validated/revalidated canonical runtime reference at baseline 3.2.1. It explicitly describes the controlled decision/validation/execution boundary and names `ENG-006` and `SRV-009`. fileciteturn1073file0

`ENG-006_EXECUTION_ENGINE.md` is canonical, critical, Integrity Hold/Revalidated, baseline 3.2.1, and explicitly requires repository operations to route through `SRV-009`, while requiring `ENG-004/SRV-005` validation and applicable Runtime controls. fileciteturn1074file0

| ID | Source | Target | Type | State | Revalidation Trigger |
|---|---|---|---|---|---|
| RUN-E01 | RUN-010 | ENG-006 | RUNTIME_CONSUMER | PARTIALLY_VERIFIED | Runtime execution boundary changes |
| RUN-E02 | RUN-010 | SRV-009 | CONTROLLED_MUTATION_PATH | PARTIALLY_VERIFIED | Mutation/update contract changes |
| RUN-E03 | ENG-006 | SRV-009 | SERVICE_DISPATCH | PARTIALLY_VERIFIED | Execution or update contract changes |
| RUN-E04 | ENG-006 | SRV-005 | VALIDATION_DEPENDENCY | PARTIALLY_VERIFIED | Validation/authorization boundary changes |
| RUN-E05 | ENG-006 | RUN-010 | RUNTIME_CONTROL | OBSERVED | Runtime state/execution policy changes |
| RUN-E06 | SRV-009 | ENG-006 | REVERSE_CONSUMER | OBSERVED | Update service contract changes |
| RUN-E07 | SRV-005 | ENG-006 | REVERSE_VALIDATION_CONSUMER | OBSERVED | Validation contract changes |

**Interpretation:** these are documentation/evidence relationships. `PARTIALLY_VERIFIED` does not claim executable runtime coupling.

## High-Value Impact Chains

### Chain A — Search / Logging / Index / Update / Validation
`SRV-006 → SRV-007 → SRV-008 → SRV-009 → SRV-005`

Material change anywhere in this chain requires targeted review of downstream consumers, reverse edges, logging, indexing, mutation controls and validation.

### Chain B — Runtime Execution / Mutation
`RUN-010 → ENG-006 → SRV-009 → SRV-005`

Material execution/update changes require Runtime + Execution Engine + Update Service + Validation Service revalidation before completion can be claimed.

### Chain C — Memory / Knowledge
`SRV-003 → SRV-004`

Reverse validation remains open.

## Baseline Control

Current development baseline: **3.2.1**. Missing baseline metadata remains `UNDECLARED`; values are never inferred. Conflicts must be reconciled against canonical version authority.

## Mutation Impact Contract

For every material mutation, lookup:

1. outgoing edges;
2. incoming/reverse edges;
3. consumers;
4. dependencies;
5. canonical authority;
6. content contract;
7. provenance/derived artifacts;
8. audit/session records requiring synchronization.

The resulting set is the minimum targeted revalidation scope.

## Open Work

- Resolve baseline metadata gaps in SRV-003/006/007/008.
- Complete bidirectional validation.
- Validate Runtime → Engine → Services relationships beyond documentation evidence.
- Expand Runtime Consumers → Repository/Index consumers.
- Preserve provisional status until evidence supports promotion.

## Integrity State

`INTEGRITY HOLD`

## Design Principle

> **Optimize lookup, not proof.**

> **Inspect once → capture node → capture edges → capture impact → continue.**

End of Document
