# MUT-2026-08-30-P2-CANONICAL-UNINDEXED-CLASSIFICATION-185

Date: 2026-08-30
Lease: `R71-20260830-P2-CANONICAL-UNINDEXED-CLASSIFICATION-185`
Execution role: HERMUZ
Entry baseline: `main@9a154b6cc71e63bb8f95edf11375919a328e2f96`
Status: `CLOSED / 15-PATH CLASSIFICATION COMPLETE / NO INDEX MUTATION`

## Trigger evidence

The last exact-head Internal Document-ID artifact `9728177701` reported 15 non-deferred `canonical_unindexed_paths`:

1. `Architecture/README.md`
2. `Core/ARGO_KERNEL.md`
3. `Core/Core.md`
4. `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
5. `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
6. `Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md`
7. `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
8. `Knowledge/KNW-005_KNOWLEDGE_GOVERNANCE.md`
9. `Knowledge/KNW-006_KNOWLEDGE_QUALITY.md`
10. `Knowledge/KNW-007_KNOWLEDGE_BASELINE.md`
11. `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md`
12. `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
13. `Knowledge/KNW-010_KNOWLEDGE_MAINTENANCE.md`
14. `Quality/QLT-001_QUALITY_ASSURANCE.md`
15. `Templates/README.md`

## Classification result

Detailed evidence:

`Repository/P2_CANONICAL_UNINDEXED_CLASSIFICATION_185_2026-08-30.md`

Final bounded counts:

- `SHOULD-BE-INDEXED = 3`
- `DECLARED-CANONICAL-BUT-DOMAIN-HOLD = 10`
- `NAVIGATION-SURFACE / DOMAIN RE-AUDIT = 1`
- `NAVIGATION-SURFACE / RECONSTRUCTION-HOLD = 1`
- `UNRESOLVED = 0`

### SHOULD-BE-INDEXED

- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`

Current evidence establishes these as reviewed/current canonical or canonical-registry surfaces whose exact paths are missing from REP-001/REP-002 active discoverability. Mapping them does not certify their domains.

### DECLARED-CANONICAL-BUT-DOMAIN-HOLD

- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `Knowledge/KNW-005_KNOWLEDGE_GOVERNANCE.md`
- `Knowledge/KNW-006_KNOWLEDGE_QUALITY.md`
- `Knowledge/KNW-007_KNOWLEDGE_BASELINE.md`
- `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Knowledge/KNW-010_KNOWLEDGE_MAINTENANCE.md`

`Knowledge/_FOLDER_STATUS.md` explicitly keeps canonical validation pending consolidated repository-wide validation and folder approval on HOLD. Therefore self-declared canonicality does not authorize active-index admission.

### NAVIGATION / DOMAIN-STATE BOUNDARIES

- `Architecture/README.md` — directory handbook/navigation surface; Architecture remains under re-audit and current promoted set excludes it.
- `Templates/README.md` — canonical directory navigation/policy surface with `Reconstruction In Progress`; no auto-index promotion.

## C1-C6 closure

- C1 PASS — unique lease/evidence paths.
- C2 PASS — no target artifact or index was mutated.
- C3 PASS — local Canonical flags were reconciled against stronger domain/index state rather than treated as unilateral authority.
- C4 PASS — no Knowledge, Architecture, Templates, Core or Quality global promotion was made.
- C5 PASS — classification is backed by exact-head audit population plus direct current file/folder-status evidence.
- C6 PASS — next work is a separately governed protected index/map synchronization for only three paths.

## Learning retained

`CANONICAL FIELD != ACTIVE INDEX ADMISSION.`

`DOMAIN HOLD CAN OVERRIDE LOCAL PROMOTION ELIGIBILITY WITHOUT INVALIDATING THE DOCUMENT.`

`INDEXING A CURRENT CANONICAL ARTIFACT != CERTIFYING ITS DOMAIN.`

`NAVIGATION SURFACE CAN BE CANONICAL WITHOUT BELONGING TO THE CURRENT PROMOTED AUTHORITY SET.`

## Closure result

`P2_CANONICAL_UNINDEXED_CLASSIFICATION_185 = CLOSED / EVIDENCE-CLASSIFIED`

`PRIORITY_2_REPOSITORY_WIDE_IDENTITY_RECONCILIATION = OPEN`

## Next legal action

Open a protected REP-001/REP-002 discoverability synchronization lease for exactly:

- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`

The transaction must use a same-change-set Mutation Matrix, fresh live parent/tree, atomic fast-forward with `force=false`, exact changed-file comparison, read-back, and exact-head CI.

The ten KNW paths, `Architecture/README.md`, and `Templates/README.md` are explicitly excluded from that transaction.