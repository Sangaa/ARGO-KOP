# Priority 7 — Core Kernel → RUN-001 Relationship E

Date: 2026-09-01
State: `CLOSURE CANDIDATE / RECOVERY CI VERIFIED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Recovery HEAD: `5e3020fe8c1bea33479edd1382c592aac3a7e64a`

## Finding

`CORE-KERNEL` is a canonical Core/Runtime Contract surface that explicitly aligns its runtime lifecycle to `Runtime/RUN-001_BOOT_SEQUENCE.md`, but the relationship registry did not represent that bounded documentary seam.

## Relationship classification

`CORE-KERNEL → RUN-001 = REFERENCES`

Disposition:

`INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

`Architecture/ARC-006_DEPENDENCY_MODEL.md` keeps Core free of lower-layer architectural dependencies. Direct reverse review did not prove a specific `RUN-001 → CORE-KERNEL` dependency/consumer edge, so no reverse relationship was manufactured for symmetry.

## Applied construction

- `REP-014` advanced to v1.2.7 and added `REL-062` only.
- Added the focused `test_core_kernel_run001_relationship_boundary.py` regression.
- `Core/_FOLDER_STATUS.md` advanced to v1.3.3 while preserving the cross-layer/certification hold.
- Current control-plane manifest was refreshed to REP-014 v1.2.7 and rebound atomically to the governing Matrix after same-change-set enforcement exposed the write-surface gap.

## CI root-cause learning

1. `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH` — repaired by protecting the durable Kernel semantic boundary rather than incidental prose.
2. `STALE REGRESSION / TRANSIENT STATUS-WORDING OVERREACH` — repaired while retaining remaining P7, REP-014, certification and no-global-close guards.
3. `REAL COMPANION EVIDENCE DRIFT / CURRENT-MANIFEST FRESHNESS VIOLATION` — REP-014 v1.2.7 required refresh of the executable current control-plane manifest.
4. `SAME-CHANGE-SET MATRIX BINDING VIOLATION / WRITE-SURFACE ATOMICITY GAP` — prewrite Matrix presence was insufficient when a later single-file protected commit omitted the Matrix from the exact Git change set; recovery used one atomic Git-object commit with manifest + Matrix.

Directly reused prior learning: EJR-179, Current Control-Plane Manifest Rebind-010, and Matrix Same-Changeset Repair-187.

## Recovery verification

Exact recovery HEAD `5e3020fe8c1bea33479edd1382c592aac3a7e64a`:

- Runtime/Integration `33485141412` — SUCCESS.
- Full-Stack Repository Audit `33485141368` — SUCCESS.
- M2 `33485141342` — SUCCESS.
- Real Mutation Matrix Regression `33485141435` — SUCCESS.
- Atomic recovery diff from authorization HEAD contained exactly two paths: this transaction Matrix and `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`; unexpected paths = `0`.

## Boundary

This transaction does not modify `CORE-KERNEL`, `RUN-001`, `CORE-003`, or `ARC-006` authority text. It does not claim executable coupling, complete Core-to-Runtime graph validation, Core certification, Phase-1 closure, repository-wide graph closure, or Global Connected Baseline PASS.

## Closure discipline

Recovery CI is green, but Transaction E becomes closed only after the formal closure-lineage commit itself passes exact-head required CI. Priority 7 remains OPEN regardless of E closure.

## Resume point

After exact closure-head CI, recompute the next material Core authority dependency/consumer seam from live repository evidence and reconcile REP-014 only where evidence requires.
