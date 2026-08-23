# EJR-334 — GT-028 Executable Regression Seam

Date: 2026-08-23
Status: COMPLETED / GOVERNED REGRESSION MUTATION
Protocol: GOV-013 + GOV-018 Candidate + RUN-012
Parent: EJR-333

## Objective

Convert the GT-027 evidence classification matrix into a governed executable regression seam using the already-existing evidence reasoning fixture. No parallel runtime model is introduced.

## Truth-eye audit

The existing fixture was inspected before mutation. It exposed a semantic compression: every mismatch in claim identity was previously classified as `DIFFERENT EVIDENCE LAYERS`. That erased an important distinction between different claims and different propositions/layers within the same claim identity.

GT-028 therefore separates the predicates in this order:

1. Claim identity mismatch → `DIFFERENT CLAIMS`.
2. Same claim identity but different proposition → `DIFFERENT EVIDENCE LAYERS`.
3. Same claim identity and proposition with equal observed value → `CONSISTENT / CORROBORATED`.
4. Same claim identity and proposition with incomplete evidence → `UNRESOLVED`.
5. Same claim identity and proposition with complete, mutually exclusive observed values → `CONTRADICTION`.

This preserves the GT-027 rule that contradiction requires identity alignment instead of treating every disagreement as contradiction.

## Mutation

Existing insertion point used:

`Quality/Integration/test_evidence_reasoning_classification.py`

Mutation commit:

`c422556ea11d7850d25a7c9b2196e481a2a2be5e`

Content SHA after mutation:

`4bb325353fb8e23d581b734f20ef0b3561b4754c`

Added regression coverage for the specific boundary:

`missing execution identity + asserted failure ≠ execution failure`

The expected classification is `UNRESOLVED`.

## Knowledge Delta

**KD-049 — Claim identity must be evaluated before evidence-layer disagreement.**

A classifier must not collapse different claim identities into an evidence-layer difference.

**KD-050 — Evidence completeness precedes negative execution inference.**

An unavailable execution identity cannot be promoted to FAIL merely because another observation asserts failure.

## Execution boundary

The mutation is repository-verified, but current GitHub connector evidence does not expose a fresh workflow run for this exact mutation. Therefore:

`REGRESSION WIRING = VERIFIED`

`CURRENT CI EXECUTION = UNRESOLVED`

`PROMOTION = NOT AUTHORIZED`

No historical run is reused as proof for the new mutation.

## Closure

`Inspect → Detect semantic compression → Mutate existing seam → Add controlled regression → Verify commit/content SHA → Preserve execution boundary → Close`

Next safe continuation:

`GT-029 — seek direct execution evidence for commit c422556...; if unavailable, test whether artifact/run identity can be correlated through another existing governed surface without creating a synthetic execution path.`
