# Priority 7 — CORE-003 ↔ RUN-003 REL-071/072 Reconciliation — Transaction Q

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-REL071-072-Q`
Work Lease: `HERMUZ-P7-Q-REL071-072-20260901`
Entry HEAD: `194b23856a5f5b45c00bdb27a9c28c43288acf11`
Pre-write Matrix HEAD: `9ac7dc336f07673a5fb666915bb6673bcc3aaf01`

## Finding

Transaction P already validated, on exact-head CI, the bounded pair:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

with disposition `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.

Fresh post-P current-state recomputation found REP-014 v1.2.13 still ending at REL-070 and therefore not yet synchronized to that material validated seam. Q performs only that synchronization.

## Registry change

Register exactly:

`REL-071 | CORE-003 | RUN-003 | GOVERNS | CONSTITUTION-AUTHORITY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`

`REL-072 | RUN-003 | CORE-003 | REFERENCES | CRITICAL-RUNTIME-CONFIGURATION / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY`

REP-014 advances only from v1.2.13 to v1.2.14.

## Evidence boundary

Direct source semantics remain unchanged from P:

- CORE-003 defines the highest governing rules and requires repository components to comply within applicable scope;
- RUN-003 is canonical/critical Runtime configuration;
- RUN-003 controls runtime behavior without modifying repository architecture or authority;
- RUN-003 explicitly states Runtime configuration does not override CORE-003;
- RUN-003 directly lists CORE-003 and keeps repository authority above runtime assumptions.

Q does not infer dependency from authority ordering.

## Synchronized control surfaces

- current control-plane manifest binds REP-014 v1.2.14 and Q refresh while preserving Phase 1 OPEN, Global integrity HOLD and Global PASS NOT CLAIMED;
- Core status adds the validated/registered seam as an eighth bounded Priority-7 seam while preserving cross-layer validation open and Folder Certification pending;
- the focused P regression changes from validation-first absence assertions to exact unique REL-071/072 assertions while retaining all direct-source and forbidden stronger-semantics checks.

## Forbidden promotion

No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, reverse RUN-003→CORE-003 GOVERNS, executable reachability, Runtime certification, Core certification, Priority-7 closure, Phase-1 closure, Connected Baseline closure, repository-wide graph completion or Global PASS is claimed.

## Verification contract

Candidate must be exactly one commit after pre-write Matrix HEAD, touch exactly six authorized paths, preserve all prior REP-014 content except the bounded version/rows/evidence addition, and pass all four required exact-head workflows before closure.

Work Lease remains `OPEN` until candidate verification and closure-head verification complete.
