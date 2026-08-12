# EJR-106 — CANDIDATE PROVENANCE CARRIED INTO GAP MAPS

Date: 2026-08-12
Session Type: Connectivity Construction / Gap-Map Evidence Plumbing
Status: CLOSED CHECKPOINT

## Starting Point

Resumed from `EJR-105 — Canonical Spine Candidate Provenance Wiring`.

The scanner already returned bounded repository-relative candidate files for same-file endpoint co-occurrence. The next useful construction step was to ensure that this provenance survives into the GAP MAP so a reviewer can move from a reported gap to the artifacts that caused it to become a candidate.

## Work Completed

### 1. Gap Map now accepts bounded candidate provenance

Updated:

- `Quality/Integration/canonical_spine_gap_map.py`
- `Quality/Integration/test_canonical_spine_gap_map.py`

`build_gap_map()` now accepts optional `candidate_files` and preserves those paths on non-connected gap entries.

The new boundary validates candidate paths as repository-relative paths and rejects:

- absolute paths;
- `..` traversal;
- empty/non-string values;
- non-list candidate collections.

### 2. Evidence boundary preserved

Candidate provenance does not alter the seam state.

A seam remains `MISSING` or `PARTIAL` even when candidate files are supplied. The gap map explicitly treats provenance as discovery context, not integration evidence.

Therefore:

`Candidate Artifact → Gap Map`

is now a navigable review path, but not a promotion path.

### 3. Regression coverage added

Tests cover:

- preserving candidate files on a gap;
- keeping the original seam state unchanged;
- rejecting repository-escaping candidate paths;
- preserving existing complete/partial/invalid-state behavior.

## Root Synchronization

Updated:

- `START_HERE.md` → EJR-106 resumption point and new Gap Map behavior.

`PROJECT_STATUS.md` was inspected before mutation. Its current content already records the EJR-105 scanner/provenance state and the standing evidence-boundary rules. It was not rewritten in this checkpoint because the available repository read was truncated; avoiding a large blind replacement preserves repository safety. A root status version increment is therefore intentionally deferred until the complete file can be safely re-read and synchronized.

## Evidence Boundary

The GitHub writes were accepted. The changed code and tests were inspected before/after mutation through repository reads where available.

No successful CI status was observed for this checkpoint. Therefore no test PASS is claimed from CI.

## Current Seam State

No canonical-spine seam was promoted to `CONNECTED` by this checkpoint.

The strongest current candidate remains the Decision/Authorization/Execution area, but candidate provenance is still not sufficient to certify the relationship.

## Next Target

Use the GAP MAP candidate locations to perform actual contract/test/trace inspection on the highest-value candidates, then validate the runtime consumer and outcome relationship. Only complete evidence sets may enter the verified registry.

Required path:

**GAP → Candidate Artifact → Contract → Consumer → Executable Test → Trace → Outcome → Verified Registry → Canonical Audit**

## Closure

This checkpoint closes only the GAP MAP provenance plumbing. It does not close the connected-baseline phase, does not certify a seam, and does not authorize feature expansion.

---

End of Checkpoint
