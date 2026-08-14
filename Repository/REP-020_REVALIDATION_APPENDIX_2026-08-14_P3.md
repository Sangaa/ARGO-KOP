# REP-020 Revalidation Appendix — 2026-08-14 P3

## Exact Integration Failure Closure

### TEST-ID: PR4-INTEGRATION-002
**Result: CONFLICT CONFIRMED — STALE MERGE SNAPSHOT**

PR #4 workflow `31773679111` / integration job `94684589028` executed against merge commit `b42b2f27719309e31aba31f037a99e12d86d56c6`.

Observed:
- `79 passed`
- `1 failed`
- failing test: `test_repository_content_tree_uses_current_baseline_and_specification_path`
- first failing assertion: `Specifications/01-Knowledge-Organization.md` missing from the checked-out REP-013 content tree.

Direct current-main evidence shows REP-013 v1.0.8 does contain the exact canonical path. Therefore the defect is in the stale merge snapshot, not in current-main REP-013.

### TEST-ID: PR4-CORE000-002
**Result: PASS**

The earlier CORE-000 formatting failure was removed by the controlled test-contract correction. The new run no longer reports that failure.

### Runtime status

Prototype acceptance remains PASS. The runtime authorization reconciliation has not produced a failing prototype scenario.

### Required next action

Create/rebase a verification candidate against the **latest current `main`**, preserving only the intended Runtime authorization change and the justified CORE-000 test contract correction. Do not modify REP-013 or weaken its test to accommodate a stale merge snapshot.

### Tests performed

- PR #4 prototype suite: PASS.
- PR #4 canonical scenarios: PASS.
- Integration suite: 79 PASS / 1 FAIL.
- Exact first assertion extracted: PASS.
- Current-main REP-013 read: PASS.
- Snapshot-vs-main discrepancy classified: PASS.

### Tests pending / not performed

- Fresh candidate from latest main: PENDING.
- Fresh integration suite: PENDING.
- Executable RUN-010 → ENG-006 → SRV-009: NOT_PERFORMED.
- Baseline authority reconciliation: CONFLICT.
- Exhaustive duplicate-ID closure: PARTIAL.
- Boot re-verification: NOT_PERFORMED.

**Integrity:** HOLD.
