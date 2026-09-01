# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C2 — STALE INTEGRATION CONTRACT CORRECTION

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2`
Parent Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1`
Root Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Work Lease: `HERMUZ-P7-T-C2-CORE-READINESS-INTEGRATION-20260901`
Priority: `7 — Core`
State: `CORRECTIVE MATERIAL CANDIDATE PREPARED / CI PENDING / LEASE ACTIVE`
Entry HEAD: `bf7e640772310b2af9be939d56535f8cf20cc0c1`
Pre-write Matrix HEAD: `1477828c46ca65d1e32779ecb43d2ead4da50716`
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

`STALE INTEGRATION STATE CONTRACT / CURRENT READINESS TRANSITION EVIDENCE SUPERSEDES OLD REMAINING-WORK LITERALS / TEST UPDATED WITHOUT WEAKENING OPEN-GATE OR ANTI-PROMOTION GUARDS`.

## Authorized corrective material change set — exactly 5 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| C2-01 | `Quality/Integration/test_core_p7_status_sync.py` | replace stale pre-readiness remaining-work literals with current readiness/open-gate assertions; retain closed-control-plane and anti-promotion checks | Y | PENDING CI |
| C2-02 | `Repository/P7_CORE_CERTIFICATION_READINESS_2026-09-01_T.md` | preserve T/T-C1 failures and bind T-C2 diagnosis/candidate | Y | PENDING CI |
| C2-03 | `Repository/REP-016_PRIORITY7_CERTIFICATION_READINESS_ADDENDUM_2026-09-01_T.md` | bind operational readiness to T-C2 verification while Priority 7 and cross-layer gate remain open | Y | PENDING CI |
| C2-04 | `Repository/MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1_CORRECTIVE_MATRIX.md` | preserve failed T-C1 exact-head evidence and handoff | Y | PENDING CI |
| C2-05 | this Matrix | bind T-C2 candidate in same material change set | Y | PENDING CI |

Candidate must be exactly one commit after pre-write Matrix HEAD `1477828c46ca65d1e32779ecb43d2ead4da50716` and exactly these five paths. Unexpected path expansion = `0`.

## Updated test contract

The revised Integration test preserves:

- all closed Priority-7 control-plane reconciliation assertions;
- `CROSS-LAYER VALIDATION OPEN`;
- `CERTIFICATION REVIEW READY`;
- `VALIDATED-NOT-REGISTERED`;
- REP-014 `not a complete graph` boundary;
- explicit final Core certification decision;
- Priority 7 OPEN;
- no Phase-1 / repository-wide graph / Connected Baseline promotion.

It additionally requires the two superseded pre-readiness remaining-work literals to be absent, preventing old queue language from becoming a permanent certification blocker.

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

## Verification contract

`ONE-COMMIT/FIVE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK SHA/MATRIX/AUDIT REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT → DOCUMENTATION-ONLY T/T-C1/T-C2 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

## Learning retained

`A REGRESSION TEST MAY PRESERVE A VALID SAFETY BOUNDARY WHILE STILL CONTAINING A STALE DESCRIPTION OF THE WORK REQUIRED TO REACH THAT BOUNDARY.`

`TEST EVOLUTION MUST FOLLOW NEW VERIFIED STATE EVIDENCE; IT MUST NOT BE USED TO ERASE A VALID FAILURE.`

No new Governance rule is warranted from T-C2 alone.
