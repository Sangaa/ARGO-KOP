# EJR-122 — Canonical Audit Verified-Status Gate

**Date:** 2026-08-12
**Status:** CLOSED

## Purpose
Harden the final canonical-spine audit boundary so a record cannot become `CONNECTED` merely because it contains `state=CONNECTED` and materialized contract/test/trace paths.

## Change
`Quality/Integration/canonical_spine_integration_audit.py` now requires:

- repository-relative regular files for contract, test, and trace;
- `state == CONNECTED`;
- `verification_status == VERIFIED`.

The audit still performs actual repository file checks. Candidate provenance remains discovery context only.

## Regression Coverage
`Quality/Integration/test_canonical_spine_integration_audit.py` now covers:

- verified materialized evidence can promote a seam;
- unverified evidence is rejected;
- incomplete evidence is rejected;
- nonexistent evidence is rejected;
- parent traversal is rejected;
- string-only connected state is rejected.

## Engineering Decision
This is a boundary hardening change, not a seam certification. No seam was promoted from repository reality during this checkpoint. The registry and audit must agree that upstream verification is explicit before `CONNECTED` can be asserted.

## Next Step
Assemble one complete evidence set from the actual runtime path, pass it through loader + lineage verifier + registry, then run the canonical audit. Do not create another persistence layer.
