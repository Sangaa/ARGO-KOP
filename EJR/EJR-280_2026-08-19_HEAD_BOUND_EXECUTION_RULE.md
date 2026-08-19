# EJR-280 — HEAD-Bound Execution Evidence Rule

Date: 2026-08-19
Status: GOVERNED LEARNING / INTEGRITY HOLD
Authority: GOV-013 + GOV-013A

## Failure Observed

Repeated verification cycles reused a successful historical GitHub Actions run after repository HEAD had changed. This produced valid execution evidence for an older SHA but invalid evidence for the current state.

## Root Cause

Execution evidence was treated as a property of the workflow rather than a property of the exact commit under verification. Historical run success was allowed to remain in the active evidence path after HEAD mutation.

## Rule

For every verification cycle:

1. Capture `HEAD_SHA` immediately before execution.
2. Bind the expected execution to that exact SHA.
3. After completion, read back the run/job/artifacts and require their recorded `head_sha` to equal `HEAD_SHA`.
4. If SHA differs, classify the result as `HISTORICAL / STALE EVIDENCE` and do not promote any gate.
5. A subsequent repository mutation invalidates all unbound execution evidence.

## Learning

A green run is not sufficient evidence. The evidence must be cryptographically bound to the exact repository state being evaluated.

## Decision

No promotion is authorized from historical SHA evidence. Current-HEAD execution must be obtained after the final mutation of the verification cycle.

End of EJR-280
