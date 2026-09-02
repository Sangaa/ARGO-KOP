# P8 — GOVERNANCE REP-013 KNOWN-MAPPED INVENTORY RECONCILIATION — MUTATION MATRIX

Transaction ID: `MUT-2026-09-02-P8-GOVERNANCE-REP013-INVENTORY-001`
Priority: `8 — Governance`
State: `MATERIAL APPLIED / POST-COMMIT READ-BACK + CI PENDING`
Entry HEAD: `c99fe4482a8f216ac61b3df4fd4f6d6e0cfa2c7e`
Pre-write Matrix HEAD: `5013c5c4b79202d6295c069a6103c0b6f2c8eb0e`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-011 / REP-013 / REP-016 + CURRENT ADDENDA`

## Legal-entry proof

- P1–P7 are operationally closed by current closure evidence/addenda; P7 closure HEAD `c99fe4482...` is exact-head 4-of-4 green.
- P8 remains `INVENTORYING / BOUNDED SEMANTIC REPAIRS IN PROGRESS` in REP-016.
- `Governance/_FOLDER_STATUS.md` remains current evidence with identity/inventory migration closed for its bounded scope and `CONTENT REVIEW HOLDS REMAIN`.
- No newer main commit established a P1–P7 reopen condition before this transaction.

Therefore `Priority 8 — Governance` is the first legal open priority. Queue reconstruction stopped here.

## Material gap

`Repository/REP-013_REPOSITORY_CONTENT_TREE.md` presented the Governance known-mapped inventory only through `GOV-013A`, while current Governance status evidence records migrated/current identities through `GOV-027` plus explicit active/candidate/compatibility distinctions.

This transaction reconciles only the **known-mapped Governance inventory surface**. It does not claim exhaustive physical enumeration, content closure, relationship completeness, authority promotion, Phase-1 closure, Connected Baseline closure, or Global PASS.

## Source boundary

- REP-013 source blob at entry: `011422383f7646630a47885fb911a40949f607e3`
- Governance status source blob at entry: `55e56d210d34dd4150ec59b4a83305db356e2332`
- Candidate REP-013 blob: `2b612272c1edba9a414bbf2a59115900e5ec588f`
- Target section: `REP-013 → Domain Content Inventory → Governance/`
- All REP-013 sections outside the Governance subsection are `KEEP`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-001 | `REP-013` Governance subsection | UPDATE | reconcile known-mapped Governance identities to current `_FOLDER_STATUS` evidence while preserving authority distinctions | Y | N |
| P8-002 | all other `REP-013` sections | KEEP | content-equivalent preservation; no unrelated queue/domain/status change | Y | N |
| P8-003 | this Matrix | UPDATE | finalize exact applied scope in same material change set | Y | N |

## Applied scope

Current known-mapped list adds the current uniquely identified Governance paths for `GOV-014`, `GOV-015`, `GOV-016`, `GOV-018`, and `GOV-019..027` from current Governance evidence.

Non-active candidate status remains explicit for `GOV-011`, `GOV-012`, `GOV-018`, and `GOV-023..026`. Superseded/colliding compatibility paths are not promoted into the current-identity list merely because they remain physically present.

REP-013 header version/date are intentionally unchanged: this bounded subsection synchronization does not independently justify a control-plane version promotion, and avoiding an unjustified version change also avoids creating a REP-020 manifest mismatch unrelated to the actual P8 gap.

## KEEP / forbidden

No mutation to Governance source authorities, REP-016 canonical body, REP-014 relationship semantics, candidate authority/status, Room71 state, Core, Architecture, Runtime, or global integrity claims.

No stale physical path may be promoted merely because it exists. No candidate becomes canonical through inventory synchronization.

## Verification contract

`MATERIAL COMMIT → EXACT TWO-PATH COMPARE → REP-013 + MATRIX READ-BACK → EXACT-HEAD CI → CLOSE OR HARD HOLD`.

Required: unexpected changes `0`; Full-Stack, Runtime/Integration, Real Mutation Matrix and M2 must remain green when triggered.

Until read-back and CI complete, this transaction is not closed and P8 remains open.

## Learning

`A CURRENT FOLDER-IDENTITY MIGRATION IS NOT CONTROL-PLANE COMPLETE WHILE ITS KNOWN-MAPPED REP-013 INVENTORY STILL DESCRIBES THE PRE-MIGRATION SURFACE.`

`BOUNDED INVENTORY SYNCHRONIZATION DOES NOT REQUIRE COSMETIC VERSION PROMOTION WHEN THE CHANGE DOES NOT ALTER THE CONTROL-PLANE CONTRACT.`
