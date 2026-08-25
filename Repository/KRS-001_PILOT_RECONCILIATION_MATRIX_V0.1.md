# KRS-001 Pilot Reconciliation Matrix v0.1

Status: CONTROLLED / ANALYSIS-ONLY

## Purpose
Compare Pilot 1 (canonical interface) and Pilot 2 (governance control) before authorizing another heterogeneous pilot or any migration.

| Dimension | Pilot 1 — INTF-006 | Pilot 2 — GOV-013 | Learning / decision |
|---|---|---|---|
| Source authority | Interface source remains canonical | Governance source remains canonical | Preserve source authority |
| Currentness | CURRENT-BUT-STALE-DEPENDENCY | CURRENT-VERIFIED | Currentness must be explicit and typed |
| Provenance | commit + CI lineage | source ref + direct-change history | Immutable/traceable provenance required |
| Relationships | architecture/integration/runtime/test | supplements/operationalized-by/verified-by | Relationship types need evidence |
| Evidence | structural/contract/runtime boundaries | canonical/change-history/governance relation | Evidence must be claim-scoped |
| Assertions | bounded contract assertions | policy assertions with validity | Assertions need lifecycle |
| Constraints | production/sensing safety | authority/migration safety | Constraints need authority + enforcement surface |
| History | P223/P224 state transitions | pre-write → pilot-verified | History must remain append-only |
| Payload strategy | intentionally partial | human-readable source-owned | Do not duplicate source unnecessarily |
| Integrity | pilot assertion | source/object/traceability | Integrity must separate source from object |

## Schema gaps to resolve before next pilot
1. `SOURCE_BLOB_SHA` must be populated with an actual immutable blob SHA, not descriptive text.
2. `SOURCE_REF` and `CURRENTNESS_AS_OF` require a precise commit/HEAD identity rather than ambiguous `main` wording.
3. Relationship targets should carry stable identity plus target version/currentness evidence.
4. Pilot 1 and Pilot 2 use slightly different serialization styles; v0.2 should define one canonical envelope grammar.
5. Evidence records should distinguish direct source evidence, derived evidence, and CI/runtime evidence.
6. `CURRENT-BUT-STALE-DEPENDENCY` needs explicit dependency IDs and the reason for staleness.
7. Integrity should include content/object identity where available, not only status labels.

## Decision
KRS v0.2 is not yet authorized for bulk migration. The next pilot should target a runtime/provenance artifact only after these gaps are addressed in a controlled schema refinement.

## Required next action
Schema v0.3 design and validation against the two existing pilots. No source replacement and no bulk migration.
