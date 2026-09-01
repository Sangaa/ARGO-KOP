# MUTATION MATRIX — P7 CORE ALLOCATION RECONCILIATION W

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-CORE-ALLOCATION-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX REFINED / VALIDATION-FIRST / LEASE ACTIVE`
Entry HEAD: `911f51d3a0881728125b36bfc09d266214730154`
Initial Matrix HEAD: `f2543f809e1058c576c59de372354bf17ee2cdb1`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-014 / REP-015 / REP-016`

## Why W exists

Explicit Core Certification Review V established a current closure blocker: REP-013 requires every known file to have an allocation record before a folder can become `CLOSED_FOR_PHASE_1`, while current REP-012 v1.0.10 contains only the initial control-plane allocation set plus DIAG-001 and no Core artifact allocation records.

This transaction returns to the missing evidence gate. It does not weaken REP-013 and does not certify Core.

## Direct current evidence

- exact current Core enumeration remains 18 top-level files;
- `Core/Core.md` independently lists the other 17 members and intentionally self-excludes;
- `CORE-000_PLATFORM_IDENTITY.md` remains physical provenance / legacy / noncanonical;
- Core readiness remains PASS but certification is blocked;
- REP-012 remains `Phase 1 Population In Progress`;
- REP-013 Completion Rule requires an allocation record for every known file before folder closure.

## Pre-write refinement finding

Before any material allocation write, direct inspection of the full current REP-012 showed a long historical/control-plane evidence body whose preservation is itself material. A proposed full-file replacement surface would create unnecessary content-preservation risk and could repeat the historical abbreviated-replacement class already documented elsewhere in the control plane.

No such replacement blob is authorized or published.

Under the repository simplicity/reviewability principle, W therefore narrows the write surface: the Core allocation population will be recorded in a bounded REP-012 allocation addendum rather than rewriting the long canonical REP-012 body merely to append one partition population. The addendum is allocation evidence subordinate to and governed by REP-012; it does not replace REP-012 or claim repository-wide allocation completeness.

A fresh Explicit Core Certification Review must decide whether the verified bounded addendum satisfies the REP-013 per-known-file allocation prerequisite. W itself does not pre-decide certification.

## Allocation semantics

W may record the exact current physical Core artifact set as `ALLOCATED` records bounded to Core partition/path ownership. Allocation does not mean canonical promotion, semantic review completion, relationship completion, certification, or Phase-1 closure.

The legacy `CORE-000_PLATFORM_IDENTITY.md` record must explicitly preserve `Canonical: No / Legacy / Superseded` provenance and must not be interpreted as a second active CORE-000 authority.

## Authorized material change set — exactly 4 paths

1. `Repository/REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md`
   - bounded REP-012 allocation evidence for all 18 current top-level Core files;
   - explicitly subordinate to REP-012 and non-replacing;
   - preserve repository-wide `Phase 1 Population In Progress` boundary.
2. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
   - record exact scope, allocation evidence, content-preservation decision, non-promotion boundaries and verification.
3. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
   - preserve V blocker and bind its corrective handoff to W; V remains blocked until W is verified and a fresh certification review occurs.
4. this Matrix
   - bind candidate and verification evidence.

Candidate after this refined pre-write Matrix must be exactly one commit and exactly these four paths. Unexpected path expansion = `0`.

## Explicitly forbidden

- no mutation of canonical `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` in W;
- no Core source mutation;
- no `Core/_FOLDER_STATUS.md` mutation in W;
- no REP-013 completion-rule weakening;
- no REP-014 relationship mutation;
- no REP-016 Priority-7 closure;
- no Core certification or `CLOSED_FOR_PHASE_1` promotion;
- no canonical promotion of legacy CORE-000 identity;
- no claim that allocation equals review or semantic validity;
- no claim that W itself proves the addendum is sufficient for certification;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Verification contract

`REFINED PRE-WRITE MATRIX → EXACT CORE INVENTORY RECHECK → ONE-COMMIT/FOUR-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY W CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

After W closure, rediscover live main and reopen a fresh Explicit Core Certification Review. Certification is not automatic.

## Learning retained

`ALLOCATION COMPLETENESS IS A CLOSURE PREREQUISITE, NOT A SUBSTITUTE FOR REVIEW, RELATIONSHIP VALIDATION OR CERTIFICATION.`

`DO NOT REWRITE A LARGE CONTROL-PLANE ARTIFACT MERELY TO APPEND BOUNDED EVIDENCE WHEN A GOVERNED NON-REPLACING ADDENDUM CAN PRESERVE THE SAME TRACEABILITY WITH LOWER CONTENT-PRESERVATION RISK.`
