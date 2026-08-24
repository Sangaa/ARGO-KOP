# EJR-302 — GT-041 Deep Provenance Root Conflict

Date: 2026-08-24
Status: CONTROLLED REGRESSION RECORDED / CI EXECUTION PENDING

## Test boundary

GT-041 extends GT-040 by placing the explicit root conflict one level deeper:

`ROOT-A → PARENT → CHILD`

where:

- `PARENT.provenance_root = ROOT-A`
- `PARENT.provenance_parent = ROOT-A`
- `CHILD.provenance_root = ROOT-B`
- `CHILD.provenance_parent = PARENT`
- `ROOT-B` exists as a separate root node.

## Expected behavior

The graph is `INVALID PROVENANCE`.

The evidence comparison is `UNRESOLVED`, not `CONTRADICTION`.

This preserves the distinction established by GT-039: provenance corruption is a validity failure and must not be reinterpreted as a semantic contradiction between claims.

## Evidence

Test:
`Quality/Integration/test_gt041_provenance_deep_root_conflict.py`

Commit:
`bee06140ba6c36fe6964bac63d311b589be24639`

## Verification boundary

The test was committed successfully. No CI PASS is claimed because the GitHub Actions connector returned no workflow runs for the preceding GT-040 commits and therefore no executable verification result was available for this mutation.

## Learning

A root mismatch remains invalid even when both competing roots are real, present, and internally valid. Existence of `ROOT-B` cannot legitimize a child whose parent chain resolves to `ROOT-A` while the child explicitly claims `ROOT-B`.
