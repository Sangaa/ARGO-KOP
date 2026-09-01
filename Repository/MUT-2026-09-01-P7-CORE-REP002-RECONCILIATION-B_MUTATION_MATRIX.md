# MUT-2026-09-01-P7-CORE-REP002-RECONCILIATION-B — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-REP002-RECONCILIATION-B
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: FUNCTIONAL-CANDIDATE / CI-PENDING / REDUNDANT-MATRIX-COMMIT-RECORDED
Date: 2026-09-01
Entry HEAD: `d3c8aed1cc9c16afb752033f6baa8005d8b0834f`
Initial prewrite HEAD: `07c4fe0305dd441d0ac8bc78c53997659a7ee9bb`
Current pre-functional HEAD: `196f9df2e73a7a76934340de8c5d22b294baeb16`

## Problem / change definition
Priority 7 Core local inventory was reconciled by P336, REP-013 physical content by P337, and REP-001 CORE-000A discoverability by the immediately preceding transaction. Current direct REP-002 inspection still shows two bounded Core mapping gaps: `Core/CORE-000A_PLATFORM_GLOSSARY.md` and `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` are physically present/current Core artifacts but absent from the REP-002 Core map.

## Prior-learning retrieval
- P336 established the exact current Core inventory and explicitly identified REP-002 gaps for CORE-000A and CORE-012.
- P337 deliberately separated large control-plane reconciliations rather than mutating REP-001/002/013 together.
- The preceding REP-001 transaction proved manifest scope must be checked directly; REP-002 is not listed in the current REP-020 executable manifest, so no manifest expansion is authorized by this transaction.
- GOV-014A requires this Matrix before protected mutation.

## Execution discipline incident
After the initial prewrite reached green exact-head CI, the Matrix was submitted again with content identical to the existing Matrix. GitHub created commit `196f9df2e73a7a76934340de8c5d22b294baeb16` with the same tree as parent `07c4fe0305dd441d0ac8bc78c53997659a7ee9bb`. This is unnecessary Matrix-only history and is retained as negative execution evidence. No protected functional target or repository content changed. The functional candidate is rebuilt from `196f9df2...`; no force update, history rewrite or bypass is used.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| B-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | Add CORE-000A and CORE-012 to Core Layer, advance bounded metadata, and add non-promotion/reconciliation wording | Y | candidate |
| B-02 | `Quality/Integration/test_core_rep002_control_plane_reconciliation.py` | CREATE | Direct regression proving both current Core paths are mapped and legacy CORE-000 identity is not promoted as active mapping | Y | candidate |
| B-03 | `Repository/P7_CORE_REP002_CONTROL_PLANE_RECONCILIATION_2026-09-01_B.md` | CREATE | Bounded progress/evidence record | Y | candidate |
| B-04 | this Matrix | UPDATE | Same-change-set execution state and exact target accounting | Y | candidate |

## KEEP requirements
KEEP unchanged: REP-001, REP-013, REP-011/014/015/016 canonical bodies, REP-020 manifest, all Core authority files, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

`Core/CORE-000_PLATFORM_IDENTITY.md` remains `Canonical: No / Legacy / Superseded` and MUST NOT be promoted into the active REP-002 Core map.

## Candidate validation
The prepared REP-002 candidate preserves all existing sections and changes only bounded metadata, Core Layer membership/wording, and a final P7 reconciliation note. The functional candidate contains exactly four authorized paths: REP-002, one direct regression, one progress record and this Matrix.

## Pre-write validation
- Live main rediscovered at `d3c8aed1cc9c16afb752033f6baa8005d8b0834f`.
- Initial prewrite exact-head CI at `07c4fe0305dd441d0ac8bc78c53997659a7ee9bb` completed without observed failures or in-progress runs in the inspected Actions response.
- `196f9df2...` is tree-identical to `07c4fe03...`; it adds no content delta.
- Direct REP-002 read confirms CORE-000A and CORE-012 absent from its Core map before mutation.
- Independent repository search recovers P336 evidence explicitly identifying exactly those two REP-002 gaps.
- REP-013 current text records CORE-000A and CORE-012 as physically present current Core artifacts while keeping active/mapped reconciliation separate.

## Functional validation required
1. Assemble exactly the four authorized paths over current pre-functional HEAD `196f9df2e73a7a76934340de8c5d22b294baeb16`.
2. Compare exact diff before ref movement.
3. Re-read live main and require unchanged current pre-functional HEAD.
4. Fast-forward `main` only with `force=false`.
5. Read back REP-002 and progress record.
6. Require all relevant exact-head workflows to complete successfully.
7. Close this Matrix only after green CI.

## Closure boundary
This transaction may close only the REP-002 Core mapping drift for CORE-000A and CORE-012. Priority 7 remains OPEN. GOV-006 disposition, Core dependency/consumer validation, relationship reconciliation, explicit Core certification, Phase 1, repository-wide graph and Global Connected Baseline remain OPEN / not certified.
