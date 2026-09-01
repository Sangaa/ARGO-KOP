# AMENDMENT MATRIX — P7 CORE ALLOCATION RECONCILIATION W-B

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-B`
Parent Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Prior Amendment: `W-A`
Work Lease: `HERMUZ-P7-W-B-CORE-ALLOCATION-PRESERVATION-20260901`
Priority: `7 — Core`
State: `PRE-WRITE SUPERSEDING AMENDMENT / LEASE ACTIVE`
Entry HEAD: `2a82218d8faf47ceea81d9e72a3edb00f0897007`

## Why W-B exists

W-A correctly detected that a direct REP-012 version mutation would require REP-020 manifest synchronization and that durable Core-allocation regression evidence is valuable.

A second pre-material inspection then established a more fundamental constraint: current canonical REP-012 contains a long historical/control-plane evidence body. Replacing that entire file merely to append one bounded partition population creates avoidable content-preservation risk. No REP-012 replacement material has been published.

The current W Matrix was refined before material mutation to use a governed non-replacing REP-012 Core allocation addendum. Because canonical REP-012 version/status/identity will no longer change, W-A's REP-020 synchronization trigger is not activated. W-B reconciles the two pre-write plans explicitly instead of silently ignoring W-A.

## Preserved W-A learning

W-B retains W-A's durable-verification requirement: a focused Integrity regression must bind the exact physical Core inventory, self-excluding `Core.md` index semantics, the bounded allocation addendum, and legacy/noncanonical CORE-000 identity treatment.

## Superseding authorized material change set — exactly 7 paths

1. `Repository/REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md`
   - bounded 18/18 Core allocation records subordinate to REP-012; non-replacing.
2. `Quality/Integrity/test_core_allocation_registry_coverage.py`
   - exact physical inventory ↔ Core index ↔ allocation-addendum coverage regression;
   - preserve legacy noncanonical identity boundary and anti-certification assertions.
3. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
   - transaction evidence and verification.
4. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
   - preserve blocked V and bind W handoff; no automatic certification.
5. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W_MUTATION_MATRIX.md`
   - bind W-B as controlling amendment.
6. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A_AMENDMENT_MATRIX.md`
   - preserve W-A finding and mark its direct-REP-012/manifest path superseded before material mutation.
7. this W-B Amendment Matrix
   - bind candidate and verification.

Canonical `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` and REP-020 are explicitly KEEP in W-B because their version/status/identity do not change.

## Atomicity contract

After this W-B pre-write commit, material candidate must be exactly one commit and exactly the seven paths above. Unexpected path expansion = `0`.

## Explicitly forbidden

- no canonical REP-012 body mutation;
- no REP-020 mutation absent a listed control-plane identity/version/status change;
- no Core source or `_FOLDER_STATUS.md` mutation;
- no REP-013 rule weakening;
- no REP-014 relationship mutation;
- no REP-016 closure mutation;
- no Core certification / `CLOSED_FOR_PHASE_1` / Priority-7 closure;
- no canonical promotion of legacy CORE-000 identity;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Verification contract

`EXACT CORE INVENTORY RECHECK → ONE-COMMIT/SEVEN-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → RUNTIME JOB REVIEW → FULL-STACK SHA/MATRIX/AUDIT REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY W/W-A/W-B CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

After closure, fresh Explicit Core Certification Review is mandatory; the review decides whether the addendum satisfies REP-013 allocation prerequisite.

## Learning

`A CORRECT PRE-WRITE AMENDMENT MAY ITSELF BE SUPERSEDED BEFORE MATERIAL MUTATION WHEN NEW EVIDENCE SHOWS A LOWER-RISK EQUIVALENT WRITE SURFACE.`

`PRESERVE THE VALID PART OF THE EARLIER AMENDMENT — HERE, DURABLE REGRESSION — WHILE REMOVING THE NOW-UNNECESSARY MANIFEST MUTATION CAUSED ONLY BY A REP-012 VERSION CHANGE THAT WILL NOT OCCUR.`
