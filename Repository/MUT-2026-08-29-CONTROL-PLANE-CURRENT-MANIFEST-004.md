# Control-Plane Current Manifest Repair — Mutation Matrix

Transaction ID: `MUT-2026-08-29-CONTROL-PLANE-CURRENT-MANIFEST-004`  
Parent: `MUT-2026-08-29-CONTROL-PLANE-CONVERGENCE-001`  
Triggering PR: `#88`  
Triggering candidate HEAD: `e769ca976ea77e5bcd3a306c44d31a298a075693`  
Triggering workflow: `ARGO Runtime Prototype and Integration Tests / run 33234422210`  
Status: `OPEN / FAILURE CLASSIFIED / PRE-MUTATION MATRIX`

## Failure evidence

The PR integration suite produced:

- `461 passed`;
- `11 subtests passed`;
- `2 failed`.

Failure 1:

`REP-016 Version='1.4.0'; P339 manifest='1.3.0'`.

Failure 2:

The Ring-0 synchronization test expected the semantically correct statement that REP-016 coordinates `REP-011 through REP-015` plus provisional `REP-020`. The current transaction had changed the queue wording to `REP-011 through REP-016`, incorrectly making the work queue describe itself as one of the artifacts it coordinates.

## Root cause

Two distinct causes:

1. **Current-boundary manifest lifecycle defect:** `Quality/Integration/control_plane_reconciliation_gate.py` still points to historical snapshot `REP-020_SESSION_DELTA_2026-08-17_P339.md`. P339 explicitly states that it must be regenerated or replaced when listed identities/statuses materially change. The gate description says it evaluates the current boundary, but its manifest pointer and `Priority 1 is still OPEN` assertion are fossilized to P339.
2. **Local semantic wording regression:** REP-016 is a member of the control plane, but it coordinates REP-011..015 plus the provisional REP-020 evidence surface; it must not claim to coordinate itself.

## Learning

`A regression gate may correctly fail while also exposing that part of its own evidence fixture has become historical.`

Do not satisfy such a gate by downgrading current artifact versions or restoring obsolete semantic state. First separate:

`VALID TEST INVARIANT` from `STALE TEST FIXTURE / MANIFEST`.

The stable solution is a current manifest surface whose path does not change every time a new snapshot is produced. Historical manifests remain immutable evidence.

## Decisions

- Preserve P339 unchanged as historical evidence.
- Add `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` as the stable current evidence surface consumed by the executable gate. It carries no independent canonical authority and no `Document ID:` identity claim.
- Update the gate to consume that stable current surface and validate explicit current integrity/closure boundaries rather than the historical P339 sentence.
- Restore REP-016's semantically correct `REP-011 through REP-015` coordination wording while retaining REP-011..016 as the overall control-plane membership in REP-001/REP-002/GOV-015.
- Do not weaken the Ring-0 test.

## Mutation matrix

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| CM-01 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | ADD | stable current manifest with exact current versions/statuses and bounded closure state | N | N |
| CM-02 | `Quality/Integration/control_plane_reconciliation_gate.py` | UPDATE | consume stable current manifest; remove fossilized P339-only closure assertion | N | N |
| CM-03 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE | restore semantically correct REP-011..015 + REP-020 coordination statement | N | N |
| CM-04 | `Quality/Integration/test_control_plane_ring0_synchronization.py` | KEEP | preserve valid invariant; no weakening | N/A | N/A |
| CM-05 | `Repository/REP-020_SESSION_DELTA_2026-08-17_P339.md` | KEEP | preserve historical manifest unchanged | N/A | N/A |
| CM-06 | PR exact-head integration suite | VERIFY | both original failures disappear without suppressing unrelated failures | N | N |

## Current version evidence for the new manifest

- REP-011 `1.1.2` — `Active / Integrity Hold`
- REP-012 `1.0.9` — `Active Control / Integrity Hold / Phase 1 Population In Progress`
- REP-013 `1.1.2` — `Active / Phase 1 Population In Progress`
- REP-014 `1.2.6` — `Active / Relationship Enumeration In Progress`
- REP-015 `1.0.7` — `Active / Phase 1 Open / Integrity Hold`
- REP-016 `1.4.0` — `Active / Phase 1 Open / Integrity Hold`
- REP-020 `0.2.3` — `Provisional / Phase-1 Seed / Not Authority`

## Non-claims

This repair does not close Phase 1, the duplicate-ID audit, broader graph validation, external authenticity, cognitive benefit, or Global PASS.
