# P2 IDENTITY-OWNER CLASSIFICATION — NON-EJR PASS — LEASE 183

Date: 2026-08-30
Execution role: HERMUZ / Room71
Baseline inspected: `main@ada1c3724bb476b0b4b80bd551469ef1786dd092`
Source audit artifact: `internal-document-id-audit-report` / artifact `9728177701`
Scope: 23 non-EJR keys from `ambiguous_duplicate_ids`
State: `CLASSIFIED / NO IDENTITY MUTATION / P2 REMAINS OPEN`

## Classification rule

This pass does not treat token equality as identity ownership.

For each ambiguity group the evidence was interpreted through:

`PATH → ARTIFACT CLASS → EXPLICIT METADATA → CANONICAL/STATUS → INDEX/CONTROL ROLE → H1 ROLE → OWNER DISPOSITION`

A current canonical or control artifact with explicit metadata may coexist with mutation matrices, review/closure records, templates, tests, and addenda whose H1 names the subject/series. Those secondary records are not promoted to competing identity owners merely because the first-H1 fallback sees the same token.

Where no single current owner is proved, the group remains a series/child or unresolved class. No ID is invented to reduce the ambiguity count.

## Evidence anchors

- `Repository/REP-001_MASTER_INDEX.md` identifies itself as canonical (`Document ID: REP-001`, `Canonical: Yes`) and explicitly inventories current active Governance, Runtime and Repository control-plane owners including GOV-015, GOV-016, REP-011, REP-012, REP-014 and RUN-010 within its inspected scope.
- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md` is `ACTIVE / GOVERNED` and directly identifies `Templates/GOV-015_EXECUTION_RECORD_TEMPLATE.md` as the reusable execution-record template, proving the template is a template surface rather than a second governing owner.
- `Quality/QLT-001_QUALITY_ASSURANCE.md` declares `Document ID: QLT-001`, `Canonical: Yes`, while `Repository/QLT001_SEMANTIC_REPAIR_CLOSURE_155_2026-08-29.md` explicitly records a bounded repair closure against QLT-001.
- `Runtime/RUN-010_RUNTIME_REFERENCE.md` declares `Document ID: RUN-010`, `Canonical: Yes`; `Repository/RUN010_HANDOFF_COVERAGE_CLOSURE_2026-08-29.md` is explicitly a direct-test-coverage closure whose mutation affected only an integration test.
- `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md` declares `Document ID: REP-011`, `Canonical: Yes`; `REP-011_P226_RECONCILIATION_ADDENDUM_2026-08-16.md` explicitly calls itself an Addendum and says it records current-session mutations without rewriting the historical REP-011 ledger body.
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` declares `Document ID: REP-012`, `Canonical: Yes`; `REP-012_RECONCILIATION_DECISION_2026-08-14.md` explicitly calls itself a Governance Decision Record and states that no authority is changed by that decision record alone.
- `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` declares `Document ID: REP-016` and `Status: Active / Phase 1 Open / Integrity Hold`.
- `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` declares `Document ID: REP-020` but also `Status: Provisional / Phase-1 Seed / Not Authority`, establishing a parent lookup/impact surface rather than universal repository authority.
- `Repository/KRS-001_SCHEMA_REFINEMENT_V0.3.md` explicitly says v0.2 is retained as a historical pilot schema; therefore repeated KRS-001 headings include versioned schema lineage and pilot/evidence artifacts, not a clean single-owner collision model.
- `Repository/KRS-002_KNOWLEDGE_OBJECT_BLOB_CANDIDATE.md` is explicitly `CANDIDATE / NOT CANONICAL`.
- `Quality/Integration/GEN-001_ELEVENTH_RULE_TEST.md` is explicitly `Prototype / Integrity Hold`, and does not establish a canonical GEN-001 authority.
- `Repository/MUT-2026-08-18-REL009-EXECUTABLE-EVIDENCE-RECONCILIATION_MATRIX.md` is explicitly a GOV-014 Mutation Matrix with transaction ID `MUT-2026-08-18-REL009-EVIDENCE-001`; its `REL-009` H1 names the relationship/evidence target, not a document authority claim.

## Non-EJR classification table

| Observed key | Classification | Proved owner / role | Disposition |
|---|---|---|---|
| `GOV-015` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md` is active governed owner; Repository review + Templates execution-record template are secondary artifact classes | Not a competing document-owner collision |
| `GOV-016` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` is current Governance owner; reconciliation Mutation Matrix is evidence/control surface | Not a competing document-owner collision |
| `QLT-001` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Quality/QLT-001_QUALITY_ASSURANCE.md` is approved canonical; three Repository records are disposition/closure/reference-resolution evidence | Not a competing document-owner collision |
| `RUN-010` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Runtime/RUN-010_RUNTIME_REFERENCE.md` is canonical; integration test matrix and closure record are test/evidence surfaces | Not a competing document-owner collision |
| `REP-001` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Repository/REP-001_MASTER_INDEX.md` is canonical master index; six MUT/section matrices are transaction evidence | Not a competing document-owner collision |
| `REP-002` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Repository/REP-002_REPOSITORY_MAP.md` is active repository map; two MUT/section matrices are transaction evidence | Not a competing document-owner collision |
| `REP-011` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | canonical traceability ledger + three reconciliation addenda | Addenda extend evidence; they do not replace owner |
| `REP-012` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | canonical allocation registry + one Governance Decision Record | Decision record is not a second owner |
| `REP-014` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` is control-plane relationship owner; MUT matrix is transaction evidence | Not a competing document-owner collision |
| `REP-016` | `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS` | active Phase-1 queue; status-freshness and session-closure records are evidence records | Not a competing document-owner collision |
| `REL-009` | `REGISTRY_RELATIONSHIP_ID_WITH_EVIDENCE_TITLE_SHADOWS` | REL-009 is a relationship/evidence identity discussed through GOV-014 mutation matrices; the matrices declare transaction IDs distinct from REL-009 | Not a competing document identity owner; relationship semantics remain governed by REP-014/evidence |
| `GEN-001` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | prototype Quality/Integration test family plus CI-harness mutation matrix; no canonical owner proved in this pass | HOLD / no rename or promotion |
| `KRS-001` | `SERIES_WITH_EXPLICIT_SUCCESSION` | schema v0.3 explicitly retains v0.2 as historical; remaining KRS-001 pilot/object/mutation matrices are versioned/pilot evidence surfaces | Identity family is structured lineage, but a single canonical document owner is not asserted here |
| `KRS-002` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | candidate model explicitly `NOT CANONICAL` plus pilot mutation matrix | HOLD / candidate lineage only |
| `REP-020` | `PARENT_SERIES_WITH_ADDENDA / NOT_AUTHORITY` | provisional REP-020 impact matrix explicitly `Not Authority`; large family of matrix/addendum/session-delta records use parent REP-020 series label | Not treated as hundreds of competing authority owners; parent-series child identity still requires normalized model before detector suppression |
| `REP-021` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | P2 index-scope reconciliation + later session closure/delta records | HOLD / series semantics; no current canonical owner proven by this pass |
| `REP-022` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | current-priority reconciliation records + session deltas | HOLD / series semantics |
| `REP-023` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/closure family | HOLD / series semantics |
| `REP-024` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/prewrite family | HOLD / series semantics |
| `REP-026` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/runtime-gate family | HOLD / series semantics |
| `REP-027` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/reconciliation-closure family | HOLD / series semantics |
| `REP-028` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/matrix-closure family | HOLD / series semantics |
| `REP-029` | `SERIES_OR_CHILD_IDENTITY_UNRESOLVED` | session-delta/checkpoint family | HOLD / series semantics |

## First-pass result

All 23 non-EJR ambiguity keys now have a bounded semantic classification.

Disposition counts:

- `INDEXED_OWNER_WITH_EVIDENCE_TITLE_SHADOWS = 10`
- `REGISTRY_RELATIONSHIP_ID_WITH_EVIDENCE_TITLE_SHADOWS = 1`
- `SERIES_WITH_EXPLICIT_SUCCESSION = 1`
- `PARENT_SERIES_WITH_ADDENDA / NOT_AUTHORITY = 1`
- `SERIES_OR_CHILD_IDENTITY_UNRESOLVED = 10`
- `PROVED_TRUE_DUPLICATE = 0` within this non-EJR pass

This does not alter the raw detector count. The raw count remains evidence of token-level ambiguity until a future classification-aware detector contract is separately designed and tested.

## Why no detector mutation was made

A generic automatic rule such as `one explicit metadata owner + any number of H1-only files = no conflict` is not yet proven safe across the whole repository. A legacy H1-only artifact could still be a real competing identity owner. EJR-013 already proves that true duplicates exist in the repository.

Therefore Lease 183 prefers evidence classification over hiding raw ambiguity.

`CLASSIFICATION PRECEDES SUPPRESSION.`

## P2 impact

The 23 non-EJR keys are no longer an undifferentiated blocker population. However Priority 2 remains OPEN because:

1. 122 EJR ambiguity keys remain to be stratified;
2. 15 canonical-unindexed records remain unresolved;
3. the series/child classes above still need a normalized identity model before any raw audit suppression is legal;
4. EJR-013 remains a proved true unresolved duplicate identity.

## Learning

- `TITLE TOKEN MATCH != IDENTITY OWNERSHIP`.
- `ARTIFACT CLASS IS PART OF IDENTITY-COLLISION ANALYSIS`.
- `ADDENDUM / MUTATION / CLOSURE / TEMPLATE / TEST SURFACES MUST NOT SILENTLY BECOME PEER AUTHORITY OWNERS`.
- `A SERIES LABEL MAY BE A NAVIGATION/LINEAGE KEY WITHOUT BEING A UNIQUE LEAF DOCUMENT ID`.
- `CLASSIFICATION PRECEDES SUPPRESSION`.

## Next legal action

Close Lease 183 as the non-EJR classification subgate, then open a new bounded EJR stratification lease.

The next EJR pass must remain read-only and distinguish at minimum:

`PROVED_TRUE_DUPLICATE / EXPLICITLY_NONCANONICAL_PAIR / JOURNAL_SERIES_OR_SESSION_VARIANT / HISTORICAL_SHADOW / UNRESOLVED`.

No EJR rename, delete, reassignment, archive move, or synthetic suffix is authorized.