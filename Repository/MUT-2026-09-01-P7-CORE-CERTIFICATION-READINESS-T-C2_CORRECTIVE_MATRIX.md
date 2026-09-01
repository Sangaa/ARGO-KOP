# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C2 — STALE INTEGRATION CONTRACT CORRECTION

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2`
Parent Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1`
Root Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Work Lease: `HERMUZ-P7-T-C2-CORE-READINESS-INTEGRATION-20260901`
Priority: `7 — Core`
State: `PRE-WRITE MATRIX / LEASE ACTIVE / NO CORRECTIVE MATERIAL WRITE YET`
Entry HEAD: `bf7e640772310b2af9be939d56535f8cf20cc0c1`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C2 exists

T-C1 correctly restored `CROSS-LAYER VALIDATION OPEN` while retaining `CERTIFICATION REVIEW READY`.

Exact-head T-C1 verification on `bf7e640772310b2af9be939d56535f8cf20cc0c1` produced:

- Full-Stack Repository Audit `33535169972` — `SUCCESS`;
- Real Mutation Matrix Regression `33535170174` — `SUCCESS`;
- M2 Multi-Channel Proposal Training `33535170346` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests `33535170040` — `FAILURE`.

Runtime job split:

- `integrity-tests` — `SUCCESS`;
- `prototype-tests` — `SUCCESS`;
- `integration-tests` — `FAILURE`.

This proves the T-C1 open-gate correction repaired the prior Integrity failure. The remaining defect is isolated to the Integration suite.

## Direct integration-contract finding

`Quality/Integration/test_core_p7_status_sync.py` still encodes two pre-readiness statements as mandatory remaining work:

- `continued dependency and consumer validation for remaining material Core authority relationships`;
- `REP-014 relationship-registry reconciliation`.

Those assertions were valid before Transaction T's direct bounded Core-member sweep and before the current readiness classification. They are no longer valid as unconditional current-state requirements because:

1. Transaction T directly re-read the remaining canonical Core members and established no additional material external coupling that must be registered before explicit certification review;
2. Transaction R's `RUN-002 → CORE-003 = REFERENCES` seam is intentionally `VALIDATED-NOT-REGISTERED`;
3. REP-014 explicitly states that its relationship list is not a complete graph, so visual registry completeness is not itself a closure criterion;
4. `CROSS-LAYER VALIDATION OPEN` remains correctly preserved until the separate Explicit Core Certification Review closes or redirects that gate.

Therefore the integration test is stale in **what it names as mandatory remaining work**, not in its requirement that Priority 7 and certification remain open.

Classification:

`STALE INTEGRATION STATE CONTRACT / CURRENT READINESS TRANSITION EVIDENCE SUPERSEDES OLD REMAINING-WORK LITERALS / TEST MUST BE UPDATED WITHOUT WEAKENING OPEN-GATE OR ANTI-PROMOTION GUARDS`.

## Authorized corrective material change set — exactly 5 paths

1. `Quality/Integration/test_core_p7_status_sync.py`
   - preserve the closed-control-plane assertions;
   - replace only the two stale mandatory remaining-work literals with current bounded readiness/open-gate assertions;
   - continue requiring `CROSS-LAYER VALIDATION OPEN`, explicit final Core certification decision, Priority 7 OPEN, and no Phase-1/Connected-Baseline promotion;
   - require `VALIDATED-NOT-REGISTERED` / non-complete-graph boundary so registry completeness cannot be manufactured.
2. `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md`
   - preserve T and T-C1 failures and record T-C2 diagnosis/candidate state.
3. `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md`
   - bind current operational readiness to T-C2 verification while keeping Priority 7 and cross-layer gate open.
4. `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1_CORRECTIVE_MATRIX.md`
   - preserve failed T-C1 exact-head evidence and hand off to T-C2.
5. this T-C2 Matrix
   - bind the corrective candidate in the same material change set.

## Explicitly forbidden

- no mutation of `Core/_FOLDER_STATUS.md` in T-C2;
- no mutation of the T-focused Integrity test;
- no weakening/removal of `CROSS-LAYER VALIDATION OPEN`;
- no mutation of canonical Core sources;
- no REP-014 or REP-020 mutation;
- no REL-073 or other relationship registration;
- no forced registration of `RUN-002 → CORE-003`;
- no Core certification;
- no Priority-7 closure;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim;
- no rerun-only bypass of T-C1 failure.

## Atomicity contract

After this pre-write Matrix commit, the T-C2 material candidate must be exactly one commit and exactly the five authorized paths above. Unexpected path expansion = `0`.

## Verification contract

`ONE-COMMIT/FIVE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK SHA/MATRIX/AUDIT REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY T/T-C1/T-C2 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

## Learning retained

`A REGRESSION TEST MAY PRESERVE A VALID SAFETY BOUNDARY WHILE STILL CONTAINING A STALE DESCRIPTION OF THE WORK REQUIRED TO REACH THAT BOUNDARY.`

`TEST EVOLUTION MUST FOLLOW NEW VERIFIED STATE EVIDENCE; IT MUST NOT BE USED TO ERASE A VALID FAILURE.`

No new Governance rule is warranted from T-C2 alone.
