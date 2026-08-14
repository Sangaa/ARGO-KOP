# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.8  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Current Development Baseline: **3.2.1**  
Last Audit: 2026-08-14  
Last Revalidation Commit: `654d7f3377003f6882794c86ffc142ec45298e64`

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
| TST-012 | Current-baseline conflict detection across control-plane records | CONFLICT DETECTED then RECONCILED | REP-020/Release authority/REP-012 |
| TST-013 | Content-fitness/currentness rule check | PARTIAL | Canonical control-plane scope |
| TST-014 | Cross-registry reconciliation state check | PARTIAL / OPEN | REP-011..016 |
| TST-015 | Direct read of authoritative version source | PASS | Release/VERSION.md |
| TST-016 | Reproduce REP-012 baseline claim | CONFLICT CONFIRMED then CORRECTED | Repository/REP-012 |
| TST-017 | Cross-check root status against version authority | SUPPORTS 3.2.1 | PROJECT_STATUS.md |
| TST-018 | Current main commit / latest repository state check | PASS | Current main |
| TST-019 | REP-020 current version/currentness verification before mutation | PASS | REP-020 v0.1.7 → v0.1.8 |
| TST-020 | RUN-001 boot sequence direct read | PASS | Runtime/RUN-001_BOOT_SEQUENCE.md @ main |
| TST-021 | Boot integrity completion gate | HOLD | Global PASS still blocked by unresolved relationship/ID scope |
| TST-022 | PR #1 complete semantic diff inspection | PASS for changed-file diff; historical | PR #1, 20 commits / 20 changed files |
| TST-023 | PR #1 divergence and conflict impact review | CONFLICT / STALE | PR #1 superseded |
| TST-024 | Runtime → Engine → Service executable consumer search | PARTIAL / DOCUMENTATION ONLY | No executable consumer established in inspected Python scope |
| TST-025 | Current-main acceptance expectation vs harness state logic | RESOLVED | Current candidate behavior reconciled to HOLD |
| TST-026 | Reconciled candidate branch created from current main | PASS | Controlled candidate lineage |
| TST-027 | PR #3 CI | HISTORICAL FAIL / SUPERSEDED | Old candidate; no longer operative |
| TST-028 | PR #3 CI retry | HISTORICAL FAIL / SUPERSEDED | Old candidate; no longer operative |
| TST-029 | Integration failure step localization | RESOLVED | First assertions identified in later runs |
| TST-030 | Integration failure reproducibility | PASS / HISTORICAL | Same failure reproduced before reconciliation |
| TST-031 | Reconciled candidate semantic acceptance | PASS | Prototype + canonical acceptance |
| TST-032 | EJR-164 checkpoint persistence | PASS | Evidence persisted |
| TST-033 | REP-020 re-read before current mutation | PASS | v0.1.6/0.1.7 history preserved |
| TST-034 | Runtime consumer expansion evidence review | PARTIAL | Executable proof remains open |
| TST-035 | PR #9 Prototype acceptance | PASS | Run #132 |
| TST-036 | PR #9 Canonical acceptance scenarios | PASS | SAFE-001, SAFE-002, SAFE-003 |
| TST-037 | PR #9 Integration quality suite | PASS | 80 passed in 0.23s |
| TST-038 | PR #9 full workflow completion | PASS | Prototype + Integration jobs successful |
| TST-039 | PR #1 closure | PASS | Closed without merge; stale/superseded |
| TST-040 | PR #3 closure | PASS | Closed without merge; stale/superseded |
| TST-041 | REP-013 canonical specification path revalidation | PASS | `Specifications/01-Knowledge-Organization.md` present and explicitly reconciled |
| TST-042 | REP-012 baseline authority reconciliation | PASS within authority scope | 3.2.1 restored as current declaration |
| TST-043 | REP-001 ↔ REP-002 current control-plane alignment | PASS within inspected scope | Both declare baseline 3.2.1 and matching control-plane inventory scope |
| TST-044 | GOV-011 existence/status verification | PASS | Exists as Proposed / Integrity Hold, not missing |
| TST-045 | Current-open-PR audit | PASS | PR #1 and #3 closed; no obsolete verification PR left open in current working set |
| TST-046 | Current REP-012 re-read after mutation | PASS | v1.0.7 / baseline 3.2.1 |
| TST-047 | Matrix re-read after mutation | PASS | v0.1.8 |

### Tests not performed / not yet sufficient

| Test ID | Check | State | Why |
|---|---|---|---|
| TST-101 | Actual executable RUN-010 → ENG-006 → SRV-009 invocation | NOT_PERFORMED | No executable consumer path established in inspected scope |
| TST-102 | Controlled repository mutation + automatic REP-001/002/011 reconciliation | NOT_PERFORMED | Requires controlled mutation harness |
| TST-103 | Automated bidirectional graph traversal across all domains | NOT_PERFORMED | REP-020 remains Phase-1 seed |
| TST-104 | Exhaustive duplicate-ID scan | PARTIAL / NOT_CLOSED | Filename namespaces reviewed; full internal-ID/content scan remains evidence-limited |
| TST-105 | Semantic content equivalence across all consumers | NOT_COMPLETED | Cross-layer consumer review required |
| TST-106 | Matrix program performance/load test | NOT_PERFORMED | Program not yet implemented |
| TST-107 | Final acceptance test after latest approved mutation | PASS for current candidate evidence; merge not performed | PR #9 passed, but repository-wide integrity remains HOLD |
| TST-108 | Full-stack integration workflow on latest main after REP-012 mutation | NOT_PERFORMED | Latest baseline mutation has not been validated on main through full-stack workflow |
| TST-109 | Final first-failing integration assertion | N/A / CLEARED | Latest PR #9 integration suite passed; historical assertion chain is documented |
| TST-110 | Baseline authority reconciliation decision | PASS | REP-012 corrected to 3.2.1 |
| TST-111 | REP-013 merge-materialization reconciliation | PASS | Current candidate explicitly re-audited REP-013 |
| TST-112 | PR #9 merge decision | NOT_PERFORMED / INTENTIONALLY NOT MERGED | Candidate evidence passed; repository-wide integrity not yet PASS |
| TST-113 | Final Boot `BOOTED / INTEGRITY PASS` | NOT_PERFORMED | Relationship and duplicate-ID blockers remain |

**Interpretation:** `PASS` is scope-bound. `PARTIAL` is incomplete evidence. `CONFLICT` is a detected contradiction requiring authority resolution. `NOT_PERFORMED` is not failure.

## Duplicate-ID Audit — 2026-08-14

The audit was performed against the current `main` tree and `REP-001` identity model. Filename namespace searches produced these current counts:

| Namespace | Current filename matches | Finding |
|---|---:|---|
| SRV-* | 10 | One current Service namespace sequence; no duplicate filename identity observed |
| REP-* | 19 | Control-plane/repository artifacts require identity-vs-reference distinction; no duplicate filename identity established by the search |
| ARC-* | 16 | Active Architecture IDs coexist with Archive/ARC-* historical artifacts; archive occurrences are historical/reference, not active duplicate authority |
| LIF-* | 1 | Current lifecycle identity is unique |
| GOV-* | 16 | Current Governance namespace search did not expose a duplicate GOV-005 active filename; former Lifecycle collision is absent from active path |
| ENG-* | 25 | Namespace requires further internal-ID reconciliation; filename search alone is not sufficient to close the audit |

### Confirmed / classified identity findings

1. **ARC historical occurrences:** `Archive/ARC-*` files are retained historical artifacts. They do not compete with the active Architecture ownership solely because the numeric prefix repeats. Decision: **RETAIN / ARCHIVE**, not merge or reassign.
2. **Lifecycle collision previously identified:** the former `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` active collision is not present in the current active filename search; current owner is `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`. Decision: **MIGRATION ACCEPTED; consumer validation remains open**.
3. **No active SRV filename duplicate established:** current Service search returns ten SRV-* artifacts. This does not by itself prove internal Document-ID uniqueness inside every non-SRV file.
4. **REP namespace:** current filename search returns 19 REP-* artifacts. Because REP identifiers can occur as references in other documents, occurrences must not be counted as duplicate artifacts without path/internal-ID evidence.

**Audit boundary:** broad repository search payloads can be truncated. Therefore this round does **not** claim a repository-wide duplicate-ID PASS. It closes clearly identified active collisions but leaves exhaustive internal-ID/content reconciliation as `PARTIAL`.

## PR Review Lineage — 2026-08-14

### PR #1

PR #1 was a stale verification branch: 20 commits / 20 changed files, with two semantic Runtime Prototype changes mixed with non-executable CI markers. Its claim that no runtime behavior changed was false for the PR as a whole. **Closed without merge.**

### PR #3

PR #3 was a controlled Runtime reconciliation candidate based on an older main snapshot. Its CI failure was superseded by later candidates. **Closed without merge.**

### PR #9

PR #9 was the latest controlled candidate in this review cycle. It explicitly reconciled `REP-013` and the Runtime `REJECTED → HOLD` semantics. Run #132 produced:

- Prototype acceptance: PASS;
- canonical acceptance scenarios: PASS;
- Integration quality suite: **80 passed in 0.23s**;
- overall prototype/integration workflow: PASS.

PR #9 was **closed without merge** because passing a controlled candidate does not itself establish repository-wide integrity PASS. Its evidence remains part of the review lineage.

## Baseline Authority Finding

`Release/VERSION.md` is authoritative for release/baseline distinction and declares Development Baseline **3.2.1**. `PROJECT_STATUS.md`, `REP-001`, `REP-002`, and `RUN-001` independently align on **3.2.1**. `REP-012` previously declared **3.3.0**; that declaration has now been reconciled to **3.2.1** in REP-012 v1.0.7.

No claim is made that every file in the repository has already been revalidated against 3.2.1. Any remaining `3.3.0` declarations are follow-up targets until reconciled.

## Boot Verification — 2026-08-14

`Runtime/RUN-001_BOOT_SEQUENCE.md` was read directly from current `main`. It is Version 1.3.0, `Validated / Integrity Hold`, Canonical, Critical, Development Baseline 3.2.1. Its mandatory sequence requires repository baseline synchronization, structural integrity validation, context hydration and state commitment. Its failure rule requires FAULT/HOLD when integrity, authority, dependency or required context validation fails.

**Boot result:** **BOOTED / INTEGRITY WARNING remains the highest justified state for the inspected scope; BOOTED / INTEGRITY PASS is NOT established.** Baseline conflict has been reconciled, but the executable relationship proof and exhaustive duplicate-ID/graph audit remain open.

## Runtime → Engine → Service → Repository Evidence

Documentation establishes the intended chains:

`RUN-010 → ENG-006 → SRV-009 → REP-001/002/011`

and

`SRV-006 → SRV-007 → SRV-008 → SRV-009 → SRV-005`.

Direct reads confirm the declared responsibilities and boundaries. However, a direct repository code search found **no Python consumer references** to `ENG-006` or `SRV-009`. Therefore these relationships remain **documentation-backed / PARTIALLY VERIFIED**, not executable integration proof.

## High-Value Impact Chains

### Chain A — Search / Logging / Index / Update / Validation
`SRV-006 → SRV-007 → SRV-008 → SRV-009 → SRV-005`

### Chain B — Runtime Execution / Mutation
`RUN-010 → ENG-006 → SRV-009 → SRV-005`

### Chain C — Runtime / Repository Control Plane
`RUN-010 → ENG-006 → SRV-009 → REP-001 + REP-002 + REP-011`

### Chain D — Memory / Knowledge
`SRV-003 → SRV-004`

## Current Blocker State — 2026-08-14

| Priority | Blocker | State | Next Action |
|---|---|---|---|
| P0 | PR #1 / PR #3 obsolete verification paths | CLOSED | No further action |
| P0 | Latest candidate Runtime + Integration evidence | PASS (candidate) | Preserve evidence; no auto-merge |
| P1 | REP-012 baseline declaration | RESOLVED | Re-read and reconcile affected control-plane nodes |
| P1 | Executable RUN-010 → ENG-006 → SRV-009 proof | OPEN / PARTIAL | Locate implementation or explicitly record implementation gap |
| P1 | Exhaustive duplicate-ID/content audit | OPEN / PARTIAL | Complete namespace-by-namespace internal-ID scan |
| P1 | Bidirectional graph validation | OPEN / PARTIAL | Validate forward and reverse edges for critical paths |
| P2 | Controlled mutation + automatic reconciliation | NOT_PERFORMED | Build/execute controlled harness later |
| P2 | Final Boot PASS | BLOCKED | Re-run only after P1 graph/ID blockers close |

## Mutation Impact Contract

For every material mutation, lookup outgoing edges, incoming/reverse edges, consumers, dependencies, authority, content contract, provenance/derived artifacts and audit/session records requiring synchronization. The resulting set is the minimum targeted revalidation scope.

## Open Work

- Complete exhaustive internal Document-ID duplicate scan across all namespaces and historical/reference occurrences.
- Complete bidirectional validation.
- Complete executable consumer proof or explicitly document the implementation gap.
- Execute controlled runtime/mutation tests with evidence capture.
- Complete REP-001/REP-002/REP-011/REP-012/REP-013/REP-014 reconciliation validation after the latest REP-012 mutation.
- Re-run final acceptance/regression after any approved corrective mutation.
- Preserve provisional status until evidence supports promotion.

## Integrity State

`INTEGRITY HOLD`

## Design Principle

> **Optimize lookup, not proof.**

> **Inspect once → capture node → capture edges → capture impact → test what can be tested → explicitly record what cannot.**

End of Document