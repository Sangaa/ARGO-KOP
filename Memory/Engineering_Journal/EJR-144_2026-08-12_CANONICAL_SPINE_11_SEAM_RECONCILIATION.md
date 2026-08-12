# EJR-144 — Canonical Spine 11-Seam Reconciliation

Date: 2026-08-12

## Trigger

CI run #96 reached 65 passing integration tests and exposed two scanner regressions. Both failures asserted a legacy seam count of 10 while the canonical seam definition contains 11 seams.

## Verified Source of Truth

`Quality/Integration/canonical_spine_gap_map.py` defines 11 canonical seams, including the explicit `Execution -> Outcome` seam.

The scanner is discovery-only and must never claim `CONNECTED` from co-occurrence. Its states remain `PARTIAL` or `MISSING` until independent evidence verification occurs.

## Change

Updated `Quality/Integration/test_canonical_spine_evidence_scanner.py`:

- reconciled expected seam count from 10 to 11;
- retained conservative-state assertions;
- added a regression proving `Execution -> Outcome` is represented by the scanner as a partial candidate only when endpoint concepts co-occur in one artifact.

## CI Evidence

Run #96: prototype job passed; integration job failed with exactly 2 scanner assertions and 65 passing tests. The failure was a stale test expectation, not evidence that the scanner should remove the `Execution -> Outcome` seam.

## Decision

Keep the 11-seam canonical spine. Do not regress the architecture to satisfy an obsolete count.

## Next

Run CI on the reconciliation commit. If green, inspect remaining repository-wide integration gaps before adding new functionality.
