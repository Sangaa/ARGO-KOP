# EJR-166 — 2026-08-14 Integration Failure Root-Cause Capture

## TEST-ID: INT-FAIL-002

**Result: CONFLICT — two deterministic contract failures identified**

PR #3 merge workflow run `31772269633`, integration job `94681554508`, checked out merge commit `c9abe45186636c9e707f969ea45c995b702c9655`.

Command executed by CI:
`python -m pytest -q`

Result: **78 passed, 2 failed**.

### Failure 1
`test_core000_canonical_reference.py::test_architecture_readme_points_to_canonical_core000`

First failing assertion:
`assert "Document ID: CORE-000" in content`

Actual `Core/CORE-000_PLATFORM_ARCHITECTURE.md` content uses the two-line metadata form:
`Document ID` then `CORE-000`.

Classification: **STALE INTEGRATION CONTRACT / FORMAT MISMATCH**, not an execution/runtime defect. The test requires an exact inline string that the current canonical document does not use.

### Failure 2
`test_repository_content_tree_canonicalization.py::test_repository_content_tree_uses_current_baseline_and_specification_path`

First failing assertion:
`assert "Specifications/01-Knowledge-Organization.md" in tree`

The current `main` version of `REP-013_REPOSITORY_CONTENT_TREE.md` now contains the canonical Specifications path. The PR #3 merge commit was built from an older main state and therefore tested a stale snapshot that predates the current REP-013 update.

Classification: **STALE MERGE SNAPSHOT / STALE INTEGRATION CONTRACT**, not evidence that current main lacks the path.

### Important distinction

The Integration suite is not an environment failure:
- runner setup PASS
- checkout PASS
- Python 3.11 setup PASS
- pytest installation PASS
- pytest execution PASS
- 78 tests PASS
- 2 deterministic assertions FAIL

The failure is therefore semantic test/document contract drift, not infrastructure instability.

### Mutation decision

No test was weakened and no assertion was removed.
No Runtime behavior was changed.
No authority declaration was changed.

Required corrective path:
1. reconcile the CORE-000 metadata contract against the canonical document format;
2. refresh PR #3 against current main so REP-013 current content is included;
3. rerun the complete integration and prototype suites;
4. update REP-020 with these exact failure nodes/edges/tests before declaring resolution.

## Session closure

State: **INTEGRITY HOLD**

Evidence captured: workflow run, job steps, full decoded integration log, exact failing test names/assertions, current-main REP-013 content, current-main CORE-000 content.

Tests performed: PR #3 integration workflow; exact failure extraction; current-main artifact comparison.

Tests not performed: post-reconciliation integration rerun; executable runtime consumer proof; baseline authority decision; exhaustive duplicate-ID closure.
