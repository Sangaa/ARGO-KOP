# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.1.7  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Current Development Baseline: **3.2.1**  
Last Audit: 2026-08-14  
Last Revalidation Commit: `f74949877b4e495ae54e57ac708be6dfb8d235eb`

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
| TST-012 | Current-baseline conflict detection across control-plane records | CONFLICT DETECTED | REP-020/Release authority vs REP-012 |
| TST-013 | Content-fitness/currentness rule check | PARTIAL | Canonical control-plane scope |
| TST-014 | Cross-registry reconciliation state check | PARTIAL / OPEN | REP-011..016 |
| TST-015 | Direct read of authoritative version source | PASS | Release/VERSION.md |
| TST-016 | Reproduce REP-012 baseline claim | CONFLICT CONFIRMED | Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md |
| TST-017 | Cross-check root status against version authority | SUPPORTS 3.2.1 | PROJECT_STATUS.md |
| TST-018 | Current main commit / latest repository state check | PASS | main @ 54dc4fe138a4954db5c68154e5ee96fbdc8f905e |
| TST-019 | REP-020 current version/currentness verification before mutation | PASS | REP-020 v0.1.5 @ main; latest main commit added evidence appendix |
| TST-020 | RUN-001 boot sequence direct read | PASS | Runtime/RUN-001_BOOT_SEQUENCE.md @ main |
| TST-021 | Boot integrity completion gate | HOLD | Baseline conflict + unresolved integrity/audit scope prevent BOOTED / INTEGRITY PASS |
| TST-022 | PR #1 complete combined semantic diff inspection | PASS for changed-file diff; commit-by-commit evidence bounded | PR #1, 20 commits / 20 changed files |
| TST-023 | PR #1 main/head divergence and conflict impact review | CONFLICT | main is 505 commits ahead; PR is 20 commits ahead; runtime files diverge |
| TST-024 | Runtime → Engine → Service executable consumer search | PARTIAL / DOCUMENTATION ONLY | No Python references to ENG-006 or SRV-009 found by direct code search |
| TST-025 | Current-main acceptance expectation vs harness state logic | CONFLICT CONFIRMED | SAFE-002 expects HOLD while current main harness still contains REJECTED path |
| TST-026 | Reconciled candidate branch created from current main | PASS | ci/runtime-prototype-reconciled-20260814 |
| TST-027 | Fresh PR CI for reconciled candidate | PASS for prototype / FAIL integration | PR #3 run #117 / retry #2 |
| TST-028 | PR #3 CI retry | PASS for prototype / FAIL integration | run #117 attempt #2, candidate `54c8a3e...` |
| TST-029 | Integration failure step localization | PARTIAL | Failure isolated to `Run integration quality suite`; first assertion unavailable through exposed log endpoint |
| TST-030 | Integration failure reproducibility | PASS | Same integration failure reproduced on retry |
| TST-031 | PR #3 semantic claim vs runtime acceptance | PASS for candidate prototype behavior | Prototype acceptance + canonical scenarios passed |
| TST-032 | EJR-164 session/checkpoint persistence | PASS | main @ `f74949877b4e495ae54e57ac708be6dfb8d235eb` |
| TST-033 | REP-020 re-read before current mutation | PASS | v0.1.6, sha `c29c0f73...` |
| TST-034 | Runtime consumer expansion evidence review | PARTIAL | EJR-181 + RUN-010 + ENG-006 evidence; executable consumer still unproven |

### Tests not performed / not yet sufficient

| Test ID | Check | State | Why |
|---|---|---|---|
| TST-101 | Actual executable RUN-010 → ENG-006 → SRV-009 invocation | NOT_PERFORMED | No executable consumer path exists in inspected Python scope; documentation path remains only partially verified |
| TST-102 | Controlled repository mutation + automatic REP-001/002/011 reconciliation | NOT_PERFORMED | Requires controlled mutation environment |
| TST-103 | Automated bidirectional graph traversal across all domains | NOT_PERFORMED | REP-020 remains Phase-1 seed |
| TST-104 | Exhaustive duplicate-ID scan | PARTIAL / NOT_CLOSED | Namespace filename searches performed; full internal-ID/content scan remains tool-limited |
| TST-105 | Semantic content equivalence across all consumers | NOT_COMPLETED | Cross-layer consumer review required |
| TST-106 | Matrix program performance/load test | NOT_PERFORMED | Program not yet implemented |
| TST-107 | Final acceptance test after reconciled candidate CI | PASS for prototype; FAIL integration | Integration suite remains unresolved |
| TST-108 | Full-stack integration workflow on current main | NOT_PERFORMED | Current main has no associated workflow run at latest commit |
| TST-109 | First failing integration assertion/file/function | NOT_IDENTIFIED | GitHub check annotation exposes exit code but not pytest traceback/log body |
| TST-110 | Baseline authority reconciliation decision | NOT_PERFORMED / CONFLICT | 3.2.1 vs 3.3.0 remains unresolved; REP-012 not modified |

**Interpretation:** `PASS` is scope-bound. `PARTIAL` is incomplete evidence. `CONFLICT` is a detected contradiction requiring authority resolution. `NOT_PERFORMED` is not failure.

## Duplicate-ID Audit — 2026-08-14

The audit was performed against the current `main` tree and `REP-001` identity model. Filename namespace searches produced these current counts:

| Namespace | Current filename matches | Finding |
|---|---:|---|
| SRV-* | 10 | One current Service namespace sequence; no duplicate filename identity observed |
| REP-* | 19 | Control-plane/repository artifacts require identity-vs-reference distinction; no duplicate filename identity established by the search |
| ARC-* | 16 | Active Architecture IDs coexist with five `Archive/ARC-*` historical artifacts; archive occurrences are historical/reference, not active duplicate authority |
| LIF-* | 1 | Current lifecycle identity is unique |
| GOV-* | 16 | Current Governance namespace search did not expose a duplicate `GOV-005` filename; the former Lifecycle collision is absent from active path |
| ENG-* | 25 | Namespace requires further internal-ID reconciliation; filename search alone is not sufficient to close the audit |

### Confirmed / classified identity findings

1. **ARC historical occurrences:** `Archive/ARC-*` files are retained historical artifacts. They do not compete with the active Architecture ownership solely because the numeric prefix repeats. Decision: **RETAIN / ARCHIVE**, not merge or reassign.
2. **Lifecycle collision previously identified:** the former `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` active collision is not present in the current active filename search; current owner is `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`. Decision: **MIGRATION ACCEPTED; consumer validation remains open**.
3. **No active SRV filename duplicate established:** current Service search returns ten `SRV-*` artifacts. This does not by itself prove internal Document-ID uniqueness inside every non-SRV file.
4. **REP namespace:** current filename search returns 19 `REP-*` artifacts. Because REP identifiers can occur as references in other documents, occurrences must not be counted as duplicate artifacts without path/internal-ID evidence.

**Audit boundary:** the repository tool returned incomplete/truncated result payloads for broad tree/search responses. Therefore this round does **not** claim a repository-wide duplicate-ID PASS. It closes the clearly identified active collisions but leaves exhaustive internal-ID/content reconciliation as `PARTIAL` rather than inventing certainty.

## PR #1 Review — 2026-08-14

PR #1 is based on merge-base `bec3958e...`, while current `main` is `54dc4fe...`. Comparison shows the PR is **20 commits ahead and 505 commits behind** current main. It changes 20 files: 18 non-executable CI marker/journal files plus two Runtime Prototype files.

### Semantic Runtime changes

1. `Runtime/Prototype/cognitive_loop_harness.py`
   - removes `State.REJECTED`;
   - changes lack of human authorization from `REJECTED` to `HOLD`;
   - collapses final state selection to `PROPOSED` or `HOLD`.
2. `Runtime/Prototype/run_acceptance_scenarios.py`
   - the PR branch changed the payload mapping so `missing_evidence` receives an empty evidence list.
   - Current `main` already contains a newer equivalent mapping, so this part of PR #1 is stale relative to current main.

**Claim assessment:** `No runtime behavior is changed` is **FALSE for PR #1 as a whole**. The CI marker files are non-executable, but the two Runtime Prototype changes alter observable state/scenario behavior.

### Conflict-resolution conclusion

The authoritative merge candidate should start from current `main`, not from PR #1's stale branch. The reconciled candidate branch therefore preserves current-main `run_acceptance_scenarios.py` and applies only the authorization-state change to the current `cognitive_loop_harness.py`.

PR #2 was opened as a controlled verification vehicle for that candidate and has not been merged.

## Baseline Conflict Finding

`Release/VERSION.md` is directly identified as authoritative for release/baseline distinction and declares Development Baseline **3.2.1**. `PROJECT_STATUS.md` independently reports **3.2.1** and points to `Release/VERSION.md` as authoritative. `REP-012` declares **3.3.0**. The conflict is therefore real and remains unresolved.

Required action: resolve the canonical authority before promoting affected control-plane artifacts or changing the matrix baseline. Do not infer that 3.3.0 is current merely because it is numerically higher.

## Boot Verification — 2026-08-14

`Runtime/RUN-001_BOOT_SEQUENCE.md` was read directly from current `main`. It is Version 1.3.0, `Validated / Integrity Hold`, Canonical, Critical, Development Baseline 3.2.1. Its mandatory sequence requires repository baseline synchronization, structural integrity validation, context hydration and state commitment. Its failure rule requires FAULT/HOLD when integrity, authority, dependency or required context validation fails.

The bootstrap specification defines `BOOTED / INTEGRITY PASS` only when required baseline documents are readable, required review scope is complete, canonical identities are unique within the claimed scope, indexes and paths are aligned, critical references resolve and no blocking conflict remains within that scope.

**Boot result:** **BOOTED / INTEGRITY WARNING is the highest justified state for the inspected scope; BOOTED / INTEGRITY PASS is NOT established.** The unresolved 3.2.1/3.3.0 baseline conflict and open duplicate/relationship audit prevent a PASS claim.

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

## Mutation Impact Contract

For every material mutation, lookup outgoing edges, incoming/reverse edges, consumers, dependencies, authority, content contract, provenance/derived artifacts and audit/session records requiring synchronization. The resulting set is the minimum targeted revalidation scope.

## Current P0/P1 Closure State — 2026-08-14

### P0 — PR #3 CI
**PARTIAL:** prototype acceptance and canonical scenarios PASS; integration job FAIL. Retry reproduced the failure. The failure is localized to the `Run integration quality suite` step, but the first pytest assertion/file/function is not exposed by the available GitHub log endpoint. No test/runtime change was made to force PASS.

### P1 — Integration failure
**CONFLICT / UNRESOLVED:** reproducible failure, but semantic classification remains open until first assertion/traceback is available. Environment setup, checkout, Python setup and test-runner installation all PASS. Only the integration suite invocation fails. fileciteturn103file0

### P1 — Baseline 3.3.0
**CONFLICT:** authority reconciliation remains open. 3.2.1 remains the current matrix baseline; REP-012 has not been changed.

### P1 — Executable relationship proof
**PARTIAL:** current evidence expands the impact surface and documents the intended edges, but no executable consumer was established. EJR-181 explicitly preserves this distinction and records no PASS promotion. fileciteturn106file0

### P2 — Duplicate-ID audit
**PARTIAL / NOT CLOSED:** active filename collisions were classified; exhaustive internal-ID/content reconciliation remains open because broad search responses can be truncated.

## Session Evidence Checkpoint

`EJR-164_2026-08-14_P0_PR3_CI_AND_INTEGRATION_FAILURE_CHECKPOINT.md` records the P0/P1 checkpoint and the missing evidence required for final classification.

## Open Work

- Obtain the first failing integration pytest assertion/traceback and classify the failure.
- Resolve the **3.2.1 vs 3.3.0 baseline authority conflict**.
- Complete exhaustive internal Document-ID duplicate scan across all namespaces and historical/reference occurrences.
- Complete bidirectional validation.
- Complete executable consumer proof or explicitly document the implementation gap.
- Execute controlled runtime/mutation tests with evidence capture.
- Complete REP-001/REP-002/REP-011 reconciliation validation.
- Re-run final acceptance/regression after any approved corrective mutation.
- Preserve provisional status until evidence supports promotion.

## Integrity State

`INTEGRITY HOLD`

## Design Principle

> **Optimize lookup, not proof.**

> **Inspect once → capture node → capture edges → capture impact → test what can be tested → explicitly record what cannot.**

End of Document
