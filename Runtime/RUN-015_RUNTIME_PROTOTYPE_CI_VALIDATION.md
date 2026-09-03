# RUN-015 — RUNTIME PROTOTYPE CI VALIDATION

Platform: ARGO KOP
Document ID: RUN-015
Version: 1.0.1
Status: Candidate / Integrity Hold / CI Evidence Available
Category: Runtime Verification
Priority: High
Date: 2026-08-11
Last Audit: 2026-09-03

---

# Purpose

Provide a repository-native path for executing the Runtime Prototype acceptance suite instead of treating source inspection as test evidence.

# CI Contract

The workflow:

`/.github/workflows/runtime-prototype-tests.yml`

runs the complete `Runtime/Prototype` pytest suite on its configured triggers and may also run as part of broader repository/runtime validation.

# Environment

The workflow currently uses Python 3.11 and installs pytest explicitly.

# Evidence Rule

A repository state may be marked **TESTED/PASS** for the prototype scope only after a real workflow run reports success for that tested head/scope.

A source review, static inspection, successful file creation or older successful run is not by itself a test result for a later changed head.

Prototype CI success is scope-bound evidence. It does not certify the full Runtime, external connector behavior, production readiness or executable promotion of candidate Runtime contracts.

# Current Bounded CI Evidence

Real Runtime Prototype / Integration workflow evidence exists on current repository history.

For the Transaction-P closure predecessor used by this review:

- Commit: `29b5b419a00c668156199a5d0c4e6f8fd819e599`
- Runtime Prototype / Integration run: `33722045550` — SUCCESS

The preceding atomic RUN-007 recovery head also produced Runtime Prototype / Integration run `33721850938` — SUCCESS.

These runs establish that real CI evidence is available for their tested repository heads. They do not pre-certify this document's later material change or any future head; each material change remains subject to its own exact-head validation.

# Failure Handling

A failed CI run becomes an engineering input. The responsible test, implementation, packaging or affected contract must be diagnosed and corrected, and the applicable suite rerun.

Tests must not be weakened merely to convert a valid failure into green status.

# Scope

This workflow validates the prototype suite for the tested repository state only. It does not imply that the full ARGO Runtime is production-ready or that candidate/prototype contracts are canonical executable authority.

# Related

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/Prototype/TEST_EXECUTION_REPORT.md`
- `Runtime/_FOLDER_STATUS.md`

# Integrity Hold

Real prototype CI evidence is available, but executable promotion and consolidated cross-layer Runtime validation remain on HOLD.

`CI EVIDENCE AVAILABLE != FULL RUNTIME CERTIFICATION`.

`PROTOTYPE TEST PASS != CANDIDATE AUTHORITY PROMOTION`.

---

End of Document
