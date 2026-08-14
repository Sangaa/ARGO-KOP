# EJR-174 — REP-020 Matrix Update Note

This note records the latest revalidation event for REP-020 because the matrix itself must be preserved as a complete canonical working document when edited.

## New evidence to enter into REP-020

| Test ID | Check | Result | Evidence |
|---|---|---|---|
| TST-111 | PR #5 full CI result | FAIL — 78 PASS / 2 FAIL | Workflow `31773821212`, integration job `94685011564` |
| TST-112 | First failing integration assertions extracted | PASS | `test_core000_canonical_reference.py`; `test_repository_content_tree_canonicalization.py` |
| TST-113 | CORE-000 current-main contract check | PASS / stale-test identified | `Core/CORE-000_PLATFORM_ARCHITECTURE.md` current main |
| TST-114 | REP-013 current-main path check | PASS / stale-merge identified | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` current main |
| TST-115 | Current main SHA verification after checkpoint | PASS | `598a523a27fece39db71348903540ae727dde77e` |
| TST-116 | Current-main candidate revalidation | NOT_PERFORMED | Candidate not yet rebuilt at time of this closure |
| TST-117 | Executable RUN-010 → ENG-006 → SRV-009 proof | NOT_PERFORMED | Still no executable consumer evidence |
| TST-118 | Baseline 3.2.1 vs 3.3.0 authority decision | CONFLICT / NOT_PERFORMED | Governance reconciliation still open |
| TST-119 | Exhaustive duplicate internal-ID audit | PARTIAL / NOT_CLOSED | Broad repository search remains bounded |
| TST-120 | Final Boot verification | NOT_PERFORMED | Blocking evidence remains |

## Matrix state

- Version before this event: `0.1.7`
- Required next matrix version: `0.1.8`
- Integrity: **INTEGRITY HOLD**
- PR #5: superseded/stale candidate; no merge.
- Correct next candidate: current-main-based Runtime reconciliation.

## Session rule

No authority, test, or Runtime file was changed to force CI green. The next mutation must be made from current `main` and followed by CI plus matrix/test-ledger update.
