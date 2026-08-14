# EJR-172 — 2026-08-14 PR #5 CI Root Cause and Current-main Revalidation

## Session

- Date: 2026-08-14
- Repository: `Sangaa/ARGO-KOP`
- Current `main`: `598a523a27fece39db71348903540ae727dde77e`
- PR #5 merge snapshot tested: `25aac2a1e5b2785f9169c784ac043fda9a16c435`
- Integrity: **INTEGRITY HOLD**

## P0 — PR #5 CI

### TEST-ID: PR5-CI-001

**Result: FAIL — root cause identified**

Workflow run `31773821212` executed the PR merge ref `pull/5/merge` at `25aac2a...`, which merged PR #5 head `2e74301e...` into the older main base `6abfd40...`.

Jobs:
- `prototype-tests`: PASS
- `Run prototype acceptance suite`: PASS
- `Run canonical acceptance scenarios`: PASS
- `integration-tests`: FAIL

Integration suite result: **78 passed / 2 failed**.

The two failures are:

1. `test_core000_canonical_reference.py::test_architecture_readme_points_to_canonical_core000`
   - Assertion expects literal `Document ID: CORE-000`.
   - Current CORE-000 authority uses the repository's established line-separated metadata form: `Document ID` followed by `CORE-000`.
   - Classification: **STALE TEST CONTRACT / FORMAT ASSUMPTION**, not Runtime defect.

2. `test_repository_content_tree_canonicalization.py::test_repository_content_tree_uses_current_baseline_and_specification_path`
   - Assertion expects `Specifications/01-Knowledge-Organization.md`.
   - Current `main` `REP-013` contains that canonical path, but the PR merge snapshot used the older `6abfd40...` base and therefore tested stale `REP-013` content.
   - Classification: **STALE MERGE SNAPSHOT**, not REP-013 defect.

The failure is therefore **not evidence of a Runtime regression**.

## Revalidation decision

Do not modify CORE-000 merely to satisfy a stale literal-format assertion.

Do not modify REP-013 merely to repair an outdated merge snapshot; current `main` already contains the specification path.

The correct next candidate must be created directly from the current `main` `598a523...`, then apply only the intended Runtime authorization-state reconciliation.

## Tests performed

- PR #5 CI run inspected: PASS prototype / FAIL integration.
- Full integration pytest output inspected: PASS 78 / FAIL 2.
- First failing assertions identified: PASS.
- CORE-000 current-main content read: PASS; line-separated canonical metadata confirmed.
- REP-013 current-main content read: PASS; `Specifications/01-Knowledge-Organization.md` confirmed.
- Current `main` branch SHA verified: PASS `598a523...`.

## Tests not performed / still open

- Re-run of integration suite on a candidate based on current `main`: NOT YET PERFORMED.
- Executable `RUN-010 → ENG-006 → SRV-009`: NOT PERFORMED.
- Baseline authority reconciliation: CONFLICT remains.
- Exhaustive internal-ID duplicate audit: PARTIAL / NOT CLOSED.
- Final Boot verification: NOT PERFORMED.

## Matrix requirement

REP-020 must record this event as a new revalidation entry. No PASS promotion is permitted from this CI result.

## Closure

No Runtime test, Integration test, CORE-000, REP-013, or baseline authority file was mutated during this checkpoint.

State remains **INTEGRITY HOLD**.
