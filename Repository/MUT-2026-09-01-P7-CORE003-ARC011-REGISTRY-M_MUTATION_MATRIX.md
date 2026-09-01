# MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 REGISTRY RECONCILIATION — M

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Priority: `7 — Core cross-layer validation`
State: `MATERIAL-CANDIDATE / LEASE ACTIVE / CI-PENDING`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

Live main was independently rediscovered at the Entry HEAD. REP-016 still places Core as the first open Phase-1 partition. Core status requires continued relationship reconciliation where evidence requires. Transaction L is closed/resume-safe and directly validated the bounded pair:

`CORE-003 → ARC-011 = GOVERNS`

`ARC-011 → CORE-003 = REFERENCES`

REP-014 v1.2.11 did not register either pair. Therefore M reconciles exactly those validated relationships before opening a new Core seam.

## Prior-learning classification

- Transaction L CORE-003↔ARC-011 validation — `DIRECTLY APPLICABLE`.
- Existing REL-037/038 CORE-003↔RUN-001 governing/reference representation — `DIRECTLY APPLICABLE` controlled-type precedent.
- Transaction K ARC-006→CORE-003 registry reconciliation — `DIRECTLY APPLICABLE` mutation/manifest synchronization pattern.
- Transactions H/J documentary one-way discipline — `TRANSFERABLE`.
- Transaction I CORE-000 semantic repair — `NOT APPLICABLE`.
- Historical broad architecture compliance claims not rebound to current source evidence — `STALE`.

## Authorized material change set

1. `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` — bump version exactly once and append exactly two bounded rows after REL-067: REL-068 GOVERNS and REL-069 REFERENCES, plus bounded reconciliation rationale.
2. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` — synchronize REP-014 version/current refresh binding.
3. `Core/_FOLDER_STATUS.md` — record the newly registered sixth cross-layer seam while preserving Integrity Hold and pending certification.
4. `Quality/Integrity/test_core003_arc011_authority_boundary.py` — convert L validation-first absence assertions into exact bounded registry assertions while retaining anti-overpromotion assertions.
5. `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M.md` — transaction evidence.
6. This Matrix — rebound in the same material change set.

## KEEP / non-authority

- No mutation to `Core/CORE-003_CONSTITUTION.md`.
- No mutation to `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`.
- No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, runtime or executable promotion.
- No reversal of governing direction.
- No Core or Architecture certification.
- No Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.
- No unrelated REP-014 cleanup.

## Verification contract

`PRE-WRITE MATRIX → ONE ATOMIC MATERIAL COMMIT → EXACT-HEAD READ-BACK → DIFF SCOPE CHECK → REQUIRED CI/RUNTIME/INTEGRITY → LEARNING CAPTURE → LEASE CLOSE → CLOSURE-HEAD CI`

The material candidate is constructed as one commit whose parent is the pre-write Matrix HEAD. Any unexpected path expansion, main movement before atomic write, failed required gate or source contradiction stops M rather than being silently repaired.
