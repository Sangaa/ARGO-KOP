# EJR-302 — CI Decision Boundary and GitHub Tool-Surface Learning

**Date:** 2026-08-25
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Status:** OPEN — LEARNING PROMOTION PENDING CI VERIFICATION
**Transaction:** MUT-2026-08-25-P221-CI-DECISION-BOUNDARY-001

## 1. Trigger

P220 was initially placed on HOLD after a narrow commit-specific workflow lookup returned no runs. A broader GitHub Actions run listing subsequently exposed an actual Full-Stack Repository Audit run for the same commit, and job-log inspection identified the real failure boundary.

## 2. Actual Failure

The Full-Stack Repository Audit failed at the Mutation Matrix preflight step because a protected session-delta mutation existed without a pre-existing Mutation Matrix.

This was a governance-compliance failure, not proof that the P220 content itself was semantically wrong.

## 3. Decision-Boundary Defect

The repeatable weakness was broader than the missing matrix:

**The engineer allowed a tool-surface result to become a repository-state conclusion before validating the result through an independent GitHub Actions surface.**

A connector endpoint that returns zero commit-associated runs does not prove that GitHub has no relevant run. Tool-specific scope, trigger filtering, pagination, indexing, branch/ref behavior, and endpoint coverage can create false negatives.

Therefore:

`Tool Result ≠ Repository Fact`

until the result has been validated against an appropriate independent surface.

## 4. Mandatory Learning

For material CI questions, the engineer MUST distinguish:

1. **What the tool actually queried**;
2. **What evidence it returned**;
3. **What repository fact is being inferred**;
4. **Whether the tool surface is sufficient to support that inference**.

When a commit-specific workflow lookup returns no run, the engineer MUST NOT conclude `CI absent` until an independent Actions surface is checked where available, including repository workflow-run listing and, when a candidate run is found, Job → Step → Log inspection.

Likewise, a green workflow headline MUST NOT be promoted to repository-wide PASS without complete required Job/Step/Log reconciliation.

## 5. Decision Discipline

The engineer must not let an existing rule, matrix classification, or workflow headline substitute for evidence inspection.

The correct sequence is:

`Question → Tool Capability Check → Evidence Retrieval → Cross-Surface Validation → Failure/Success Boundary → Prior Learning → Decision → Mutation → Revalidation`

If a rule repeatedly produces decisions that conflict with observed repository reality, the rule itself becomes a candidate defect and must be evaluated rather than blindly obeyed.

Higher ARGO authority remains binding; this learning does not authorize bypasses.

## 6. Relation to Existing Learning

- GOV-013 §5/§6: materially different search methods and search-failure learning.
- GOV-013 §9B/§9B.4: complete CI failure and evidence reconciliation.
- GOV-014A: Mutation Matrix is a pre-write control.
- EJR-280: validator must enforce semantic contract without accidental schema assumptions.

This event extends those rules with an explicit **Tool-Surface / Decision-Boundary Check**.

## 7. Proposed Canonical Rule

Before a material conclusion is made from any GitHub connector result:

**Evidence returned by tool → verify endpoint scope/limitations → corroborate through an independent suitable GitHub surface when available → only then classify repository state.**

No single connector response should be treated as an omniscient repository state oracle.

## 8. Closure

- [x] Failure discovered through broader GitHub Actions surface.
- [x] Job and log inspected.
- [x] Root cause isolated.
- [x] Prior learning retrieved.
- [x] Repeatable decision-boundary weakness identified.
- [x] Mutation Matrix created before this learning artifact.
- [ ] Learning promotion into canonical governance verified by CI.
- [ ] Mutation Matrix post-write reconciliation complete.

## 9. Next Step

Evaluate whether this rule belongs as a canonical addendum to GOV-013 or as a mandatory section in the existing CI Failure Root-Cause Gate. Do not duplicate governance text if an existing canonical rule can be strengthened with the same semantic control.
