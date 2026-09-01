# MUTATION MATRIX — P7 CORE EXPLICIT CERTIFICATION CLOSURE X

Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Work Lease: `HERMUZ-P7-X-CORE-CERTIFICATION-CLOSURE-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX / EXPLICIT CERTIFICATION REVIEW / LEASE ACTIVE`
Entry HEAD: `4fd7d71d7e1320b643e229093a6910e18965b279`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 + W ADDENDUM / REP-013 / REP-014 / REP-015 / REP-016 / REP-020 / ARC-006 / ARC-011`

## Review question

Can `Core/` now be explicitly certified `CLOSED_FOR_PHASE_1` within the bounded Core partition after Transaction W closed the allocation prerequisite found by Explicit Certification Review V?

## Current direct evidence before write

1. live `main` at entry is `4fd7d71d7e1320b643e229093a6910e18965b279`, W closure, and W closure HEAD passed the required four workflows;
2. current `Core/` physical inventory is still exactly 18 top-level files and `Core/Core.md` remains the 17-member self-excluding inventory surface;
3. W establishes `18/18` bounded Core allocation records without canonical promotion of legacy `CORE-000_PLATFORM_IDENTITY.md`;
4. REP-013 Completion Rule requires inventory reconciliation, allocation, review state, dependency/consumer assessment, material relationship disposition, unresolved-item recording, and explicit closure decision;
5. REP-011 permits reuse of prior review evidence when content identity is unchanged, bindings remain consistent, scope remains sufficient, and current-fitness conditions are still satisfied;
6. compare from T-C2 semantic candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` to X entry HEAD contains no `Core/` path mutation; later changes are CI/Quality/Repository evidence and W allocation evidence;
7. current Core status records Transaction T's direct sweep of remaining canonical members and no additional material external coupling requiring REP-014 registration within bounded readiness scope;
8. current REP-014 v1.2.14 records the material registered/reconciled Core seams and explicitly remains a non-complete graph; `RUN-002 → CORE-003 = REFERENCES` remains `VALIDATED-NOT-REGISTERED / INTENTIONAL ONE-WAY / NON-DEPENDENCY`;
9. prior Release partition closure demonstrates the directly applicable rule that partition closure must be explicitly bound to REP-016 and cannot be inferred from green CI or closed subgates.

## Certification disposition authorized for candidate

If the exact pre-publication checks remain unchanged, X may record:

`CORE = CLOSED_FOR_PHASE_1 / BOUNDED CORE PARTITION CERTIFIED`

and:

`PRIORITY 7 = CLOSED_FOR_PHASE_1 / BOUNDED CORE PARTITION CERTIFIED / GLOBAL PHASE 1 REMAINS OPEN`.

This closes the Core-specific `CROSS-LAYER VALIDATION OPEN` certification gate only within the bounded Priority-7 evidence scope. It does not claim repository-wide graph completion or that all external domains are certified.

## Authorized material change set — exactly 20 paths

### Current state / queue / evidence surfaces
1. `Core/_FOLDER_STATUS.md`
   - v1.3.13 → v1.3.14;
   - record explicit bounded Core certification / `CLOSED_FOR_PHASE_1`;
   - preserve all historical failure/recovery evidence and all seam semantics;
   - preserve global Integrity Hold / Phase 1 open boundary.
2. `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md`
   - preserve full history and version/header;
   - change Priority 7 Core row only to bounded `CLOSED_FOR_PHASE_1` state;
   - append X closure checkpoint; Priority 8 remains the next queue row, not automatically started.
3. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
   - refresh current queue/closure binding to X while preserving listed control-plane versions/statuses, Phase 1 OPEN and Global HOLD.
4. `Repository/REP-011_PRIORITY7_CORE_CLOSURE_ADDENDUM_2026-09-01_X.md`
   - create bounded review/traceability closure evidence under REP-011.
5. `Repository/REP-013_PRIORITY7_CORE_CLOSURE_ADDENDUM_2026-09-01_X.md`
   - create explicit REP-013 Completion Rule 1–7 satisfaction mapping for Core only.
6. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_CLOSURE_2026-09-01_X.md`
   - create the explicit certification/closure decision and non-claims.

### Current-state regression transition
7. `Quality/Integration/test_core_p7_status_sync.py`
8. `Quality/Integrity/test_core_certification_readiness_boundary.py`
9. `Quality/Integration/test_core_local_inventory_reconciliation.py`
10. `Quality/Integrity/test_core003_arc011_authority_boundary.py`
11. `Quality/Integrity/test_arc006_core003_authority_boundary.py`
12. `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py`
13. `Quality/Integrity/test_core011_arc005_charter_rules_boundary.py`
14. `Quality/Integrity/test_core012_gov016_learning_boundary.py`
15. `Quality/Integrity/test_core003_run003_authority_boundary.py`
16. `Quality/Integrity/test_core_allocation_registry_coverage.py`
17. `Quality/Integrity/test_run002_core003_initialization_authority_reference.py`
18. `Quality/Integrity/test_core009_lif001_lifecycle_boundary.py`
19. `Quality/Integrity/test_core000_canonical_architecture_boundary.py`
20. `Quality/Integrity/test_architecture_readme_authority_boundary.py`

### Matrix binding
21. this Matrix.

**Correction:** the enumerated candidate set is exactly **21 paths**, not 20; the numbered list is authoritative and this correction is part of the pre-write Matrix itself. Candidate comparison must show exactly 21 changed paths and unexpected expansion = `0`.

## Regression transition rule

The test changes are not permission to weaken prior failure-detection logic. They may change only the transient current-state assertions that previously required:

- `CROSS-LAYER VALIDATION OPEN` for Core;
- `Folder Certification = Pending`;
- `Priority 7 remains OPEN`;
- readiness-but-not-certification wording.

All durable assertions MUST remain intact, including:

- exact 18-file / 17-member Core inventory;
- legacy CORE-000 `Canonical: No / Legacy / Superseded`;
- exact REL-062..072 relationship direction/type and anti-overpromotion checks;
- `RUN-002 → CORE-003` remains unregistered and non-dependency;
- REP-014 remains explicitly not a complete graph;
- Architecture/Lifecycle/Runtime external-domain holds remain independent;
- W allocation evidence remains non-promotional by itself;
- Phase 1 overall remains OPEN;
- Connected Baseline / repository-wide graph remain OPEN;
- Global integrity remains HOLD and Global PASS is NOT CLAIMED.

No test may pass merely because historical text still contains an old open-state literal. Current-state tests must assert the new explicit X closure markers.

## Explicitly forbidden

- no Core source-authority mutation other than `Core/_FOLDER_STATUS.md`;
- no REP-014 mutation or REL-073 fabrication;
- no forced registration of RUN-002→CORE-003;
- no Architecture, Runtime, Lifecycle, Governance, Services, Engine, AI or other-domain certification;
- no Phase-1 closure;
- no Connected Baseline closure;
- no repository-wide graph completion claim;
- no Global `BOOTED / INTEGRITY PASS`;
- no deletion/rewrite of historical T/T-C1/T-C2/T-C3/V/W failure or blocker evidence;
- no weakening of REP-013 Completion Rule;
- no inference that allocation alone certifies Core.

## Pre-publication fail-closed checks

Before moving `main` to the candidate:

1. re-read current live `main` and require it still equals this Matrix HEAD;
2. re-enumerate `Core/` and require exactly the same 18-file set;
3. require no Core source mutation since T-C2 semantic candidate other than the planned X status mutation;
4. require W allocation addendum still matches the exact 18-file set;
5. require REP-014 remains v1.2.14 and no new material Core relationship evidence appeared;
6. compare Matrix HEAD → candidate: exactly one commit, exactly 21 authorized paths, no others.

Any contradiction or divergence aborts X and returns to the affected gate.

## Verification contract

`PRE-WRITE MATRIX → LIVE RECHECK → EXACT INVENTORY/ALLOCATION/RELATIONSHIP RECHECK → ONE-COMMIT/21-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY X CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION → REDISCOVER LIVE MAIN → RECOMPUTE GLOBAL QUEUE`.

## Learning target

`A CERTIFICATION TRANSITION MUST UPDATE THE TESTS THAT GUARDED THE PRE-CERTIFICATION STATE WITHOUT WEAKENING THE DURABLE SEMANTIC BOUNDARIES THOSE TESTS PROVED.`
