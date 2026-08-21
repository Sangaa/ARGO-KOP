# EJR-289 — HERMUZ P6 Scope Boundary Repair — Step 02

## Status
CLOSED — STEP 02 COMPLETE / PRE-IMPLEMENTATION CHECKPOINT

## Trigger
Continuation authorized after EJR-288. This step prepares the correlator mutation under GOV-013 using the canonical P6 Scope / Eligibility Registry created in Step 01.

## Objective
Make the correlator consume the canonical scope boundary before performing mapping correlation, with no policy inference from missing evidence.

## Required behavior
- `IN_SCOPE` → perform correlation and return `MAPPED` or `UNMAPPED`.
- `OUT_OF_SCOPE` → return `NOT_APPLICABLE`.
- `UNRESOLVED` → return `POLICY_UNRESOLVED`.
- `UNRESOLVED` must never reach the existing mapping decision as `UNMAPPED`.

## Pre-Mutation Inspection
Current correlator evidence at the previous checkpoint confirms that `correlate_paths()` currently derives status solely from matrix/registry path hits and emits `UNMAPPED` when neither contains the path. This is the exact policy/correlation coupling targeted by Step 02.

The P6 matrix already requires changed-path correlation to remain distinct from relationship proof and forbids auto-promotion. The new registry adds the missing eligibility boundary.

## Safety Decision
This checkpoint does NOT modify the correlator. It records the exact mutation contract before the write so the next command can be independently verified and closed.

No REP-020 mutation.
No REP-014 mutation.
No Issue #15 decision.
No relationship promotion.
No runtime semantic change.

## Mutation Contract
The next implementation change must:
1. load `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` as canonical repository input;
2. resolve path class deterministically;
3. evaluate eligibility before matrix/registry correlation;
4. emit `POLICY_UNRESOLVED` for `EJR/**` and any other unresolved class;
5. preserve existing exact-path correlation behavior for `IN_SCOPE` paths;
6. emit `NOT_APPLICABLE` for explicitly `OUT_OF_SCOPE` paths;
7. fail closed for malformed/absent eligibility data rather than silently treating it as mapped;
8. add regression coverage in a subsequent step.

## Verification Boundary
No implementation PASS is claimed at this checkpoint. The purpose is to preserve a clean pre-mutation boundary and make the next mutation auditable.

## Learning
Scope policy is an input contract to correlation, not an outcome of correlation. The implementation must therefore read policy before evidence lookup rather than derive policy from evidence lookup results.

## Closure Audit
- Step: P6 Scope Boundary Repair — Step 02
- State: CLOSED
- Mutation performed: none
- Evidence inspected: current correlator + P6 matrix + canonical scope registry
- Next mutation: update `Quality/Integration/ci_impact_correlation.py`
- Governance blocker: Issue #15 remains open and unresolved
- Promotion: prohibited
- Checkpoint source: EJR-289

## Session Closure
Closed under GOV-013 because the pre-mutation inspection and exact mutation contract are complete. The next command is a separate implementation mutation and must receive its own post-command verification and closure record.

---

End of EJR-289
