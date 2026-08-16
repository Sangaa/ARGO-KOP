# REP-020 — SESSION DELTA 2026-08-16 — P204

## Objective
Turn the already-resolved CORE-000 reference-path inconsistency into a regression-protected integrity rule without recreating a duplicate canonical artifact.

## Discovery

`EJR-155` established that `Architecture/README.md` once pointed to a non-existent `Architecture/CORE-000_PLATFORM_ARCHITECTURE.md`, while the authoritative artifact is `Core/CORE-000_PLATFORM_ARCHITECTURE.md`.

Current `Architecture/README.md` is already corrected to the authoritative `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` path, and no duplicate Architecture-owned CORE-000 artifact exists.

## Work Completed

Added:

`Quality/Integrity/test_canonical_reference_regressions.py`

The regression guard now verifies:
- Architecture README points to the authoritative Core-owned path;
- the authoritative CORE-000 file exists;
- the stale Architecture duplicate does not exist;
- exactly one repository markdown artifact owns `CORE-000_PLATFORM_ARCHITECTURE.md`.

A path-resolution defect in the first test revision was caught during immediate readback and corrected in commit `6c7e65904adbc123328cffa7abcfbc40d2d1aae5`.

## Safety Boundary

No canonical content was rewritten. No duplicate artifact was created. This checkpoint hardens an already-correct relationship rather than performing speculative normalization.

## Status

`REFERENCE_INTEGRITY_REGRESSION_GUARD_BUILT / CI_PENDING`

## Next Priority

Continue the repository-wide identity/reference audit with the next evidence-backed unresolved relationship, prioritizing duplicate IDs and cross-layer references before any capability expansion.
