# GOV-013A — HERMUZ SESSION WORKGROUP CONTINUATION AMENDMENT

Status: APPROVED SESSION OPERATING AMENDMENT / CANONICAL ADDENDUM
Parent Protocol: `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
Effective: 2026-08-27

## 1. Purpose

This amendment makes the session operate as a **continuous coherent workgroup**, rather than treating every completed task as an automatic session boundary.

It is subordinate to higher ARGO authority and does not authorize bypassing any integrity, governance, CI, runtime, or mutation gate.

## 2. Continuous Workgroup Rule

When the canonical invocation phrase is received:

> «أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»

HERMUZ MUST continue through the highest-priority safe sequence of related tasks available in the same session.

The engineer MUST NOT close the session merely because:

- one task completed;
- one checkpoint was recorded;
- one mutation succeeded;
- one test passed; or
- one report could be written.

Instead:

`RE-ENTRY → BASELINE → PRIOR-LEARNING → GAP → ANALYSIS → SAFE TASKS → TEST → VALIDATE → NEXT SAFE TASK`

is repeated within the same session until a genuine closure condition is reached.

## 3. Maximum Useful Work Rule

The engineer SHOULD perform the maximum useful amount of safe analysis, tracing, testing, reconciliation, mutation and documentation that the current session permits.

Work may continue across multiple coherent checkpoints without waiting for another user instruction.

The stopping criterion is **not time spent or number of commits**. It is the first applicable condition in the parent protocol's closure rules:

1. no useful safe high-priority work remains;
2. a real blocker prevents safe continuation;
3. required evidence is unavailable and the remaining work cannot be bounded honestly;
4. a mandatory CI/integration/validation hold prevents transition;
5. the user explicitly requests closure.

## 4. Closure-Only-At-End Rule

A user-facing build report MUST NOT be issued as a substitute for session closure.

Before the final report, HERMUZ MUST perform the parent protocol's closing audit and explicitly record:

`CURRENT STATE → COMPLETED WORKGROUP → CHANGES → EVIDENCE → TEST/CI → MATRICES → REMAINING WORK/BLOCKER → NEXT POINT → LEARNING → FINAL CHECKPOINT → SESSION CLOSED`

Only after that closure record is verified may the concise report be returned to the user.

## 5. Failure and Hold Rule

A failed required CI/integration/validation check does not close the session. The session remains in `OPEN/HOLD` and HERMUZ MUST perform the required root-cause/recovery sequence before any transition.

A blocker is a valid closure reason only when it is real, evidenced, and prevents safe continuation—not merely because the current micro-task is complete.

## 6. Cross-Session Determinism

This amendment is part of the HERMUZ operating rule set. A new AI instance MUST discover and apply it from the repository without requiring the user to repeat the instruction.

Resolution order:

`Invocation Phrase → GOV-013 → GOV-013A → PROJECT_BOOTSTRAP → Current State → REP-020/EJR/Matrices/Test State → Highest-Priority Safe Work`

## 7. Authority Boundary

This amendment changes **session continuation behavior only**.

It does NOT:

- grant new authority;
- permit speculative artifacts;
- permit unsupported relationship promotion;
- permit bypassing failed CI;
- convert structural evidence into runtime proof;
- authorize production side effects;
- override higher ARGO governance.

## 8. Canonical Operational Formula

**`BUILD UNTIL SAFE WORK IS EXHAUSTED — THEN CLOSE — THEN REPORT.`**

Not:

**`TASK COMPLETE — CLOSE — REPORT.`**

## 9. Adoption

All future uses of the HERMUZ invocation phrase MUST apply this amendment unless a higher-authority ARGO rule supersedes it.
