# EJR-104 — CANONICAL SPINE SCANNER FALSE-POSITIVE HARDENING

Date: 2026-08-12
Session Type: Evidence Discovery / Seam Detection Hardening
Status: CLOSED CHECKPOINT

## Starting Point

Resumed from EJR-103 with the objective of continuing repository construction while prioritizing connectivity and evidence quality over file-count throughput.

## Finding

`Quality/Integration/canonical_spine_evidence_scanner.py` previously combined the text of the entire repository and then asked whether source and destination keywords existed anywhere in that combined text.

That method could classify an unrelated pair of files as a `PARTIAL` seam merely because one file mentioned the source and another unrelated file mentioned the destination.

This was an audit-quality defect: the scanner was conservative about `CONNECTED`, but its `PARTIAL` discovery signal could still be inflated by repository-wide keyword co-occurrence.

## Change

The scanner now evaluates endpoint keyword co-occurrence **within the same repository file** before returning `PARTIAL`.

It still:

- never emits `CONNECTED`;
- returns only `PARTIAL` or `MISSING`;
- skips `.git` content;
- treats unreadable files as non-evidence;
- remains a candidate-discovery layer rather than an integration-certification layer.

## Tests Added

`Quality/Integration/test_canonical_spine_evidence_scanner.py` now verifies:

1. the scanner never claims `CONNECTED`;
2. an empty repository produces only `MISSING`;
3. source and destination in unrelated files do not create a false seam;
4. source and destination in one file produce only a `PARTIAL` candidate.

## Evidence Boundary

This change improves the quality of candidate discovery. It does not prove any canonical-spine seam is connected.

`PARTIAL` means only that a file contains textual evidence for both endpoint concepts. A real `CONNECTED` claim still requires registry evidence with contract/test/trace artifacts that are materialized inside the repository and then pass the canonical audit boundary.

## Next Target

Use the hardened scanner to prioritize actual seam candidates, then inspect each candidate's contract, executable/synthetic test and traceability/outcome evidence. Do not promote keyword co-occurrence to architectural connectivity.

## Root Synchronization

Root status and resumption documents must be synchronized at the next material root checkpoint; no unrelated root rewrite was made solely to increase file count.

## Closure

Checkpoint closes scanner false-positive hardening and its regression boundary. Repository-wide connectivity remains open.

---

End of Checkpoint
