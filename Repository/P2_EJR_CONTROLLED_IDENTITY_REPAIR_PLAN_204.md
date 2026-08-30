# P2 EJR CONTROLLED IDENTITY-REPAIR PLAN — 204

Status: `PLAN VERIFIED / EXECUTION NOT AUTHORIZED`
Baseline: `main@89c46c600550fb1d70054c6a2089c0507fb51681`
Source evidence: Leases 202–203, REP-012 v1.0.10, Git path creation history.

## Governing rule

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE PROVES THAT FIRST ALLOCATION WAS INVALID, UNAUTHORIZED, OR NEVER CONSTITUTED AN IDENTITY ALLOCATION.`

Rationale:
- REP-012 treats stable Document ID plus canonical path history as inode-like identity and requires identity/history verification before mutation.
- A later consumer can recover a referent without retroactively transferring ownership of an already-used identifier.
- No evidence reviewed in Lease 203 or this plan invalidates the first allocations in the five groups.
- Therefore historical continuity is preserved by retaining the earliest valid allocation and repairing later reuse events.

This is a bounded repair rule for the five proven collision groups; it is not a repository-wide migration policy.

## Dispositions

### EJR-211
RETAIN:
- `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md`
- creation: `eb9fd770e0b4c52f86e813341a92da2fc6063b67` / 2026-08-14.
- protected provenance: `Memory/MEM-009_MEMORY_EVOLUTION.md`; `Repository/REP-020_SESSION_DELTA_2026-08-14_P29.md`.

DISPLACE IN FUTURE EXECUTION:
- `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`
- creation: `e54fb22f9f582b4e3bf164aa05e4a3a97a0f8950` / 2026-08-17.
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

### EJR-214
RETAIN:
- `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`
- current governed provenance includes `Memory/MEM-009_MEMORY_EVOLUTION.md` and the P31 semantic-memory chain established by Lease 203.

DISPLACE IN FUTURE EXECUTION:
- `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
- creation: `7207214ace7a44dc80bbbc0b0a34d771858988c5` / 2026-08-17.
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

### EJR-219
RETAIN:
- `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md`
- protected provenance: `Memory/MEM-009_MEMORY_EVOLUTION.md`.

DISPLACE IN FUTURE EXECUTION:
- `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md`
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

### EJR-301
RETAIN:
- `Memory/Engineering_Journal/EJR-301_2026-08-22_HERMUZ_P6_CI_EXECUTION_RECHECK.md`
- creation: `079d7042583e01e8c831bf0f9592bbf6cf3fd648` / 2026-08-22.

DISPLACE IN FUTURE EXECUTION:
- `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`
- creation: `cc90f7822460ccbfb60e3e083c3189b04a3ed4eb` / 2026-08-24.
- current exact-path consumer that MUST move with identity rewrite: `Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md`.
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

### EJR-302
RETAIN:
- `Memory/Engineering_Journal/EJR-302_2026-08-22_HERMUZ_CURRENT_HEAD_STATUS_RECHECK.md`
- creation: `9e8a73a8bd52b30f632569348b513e7ec2f2f77e` / 2026-08-22.

DISPLACE A IN FUTURE EXECUTION:
- `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`
- creation: `3b6ecfb236bc1baa2592fd083b0eb6fcb6156add` / 2026-08-24.
- exact-path consumer that MUST be rewritten consistently: `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`.
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

DISPLACE B IN FUTURE EXECUTION:
- `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`
- creation: `eb1c200740c6c5fac4380c5d42ced6c0584f67d9` / 2026-08-25.
- semantic provenance consumer that MUST be rewritten consistently if promoted/retained: `GOV-013B` learning provenance `EJR-302 / P221`.
- replacement ID: `UNALLOCATED / LEASE-193 VACANCY PROOF REQUIRED`.

## Planned execution units
Identity repair MUST NOT be executed as one bulk rename. Use one material displaced record per governed lease:

`PROVE REPLACEMENT VACANCY → PREWRITE LEASE+MATRIX → READ FULL SOURCE → ENUMERATE CONSUMERS → RENAME/IDENTITY REWRITE + REQUIRED CONSUMER REWRITES IN ONE FUNCTIONAL CHANGE SET → READ-BACK → INTERNAL-ID + FULL STACK VERIFICATION → SYNC REGISTRIES/MANIFESTS IF TRIGGERED → CLOSE/RESUME-SAFE`.

EJR-302 requires two independent replacement allocations and two separate repair units unless a later evidence review proves a safer atomic grouping.

## Consumer preservation rule

`IDENTITY REPAIR IS INCOMPLETE IF THE RECORD MOVES BUT A GOVERNED CONSUMER STILL NAMES THE OLD ID OR OLD PATH.`

Exact-path and semantic-ID consumers are different surfaces; both must be checked. Analytical/self-referential evidence does not automatically become an operational rewrite obligation.

## Replacement allocation rule
No concrete replacement number is assigned by this plan. Every candidate MUST pass `Quality/Integration/ejr_allocation_vacancy_gate.py` with complete locally reachable history and decision `VACANT`. `OCCUPIED` or `HISTORY_INCOMPLETE` blocks allocation.

## Content preservation
All six displaced records are legitimate engineering evidence. Future repair is identity/path correction only; semantic content, chronology, original event dates, and historical meaning must be preserved except for the minimum identity/provenance metadata needed to make the new identity self-consistent.

## Synchronization obligations
Before each execution lease, determine whether the moved record is represented by:
- REP-001 / REP-002 indexes/maps;
- REP-011 review evidence;
- REP-012 allocation registry;
- REP-013 inventory;
- REP-014 relationships/consumers;
- REP-016 queue;
- REP-020 current control-plane manifest;
- domain memory/governance consumers.

Only consumers materially affected by that repair enter the same or an explicitly governed corrective successor change set. No registry is changed merely for cosmetic synchronization.

## Boundaries
This plan performs no EJR mutation, rename, delete, reassignment, allocation, consumer rewrite, suppression, or canonical promotion. Priority 2 historical/provenance identity remains OPEN. Active indexed canonical uniqueness remains previously CLOSED/PASS. Phase 1 and Global Connected Baseline remain OPEN. Global BOOTED / INTEGRITY PASS is NOT CLAIMED.

## Next legal action
Select exactly one displaced record, discover a replacement candidate, prove it `VACANT` through Lease-193 gate evidence, enumerate its exact consumers, then open a separate execution lease. The first execution candidate should be chosen by lowest rewrite-risk and strongest consumer visibility, not merely lowest EJR number.
