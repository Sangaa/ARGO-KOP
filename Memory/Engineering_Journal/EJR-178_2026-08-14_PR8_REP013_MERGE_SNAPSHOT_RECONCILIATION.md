# EJR-178 — PR #8 / REP-013 Merge Snapshot Reconciliation

## State

- Repository: `Sangaa/ARGO-KOP`
- Current main: `222635aea2d173400acc4697e520d43a6b2d2ee1`
- Integrity: **INTEGRITY HOLD**
- Date: 2026-08-14

## Evidence

`Repository/REP-013_REPOSITORY_CONTENT_TREE.md` was read directly at `main@222635a...` and contains:

`Specifications/01-Knowledge-Organization.md`

The same file was read at the exact base commit `222635a...` and contains the same canonical path.

However, PR #8 integration run #130 checked out merge ref `4a5d451...` and the integration test reported that the path was absent from the checked-out `REP-013` content.

Therefore the observed failure is classified as:

**MERGE MATERIALIZATION / PR CHECKOUT SNAPSHOT MISMATCH**

It is not currently classified as a defect in the canonical `REP-013` on `main`.

## Tests

| Test ID | Check | Result |
|---|---|---|
| REP13-MAIN-001 | Read REP-013 at current main | PASS |
| REP13-BASE-002 | Read REP-013 at PR #8 base SHA | PASS |
| PR8-INT-003 | Run integration suite on PR #8 merge ref | FAIL — 79 pass / 1 fail |
| PR8-FAIL-004 | Identify first assertion | PASS — REP-013 specification path assertion |
| PR8-CLASS-005 | Classify failure | CONFLICT / MERGE MATERIALIZATION MISMATCH |
| PR8-RUNTIME-006 | Prototype + canonical acceptance | PASS |

## Not yet performed

| Test ID | Check | State |
|---|---|---|
| REP13-MERGE-007 | Fresh PR candidate with explicit REP-013 reconciliation | NOT_PERFORMED |
| INT-ROOT-008 | Integration re-run after reconciliation | PENDING |
| REL-EXEC-009 | Executable RUN-010 → ENG-006 → SRV-009 proof | NOT_PERFORMED |
| BASELINE-010 | Governance correction of REP-012 | NOT_PERFORMED |
| BOOT-FINAL-011 | Final boot verification | BLOCKED |

## Decision

Do not weaken `test_repository_content_tree_canonicalization.py` and do not remove the canonical specification path from `REP-013`.

A fresh candidate will explicitly reconcile `REP-013` on its branch and re-run CI.

## Session closure

PR #8 remains unmerged. This checkpoint records the exact discrepancy and the controlled next mutation.
