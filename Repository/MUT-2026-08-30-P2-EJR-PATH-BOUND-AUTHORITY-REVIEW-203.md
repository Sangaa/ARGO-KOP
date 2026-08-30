# MUT-2026-08-30-P2-EJR-PATH-BOUND-AUTHORITY-REVIEW-203

Status: OPEN / PREWRITE
Lease: R71-20260830-P2-EJR-PATH-BOUND-AUTHORITY-REVIEW-203
Baseline: main@ab0046baa80b45e36fc87c48df63393172ae01c1
Scope: bounded evidence-only authority/disposition review for EJR-211, EJR-214, EJR-219, EJR-301, EJR-302.

## Objective
Determine whether current governed consumers and artifact semantics identify a bounded referent for each duplicate EJR identity group without assigning a global namespace owner or mutating any EJR.

## Evidence to inspect
- exact competing member contents;
- exact-path consumers recovered by Lease 202;
- consumer authority/status and semantic role;
- current canonical/governed artifacts that explicitly bind learning provenance to a member;
- same-ID reuse where multiple independently legitimate records exist.

## Authorized functional scope
- Repository/P2_EJR_PATH_BOUND_AUTHORITY_REVIEW_203.md
- Repository/MUT-2026-08-30-P2-EJR-PATH-BOUND-AUTHORITY-REVIEW-203_MUTATION_MATRIX.md

## Forbidden
No EJR mutation, rename, delete, reassignment, migration, suppression, replacement allocation, canonical promotion, REP-012/016/020 change, scanner change, or Priority-2/global closure.

## Decision vocabulary
- GOVERNED_REFERENT: a current governed/canonical consumer binds the identity to the exact member path for a defined semantic role.
- BOUNDED_CHECKPOINT_REFERENT: a checkpoint/session-delta explicitly binds the identity to the exact member path, without granting global canonical ownership.
- DISTINCT_LEGITIMATE_COLLISION: multiple records are independently semantically legitimate under the reused ID; identity repair is required before uniqueness can be claimed for the historical namespace.
- UNRESOLVED: evidence remains insufficient.

No decision in this lease authorizes identity mutation by itself.
