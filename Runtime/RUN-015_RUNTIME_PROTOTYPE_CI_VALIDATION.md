# RUN-015 — RUNTIME PROTOTYPE CI VALIDATION

Platform: ARGO KOP
Document ID: RUN-015
Version: 1.0.0
Status: Candidate / Awaiting CI Evidence
Category: Runtime Verification
Priority: High
Date: 2026-08-11

---

# Purpose

Provide a repository-native path for executing the Runtime Prototype acceptance suite instead of treating source inspection as test evidence.

# CI Contract

The workflow:

`/.github/workflows/runtime-prototype-tests.yml`

runs the complete `Runtime/Prototype` pytest suite on:

- push affecting the prototype;
- pull requests affecting the prototype;
- manual workflow dispatch.

# Environment

The workflow currently uses Python 3.11 and installs pytest explicitly.

# Evidence Rule

A repository state may be marked **TESTED/PASS** only after a real workflow run reports success.

A source review, static inspection, or successful file creation is not a test result.

# Failure Handling

A failed CI run becomes an engineering input. The responsible test or implementation must be corrected and the suite rerun.

# Scope

This workflow validates the prototype only. It does not imply that the full ARGO Runtime is production-ready.

# Related

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/Prototype/TEST_EXECUTION_REPORT.md`

# Integrity Hold

No PASS claim is made by this document. CI execution evidence is required.

---

End of Document
