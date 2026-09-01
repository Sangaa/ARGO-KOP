# MUTATION MATRIX — P7 CORE ALLOCATION RECONCILIATION W

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-CORE-ALLOCATION-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX / VALIDATION-FIRST / LEASE ACTIVE`
Entry HEAD: `911f51d3a0881728125b36bfc09d266214730154`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-014 / REP-015 / REP-016`

## Why W exists

Explicit Core Certification Review V established a current closure blocker: REP-013 requires every known file to have an allocation record before a folder can become `CLOSED_FOR_PHASE_1`, while current REP-012 v1.0.10 contains only the initial control-plane allocation set plus DIAG-001 and no Core artifact allocation records.

This transaction returns to the missing evidence gate. It does not weaken REP-013 and does not certify Core.

## Direct current evidence

- live Core inventory is 18 top-level files;
- `Core/Core.md` is the canonical local inventory surface and intentionally self-excludes, leaving 17 listed members;
- `CORE-000_PLATFORM_IDENTITY.md` is physical provenance / legacy / noncanonical and must remain represented without authority promotion;
- current Core readiness remains PASS but certification is blocked;
- REP-012 remains `Phase 1 Population In Progress` and explicitly defines allocation as owner/domain/path assignment, not semantic certification;
- REP-013 Completion Rule requires an allocation record for every known file before folder closure.

## Allocation semantics

W may populate REP-012 with the exact current physical Core artifact set as `ALLOCATED` records bounded to Core partition/path ownership. Allocation does not mean canonical promotion, semantic review completion, relationship completion, certification, or Phase-1 closure.

The legacy `CORE-000_PLATFORM_IDENTITY.md` record must explicitly preserve `Canonical: No / Legacy / Superseded` provenance and must not be interpreted as a second active CORE-000 authority.

## Authorized material change set

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
   - increment version;
   - add an exact bounded Core allocation population section covering all 18 current top-level Core files;
   - preserve `Phase 1 Population In Progress` and repository-wide incompleteness.
2. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
   - record exact scope, allocation evidence, non-promotion boundaries and verification.
3. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
   - preserve V blocker and bind its corrective handoff to W; V remains blocked until W is verified and a fresh certification review occurs.
4. this Matrix
   - bind candidate and verification evidence.

Candidate after this pre-write Matrix must be exactly one commit and exactly these four paths. Unexpected path expansion = `0`.

## Explicitly forbidden

- no Core source mutation;
- no `Core/_FOLDER_STATUS.md` mutation in W;
- no REP-013 completion-rule weakening;
- no REP-014 relationship mutation;
- no REP-016 Priority-7 closure;
- no Core certification or `CLOSED_FOR_PHASE_1` promotion;
- no canonical promotion of legacy CORE-000 identity;
- no claim that allocation equals review or semantic validity;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Verification contract

`PRE-WRITE MATRIX → EXACT CORE INVENTORY RECHECK → ONE-COMMIT/FOUR-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY W CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

After W closure, rediscover live main and reopen a fresh Explicit Core Certification Review. Certification is not automatic.

## Learning target

`ALLOCATION COMPLETENESS IS A CLOSURE PREREQUISITE, NOT A SUBSTITUTE FOR REVIEW, RELATIONSHIP VALIDATION OR CERTIFICATION.`
