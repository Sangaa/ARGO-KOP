# REP-020 — DEPENDENCY & CONSUMER IMPACT MATRIX

Platform: ARGO KOP  
Document ID: REP-020  
Version: 0.2.3  
Status: **Provisional / Phase-1 Seed / Not Authority**  
Current Development Baseline: **3.2.1**  
Last Audit: 2026-08-25  
Last Revalidation Evidence: `P4 REL-009 directional disposition / main 94a9bbb43432f3e098854571130778a498f76299`

## Current Evidence Boundary

This matrix remains a lookup and impact-analysis surface. It does not grant authority, certify universal runtime coupling, or certify repository-wide integrity.

The latest bounded REL-009 evidence is the P3 clean proof merged at `a538325bcde36d3a45f19583ca20d72d8f591e0a` plus the P4 semantic reconciliation merged at `94a9bbb43432f3e098854571130778a498f76299`. The evidence establishes an isolated governed RUN-010-attributed observation reaching the existing ENG-006/SRV-009 adapter while preserving the normal connected-spine non-production boundary.

Historical `P203`, `P204` and `P211` evidence remains valid for its original execution boundaries. Current evidence supersedes only the earlier claim that no independent callable/dispatch observation had been recovered for REL-009.

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
| RUN-E03 | ENG-006 → SRV-009 | Isolated P3 E2E proof exists; ordinary `RUN-010` service coupling is not established by that proof | PARTIALLY_VERIFIED | E2E execution verified in isolation; ordinary runtime-service coupling remains non-universal |

`RUN-E03` is retained because the relationship registry and integrity tests require an explicit evidence row for this edge. Its `PARTIALLY_VERIFIED` classification is intentional at this impact-matrix layer: the isolated E2E proof verifies the governed ENG-006 → SRV-009 path, but does not prove that the ordinary RUN-010 runtime path dispatches through SRV-009 on every operation.

Authoritative isolated E2E evidence remains `Repository/P3_EXECUTABLE_PROOF_CLOSURE_2026-08-17.md` plus the current P3 clean evidence. Historical entries claiming that the isolated executable invocation was never performed are superseded for that narrow E2E scope, while the absence of universal ordinary-runtime routing remains an explicit boundary.

## SERVICE_DISPATCH — RUN-010 → SRV-009 Evidence Boundary

`SERVICE_DISPATCH` now records the bounded evidence actually observed. It is no longer an absence marker.

| Evidence ID | Relationship | Evidence Scope | Current State | Boundary |
|---|---|---|---|---|
| SERVICE_DISPATCH | RUN-010 → SRV-009 | An isolated governed observation starts from RUN-010-attributed execution context, preserves authorization/provenance, and reaches the existing ENG-006/SRV-009 adapter with post-read verification | PARTIALLY_VERIFIED | Intentional directional consumption is observed in isolated integration; ordinary connected-spine routing remains unproven and no universal runtime claim is allowed |

Current interpretation:

- callable/dispatch evidence now exists in the isolated integration boundary;
- exact-main Full-Stack and Runtime/Integration CI verify the positive observation together with the negative connected-spine guard;
- `PARTIALLY_VERIFIED` here expresses scope, not lack of evidence: the ordinary connected spine remains simulation-oriented and is not claimed to route every runtime operation through SRV-009;
- provider-backed ENG-006/SRV-009 E2E and the isolated RUN-010 observation remain distinct evidence classes;
- no reverse `SRV-009 → RUN-010` dependency is implied.

## P6 Quality / Integration exact-path correlation evidence — 2026-08-29

The following in-scope regression path is explicitly bound to the already-existing bounded RUN-010 / ENG-006 / SRV-009 impact evidence so P6 correlation can discover it by exact repository-relative path:

`Quality/Integration/test_run010_eng006_handoff_contract.py`

Correlation meaning is intentionally narrow:

- P6 scope eligibility: `IN_SCOPE`;
- expected correlation state: `MAPPED`;
- promotion: `NO_AUTO_PROMOTION`;
- evidence role: direct regression coverage for the RUN-010 handoff contract and its bounded ENG-006/SRV-009 impact seam;
- relationship state remains `PARTIALLY_VERIFIED`;
- this mapping is not runtime reachability evidence and does not establish universal ordinary-runtime routing.

This exact-path binding exists to make current test-impact evidence discoverable. It does not create a new relationship and does not widen the semantic authority of this provisional matrix.

## Control-Plane Reconciliation State

- `Release/VERSION.md` remains authoritative for official release `1.0.0` and development baseline `3.2.1`.
- `PROJECT_STATUS.md` remains the canonical summary surface but is not itself authority for repository-wide integrity.
- `REP-001` remains the canonical inventory index within its inspected scope.
- `VERIFIED_SEAM_EVIDENCE_REGISTRY.md` remains the evidence-backed seam admission surface.
- P3/P4 current evidence supersedes the older REL-009 absence claim only within the declared bounded execution scope.
- Global integrity remains `INTEGRITY HOLD` pending broader relationship/domain gates.

## Current Bounded Next Work

1. Preserve the distinction between isolated executable observation and universal ordinary-runtime routing.
2. Continue Services → Runtime Consumers → Repository / Index Services relationship enumeration after current P4 disposition is canonically synchronized.
3. Reconcile `SRV-001` through `SRV-009` against current Validation Engine declarations and actual consumers/dependencies.
4. Continue duplicate-ID and authority-path validation without inferring missing artifacts from numeric sequences.
5. Revalidate affected indexes/status artifacts after every material mutation.

## Historical Evidence Rule

Older entries in this matrix remain useful as provenance and prior observations. They must not be interpreted as current execution proof unless their evidence binding is explicitly refreshed.

## Interpretation

`PASS` is scope-bound. `PARTIAL` is incomplete or deliberately bounded evidence. `CONFLICT` is a detected contradiction requiring authority resolution. `NOT_PERFORMED` is not failure.

## Integrity Boundary

This matrix intentionally remains **non-authoritative**. It may narrow rediscovery and expose consumer/dependency impact, but canonical authority remains with the applicable governed artifact and current repository evidence.

---

End of Document
