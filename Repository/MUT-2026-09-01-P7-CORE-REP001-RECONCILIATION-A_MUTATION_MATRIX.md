# MUT-2026-09-01-P7-CORE-REP001-RECONCILIATION-A — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-REP001-RECONCILIATION-A
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: PREWRITE / OPEN
Date: 2026-09-01
Entry HEAD: `044c40c6b36fad9ab9c059322073ff7a2e03c98b`

## Problem / change definition
Priority 7 Core local inventory is reconciled, and REP-013 Core physical inventory was reconciled in P337. Current evidence still records a bounded REP-001 drift: `Core/CORE-000A_PLATFORM_GLOSSARY.md` is a current official/revalidated Core reference and appears in exact current Core inventory, but the REP-001 active Core list does not visibly include it. REP-002 remains a separate follow-up because it has two mapped-path gaps (`CORE-000A` and `CORE-012`).

## Prior-learning retrieval
- P336 established the exact 18-file top-level Core inventory and explicitly recorded the REP-001/REP-002 drift.
- P337 proved that large control-plane documents should be reconciled in separate bounded transactions.
- P337 HARD HOLD proved that any version change to a current-manifest-listed REP artifact must synchronize `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` in the same functional change set or immediately fail closed.
- GOV-014A requires this Matrix to exist before protected mutation.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| A-01 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | Add `Core/CORE-000A_PLATFORM_GLOSSARY.md` to Core Layer, advance REP-001 version/audit metadata, and append bounded reconciliation wording without promoting Core certification | N | N |
| A-02 | `Quality/Integration/test_core_rep001_control_plane_reconciliation.py` | CREATE | Direct regression proving CORE-000A is indexed while legacy `CORE-000_PLATFORM_IDENTITY.md` remains outside active REP-001 inventory | N | N |
| A-03 | `Repository/P7_CORE_REP001_CONTROL_PLANE_RECONCILIATION_2026-09-01_A.md` | CREATE | Bounded progress/evidence record | N | N |
| A-04 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | Synchronize REP-001 version row and current checkpoint/source baseline only | N | N |
| A-05 | this Matrix | UPDATE | Same-change-set execution state and exact target accounting | N | N |

## KEEP requirements
Preserve byte/content-equivalent state outside the explicitly authorized REP-001 metadata/Core-section/reconciliation wording and the current-manifest checkpoint/REP-001 row. KEEP unchanged: REP-002, REP-013, REP-011/014/015/016 canonical bodies, all Core authority files, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

`Core/CORE-000_PLATFORM_IDENTITY.md` is a physical provenance artifact with `Canonical: No / Legacy / Superseded` and MUST NOT be promoted into the active REP-001 Core list.

## Pre-write validation state
- Live main rediscovered at `044c40c6b36fad9ab9c059322073ff7a2e03c98b`.
- Exact-head workflows at that head are green.
- Direct current REP-001 read confirms CORE-000A absent from its active Core list.
- Direct current Core status read confirms CORE-000A is present in the exact physical inventory and explicitly records the REP-001 gap.
- Direct current CORE-000A read confirms `Document ID: CORE-000A`, `Version: 1.2.0`, `Status: Official / Revalidated / Integrity Hold`, `Classification: Core Reference`.
- Current manifest lists REP-001 version `1.11.3`; any REP-001 version advance must be synchronized atomically.

## Closure boundary
This transaction may close only the REP-001 Core inventory drift for CORE-000A. Priority 7 remains OPEN. REP-002 Core mapping drift, GOV-006 disposition, Core dependency/consumer validation, relationship reconciliation, Core certification, Phase 1, repository-wide graph and Global Connected Baseline remain OPEN / not certified.
