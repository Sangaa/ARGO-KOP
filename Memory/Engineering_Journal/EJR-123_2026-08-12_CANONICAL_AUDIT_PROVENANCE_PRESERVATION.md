# EJR-123 — Canonical Audit Provenance Preservation

**Date:** 2026-08-12
**Status:** CLOSED

## Purpose
Preserve bounded candidate provenance when the canonical spine audit builds its GAP MAP, without allowing candidate paths to affect seam state.

## Change
`Quality/Integration/canonical_spine_integration_audit.py` now passes the scanner's bounded `candidate_files` into `build_gap_map()`.

This preserves useful navigation context for unresolved seams while keeping the existing rule intact:

- candidate provenance is discovery context only;
- it cannot promote a seam;
- `CONNECTED` still requires an explicit `verification_status == VERIFIED` record;
- contract, test, and trace references must be repository-relative regular files.

## Why This Is Conservative
The change does not alter seam states or invent evidence. It only prevents already-collected bounded provenance from being discarded before the GAP MAP is produced.

## Validation Boundary
No seam was promoted during this checkpoint. CI must validate the change before any certification decision.

## Next Step
Use the preserved provenance to inspect the highest-value unresolved seam, then assemble one complete actual-runtime evidence set and run the canonical audit before expanding further.
