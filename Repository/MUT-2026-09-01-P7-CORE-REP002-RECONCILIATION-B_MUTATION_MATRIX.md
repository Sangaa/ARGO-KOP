# MUT-2026-09-01-P7-CORE-REP002-RECONCILIATION-B — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-REP002-RECONCILIATION-B
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: PREWRITE / OPEN
Date: 2026-09-01
Entry HEAD: `d3c8aed1cc9c16afb752033f6baa8005d8b0834f`

## Problem / change definition
Priority 7 Core local inventory was reconciled by P336, REP-013 physical content by P337, and REP-001 CORE-000A discoverability by the immediately preceding transaction. Current direct REP-002 inspection still shows two bounded Core mapping gaps: `Core/CORE-000A_PLATFORM_GLOSSARY.md` and `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` are physically present/current Core artifacts but absent from the REP-002 Core map.

## Prior-learning retrieval
- P336 established the exact current Core inventory and explicitly identified REP-002 gaps for CORE-000A and CORE-012.
- P337 deliberately separated large control-plane reconciliations rather than mutating REP-001/002/013 together.
- The preceding REP-001 transaction proved manifest scope must be checked directly; REP-002 is not listed in the current REP-020 executable manifest, so no manifest expansion is authorized by this transaction.
- GOV-014A requires this Matrix before protected mutation.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| B-01 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | Add CORE-000A and CORE-012 to Core Layer, advance bounded metadata, and add non-promotion/reconciliation wording | N | N |
| B-02 | `Quality/Integration/test_core_rep002_control_plane_reconciliation.py` | CREATE | Direct regression proving both current Core paths are mapped and legacy CORE-000 identity is not promoted as active mapping | N | N |
| B-03 | `Repository/P7_CORE_REP002_CONTROL_PLANE_RECONCILIATION_2026-09-01_B.md` | CREATE | Bounded progress/evidence record | N | N |
| B-04 | this Matrix | UPDATE | Same-change-set execution state and exact target accounting | N | N |

## KEEP requirements
KEEP unchanged: REP-001, REP-013, REP-011/014/015/016 canonical bodies, REP-020 manifest, all Core authority files, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

`Core/CORE-000_PLATFORM_IDENTITY.md` remains `Canonical: No / Legacy / Superseded` and MUST NOT be promoted into the active REP-002 Core map.

## Pre-write validation
- Live main rediscovered at `d3c8aed1cc9c16afb752033f6baa8005d8b0834f`.
- Exact-head workflows visible at entry head are green.
- Direct REP-002 read confirms CORE-000A and CORE-012 absent from its Core map.
- Independent repository search recovers P336 evidence explicitly identifying exactly those two REP-002 gaps.
- REP-013 current text records CORE-000A and CORE-012 as physically present current Core artifacts while keeping active/mapped reconciliation separate.

## Closure boundary
This transaction may close only the REP-002 Core mapping drift for CORE-000A and CORE-012. Priority 7 remains OPEN. GOV-006 disposition, Core dependency/consumer validation, relationship reconciliation, explicit Core certification, Phase 1, repository-wide graph and Global Connected Baseline remain OPEN / not certified.
