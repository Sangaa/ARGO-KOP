# P6 Test Architecture — Shared Infrastructure and Thin Regressions

**Status:** Proposed / governed improvement  
**Date:** 2026-08-19

## Purpose

Prevent duplicated test logic and prevent false-positive CI execution by separating shared P6 test infrastructure from individual regression cases.

## Target Structure

```text
Quality/Integration/P6/
├── p6_models.py
├── p6_reconciliation.py
├── p6_assertions.py
└── test_*.py
```

### Shared layer

- `p6_models.py`: immutable evidence/value objects.
- `p6_reconciliation.py`: the single source of truth for classification/reconciliation rules.
- `p6_assertions.py`: reusable boundary assertions and execution-authenticity checks.

### Test layer

Individual `test_*.py` modules should contain scenarios, fixtures, and minimal orchestration only. They must call the shared infrastructure rather than reimplementing classification logic.

## Design Rules

1. One governed rule has one canonical implementation.
2. Tests may specialize scenarios but must not fork reconciliation semantics.
3. Test modules must be executable through the repository-approved test runner.
4. A CI step is not execution-verified merely because `python file.py` exits with code 0.
5. CI must prove test discovery/execution, not only process exit status.
6. Shared infrastructure must remain independent of GitHub-specific transport details.
7. Live CI evidence, artifact identity, and SHA reconciliation remain separate from pure unit/regression logic.

## Object-Oriented Boundary

Prefer composition and small value objects over inheritance. The intended dependency direction is:

`Test Scenario → Reconciliation Service → Evidence Model`

and

`Test Scenario → Boundary Assertions`

The test suite must not own the canonical reconciliation algorithm.

## Required Execution Contract

The approved runner must execute the test functions explicitly. Preferred pytest invocation:

```yaml
run: python -m pytest Quality/Integration/P6/test_*.py
```

If the repository's existing Integration Quality Suite already provides the approved runner, P6 should reuse that mechanism instead of introducing a second execution model.

## Anti-Pattern

```yaml
run: python Quality/Integration/test_p6_reconciliation_boundaries.py
```

This is unsafe when the module only defines `test_*` functions without explicitly invoking them. It can produce a successful process exit without executing the intended assertions.

## Migration Order

1. Preserve current regression behavior.
2. Extract canonical evidence models.
3. Extract reconciliation/classification logic.
4. Extract reusable assertions.
5. Convert individual tests to thin scenarios.
6. Add execution-authenticity regression.
7. Change CI to the approved runner.
8. Run fresh CI on the current HEAD.
9. Verify test count/output and artifact identity.
10. Only then reconcile and close P6.

## Non-Goals

This document does not authorize changing P6 semantics merely to reduce duplication. Behavioral changes require their own evidence, regression coverage, and mutation documentation.
