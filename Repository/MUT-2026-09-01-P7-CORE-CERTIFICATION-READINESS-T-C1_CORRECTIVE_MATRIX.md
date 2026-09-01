# MUTATION MATRIX — P7 CORE CERTIFICATION READINESS T-C1 — STATE-TRANSITION CORRECTION

Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T`
Work Lease: `HERMUZ-P7-T-C1-CORE-READINESS-20260901`
Priority: `7 — Core`
State: `FAILED MATERIAL CANDIDATE PRESERVED / INTEGRITY DEFECT REPAIRED / HANDOFF TO T-C2`
Entry HEAD: `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d`
Pre-write Matrix HEAD: `110eab997d9027f575cb306d9175565834098e82`
Failed T-C1 candidate: `bf7e640772310b2af9be939d56535f8cf20cc0c1`
Corrective successor: `MUT-2026-09-01-P7-CORE-CERTIFICATION-READINESS-T-C2`
T-C2 pre-write Matrix HEAD: `1477828c46ca65d1e32779ecb43d2ead4da50716`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-014 / REP-016 / ARC-006 / ARC-011`

## Why T-C1 existed

Parent T candidate `8d01a3cd19e0f7d630bf6c60fc62b05460b82b1d` structurally satisfied its one-commit/five-path authorization and passed Full-Stack, Real Mutation Matrix and M2, but exact-head Runtime verification failed.

Exact T workflow evidence:

- Full-Stack Repository Audit `33534072084` — `SUCCESS`;
- Real Mutation Matrix Regression `33534071888` — `SUCCESS`;
- M2 Multi-Channel Proposal Training `33534072032` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests `33534072160` — `FAILURE`.

Runtime jobs:

- integrity-tests — `FAILURE`;
- prototype-tests — `SUCCESS`;
- integration-tests — `FAILURE`.

The primary defect was a premature state transition: T removed `CROSS-LAYER VALIDATION OPEN` before a separate Explicit Core Certification Review closed or redirected the gate.

## T-C1 corrective semantic decision

T-C1 preserved both truths simultaneously:

- `CROSS-LAYER VALIDATION OPEN` remains explicit until the separate certification review closes or redirects it;
- `CERTIFICATION REVIEW READY` remains explicit because bounded evidence is sufficient to open that review.

Target status semantics were correctly restored as:

`INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN / CERTIFICATION REVIEW READY`.

## T-C1 exact-head result

T-C1 candidate `bf7e640772310b2af9be939d56535f8cf20cc0c1` did not fully pass CI and remains failed evidence.

- Full-Stack Repository Audit `33535169972` — `SUCCESS`;
- Real Mutation Matrix Regression `33535170174` — `SUCCESS`;
- M2 Multi-Channel Proposal Training `33535170346` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests `33535170040` — `FAILURE`.

Runtime jobs:

- integrity-tests — `SUCCESS`;
- prototype-tests — `SUCCESS`;
- integration-tests — `FAILURE`.

This split is material evidence: T-C1 repaired the original Integrity/open-marker defect. The remaining failure is a distinct Integration contract defect.

## T-C2 handoff finding

Direct inspection of `Quality/Integration/test_core_p7_status_sync.py` shows its remaining-boundary test still encodes two pre-readiness statements as unconditional current requirements:

- `continued dependency and consumer validation for remaining material Core authority relationships`;
- `REP-014 relationship-registry reconciliation`.

Those statements were valid before Transaction T's direct bounded Core-member sweep. They are stale as permanent requirements now because T established no additional material external coupling requiring registration before explicit certification review, Transaction R intentionally preserves one validated-not-registered seam, and REP-014 states its list is not a complete graph.

The valid parts of that integration boundary remain authoritative and must be preserved by T-C2:

- `CROSS-LAYER VALIDATION OPEN`;
- explicit final Core certification decision;
- Priority 7 OPEN;
- no Phase-1 / repository-wide graph / Connected Baseline promotion.

Classification:

`T-C1 MATERIAL CANDIDATE CI FAILURE / PRIMARY STATE-MARKER REPAIR VERIFIED BY INTEGRITY SUCCESS / REMAINING STALE INTEGRATION STATE CONTRACT HANDOFF TO T-C2`.

## Original T-C1 material boundary

T-C1 changed exactly six authorized paths and did not modify the pre-existing failure-detecting tests. Its atomicity evidence remains preserved.

## Non-authority preserved

- no canonical Core source mutation beyond the status/evidence surface already authorized in T-C1;
- no REP-014 or REP-020 mutation;
- no REL-073 or other registry mutation;
- no Core certification;
- no Priority-7 closure;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS claim.

## Learning retained

`READINESS MAY OPEN THE NEXT REVIEW WITHOUT CLOSING THE CURRENT VALIDATION GATE.`

`A STATE LABEL MUST NOT REMOVE AN OPEN-GATE MARKER UNTIL THE GOVERNED CLOSURE DECISION HAS ACTUALLY OCCURRED.`

`A FAILED CORRECTIVE CANDIDATE CAN STILL PROVE THAT ONE FAILURE CLASS WAS REPAIRED WHEN THE EXACT-HEAD JOB SPLIT CHANGES FROM FAILURE TO SUCCESS.`

No new Governance rule is created; T-C2 continues under existing failure/evidence discipline.
