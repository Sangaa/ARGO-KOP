# EJR-338 — IGT / LPE Transfer-Learning Boundary

Status: `REUSABLE-LEARNING / VALIDATION-READY / NOT-AUTHORITY`

## Source
HORUS Session Record 027, commit `7fbd1aab95dba40d5b9fc9a528760108e8733097`.

## Reconciled Insight
The important distinction is not whether a rule can be repeated, but whether its invariants transfer to materially novel cases without answer leakage.

## Implemented Governance Artifact
`Governance/IGT_INVARIANT_GENERALIZATION_TEST_v1.0.md`

## Invariants for Repository-First Candidate
- current-state priority;
- reconciliation before action;
- bounded scope;
- relationship revalidation;
- evidence-bounded claims.

## Provenance Requirement
Learning evidence should preserve:
`SOURCE → OBSERVATIONS → INVARIANTS → EXCLUDED INTERPRETATIONS → TRANSFER CASES → PREDICTIONS → VERIFICATIONS → FAILURES → REVISION → PROMOTION_STATUS`.

## Important Boundary
IGT can provide behavioral transfer evidence. It cannot by itself prove model-weight learning, causal learning, or permanent persistence. Those claims require additional evidence.

## Next Action
Execute the two or more novel authority-conflict cases defined by IGT, with independent contexts and a baseline comparison. Record failures as boundaries, not as noise.

`AUTHORITY = NONE`
`GOV-013A = PROPOSED`
`PROMOTION = PENDING INDEPENDENT VALIDATION`
