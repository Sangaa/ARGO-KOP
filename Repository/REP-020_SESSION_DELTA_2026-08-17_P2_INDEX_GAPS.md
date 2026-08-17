# P2 — Confirmed Canonical Index Scope Gaps

Date: 2026-08-17
Status: Open / Master-Index Reconciliation Pending

## Confirmed Domains

### Intelligence

Current `Intelligence/_FOLDER_STATUS.md` declares:

- Status: `COMPLETED`
- Canonical: `Yes`
- Master Index Cross-Reference: `Synchronized`

Current canonical artifacts confirmed directly:

- `Intelligence/INT-001_INTELLIGENCE_LAYER.md`
- `Intelligence/INT-002_PATTERN_EXTRACTION.md`
- `Intelligence/INT-003_ANOMALY_DETECTOR.md`

These three artifacts are currently outside the active Master Index identity set detected by the P2 audit and therefore constitute a real current index-scope gap unless REP-001 authority is amended to explicitly include them.

### Repository

Current `Repository/_FOLDER_STATUS.md` declares:

- Status: `APPROVED`
- Inventory: `Completed`
- Navigation Review: `Completed`
- Folder Approval: `Approved`

The P2 audit identifies these canonical repository artifacts outside the active Master Index identity set:

- `Repository/REP-004_REPOSITORY_NAVIGATION.md`
- `Repository/REP-005_REPOSITORY_COMPONENTS.md`
- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`
- `Repository/REP-008_REPOSITORY_BASELINE.md`

These are current index-scope gaps requiring explicit REP-001 reconciliation.

## Non-Closure Groups

Core and Knowledge are intentionally not auto-promoted from this checkpoint because:

- Core remains `INTEGRITY HOLD — RE-AUDIT IN PROGRESS` with folder certification pending;
- Knowledge remains `INTEGRITY HOLD` with canonical validation pending consolidated repository-wide validation.

Their canonical-unindexed state remains an open scoped reconciliation item, not an assumed indexing error.

## P2 Decision

P2 remains `OPEN`.

Required next mutation:

`REP-001 current full-content read → add confirmed Intelligence/Repository bindings → full-content write → read-back → CI → rerun P2 audit`.
