# EJR-290 — HERMUZ P6 Scope Boundary Repair — Step 02

## Status
CLOSED — STEP 02 COMPLETE / IMPLEMENTATION CHECKPOINT PRESERVED / RUNTIME VERIFICATION PENDING

## Trigger
Continuation of EJR-289 under GOV-013 after Step 01 materialized the canonical P6 scope contract.

## Pre-Change Evidence
- Canonical scope contract: `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md`
- Existing correlator was directly mapping paths from `REP-020`/`REP-014` before any scope decision.
- Existing P6 regression tests were synthetic and did not consume the canonical scope registry.
- Issue #15 remains open and explicitly prohibits resolving the gap by speculative mappings or classifier exceptions.

## Mutation
Updated:
`Quality/Integration/ci_impact_correlation.py`

Commit:
`aa3282314b3e4b1ebf2f3d5511651b09bcfa15e3`

Implementation changes:
1. Added canonical `P6_SCOPE_ELIGIBILITY_REGISTRY.md` as the scope-policy input.
2. Added deterministic scope parsing and path eligibility resolution.
3. Enforced scope-before-correlation ordering.
4. Added `POLICY_UNRESOLVED` for unresolved eligibility.
5. Added `NOT_APPLICABLE` for explicit out-of-scope paths.
6. Preserved `UNMAPPED` only for paths explicitly `IN_SCOPE` but lacking canonical mapping evidence.
7. Kept `NO_AUTO_PROMOTION` unchanged.
8. Preserved execution-evidence classification as an independent layer.

## Post-Change Read-Back
The resulting implementation was read directly from commit `aa3282314b3e4b1ebf2f3d5511651b09bcfa15e3`.
The new implementation visibly consumes `P6_SCOPE_ELIGIBILITY_REGISTRY.md` and returns `POLICY_UNRESOLVED` before correlation for unresolved scope.

## Regression Mutation
Created:
`Quality/Integration/test_p6_canonical_repository.py`

Commit:
`ef892f589f635e5c5c8aadf7425fe9ca6f836724`

This test reads the real canonical scope registry, `REP-020`, and `REP-014`, and verifies:
- canonical IN_SCOPE behavior;
- canonical EJR UNRESOLVED behavior;
- unresolved policy cannot be promoted by matching evidence;
- unknown paths remain policy-unresolved rather than implicit UNMAPPED.

Updated:
`Quality/Integration/test_ci_impact_correlation.py`

Commit:
`5f809729340a06c9a05576a437bea4bb7ea0fae1`

The existing synthetic suite was corrected to use an explicit synthetic scope fixture. This preserves controlled synthetic coverage without allowing canonical repository policy to silently change synthetic expectations.

## Workflow Evidence
The current `full-stack-audit.yml` was re-read and confirmed to run the existing P6 regression and the correlation script on pushes to `main`. The workflow also contains the repository-wide audit and artifact emission stages.

No new workflow run was available through the connected workflow lookup for the latest commit at this checkpoint. Therefore **no CI PASS is claimed**.

## Boundaries Preserved
- No `REP-020` relationship mapping added.
- No `REP-014` relationship promoted.
- No Issue #15 decision inferred or closed.
- No runtime semantics changed.
- No synthetic evidence promoted to canonical/runtime evidence.
- No relationship verification inferred from code/test existence.

## Learning
Confirmed and preserved the central repair rule:

> Correlation absence is not policy absence. Scope must be evaluated before mapping, and unresolved policy must remain a first-class result.

This remains candidate learning pending final integration validation and learning-promotion review.

## Closure Audit
- Current state: P6 Scope Boundary Repair — Step 02 complete.
- Work completed: scope-aware correlator + canonical repository test layer + synthetic regression separation.
- Changed artifacts re-read: yes.
- Integration/regression: implementation coverage added; actual execution/CI evidence pending.
- Matrix/index synchronization: no relationship matrix mutation made; no authority state changed.
- Governance: Issue #15 remains open.
- Next continuation: execute/recover the affected regression and full-stack CI evidence, inspect first failure if any, then add the regression preventing `UNRESOLVED → MAPPED/PROMOTED` at the strongest available test boundary.
- Final implementation checkpoint: `5f809729340a06c9a05576a437bea4bb7ea0fae1`

## Session Closure
Closed under the user's requested command-level checkpoint discipline because this coherent implementation work group is complete. Closure does not represent P6 final completion; runtime/CI validation remains explicitly pending.

---

End of EJR-290
