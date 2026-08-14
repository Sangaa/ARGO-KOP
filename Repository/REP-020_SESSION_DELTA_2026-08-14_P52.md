# REP-020 — SESSION DELTA — 2026-08-14 — P52

Platform: ARGO KOP  
Document ID: REP-020-P52  
Status: Evidence / Integrity Hold  
Source authority: current `main`

## Objective

Continue Priority 2 duplicate-ID audit using the mandatory multi-method search discipline. P52 audits the `DEC-*` namespace and tests whether search results agree with direct current-main content. Any negative result is treated as bounded until independently disproven or confirmed.

## Three-Method Search

| Test | Method | Result | Decision |
|---|---|---|---|
| P52-S1 | Namespace/path-oriented search for `DEC-` | Recovered DEC-001 through DEC-010 plus cross-layer references; result set was bounded/truncated | PASS / PHYSICAL SURFACE |
| P52-S2 | Alternate structural/content search for `Decision DEC-001 DEC-002 DEC-003 DEC-004` | Returned DEC-010 only | PASS / PARTIAL COVERAGE; NOT NEGATIVE PROOF |
| P52-S3 | Semantic search for `decision lifecycle validation governance traceability risk assessment` | Recovered DEC-002 and DEC-010 plus related risk/runtime artifacts | PASS / SEMANTIC CROSS-CHECK |
| P52-S4 | Direct current-main retrieval of DEC-010 | Found a real identity mismatch: filename/index position `DEC-010`, internal Document ID incorrectly declared `DEC-001` | PASS / DEFECT CONFIRMED |
| P52-S5 | Direct current-main retrieval of DEC-001 | Confirmed `DEC-001` is independently and correctly declared by DEC-001 Decision Model | PASS / COLLISION CONFIRMED |

## Search Failure / Why the File Was Not Found

The alternate content search did not return DEC-001 through DEC-004 even though direct retrieval confirms those files exist. This is therefore classified as bounded search coverage, not file absence.

The more important discovery came from direct retrieval: `Decision/DEC-010_DECISION_INDEX.md` existed, but its internal `Document ID` was incorrectly set to `DEC-001`. A second direct read of `Decision/DEC-001_DECISION_MODEL.md` confirmed that `DEC-001` is legitimately owned by the Decision Model. The mismatch was therefore a real identity collision/stale internal header, not a search artifact.

## Corrective Mutation

`Decision/DEC-010_DECISION_INDEX.md` was updated on `main` so its internal identity now reads `Document ID: DEC-010`, matching its filename and index role.

The updated file was re-read from current `main` after mutation and confirmed to contain `Document ID: DEC-010`.

## Identity Findings

- `DEC-001` — Decision Model — independently confirmed as `Document ID: DEC-001`.
- `DEC-010` — Decision Index — now independently confirmed as `Document ID: DEC-010` after correction.
- The pre-mutation DEC-010 header was a confirmed duplicate internal identity for DEC-001.

## Duplicate-ID Decision

**One real internal-ID collision was found and corrected within the inspected DEC namespace.**

The correction does not close the repository-wide duplicate-ID blocker. It demonstrates why filename-only inventory and search-only negatives are insufficient; internal `Document ID` extraction and direct verification remain necessary.

## Matrix Edges

`DEC-010 → DEC-001..DEC-009` — canonical navigation/index relationship; directly documented.

`DEC-001 → Governance / Knowledge / Memory / Runtime / Repository` — documented dependencies; not executable proof.

`DEC-010 identity correction → REP-020 evidence` — mutation/evidence edge.

`P52 search coverage anomaly → repository search-method discipline` — search-method evidence.

## Tests Completed

- Namespace/path search.
- Alternate structural/content search.
- Semantic search.
- Direct read of DEC-010 before mutation.
- Direct read of DEC-001 to establish legitimate ownership.
- Identity collision classification.
- Corrective mutation of DEC-010.
- Direct re-read of DEC-010 after mutation.
- Matrix/evidence documentation.

## Tests Not Completed

- Deterministic repository-wide extraction of every internal `Document ID` declaration.
- Exhaustive duplicate classification across every namespace.
- Full DEC cross-layer bidirectional validation.
- Executable runtime proof for Decision edges.
- Final Boot verification.

## Permanent Learning Decision

**NO NEW MEM-009 LESSON.**

The finding is a concrete instance of existing rules: internal identity must be verified independently of filename/search results, and a search miss cannot prove absence. No materially new reusable engineering principle was established.

## Resume Point

Continue Priority 2 with the next namespace. Preserve the confirmed DEC-010 correction. After namespace sampling, perform deterministic repository-wide internal-ID extraction before declaring the duplicate-ID blocker closed.

## Checkpoint Closure

`P52 = CLOSED FOR THIS CHECKPOINT`

`DEC duplicate audit = ONE COLLISION FOUND AND CORRECTED / REPOSITORY-WIDE AUDIT OPEN`

`ARGO = INTEGRITY HOLD`

`FINAL BOOT = BLOCKED`
