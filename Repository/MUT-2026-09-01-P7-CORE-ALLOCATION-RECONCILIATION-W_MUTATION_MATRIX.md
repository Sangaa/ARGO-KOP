# MUTATION MATRIX — P7 CORE ALLOCATION RECONCILIATION W

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-CORE-ALLOCATION-20260901`
Priority: `7 — Core`
State: `MATERIAL CANDIDATE PREPARED / W-B CONTROLLING / CI PENDING / LEASE ACTIVE`
Entry HEAD: `911f51d3a0881728125b36bfc09d266214730154`
Initial Matrix HEAD: `f2543f809e1058c576c59de372354bf17ee2cdb1`
W-A pre-write amendment: `73026147ae2a084f7be89c4c43ef70faab39fbdd`
Refined Matrix HEAD: `2a82218d8faf47ceea81d9e72a3edb00f0897007`
W-B pre-write amendment HEAD: `f0f564b68cd6e0f957327839db40316ea73c22cf`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-014 / REP-015 / REP-016`

## Current controlling plan

V established the missing Core allocation prerequisite. Exact current Core inventory remains 18 top-level files and `Core/Core.md` independently lists the other 17 members.

W-A correctly detected manifest synchronization if canonical REP-012 were version-mutated and required durable regression. Deeper pre-material inspection then established content-preservation risk from rewriting the long REP-012 body merely to append bounded records.

W-B supersedes only the direct REP-012/REP-020 write surface. It preserves W-A's focused regression requirement and records Core allocation in a non-replacing REP-012 addendum subordinate to canonical REP-012.

## Authorized material change set — exactly 7 paths

1. `Repository/REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md`
2. `Quality/Integrity/test_core_allocation_registry_coverage.py`
3. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
4. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
5. this W Matrix
6. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A_AMENDMENT_MATRIX.md`
7. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-B_CONTENT_PRESERVATION_AMENDMENT.md`

Candidate must be exactly one commit after W-B pre-write HEAD `f0f564b68cd6e0f957327839db40316ea73c22cf`, exactly seven paths, unexpected expansion `0`.

## Allocation semantics

`ALLOCATED = valid Core domain/path assignment only`.

Legacy `Core/CORE-000_PLATFORM_IDENTITY.md` remains `Canonical: No / Legacy / Superseded` and is allocated only because it is a known physical Core file.

## Explicitly forbidden

- no canonical REP-012 body mutation;
- no REP-020 mutation because canonical REP-012 identity/version/status remain unchanged;
- no Core source/status mutation;
- no REP-013 weakening;
- no REP-014 relationship mutation;
- no REP-016 closure mutation;
- no Core certification / `CLOSED_FOR_PHASE_1` / Priority-7 closure;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Verification contract

`ONE-COMMIT/SEVEN-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY W/W-A/W-B CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

After W closure: fresh Explicit Core Certification Review is mandatory. No automatic certification.

## Learning retained

`ALLOCATION COMPLETENESS IS A CLOSURE PREREQUISITE, NOT A SUBSTITUTE FOR REVIEW, RELATIONSHIP VALIDATION OR CERTIFICATION.`

`BOUNDED ADDITIVE EVIDENCE SHOULD NOT FORCE A HIGH-RISK WHOLE-FILE REWRITE OF A LARGE CONTROL-PLANE HISTORY.`
