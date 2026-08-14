# REP-020 Revalidation Addendum — 2026-08-14 / PR #8

## Matrix Delta

| Test ID | Source | Result | Impact | Required Revalidation |
|---|---|---|---|---|
| REP13-MAIN-001 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md@main` | PASS | Confirms canonical specification path is present in main | Re-read candidate after merge materialization |
| REP13-BASE-002 | `REP-013@222635a...` | PASS | Confirms path exists at PR base | Compare merge ref |
| PR8-INT-003 | PR #8 run #130 | FAIL | 79 PASS / 1 FAIL in integration suite | Fresh candidate after explicit REP-013 reconciliation |
| PR8-FAIL-004 | PR #8 integration log | PASS | First assertion identified as REP-013 path assertion | Re-run after candidate correction |
| PR8-CLASS-005 | EJR-178 | CONFLICT | Canonical main differs from tested merge snapshot | Verify fresh merge materialization |
| PR8-RUNTIME-006 | PR #8 prototype job | PASS | Runtime HOLD reconciliation did not regress prototype acceptance | Preserve runtime fix |

## Tests Not Completed

| Test ID | State | Reason |
|---|---|---|
| REP13-MERGE-007 | NOT_PERFORMED | Fresh candidate with explicit REP-013 reconciliation not yet tested |
| INT-ROOT-008 | PENDING | Must follow fresh candidate |
| REL-EXEC-009 | NOT_PERFORMED | Executable consumer still unproven |
| BASELINE-010 | NOT_PERFORMED | Governance correction remains separate P1 |
| BOOT-FINAL-011 | BLOCKED | Integrity blockers remain |

## Node / Edge Impact

**Node:** REP-013

**Edges:**
- REP-013 → REP-014 relationship validation remains open.
- REP-013 → REP-020 revalidation required after candidate mutation.
- REP-013 → Integration canonicalization test directly impacted.

## Current Classification

`MERGE MATERIALIZATION / PR CHECKOUT SNAPSHOT MISMATCH`

Canonical `main` evidence does not currently show a REP-013 content defect.

## Integrity State

**INTEGRITY HOLD**

No merge decision authorized.
