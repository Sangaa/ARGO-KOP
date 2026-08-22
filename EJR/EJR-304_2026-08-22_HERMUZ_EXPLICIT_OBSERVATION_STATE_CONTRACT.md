# EJR-304 — HERMUZ Explicit Observation-State Contract Enforcement

Date: 2026-08-22
Status: Closed — Mutation + Read-back Verified
Scope: P6 evidence boundary

## Trigger

EJR-303 established that `NO_OBSERVATION`, `SURFACE_UNAVAILABLE`, and `SURFACE_REJECTED` are materially different states. The next risk was that an adapter could silently omit or mislabel observation provenance and thereby collapse a connector capability failure back into `NO_OBSERVATION`.

## Prior learning

`Observed empty result` is a repository observation.
`Unavailable/rejected observer` is an observation-channel condition.
The latter must not be interpreted as repository absence.

## Mutation

`Quality/Integration/p6_reconciliation.py` now exposes the explicit `OBSERVATION_STATES` vocabulary and documents that callers must provide observation provenance. The reconciliation decision order remains deterministic and backward-compatible through the existing default `OBSERVED` state.

## Regression

`Quality/Integration/test_p6_reconciliation_boundaries.py` now verifies the exact observation-state vocabulary and preserves all previous P6-08/P6-09 boundary cases, including the invariant that surface failures cannot become `NO_OBSERVATION`.

## Verification

Both mutated files were read back after sequential writes.

The repository-level controlled regression suite is the authoritative next execution step. No claim of canonical CI execution is made by this record.

Current file blob SHAs after read-back:

- `p6_reconciliation.py`: `af9bdc7ae1c17c301160a185222eb813b2b30281`
- `test_p6_reconciliation_boundaries.py`: `2990ce468ff6bae52d8d26f9e6bf44cc17d4d833`

Mutation commits:

- engine: `17794d1a20b93de2d117e8cbd99823c24456f49a`
- regression test: `06bf4cce865862b3660870bcd0462c3deb831676`

## Learning

The evidence boundary is safer when the provenance state is explicit and machine-checkable rather than inferred from missing fields. This converts a learned diagnostic rule into an enforced architectural contract.

## Closure

Mutation: COMPLETE
Read-back: VERIFIED
Canonical CI: NOT CLAIMED
P6 root cause: NOT CLAIMED
Relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — READ-BACK VERIFIED`.
