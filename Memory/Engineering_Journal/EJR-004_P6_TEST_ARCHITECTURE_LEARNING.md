# EJR-004 — P6 Test Architecture Learning

**Date:** 2026-08-19  
**Status:** GOVERNED LEARNING

## Observation

P6 regression modules began to accumulate repeated evidence construction, reconciliation rules, and boundary assertions. This makes the test suite harder to audit and creates a risk that different tests silently implement different interpretations of the same invariant.

## Architectural Finding

P6 should use a shared test infrastructure with thin scenario-specific test modules. The canonical reconciliation/classification behavior belongs in one reusable component; individual tests should supply scenarios and verify boundaries.

## Why This Matters

Duplication in tests is not harmless when the duplicated code represents governed knowledge. If the same rule is copied into multiple tests, a future correction can update one test while leaving another stale, creating false confidence.

## Execution Lesson

The earlier direct Python invocation demonstrated a second class of false confidence: a test module containing `test_*` functions can exit successfully without executing those functions when invoked as `python file.py`.

Therefore P6 now treats **test architecture** and **test execution authenticity** as related controls:

- shared canonical logic prevents semantic drift;
- an approved test runner prevents execution drift;
- test-count/output evidence proves that the intended tests actually ran.

## Governing Principle

> Do not duplicate governed knowledge merely because it is convenient to write an isolated test.

## Required Future Pattern

`thin test scenario → shared P6 service/model → boundary assertion → explicit test-runner execution → fresh CI evidence`

## Constraint

This learning does not authorize a broad refactor without staged regression. Refactoring must preserve current behavior first, then improve structure incrementally with read-back and execution evidence after each controlled mutation.
