# EJR-121 — VERIFIED REGISTRY PROMOTION GUARD

**Date:** 2026-08-12
**Status:** Closed checkpoint

## Objective

Strengthen the boundary between evidence discovery/validation and `CONNECTED` seam certification.

## Finding

The verified seam registry accepted complete repository-relative references for `contract`, `test`, and `trace`, but the registry itself did not require an explicit verification result. That allowed a complete-looking record to become `CONNECTED` based on shape alone.

## Change

`Quality/Integration/verified_seam_evidence_registry.py` now requires:

- a canonical seam key;
- unique seam record;
- repository-relative evidence references;
- explicit `verification_status == VERIFIED`.

The registry remains a promotion boundary, not a discovery mechanism. Candidate provenance and path existence are insufficient.

## Regression Coverage

Added registry regression coverage for:

1. explicitly verified complete evidence → `CONNECTED`;
2. complete but unverified evidence → rejected.

## Evidence Boundary

The registry does not itself prove semantic correctness. The upstream loader/audit/verifier chain must establish the verification result from concrete artifacts and runtime evidence before a record is submitted.

## Current Seam State

The controlled Execution → Execution Trace → Outcome path has runtime-produced trace/outcome lineage verification and explicit-target materialization tests. It is still not promoted automatically; canonical certification requires the complete evidence set to pass the upstream boundaries and then the canonical audit.

## Deferred

- Do not create another persistence layer.
- Do not treat external model reviews as build authority.
- Do not reconcile repository-wide version drift during this checkpoint.
- Full repository inventory and construction-priority audit remain scheduled after the current seam set is sufficiently mature.

## Resumption Point

Inspect the latest Actions result, assemble the complete evidence record from actual runtime artifacts, pass it through the loader/verifier boundaries, then evaluate registry promotion and run the canonical spine audit.
