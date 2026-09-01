# MUT-2026-09-01-P7-CORE-LOCAL-INVENTORY-336 — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-LOCAL-INVENTORY-336
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: OPEN / PREWRITE
Date: 2026-09-01
Entry HEAD: `e108f36975caae209d82a71f85c9a7e3c9e87755`

## Objective
Perform the smallest sufficient Priority-7 Core mutation: reconcile the exact current top-level Core physical inventory with the local `Core/Core.md` inventory surface and `Core/_FOLDER_STATUS.md`, add a direct regression, and record bounded P7 progress without claiming Core certification or modifying broader repository control-plane / cross-layer authority.

## Evidence basis
- Exact current `Core/` enumeration contains 18 top-level files, including `CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`.
- `CORE-012` is a legitimate canonical Core artifact created by the 2026-08-18 identity-collision repair, not an accidental duplicate.
- Current `Core/Core.md` omits `CORE-012` from its member inventory.
- Current `Core/_FOLDER_STATUS.md` predates `CORE-012` and leaves cross-layer review / certification open.
- Current REP-002 and REP-013 remain separately stale for Core; current REP-001 also omits CORE-000A from its visible active Core list. Those protected control-plane repairs are intentionally deferred to a whole-file-safe follow-up transaction.
- Current GOV-006 still contains a cross-layer Core path/naming discrepancy; Governance disposition is intentionally outside this local P336 mutation.
- No current `Quality/Integration/test_core_inventory_discoverability.py` exists; independent search confirms only the historical aborted-P136 reference.

## Authorized functional change set
| Change | Target | Action | Applied | Verified |
|---|---|---|---:|---:|
| 336-01 | `Core/Core.md` | UPDATE local inventory to include CORE-012 and current reconciliation boundary | N | N |
| 336-02 | `Core/_FOLDER_STATUS.md` | UPDATE exact local inventory/re-audit state while preserving Integrity Hold and certification hold | N | N |
| 336-03 | `Quality/Integration/test_core_local_inventory_reconciliation.py` | CREATE direct exact-inventory regression | N | N |
| 336-04 | `Repository/P7_CORE_LOCAL_INVENTORY_RECONCILIATION_336_2026-09-01.md` | CREATE bounded P7 progress record | N | N |
| 336-05 | `Repository/REP-016_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P336.md` | CREATE current P7 operational progress addendum | N | N |
| 336-06 | `Repository/REP-011_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P336.md` | CREATE traceability addendum | N | N |
| 336-07 | this Matrix | UPDATE in same functional change set | N | N |

## KEEP requirement
KEEP unchanged in P336: `Repository/REP-001_MASTER_INDEX.md`, `Repository/REP-002_REPOSITORY_MAP.md`, `Repository/REP-013_REPOSITORY_CONTENT_TREE.md`, `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`, all Governance/Architecture/Runtime/Engine/Services/Interfaces artifacts, all Core authority documents `CORE-000*` through `CORE-012` and `ARGO_KERNEL.md`, and all relationship semantics. The legacy noncanonical `CORE-000_PLATFORM_IDENTITY.md` remains preserved. No Core certification, Phase-1 closure, Global Connected Baseline, or global integrity claim is authorized.

## Pre-write classification
`PRIORITY 7 = IN_PROGRESS / LOCAL INVENTORY DRIFT VERIFIED / CONTROL-PLANE + CROSS-LAYER VALIDATION OPEN`.

P336 closes only the Core-local inventory/index/status subgate if exact-head verification succeeds. It must not close Priority 7.

## Required verification
1. Functional diff limited to exactly the seven authorized paths.
2. Local regression proves `Core/Core.md` member inventory equals exact current top-level `Core/` files excluding the self-index file, and proves CORE-012/status synchronization.
3. Exact-head Full-Stack Repository Audit succeeds.
4. Exact-head Runtime/Integration suite succeeds.
5. Exact-head Real Mutation Matrix Regression succeeds.
6. Exact-head M2 succeeds.
7. Post-write read-back of Core index/status and Matrix succeeds.

Any relevant failure is a HARD HOLD.
