# AMENDMENT MATRIX — P7 CORE ALLOCATION RECONCILIATION W-A

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A`
Parent Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-A-CORE-ALLOCATION-MANIFEST-20260901`
Priority: `7 — Core`
State: `PRE-WRITE AMENDMENT / LEASE ACTIVE`
Entry HEAD: `f2543f809e1058c576c59de372354bf17ee2cdb1`

## Why this amendment exists

W correctly identified REP-012 Core allocation reconciliation as the blocker returned by Explicit Certification Review V, but its original four-path authorized set omitted the current control-plane boundary manifest.

Current `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` explicitly lists REP-012 v1.0.10 and requires the manifest to be refreshed whenever a listed artifact materially changes identity, version, or status.

Because W must increment REP-012 version while preserving its status, mutating REP-012 without synchronizing the manifest would create a deterministic control-plane mismatch. W-A repairs the mutation plan before any W material mutation occurs.

## Additional durable verification rationale

REP-013 requires every known Core file to have an allocation record before folder closure. A focused regression should bind the Core physical inventory, Core local index and REP-012 Core allocation population so future inventory drift fails closed instead of silently invalidating certification evidence.

The regression must preserve:

- physical inventory coverage, not semantic certification;
- exact current 18 top-level Core paths;
- self-excluding `Core.md` index semantics;
- explicit legacy/noncanonical treatment for `CORE-000_PLATFORM_IDENTITY.md`;
- no inference that allocation means review, relationship validation or Phase-1 closure.

## Superseding authorized material change set — exactly 7 paths

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
   - bump version;
   - add exact bounded Core allocation population for all 18 current top-level Core files;
   - keep `Phase 1 Population In Progress` and repository-wide incompleteness.
2. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
   - synchronize only the REP-012 version boundary and refresh binding; preserve all open/global-hold semantics.
3. `Quality/Integrity/test_core_allocation_registry_coverage.py`
   - enforce exact physical Core allocation coverage, self-index treatment, and legacy noncanonical preservation.
4. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
   - record evidence, scope and verification.
5. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
   - preserve the blocked V result and bind corrective handoff; no certification promotion.
6. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W_MUTATION_MATRIX.md`
   - record W-A as the controlling scope amendment and bind the final candidate.
7. this W-A Amendment Matrix
   - bind amendment and final verification evidence.

This seven-path set supersedes W's original four-path material set. No W material mutation occurred before this amendment.

## Explicitly forbidden

- no Core source or `Core/_FOLDER_STATUS.md` mutation;
- no REP-013 rule weakening;
- no REP-014 relationship mutation;
- no REP-016 Priority-7 closure;
- no Core certification or `CLOSED_FOR_PHASE_1` promotion;
- no canonical promotion of legacy `CORE-000_PLATFORM_IDENTITY.md`;
- no claim allocation = review/semantic validity/relationship completeness;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Atomicity contract

After this amendment pre-write commit, W material candidate must be exactly one commit and exactly the seven paths above. Unexpected path expansion = `0`.

## Verification contract

`EXACT CORE INVENTORY RECHECK → ONE-COMMIT/SEVEN-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → RUNTIME JOB REVIEW → FULL-STACK SHA/MATRIX/AUDIT REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY W/W-A CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

After W/W-A closure, rediscover live main and open a fresh Explicit Core Certification Review only if no new blocker exists.

## Learning

`A PRE-WRITE MATRIX IS ITSELF REVIEWABLE: IF A REQUIRED SYNCHRONIZATION SURFACE IS DISCOVERED BEFORE MATERIAL MUTATION, AMEND THE LEASE BEFORE WRITING THE MATERIAL CHANGE.`
