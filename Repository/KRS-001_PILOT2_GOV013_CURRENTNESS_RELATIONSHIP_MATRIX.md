# KRS-001 Pilot 2 — GOV-013 Currentness & Relationship Matrix

Transaction: `MUT-2026-08-25-KRS001-PILOT-002`
Status: `PRE-WRITE / CONTROLLED`
Authority: `GOV-013 + KRS-001_SCHEMA_REFINEMENT_V0.2`

## Candidate
`Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`

## Why this artifact
A heterogeneous governance/control artifact is required by KRS-001 v0.2 to test temporal validity, policy assertions, authority and relationships without interface-specific assumptions.

## Currentness Gate
- Current content: inspected at the current repository lineage before mutation.
- Declared identity: GOV-013, Version 1.1.2, Approved / Canonical / Session Operating Contract.
- Known direct-change history: includes the 2026-08-25 CI failure/root-cause and no-transition gate change; earlier registration/reconciliation changes also exist.
- Later relevant evidence: current KRS-001/ERIG learning must be checked before any objectization.
- Currentness classification for this pilot: `CURRENT-VERIFIED` for its governance-contract role, subject to relationship reconciliation below.

## Relationship Review
1. GOV-013 → KRS-001 work plan: governing/operating authority; verify current reference.
2. GOV-013 → session closure: governing procedure; verify current closure clauses.
3. GOV-013 → CI failure gate: explicit policy; current direct-change lineage exists.
4. GOV-013 → repository control-plane artifacts: authority relationship; do not infer executable dependency.
5. GOV-013A references: must distinguish reference/registration from authority or implementation.

## Evidence Classification
- `GOV-013` content itself: canonical policy source.
- Commit history: provenance evidence for policy evolution.
- KRS-001 work plan: downstream operationalization evidence, not replacement authority.
- CI runs: execution evidence for implementations, not proof that a governance statement is true.

## Critical Questions Before Object Creation
- Can v0.2 represent policy assertions with temporal validity without treating them as executable facts?
- Can authority and reference relationships remain distinct?
- Can historical policy changes be preserved append-only?
- Can the object distinguish `CANONICAL` from `CURRENT-VERIFIED`?
- Can a later policy mutation supersede a prior assertion without deleting it?

## Mutation Boundary
No source replacement. No modification to GOV-013 in this transaction. The only authorized next mutation is a supplemental v0.2 Knowledge Object after this matrix is reviewed and the relationship/currentness questions are resolved.

## Stop Conditions
Stop if current content cannot be reconciled with its latest direct changes; if a material authority relationship is contradictory; if v0.2 requires interface-specific fields; or if the object would imply executable authority unsupported by evidence.

## Next Action
Review this matrix and perform direct relationship verification. Only then create the second-pilot Knowledge Object if the schema survives the heterogeneous governance case.
