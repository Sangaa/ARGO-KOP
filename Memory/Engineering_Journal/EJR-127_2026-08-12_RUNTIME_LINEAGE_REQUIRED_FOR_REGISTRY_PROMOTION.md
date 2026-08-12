# EJR-127 — Runtime Lineage Required for Registry Promotion

Date: 2026-08-12

## Decision

A runtime-produced trace may participate in Verified Seam Registry promotion only after the actual runtime result has passed the existing runtime/outcome lineage verifier.

## Why

The registry was deliberately hardened to require `verification_status = VERIFIED`. The existing end-to-end test still attempted to promote a runtime-produced trace without explicitly carrying the result of lineage verification. That was a test inconsistency, not a reason to weaken the registry.

## Minimal correction

The integration test now:

1. Runs the controlled runtime.
2. Verifies trace/outcome lineage with `verify_runtime_outcome_evidence()`.
3. Materializes the exact runtime trace through the existing explicit-target persistence boundary.
4. Carries the verifier result as `verification_status` into the registry candidate.
5. Promotes only after the loader confirms the materialized evidence.

No new persistence layer or architecture was introduced.

## Safety rule

`Candidate -> CONNECTED` remains forbidden without explicit verified status. File existence, names, and candidate provenance are not verification.

## Deferred

Permanent governed evidence placement and the full repository connectivity/construction audit remain later-stage work. Version reconciliation from external advisory reports remains deferred until the planned full audit.
