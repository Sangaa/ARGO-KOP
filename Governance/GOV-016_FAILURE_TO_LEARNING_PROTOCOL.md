# GOV-016 — Failure-to-Learning Protocol

**Status:** ACTIVE / MANDATORY
**Scope:** All ARGO KOP construction, testing, audit, CI, runtime, tooling, and knowledge-transfer sessions.

## 1. Purpose

Failure is an evidence source, not merely an obstacle. Every unexpected failure must be analyzed before the session closes so ARGO can convert failure into reusable capability.

## 2. Mandatory Rule

No unexpected failure may be silently fixed, ignored, or classified as a generic tool problem without first determining what the available evidence supports.

The required chain is:

**Failure → Evidence → Root Cause → Failure Class → Why the Approach Failed → Corrective Pattern → Regression Test → Reuse → Knowledge Transfer**

## 3. Failure Classification

Every material failure must be classified as one or more of:

- **IDEA_FAILURE** — the proposed approach is fundamentally unsuitable.
- **IMPLEMENTATION_FAILURE** — the idea is valid but implementation is defective.
- **TEST_FAILURE** — the test/assertion is defective or too brittle.
- **INFRASTRUCTURE_FAILURE** — CI/tool/connector/runtime infrastructure prevented valid execution.
- **MODEL_ASSUMPTION_FAILURE** — an unverified model assumption caused the failure.
- **GOVERNANCE_GAP** — existing controls did not adequately govern the situation.
- **EVIDENCE_GAP** — execution occurred but did not produce sufficient proof.
- **SCHEMA_DRIFT** — a previously accepted structure changed across real artifacts.

Do not collapse these classes into a generic `FAILED` state when evidence supports a more precise classification.

## 4. Required Failure Analysis

For every material failure record:

1. What actually failed.
2. What evidence proves the failure.
3. What did **not** fail, to prevent overcorrection.
4. Root cause, with confidence level.
5. Whether the idea, implementation, test, or execution channel was at fault.
6. Corrective action.
7. Whether the correction changes authority, governance, or only implementation.
8. Regression test or other repeatable verification.
9. Reuse conditions and known limits.
10. Whether the learning should be transferred to protocol, template, matrix, test corpus, or future ARGO architecture.

## 5. Failure Must Not Destroy Good Ideas

A failed implementation must not automatically invalidate the underlying idea.

The analysis must explicitly distinguish:

**Bad Idea ≠ Bad Implementation ≠ Bad Test ≠ Bad Execution Channel.**

Example: a multi-Matrix regression concept may remain valuable even if embedding it directly in a workflow causes workflow-loading failure. The failure should refine the architecture rather than discard the capability without evidence.

## 6. Regression Requirement

A corrected failure should, when practical, receive a regression test that would fail if the same failure mechanism returns.

Where the failed approach revealed a reusable technique, preserve at least one representative real artifact in the regression corpus. Prefer multiple real variants over a single synthetic fixture when the purpose is to detect schema or behavior drift.

## 7. Promotion and Knowledge Transfer

Learning follows:

**Observation → Root Cause → Lesson → General Rule → Test → Validation → Promotion → Transfer**

Promotion levels:

- `SESSION-LEARNING`
- `REUSABLE-LEARNING`
- `GOVERNANCE-RULE`
- `DEFAULT-PRACTICE`

No learning may become a governance rule or default practice solely because a model proposes it. It requires evidence and repeat validation appropriate to its scope.

## 8. Session Closure Gate

Before closing a session containing a material failure, the session record must state:

- failure and classification;
- evidence and confidence;
- root cause or explicitly unresolved root-cause status;
- corrective action or safe containment;
- regression/revalidation status;
- learning classification;
- transfer destination or reason for not transferring;
- next safe checkpoint.

If root cause is unresolved, the correct state is **UNRESOLVED / CONTAINED**, not PASS.

## 9. Relationship to Existing Governance

GOV-016 supplements GOV-013 session execution, GOV-013A bootstrap integrity, GOV-014 controlled mutation, and GOV-015 execution documentation and knowledge transfer. It does not grant mutation authority and cannot promote an artifact or relationship by itself.

## 10. Architectural Principle

ARGO should continuously increase its ability to turn failure into future capability:

**Failure → Understanding → Correction → Verification → Memory → Reuse → Greater Resilience.**

The objective is not to eliminate all failure. The objective is to make failure increasingly informative, bounded, recoverable, and reusable while preventing the same failure mechanism from silently recurring.
