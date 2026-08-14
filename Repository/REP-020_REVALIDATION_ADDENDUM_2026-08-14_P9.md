# REP-020 Revalidation Addendum — PR #9 Preparation

## Evidence delta

- PR #8 Run #130: prototype acceptance PASS; canonical scenarios PASS; integration 79 PASS / 1 FAIL.
- First failing assertion: `test_repository_content_tree_uses_current_baseline_and_specification_path`.
- `REP-013@main` and `REP-013@222635a...` both contain `Specifications/01-Knowledge-Organization.md`.
- PR #8 merge snapshot `4a5d451...` did not expose the path to the test.
- Classification: **MERGE MATERIALIZATION / CHECKOUT SNAPSHOT MISMATCH**.

## Required candidate mutation

Re-audit `REP-013` without changing the canonical physical tree semantics, then rerun Integration.

## Test ledger

| TEST-ID | State |
|---|---|
| REP13-MAIN-001 | PASS |
| REP13-BASE-002 | PASS |
| PR8-INT-003 | FAIL |
| PR8-FAIL-004 | PASS |
| REP13-MERGE-007 | PENDING |
| INT-ROOT-008 | PENDING |
| REL-EXEC-009 | NOT_PERFORMED |
| BASELINE-010 | NOT_PERFORMED |
| BOOT-FINAL-011 | BLOCKED |

Integrity: **INTEGRITY HOLD**
