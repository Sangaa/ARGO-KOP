# EJR-131 — Repository Evidence Capture Integration

Date: 2026-08-12
Status: Checkpoint / Evidence Capture Integration

## Purpose

Close the smallest remaining seam between the actual runtime trace and the governed repository evidence boundary without introducing a new persistence layer.

## Evidence

The existing `capture_repository_evidence()` boundary composes all repository evidence paths beneath `Quality/Integration/evidence/runtime` and rejects absolute/traversal targets.

The new integration regression executes the real connected-spine runner, captures its actual execution trace through that boundary, re-reads the materialized artifact, and verifies the returned repository-relative path and trace identity.

## Verified path

Runtime → actual execution trace → governed repository evidence boundary → materialized evidence artifact → re-read.

## Non-claims

This checkpoint does not promote a seam to `CONNECTED` by itself. Registry promotion still requires explicit `VERIFIED` status plus complete contract/test/trace evidence, and the canonical audit remains authoritative.

No canonical Memory mutation was introduced. No second persistence layer was introduced.

## Failure-learning rule

A temporary test target is not evidence of repository integration. The integration test therefore exercises the repository-boundary API and verifies the governed relative path explicitly.

## Next

Run/inspect CI evidence for this integration, then attempt the complete path through loader → verified registry → canonical audit. If successful, move to the next highest-value seam rather than over-polishing this one.
