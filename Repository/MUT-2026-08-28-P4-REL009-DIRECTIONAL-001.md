# P4 REL-009 Directional Disposition Mutation Matrix

Transaction ID: `MUT-2026-08-28-P4-REL009-DIRECTIONAL-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@a538325bcde36d3a45f19583ca20d72d8f591e0a`
Working branch: `hermuz/p4-rel009-directional-disposition-20260828`
Scope: semantic disposition and evidence reconciliation for `REL-009: RUN-010 -> SRV-009` only.

## Intent

Resolve the remaining P4 ambiguity without manufacturing a reverse dependency merely to satisfy graph symmetry.

The controlled relationship remains:

`RUN-010 -> SRV-009 = CONSUMES`

The candidate disposition is intentionally directional because the source consumes a governed service capability. This transaction does not claim that every RUN-010 operation reaches SRV-009 and does not create an SRV-009 -> RUN-010 dependency.

## Current Evidence

1. `Runtime/RUN-010_RUNTIME_REFERENCE.md` explicitly describes the governed decision/execution path ending in `SRV-009 Controlled Mutation`, while explicitly limiting that statement: it is a relationship description, not a claim that every runtime operation follows that path.
2. `Services/SRV-009_UPDATE_SERVICE.md` identifies `SRV-009` as the controlled mutation service consumed by `ENG-006`; it does not independently name `RUN-010` as a caller or dependency endpoint.
3. `Architecture/ARC-006_DEPENDENCY_MODEL.md` requires dependencies to be necessary, justified and free of circular dependency.
4. `Architecture/ARC-007_INTEGRATION_MODEL.md` states Runtime may consume approved service interfaces and does not require every directional consumption relationship to be mirrored as a reverse dependency.
5. Main commit `a538325bcde36d3a45f19583ca20d72d8f591e0a` now contains:
   - pure `RUN-010 -> ENG-006` handoff construction;
   - integration-only `RUN-010 -> SRV-009` dispatch observation through the existing governed production adapter;
   - authorization identity preservation;
   - positive and fail-closed integration tests;
   - unchanged normal connected-spine simulation semantics.
6. Exact-main push workflows on `a538325b...` all completed successfully:
   - Full-Stack Repository Audit `33196013636` — SUCCESS;
   - ARGO Runtime Prototype and Integration Tests `33196013609` — SUCCESS;
   - Real Mutation Matrix Regression `33196013638` — SUCCESS;
   - M2 Multi-Channel Proposal Training `33196013623` — SUCCESS.

## Semantic Decision Boundary

Supported:

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`

Not supported:

- `BIDIRECTIONAL`;
- universal RUN-010 runtime routing through SRV-009;
- a new SRV-009 -> RUN-010 dependency;
- normal connected-spine production dispatch;
- automatic repository-wide graph closure.

## Mutation Rows

| Change ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|---|---|
| C01 | `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` | UPDATE | reconcile REL-009 as intentional one-way with bounded isolated execution evidence; keep registry synchronization explicit | N | N |
| C02 | `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` | UPDATE | reconcile B07/B08 against merged exact-main evidence and preserve non-universal boundary | N | N |
| C03 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE LATER | update only REL-009 state after complete full-content preservation candidate is available | N | N |

## Preservation Controls

KEEP unchanged:

- `Runtime/RUN-010_RUNTIME_REFERENCE.md`;
- `Services/SRV-009_UPDATE_SERVICE.md`;
- `Runtime/Execution/connected_spine_runner.py`;
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`;
- `Architecture/ARC-007_INTEGRATION_MODEL.md`;
- REL-009 source, target and relationship type;
- all unrelated `REP-014` rows and historical reconciliation content.

Unexpected Changes required: `0`.

## REP-014 Tool / Preservation Boundary

`REP-014` is a large canonical registry and GOV-014 requires complete-source preservation before replacement. The current connector write surface replaces whole file content and does not provide a server-side section patch. The local execution environment cannot independently clone GitHub.

Therefore C03 MUST remain pending until a complete current-source candidate can be constructed and verified. A truncated/snippet-based replacement is prohibited.

This tool limitation is not evidence that the relationship remains semantically unresolved; it is a mutation-safety boundary.

## Closure Rule

This transaction may advance C01/C02 to verified independently. P4/REL-009 canonical registry closure remains pending until C03 is safely applied, read back and CI-verified.

`SEMANTIC DISPOSITION != REGISTRY PERSISTENCE != P4 CANONICAL CLOSURE`.
