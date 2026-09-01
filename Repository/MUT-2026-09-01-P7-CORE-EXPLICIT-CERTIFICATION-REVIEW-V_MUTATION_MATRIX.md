# MUTATION MATRIX — PRIORITY 7 CORE EXPLICIT CERTIFICATION REVIEW V

Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-REVIEW-V`
Work Lease: `HERMUZ-P7-V-CORE-EXPLICIT-CERTIFICATION-REVIEW-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX / VALIDATION-FIRST / LEASE ACTIVE`
Entry HEAD: `b10e9e5733fe1586a7f15f1bb2f7f54df8df31c5`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / REP-011 / REP-012 / REP-013 / REP-014 / REP-016 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / ARC-006 / ARC-011`

## Question

May the current Core partition be explicitly certified and closed for Phase 1 under current live evidence, or does a material control/evidence gap require routing back to an earlier reconciliation gate?

## Current evidence entering review

- Certification-readiness chain T/T-C1/T-C2/T-C3 is closed Resume-Safe.
- Closure HEAD `b10e9e5733fe1586a7f15f1bb2f7f54df8df31c5` passed all four required workflows.
- Runtime closure jobs integrity/prototype/integration all succeeded.
- Core status remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY / NOT CERTIFIED`.
- Direct compare from T-C2 semantic candidate `f63c7b3c1838ef7643d7f2d842e0d699304ac9d0` to current entry HEAD shows no `Core/` path changes; intervening changes are CI/Quality/Repository evidence only.
- Exact live `Core/` enumeration remains 18 top-level files; `Core/Core.md` still lists the corresponding 17 self-excluding members.

## Material blocker candidate discovered during explicit review

Current `REP-013` Completion Rule requires, before a folder may become `CLOSED_FOR_PHASE_1`, that every known file have an allocation record.

Current `REP-012` v1.0.10 is still `Phase 1 Population In Progress`; its directly readable current content and direct current Git blob show allocation rows only for the initial control-plane set plus DIAG-001, and contain no Core artifact allocation records such as `CORE-003` or `Core/` paths.

This candidate blocker must be preserved as a certification-review finding rather than bypassed by readiness evidence.

## Review decision rule

If current evidence confirms missing Core allocation records under REP-012 while REP-013 retains the explicit per-known-file allocation prerequisite, V must close as:

`CERTIFICATION REVIEW = BLOCKED / CORE NOT CERTIFIED / RETURN TO REP-012 CORE ALLOCATION RECONCILIATION`.

If contrary current evidence is discovered before material commit, V must record that evidence and recompute disposition rather than forcing the expected blocker.

## Authorized material change set — exactly 2 paths

1. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
   - record current certification review evidence, freshness proof, blocker classification and bounded disposition.
2. this Matrix
   - bind the review candidate and verification evidence.

## Explicitly forbidden

- no mutation of `Core/_FOLDER_STATUS.md` in V;
- no Core certification or `CLOSED_FOR_PHASE_1` promotion;
- no mutation of REP-012, REP-013, REP-014, REP-016 or REP-020 in V;
- no relationship creation/registration;
- no Phase-1, Connected Baseline, repository-wide graph or Global PASS claim;
- no weakening of REP-013 Completion Rule to make certification pass;
- no treating readiness PASS as certification authority.

## Atomicity and verification contract

After this pre-write Matrix commit, V material candidate must be exactly one commit and exactly the two authorized paths. Unexpected path expansion = `0`.

Then:

`LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK JOB REVIEW → RUNTIME JOB REVIEW → DOCUMENTATION-ONLY CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

## Learning target

`READINESS IS A LICENSE TO REVIEW, NOT A LICENSE TO CERTIFY.`

`AN EXPLICIT CLOSURE REVIEW MUST APPLY THE CURRENT CLOSURE CONTRACT, INCLUDING CONTROL-REGISTRY PRECONDITIONS THAT EARLIER BOUNDED SWEEPS DID NOT NEED TO SATISFY.`
