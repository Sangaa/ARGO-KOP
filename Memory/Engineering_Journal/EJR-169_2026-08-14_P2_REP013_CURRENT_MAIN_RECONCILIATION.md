# EJR-169 — 2026-08-14 REP-013 Current-Main Reconciliation

## Finding

PR #4 CI run `31773679111` used merge commit `b42b2f2`, whose `REP-013` snapshot did not contain `Specifications/01-Knowledge-Organization.md`.

A direct read of current `main` proves `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` version `1.0.8` does contain:

```text
Specifications/
├── README.md
└── 01-Knowledge-Organization.md
```

Therefore the remaining integration failure is a **STALE MERGE SNAPSHOT**, not evidence that current `main` lacks the specification path.

## CI evidence

Run `31773679111` / integration job `94684589028`:

- 79 passed
- 1 failed
- failing test: `test_repository_content_tree_uses_current_baseline_and_specification_path`
- exact failing assertion: `assert "Specifications/01-Knowledge-Organization.md" in tree`

This is stronger than the previous diagnosis because the first failure is now directly identified from the CI log.

## Decision

Do not modify `REP-013` to add content that is already present on current `main`.
Do not weaken the test.
The correct corrective action is to rebase/recreate the candidate against the latest `main` so the CI merge snapshot includes the current REP-013.

## Tests performed

- PR #4 prototype acceptance: PASS.
- PR #4 canonical acceptance scenarios: PASS.
- PR #4 integration suite: 79 PASS / 1 FAIL.
- First failing assertion extraction: PASS.
- Current-main REP-013 direct read: PASS.
- Merge-snapshot comparison: CONFLICT CONFIRMED.

## Not performed

- Fresh candidate rebased onto latest `main`: pending.
- Integration rerun after fresh candidate: pending.
- Full executable relationship proof: not performed.
- Baseline authority reconciliation: unresolved.
- Exhaustive duplicate-ID closure: partial.
- Boot re-verification: not performed.

## Integrity

**INTEGRITY HOLD** remains mandatory.
