# MUT-2026-08-29 — CURRENT CONTROL-PLANE MANIFEST REBIND — 010

State: APPLIED / PENDING EXACT-HEAD CI
Lease: R71-20260829-CONTROL-MANIFEST-010
Baseline: acb2d0f434f55b86d816ca5fb266d903f4b370a9
Scope: control-plane evidence freshness only

## Problem

`Quality/Integration/control_plane_reconciliation_gate.py` still consumed the historical `REP-020_SESSION_DELTA_2026-08-17_P339.md` snapshot. A historical checkpoint is valid evidence for its original date but is unsafe as the permanent source for a current-state executable gate.

## Decision

Create `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` as a non-authoritative current evidence manifest and bind the executable gate to it. Preserve historical manifests unchanged.

## Mutation Matrix

| Target | Action | Expected Content | Applied | Verified |
|---|---|---|:---:|:---:|
| `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | CREATE | current REP-011..016 + REP-020 identity/status/version boundary and open/global-hold semantics | Y | N |
| `Quality/Integration/control_plane_reconciliation_gate.py` | UPDATE | consume current manifest, fail closed on missing/drift, preserve Phase-1/Open/Hold/non-PASS boundary | Y | N |
| `Quality/Integration/test_control_plane_current_manifest.py` | CREATE | regression forbidding historical-session manifest binding and verifying current repository match | Y | N |

## KEEP REQUIREMENT

Historical manifests remain immutable evidence. No repository-wide closure, identity promotion, or authority change is performed.

## Continuous-improvement learning

A current-state executable gate must not use an immutable historical snapshot as its permanent truth source. Separate `historical checkpoint evidence` from a `refreshable current evidence manifest`, and regression-test the binding itself.
