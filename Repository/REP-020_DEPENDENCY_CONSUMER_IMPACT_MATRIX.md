# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.2.2  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Current Development Baseline: **3.2.1**  
Last Audit: 2026-08-25  
Last Revalidation Evidence: `P211` / `RUN-E03 boundary reconciliation`

## Current Evidence Boundary

This matrix remains a lookup and impact-analysis surface. It does not grant authority, certify runtime coupling, or certify repository-wide integrity.

The latest bounded execution evidence is `P203`, verified by workflow run `32810102376` at commit `4284ee9265f66e4631425f3cfddd84ab42dbcfbc`. `GT-018 = VERIFIED`, `P203 = VERIFIED`, and the Full-Stack Repository Audit = PASS for that execution boundary. This evidence does not close the Connected-Baseline Completion Gate.

`P204` reconciled the stale execution-boundary wording found in root status evidence without promoting the global integrity state. `P211` reconciles a current executable-boundary consumer entry exposed by Runtime Prototype CI while preserving the distinction between isolated E2E proof and runtime service coupling.

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

## RUN-E03 — ENG-006 → SRV-009 Evidence Boundary

| Evidence ID | Relationship | Evidence Scope | Current State | Boundary |
|---|---|---|---|---|
| RUN-E03 | ENG-006 → SRV-009 | Isolated P3 E2E proof exists; runtime `RUN-010` service coupling is not established by that proof | PARTIALLY_VERIFIED | E2E execution verified in isolation; runtime-service coupling remains unproven |

`RUN-E03` is retained because the relationship registry and integrity tests require an explicit evidence row for this edge. Its `PARTIALLY_VERIFIED` classification is intentional: the isolated E2E proof verifies the governed ENG-006 → SRV-009 path in its isolated execution boundary, but does not prove that the ordinary RUN-010 runtime path dispatches through SRV-009.

Authoritative isolated E2E evidence remains `Repository/P3_EXECUTABLE_PROOF_CLOSURE_2026-08-17.md` and the P3 reconciliation addendum. Historical entries claiming that the isolated executable invocation was never performed are superseded for that narrow E2E scope, while the absence of ordinary runtime-service proof remains open.

## Control-Plane Reconciliation State

- `Release/VERSION.md` remains authoritative for official release `1.0.0` and development baseline `3.2.1`.
- `PROJECT_STATUS.md` remains the canonical summary surface but is not itself authority for repository-wide integrity.
- `REP-001` remains the canonical inventory index within its inspected scope.
- `VERIFIED_SEAM_EVIDENCE_REGISTRY.md` remains the evidence-backed seam admission surface.
- `P203` execution evidence supersedes the older statement that no successful run had been observed at that checkpoint.
- Global integrity remains `INTEGRITY HOLD` pending the broader relationship gates.

## Current Bounded Next Work

1. Preserve the distinction between isolated executable proof and ordinary runtime consumer proof.
2. Continue Services → Runtime Consumers → Repository / Index Services relationship enumeration.
3. Reconcile `SRV-001` through `SRV-009` against current Validation Engine declarations and actual consumers/dependencies.
4. Continue duplicate-ID and authority-path validation without inferring missing artifacts from numeric sequences.
5. Revalidate affected indexes/status artifacts after every material mutation.

## Historical Evidence Rule

Older entries in this matrix remain useful as provenance and prior observations. They must not be interpreted as current execution proof unless their evidence binding is explicitly refreshed.

## Interpretation

`PASS` is scope-bound. `PARTIAL` is incomplete evidence. `CONFLICT` is a detected contradiction requiring authority resolution. `NOT_PERFORMED` is not failure.

## Integrity Boundary

This matrix intentionally remains **non-authoritative**. It may narrow rediscovery and expose consumer/dependency impact, but canonical authority remains with the applicable governed artifact and current repository evidence.

---

End of Document
