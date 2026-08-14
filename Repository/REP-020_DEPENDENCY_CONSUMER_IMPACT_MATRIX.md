# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.5  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Current Development Baseline: **3.2.1**  
Last Audit: 2026-08-14

## Purpose

Repository-wide lookup surface:
`Artifact → Relationship → Consumer/Dependency → Revalidation Scope`

The matrix narrows rediscovery. It does **not** grant authority or prove runtime coupling.

## Relationship States

`NOT_CHECKED` · `OBSERVED` · `PARTIALLY_VERIFIED` · `VERIFIED` · `REVALIDATION_REQUIRED` · `STALE` · `CONFLICT` · `UNAVAILABLE`

## Service + Runtime Nodes

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
| RUN-001 | Runtime/RUN-010_RUNTIME_REFERENCE.md | 3.2.1 | PARTIALLY_VERIFIED boundary |
| ENG-001 | Engine/ENG-006_EXECUTION_ENGINE.md | 3.2.1 | PARTIALLY_VERIFIED boundary |

## Repository / Index Expansion

REP-001 and REP-002 are canonical Repository control-plane artifacts at Integrity Hold and baseline 3.2.1. REP-001 explicitly states that index membership records inventory and does not itself certify graph relationships; REP-002 separates physical mapping from review/relationship evidence. 

| ID | Source | Target | Type | State | Impact |
|---|---|---|---|---|---|
| REP-E01 | SRV-009 | REP-001 | INDEX_CONSUMER | OBSERVED | Update mutations require index revalidation |
| REP-E02 | SRV-009 | REP-002 | PHYSICAL_MAP_IMPACT | OBSERVED | Path/inventory mutations require map revalidation |
| REP-E03 | ENG-006 | REP-001 | REPOSITORY_CONSUMER | PARTIALLY_VERIFIED | Execution-driven repository changes must preserve index integrity |
| REP-E04 | ENG-006 | REP-002 | REPOSITORY_MAP_CONSUMER | PARTIALLY_VERIFIED | Execution-driven path changes require physical-map check |
| REP-E05 | REP-001 ↔ REP-002 | CROSS_REGISTRY | CONTROL_PLANE_RECONCILIATION | PARTIALLY_VERIFIED | Material inventory changes require both registries to be reconciled |
| REP-E06 | REP-001 | REP-011 | REVIEW_EVIDENCE | OBSERVED | Review/completion evidence is controlled by REP-011 |
| REP-E07 | REP-002 | REP-011 | REVIEW_EVIDENCE | OBSERVED | Physical mapping does not equal review completion |

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

## Runtime Consumer Edges

| ID | Source | Target | Type | State |
|---|---|---|---|---|
| RUN-E01 | RUN-010 | ENG-006 | RUNTIME_CONSUMER | PARTIALLY_VERIFIED |
| RUN-E02 | RUN-010 | SRV-009 | CONTROLLED_MUTATION_PATH | PARTIALLY_VERIFIED |
| RUN-E03 | ENG-006 | SRV-009 | SERVICE_DISPATCH | PARTIALLY_VERIFIED |
| RUN-E04 | ENG-006 | SRV-005 | VALIDATION_DEPENDENCY | PARTIALLY_VERIFIED |
| RUN-E05 | ENG-006 | RUN-010 | RUNTIME_CONTROL | OBSERVED |
| RUN-E06 | SRV-009 | ENG-006 | REVERSE_CONSUMER | OBSERVED |
| RUN-E07 | SRV-005 | ENG-006 | REVERSE_VALIDATION_CONSUMER | OBSERVED |

## Test / Verification Ledger

### Tests / checks performed

| Test ID | Check | Result | Scope |
|---|---|---|---|
| TST-001 | Exact Services inventory reconciliation | PASS within inspected scope | Services |
| TST-002 | Artifact path/readability check | PASS | Inspected artifacts |
| TST-003 | Identity/version/status extraction | PASS | Inspected SRV artifacts |
| TST-004 | Baseline check against current canonical version authority | PASS for declared values; four undeclared gaps preserved | Services |
| TST-005 | Forward relationship extraction | PASS | Services → Runtime/Engine/Repository |
| TST-006 | Documentation reverse-edge check | PARTIAL | Service boundary |
| TST-007 | Runtime → Engine → Service extraction | PARTIAL | RUN-010/ENG-006/Services |
| TST-008 | REP-001 ↔ REP-002 comparison | PARTIAL | Repository control plane |
| TST-009 | REP-020 mutation persistence + re-read | PASS | REP-020/main |
| TST-010 | REP-011 review-traceability rule re-read | PASS | Review/evidence control |
| TST-011 | REP-012 allocation/recovery rule re-read | PASS | Allocation/recovery control |
| TST-012 | Current-baseline conflict detection across control-plane records | **CONFLICT DETECTED** | REP-020/Release authority vs REP-012 |
| TST-013 | Content-fitness/currentness rule check | PARTIAL | Canonical control-plane scope |
| TST-014 | Cross-registry reconciliation state check | PARTIAL / OPEN | REP-011..016 |

### Tests not performed / not yet sufficient

| Test ID | Check | State | Why |
|---|---|---|---|
| TST-101 | Actual executable RUN-010 → ENG-006 → SRV-009 invocation | NOT_PERFORMED | No runtime execution evidence captured |
| TST-102 | Controlled repository mutation + automatic REP-001/002/011 reconciliation | NOT_PERFORMED | Requires controlled mutation environment |
| TST-103 | Automated bidirectional graph traversal across all domains | NOT_PERFORMED | REP-020 remains Phase-1 seed |
| TST-104 | Exhaustive duplicate-ID scan | NOT_COMPLETED | Existing audit item remains open |
| TST-105 | Semantic content equivalence across all consumers | NOT_COMPLETED | Cross-layer consumer review required |
| TST-106 | Matrix program performance/load test | NOT_PERFORMED | Program not yet implemented |

**Interpretation:** `PASS` is scope-bound. `PARTIAL` is incomplete evidence. `CONFLICT` is a detected contradiction requiring authority resolution. `NOT_PERFORMED` is not failure.

## Baseline Conflict Finding

`REP-012` currently declares Development Baseline **3.3.0**, while the current version authority used by this matrix is **3.2.1**. This is now explicitly recorded as a **CONFLICT**, not silently normalized.

Required action: resolve the canonical authority before promoting affected control-plane artifacts or changing the matrix baseline. Do not infer that 3.3.0 is current merely because it is numerically higher.

## High-Value Impact Chains

### Chain A — Search / Logging / Index / Update / Validation
`SRV-006 → SRV-007 → SRV-008 → SRV-009 → SRV-005`

### Chain B — Runtime Execution / Mutation
`RUN-010 → ENG-006 → SRV-009 → SRV-005`

### Chain C — Runtime / Repository Control Plane
`RUN-010 → ENG-006 → SRV-009 → REP-001 + REP-002 + REP-011`

### Chain D — Memory / Knowledge
`SRV-003 → SRV-004`

## Mutation Impact Contract

For every material mutation, lookup outgoing edges, incoming/reverse edges, consumers, dependencies, authority, content contract, provenance/derived artifacts and audit/session records requiring synchronization. The resulting set is the minimum targeted revalidation scope.

## Open Work

- Resolve the **3.2.1 vs 3.3.0 baseline authority conflict**.
- Resolve baseline metadata gaps in SRV-003/006/007/008.
- Complete bidirectional validation.
- Execute controlled runtime/mutation tests with evidence capture.
- Complete REP-001/REP-002/REP-011 reconciliation validation.
- Continue Runtime Consumers → Repository/Index expansion.
- Preserve provisional status until evidence supports promotion.

## Integrity State

`INTEGRITY HOLD`

## Design Principle

> **Optimize lookup, not proof.**

> **Inspect once → capture node → capture edges → capture impact → test what can be tested → explicitly record what cannot.**

End of Document
