# EJR-207 — P2 REL-003 Semantic Direction Decision

Date: 2026-08-17  
Status: RECORDED / SESSION-CLOSABLE / DECISION ESTABLISHED — MUTATION PENDING  
Scope: Priority-2 relationship validation — `REL-003`  
Repository: Sangaa/ARGO-KOP  
Branch: main  
Development Baseline: 3.2.1  
Integrity State: INTEGRITY HOLD / CONNECTED-BASELINE AUDIT

## Decision Evidence

Current canonical endpoints were re-read:

- `ENG-004_VALIDATION_ENGINE.md` states that the Validation Engine is consumed by `SRV-005` at the Service layer.
- `SRV-005_VALIDATION_SERVICE.md` states that `SRV-005` is the Service-layer consumer of `ENG-004`.

The two independent endpoint statements are semantically consistent.

## Decision

The controlled relationship representation for `REL-003` is:

`SRV-005 → ENG-004 = CONSUMES`

This decision corrects the direction/type semantic representation only.

It does **not** promote the relationship to `Verified`, does not claim executable coupling, and does not alter either endpoint.

## Mutation Boundary

Only the single `REL-003` registry record is eligible for mutation.
All other `REP-014` content must remain byte/content-preserved.

## Learning / Error Correction

1. Historical registry origin establishes provenance, not semantic authority.
2. When both current canonical endpoints independently state the same relationship direction, that aligned endpoint evidence can establish the semantic decision.
3. Relationship decision and registry promotion are separate gates.
4. Correcting direction/type does not by itself justify `Verified` state.

## Current State

`REL-003 = SEMANTIC DIRECTION RESOLVED / CONTROLLED TYPE CONSUMES / STATE REVALIDATION REQUIRED`

`P2 = OPEN / RELATIONSHIP_VALIDATION`

## Next Safe Action

Perform the single-row content-preserving REP-014 mutation, re-read the file, verify only the intended REL-003 row changed, and preserve the `Revalidation Required` state until the broader relationship validation gates are satisfied.

---

End of EJR-207
