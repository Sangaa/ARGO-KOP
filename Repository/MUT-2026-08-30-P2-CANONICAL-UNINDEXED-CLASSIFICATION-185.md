# MUT-2026-08-30-P2-CANONICAL-UNINDEXED-CLASSIFICATION-185

Date: 2026-08-30
Lease: `R71-20260830-P2-CANONICAL-UNINDEXED-CLASSIFICATION-185`
Execution role: HERMUZ
Entry baseline: `main@9a154b6cc71e63bb8f95edf11375919a328e2f96`
Status: `PREWRITE / LEASE ACTIVE / CANONICAL-UNINDEXED CLASSIFICATION`

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

The detector excludes recognized deferred domains before raising `canonical_unindexed`; therefore these paths require explicit semantic classification rather than being assumed safe merely because their domain is generally under review.

## Objective

Classify each path into one of:

- `SHOULD-BE-INDEXED` — current repository evidence establishes active/canonical discoverability obligation.
- `DECLARED-CANONICAL-BUT-DOMAIN-HOLD` — file self-declares canonicality, but current domain authority/status does not support indexing as active canonical inventory yet.
- `LEGACY-OR-STALE-CANONICAL-CLAIM` — canonical marker is historical/stale or contradicted by stronger current evidence.
- `NAVIGATION-SURFACE` — canonical navigation/status helper whose indexing obligation differs from a domain authority artifact.
- `UNRESOLVED` — insufficient evidence.

## Allowed paths

- this Lease 185 record
- new bounded Repository classification evidence
- direct reads/search/history for the 15 target paths and their current folder/domain status

No target artifact mutation is authorized by this classification lease.

## Forbidden paths

- `Repository/REP-001_*` mutation
- `Repository/REP-002_*` mutation
- `Repository/REP-014_*` mutation
- `Repository/REP-016_*` mutation
- any target path mutation
- any domain authority promotion
- branch deletion
- force ref mutation

## C1-C6

- C1 PASS — unique lease path.
- C2 PASS — classification only; no index or canonical marker changes.
- C3 PASS — self-declared Canonical cannot override current domain/index authority.
- C4 PASS — classification does not close P2 or promote a domain.
- C5 PASS — exact-head audit artifact provides the target population; direct current authority/status reads will provide disposition evidence.
- C6 PASS — Leases 183 and 184 are closed; this is the next independent P2 population.

## Stop conditions

HOLD if:

- self-declared canonicality conflicts with current folder/domain status;
- indexing would implicitly promote an unresolved domain;
- a path is navigation-only and current indexing policy is unclear;
- REP-001 and REP-002 disagree about the target's active role;
- protected-index mutation would be required before classification itself is complete.

Initial state:

`P2_CANONICAL_UNINDEXED_CLASSIFICATION_185 = IN_PROGRESS / NO INDEX MUTATION AUTHORIZED`.