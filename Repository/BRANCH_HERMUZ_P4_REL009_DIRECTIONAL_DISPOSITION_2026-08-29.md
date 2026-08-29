# Branch Disposition — hermuz/p4-rel009-directional-disposition-20260828

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-039`
Authority: `OPERATIONAL CLASSIFICATION ONLY`

Compared from `main@a6d5403f363a65686d721cb173a47f56a1c6c39c`:
- diverged;
- ahead_by 5;
- behind_by 163;
- merge base `a538325bcde36d3a45f19583ca20d72d8f591e0a`.

The branch matrix still states `Registry Sync Pending` and P4 remains open until REL-009 registry synchronization. Current main's matrix is later and stronger: `CLOSED / LISTED CRITICAL-EDGE SET / BOUNDED SCOPE`, with REL-009 registry synchronized and complete transaction CI evidence recorded.

Disposition:
`HISTORICAL_PRE_REGISTRY_SYNC_DIRECTIONAL_STAGE / SUPERSEDED_BY_MAIN_P4_BOUNDED_CLOSURE / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

The branch must not be replayed because doing so would regress current closure semantics back to a pre-sync state.

Non-claims:
- P4 closure is only for the listed critical-edge set;
- Connected Baseline global remains open;
- no universal RUN-010→SRV-009 routing is claimed;
- no deletion authorized;
- no new CI claim is made by this documentation-only disposition.

Learning:
When a branch contains an earlier valid intermediate state, semantic chronology outranks raw ahead-count. Merging an older pre-closure stage over a later verified closure would be regression, not recovery.
