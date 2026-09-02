# P8 — GOVERNANCE REP-013 KNOWN-MAPPED INVENTORY RECONCILIATION — MUTATION MATRIX

Transaction ID: `MUT-2026-09-02-P8-GOVERNANCE-REP013-INVENTORY-001`
Priority: `8 — Governance`
State: `PRE-WRITE / MATERIAL MUTATION NOT YET APPLIED`
Entry HEAD: `c99fe4482a8f216ac61b3df4fd4f6d6e0cfa2c7e`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-011 / REP-013 / REP-016 + CURRENT ADDENDA`

## Legal-entry proof

- P1–P7 are operationally closed by current closure evidence/addenda; P7 closure HEAD `c99fe4482...` is exact-head 4-of-4 green.
- P8 remains `INVENTORYING / BOUNDED SEMANTIC REPAIRS IN PROGRESS` in REP-016.
- `Governance/_FOLDER_STATUS.md` remains current evidence with identity/inventory migration closed for its bounded scope and `CONTENT REVIEW HOLDS REMAIN`.
- No newer main commit establishes a P1–P7 reopen condition.

Therefore `Priority 8 — Governance` is the first legal open priority. Queue reconstruction stops here.

## Material gap

`Repository/REP-013_REPOSITORY_CONTENT_TREE.md` currently presents the Governance known-mapped inventory only through `GOV-013A`, while the current Governance status evidence records migrated/current identities through `GOV-027` plus explicit active/candidate/compatibility distinctions.

This transaction reconciles only the **known-mapped Governance inventory surface**. It does not claim exhaustive physical enumeration, content closure, relationship completeness, authority promotion, Phase-1 closure, Connected Baseline closure, or Global PASS.

## Source boundary

- REP-013 source blob at entry: `011422383f7646630a47885fb911a40949f607e3`
- Governance status source blob at entry: `55e56d210d34dd4150ec59b4a83305db356e2332`
- Target section: `REP-013 → Domain Content Inventory → Governance/`
- All REP-013 sections outside the Governance subsection are `KEEP`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-001 | `REP-013` Governance subsection | UPDATE | reconcile known-mapped Governance identities to current `_FOLDER_STATUS` evidence while preserving authority distinctions | N | N |
| P8-002 | all other `REP-013` sections | KEEP | content-equivalent preservation; no unrelated queue/domain/status change | N | N |
| P8-003 | this Matrix | UPDATE | finalize exact applied scope and verification evidence in same material change set | N | N |

## KEEP / forbidden

No mutation to Governance source authorities, REP-016 canonical body, REP-014 relationship semantics, candidate authority/status, Room71 state, Core, Architecture, Runtime, or global integrity claims.

No stale physical path may be promoted merely because it exists. No candidate becomes canonical through inventory synchronization.

## Verification contract

`PRE-WRITE MATRIX → LIVE HEAD RECHECK → COMPLETE REP-013 SOURCE READ FOR TARGET/PRESERVATION BOUNDARY → BUILD COMPLETE CANDIDATE → EXPECTED CHANGE ONLY → MATERIAL COMMIT WITH FINALIZED MATRIX → READ-BACK → EXACT-HEAD CI → CLOSE OR HARD HOLD`.

Required: unexpected changes `0`; Full-Stack, Runtime/Integration, Real Mutation Matrix and M2 must remain green when triggered.

## Learning

`A CURRENT FOLDER-IDENTITY MIGRATION IS NOT CONTROL-PLANE COMPLETE WHILE ITS KNOWN-MAPPED REP-013 INVENTORY STILL DESCRIBES THE PRE-MIGRATION SURFACE.`
