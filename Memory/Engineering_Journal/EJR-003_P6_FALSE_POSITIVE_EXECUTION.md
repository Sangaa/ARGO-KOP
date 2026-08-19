# EJR-003 — P6 False-Positive Execution Finding

**Date:** 2026-08-19  
**Project:** ARGO KOP  
**Area:** P6 reconciliation / CI execution evidence  
**Status:** OPEN — root cause identified, corrective execution pending

## 1. Incident

P6 reconciliation regression was introduced in commit `66e9ed3e54bd0561ae1a98d346b135a0145890ea` and later wired into the Full-Stack workflow by `938b2ddb4193cb26a5dc08112a1dd0a05bacfb01`.

The earlier Integration Quality Suite reported a failure at the suite level. The later workflow wiring appeared successful, creating a misleading green/success condition.

## 2. Root Cause

`test_p6_reconciliation_boundaries.py` defines `test_*` functions but does not invoke them when executed directly.

The workflow added by `938b2ddb` executes the file with:

```yaml
run: python Quality/Integration/test_p6_reconciliation_boundaries.py
```

Plain `python file.py` imports/defines the functions and exits successfully; it does not automatically discover and execute `test_*` functions.

Therefore a successful workflow step using this command can be a **false-positive / vacuous success**: the step can pass without executing the assertions it is intended to validate.

## 3. Evidence Chain

- `66e9ed3e`: added the reconciliation regression test file.
- Integration Quality Suite subsequently exposed a failure at suite level.
- `938b2ddb`: added the workflow step invoking the test file directly.
- The workflow line is syntactically valid YAML, but the execution command is semantically insufficient for a test module containing `test_*` functions.

## 4. Corrective Principle

Test definitions and test execution must remain separate:

- Test module: defines regression tests.
- CI runner: invokes a real test runner (`pytest`) or an explicitly approved equivalent.
- CI success must prove that the intended test functions were actually executed.

Do **not** add ad-hoc self-invocation to the test module merely to make `python file.py` execute assertions. The CI execution layer should be corrected instead.

## 5. New Governance Rule

A CI step that executes a test module directly with `python <test_file.py>` MUST NOT be considered execution-verified unless the module explicitly invokes its tests and the invocation is independently verified.

Preferred pattern for pytest-based repositories:

```yaml
run: python -m pytest Quality/Integration/test_p6_reconciliation_boundaries.py
```

The repository's established Integration Quality Suite remains the reference for the approved test runner and should be reused where practical.

## 6. Learning

1. A green CI step proves only that the invoked process exited successfully; it does not automatically prove that tests ran.
2. Test discovery and test execution are separate architectural layers.
3. P6 must validate not only evidence identity/freshness, but also **execution authenticity**.
4. A regression test must itself be regression-tested against the CI invocation path.
5. Historical successful runs cannot validate a current baseline unless SHA and executed test identity are reconciled.

## 7. Required Follow-up

- Correct the CI invocation to use the approved test runner.
- Execute the corrected workflow on the current HEAD.
- Verify the test count/output, not merely the exit code.
- Preserve the failed run and the false-positive run as historical evidence.
- Update the P6 matrix only after fresh execution and read-back reconciliation.

## 8. Current State

`P6 RECONCILIATION = IMPLEMENTED`  
`P6 CI WIRING = PRESENT`  
`CURRENT EXECUTION AUTHENTICITY = NOT VERIFIED`  
`FALSE-POSITIVE PATH = IDENTIFIED`  
`CORRECTION = PENDING`
