# EJR-178 — 2026-08-14 PR #6 Revalidation + Matrix Checkpoint

## Scope

Repository: `Sangaa/ARGO-KOP`

Latest main before this checkpoint: `68f7d5c5a26fd7c0aa055d34a59fbe7e1312cfb8`

Integrity state: `INTEGRITY HOLD`

Matrix authority: `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` v0.1.7

## CI Evidence

### TST-121 — PR #6 CI

Result: **FAIL / REPRODUCED**

Run: `31774649867` (#125)

Prototype tests: PASS.

Integration suite: FAIL with `78 passed, 2 failed`.

Observed failures:

1. `test_architecture_readme_points_to_canonical_core000` expected `Document ID: CORE-000`, while canonical CORE-000 uses the two-line metadata form `Document ID` / `CORE-000`.
2. `test_repository_content_tree_uses_current_baseline_and_specification_path` failed in the PR merge snapshot because that snapshot was based on an older main state; current main `REP-013` contains `Specifications/01-Knowledge-Organization.md`.

Conclusion: PR #6 did not provide a valid final validation of current main. Runtime prototype behavior remained PASS; integration was blocked by stale/incorrect test contract and stale merge snapshot.

## TST-122 — CORE-000 test contract inspection

Result: **PASS / ROOT CAUSE CONFIRMED**

Current canonical CORE-000 evidence uses:

`Document ID`\n`CORE-000`

and

`Canonical`\n`Yes`

The integration test was corrected on `main` to test the actual canonical metadata format without changing CORE-000 itself.

Commit: `68f7d5c5a26fd7c0aa055d34a59fbe7e1312cfb8`

## TST-123 — REP-013 current-main inspection

Result: **PASS / CURRENT MAIN CONSISTENT**

Current `REP-013` contains the canonical specification path:

`Specifications/01-Knowledge-Organization.md`

No REP-013 content mutation was required by this checkpoint.

## TST-124 — Current-main revalidation boundary

Result: **PENDING**

A fresh runtime candidate must be based on the post-fix current `main`, not PR #6's older base snapshot.

## Matrix Delta

Add/record in REP-020 test ledger:

| Test ID | Check | Result | Scope |
|---|---|---|---|
| TST-121 | PR #6 fresh CI | FAIL / REPRODUCED | PR #6 / current-main comparison |
| TST-122 | CORE-000 test contract inspection | PASS / ROOT CAUSE CONFIRMED | CORE-000 integration test |
| TST-123 | REP-013 current-main inspection | PASS | Repository content tree |
| TST-124 | Fresh current-main runtime candidate | PENDING | Runtime + Integration |

### Tests not performed / not yet sufficient

| Test ID | Check | State | Why |
|---|---|---|---|
| TST-125 | Fresh current-main CI after test-contract correction | NOT_PERFORMED | Candidate must be created from the new main commit |
| TST-126 | Full integration suite PASS on corrected current-main candidate | NOT_PERFORMED | Blocked pending TST-125 |
| TST-127 | Executable RUN-010 → ENG-006 → SRV-009 invocation | NOT_PERFORMED | No executable consumer proof established |
| TST-128 | Final boot integrity gate | NOT_PERFORMED | Integrity HOLD remains |

## Decision

Do not merge PR #6.

Do not alter CORE-000 or REP-013 to satisfy the stale test snapshot.

Use the corrected current `main` as the sole base for the next controlled candidate.
