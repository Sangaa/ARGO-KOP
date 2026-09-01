# Priority 7 — Core Kernel → RUN-001 Relationship E

Date: 2026-09-01
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Atomic Recovery HEAD: `5e3020fe8c1bea33479edd1382c592aac3a7e64a`
Closure-Lineage HEAD: `adf8a10774ab8cf20b05aef2c66296b1f1054d6d`

## Finding

`CORE-KERNEL` explicitly aligns its runtime lifecycle to `Runtime/RUN-001_BOOT_SEQUENCE.md`. The strongest justified registry state is:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

ARC-006 keeps Core free of lower-layer architectural dependencies. Direct reverse review did not prove a specific `RUN-001 → CORE-KERNEL` dependency/consumer edge, so no reverse edge was manufactured for symmetry.

## Applied construction

- `REP-014` advanced to v1.2.7 and added `REL-062` only.
- Added focused seam regression `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py`.
- `Core/_FOLDER_STATUS.md` advanced to v1.3.3 while preserving cross-layer validation and certification HOLD.
- Current control-plane manifest was refreshed to REP-014 v1.2.7.
- Same-change-set enforcement recovery atomically rebound the protected current manifest and Transaction E Matrix.

## Captured failure learning

1. `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH` — protect durable semantics, not incidental prose.
2. `STALE REGRESSION / TRANSIENT STATUS-WORDING OVERREACH` — preserve semantic HOLD boundaries while allowing truthful bounded progress wording.
3. `REAL COMPANION EVIDENCE DRIFT / CURRENT-MANIFEST FRESHNESS VIOLATION` — refresh executable current evidence when a listed artifact version changes.
4. `SAME-CHANGE-SET MATRIX BINDING VIOLATION / WRITE-SURFACE ATOMICITY GAP` — prewrite authorization does not replace exact-change-set Matrix binding; atomic Git-object recovery is required where the write surface otherwise splits protected mutation from its Matrix.

Prior learning reused: EJR-179, Current Control-Plane Manifest Rebind-010, Matrix Same-Changeset Repair-187.

## Recovery CI

Exact atomic recovery HEAD `5e3020fe8c1bea33479edd1382c592aac3a7e64a`:
- Runtime/Integration `33485141412` — SUCCESS.
- Full-Stack `33485141368` — SUCCESS.
- M2 `33485141342` — SUCCESS.
- Real Mutation Matrix Regression `33485141435` — SUCCESS.

## Closure-lineage CI

Exact closure-lineage HEAD `adf8a10774ab8cf20b05aef2c66296b1f1054d6d`:
- Runtime/Integration `33485367772` — SUCCESS.
- Full-Stack `33485367631` — SUCCESS.
- M2 `33485367723` — SUCCESS.
- Real Mutation Matrix Regression `33485367670` — SUCCESS.

Therefore Transaction E is functionally closed and CI-verified.

## Boundary

Transaction E does not modify `CORE-KERNEL`, `RUN-001`, `CORE-003`, or `ARC-006` authority text and does not claim executable coupling, complete Core graph validation, Core certification, Phase-1 closure, repository-wide graph closure, or Global Connected Baseline PASS.

Priority 7 remains OPEN.

## Next legal action

Rediscover live `main`, then recompute the next material Core authority dependency/consumer seam from current repository evidence. Reconcile REP-014 only where evidence requires; do not create graph symmetry without evidence.
