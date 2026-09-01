# AMENDMENT MATRIX — P7 CORE ALLOCATION RECONCILIATION W-B

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-B`
Parent Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Prior Amendment: `W-A`
Work Lease: `HERMUZ-P7-W-B-CORE-ALLOCATION-PRESERVATION-20260901`
Priority: `7 — Core`
State: `MATERIAL CANDIDATE PREPARED / CONTROLLING AMENDMENT / CI PENDING`
Entry HEAD: `2a82218d8faf47ceea81d9e72a3edb00f0897007`
Pre-write W-B HEAD: `f0f564b68cd6e0f957327839db40316ea73c22cf`

## Controlling decision

W-A's manifest rule remains valid conditionally: direct canonical REP-012 version mutation would require REP-020 synchronization. W-B removes that condition before material mutation by using a governed non-replacing Core allocation addendum subordinate to REP-012.

Canonical REP-012 and REP-020 are KEEP. W-A's focused regression requirement is retained.

## Authorized material change set — exactly 7 paths

1. `Repository/REP-012_CORE_ALLOCATION_ADDENDUM_2026-09-01_W.md`
2. `Quality/Integrity/test_core_allocation_registry_coverage.py`
3. `Repository/P7_CORE_ALLOCATION_RECONCILIATION_2026-09-01_W.md`
4. `Repository/P7_CORE_EXPLICIT_CERTIFICATION_REVIEW_2026-09-01_V.md`
5. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W_MUTATION_MATRIX.md`
6. `Repository/MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A_AMENDMENT_MATRIX.md`
7. this W-B Amendment Matrix

Candidate must be exactly one commit after `f0f564b68cd6e0f957327839db40316ea73c22cf`; unexpected path expansion = `0`.

## Evidence boundary

The addendum records 18/18 current top-level Core paths as allocation evidence. The regression binds physical inventory, self-excluding Core index, allocation coverage and legacy noncanonical identity. None of these establish certification.

## Forbidden

No canonical REP-012/REP-020 mutation; no Core source/status mutation; no REP-013 weakening; no relationship mutation; no certification; no Priority-7/Phase-1/Connected-Baseline/Global PASS promotion.

## Verification

`ONE-COMMIT/SEVEN-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD FOUR REQUIRED WORKFLOWS → JOB-LEVEL REVIEW → DOCUMENTATION-ONLY CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

Fresh Explicit Core Certification Review is mandatory after verified closure.

## Learning

`A LOWER-RISK EQUIVALENT WRITE SURFACE MAY SUPERSEDE AN EARLIER PRE-WRITE PLAN, BUT THE SUPERSESSION ITSELF MUST BE EXPLICIT AND THE VALID LEARNING FROM THE EARLIER PLAN MUST BE RETAINED.`
