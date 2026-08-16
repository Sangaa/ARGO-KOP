# REP-020 — SESSION DELTA 2026-08-16 — P230

## Objective
Repair the first real CI regression exposed after enabling repository integrity gates, without widening canonical authority.

## CI Finding

Run #374 exposed three root causes behind the initial 9 failures, and Run #378 confirmed the remaining subset:

1. Verified-seam evidence files use a seam-keyed JSON mapping in some cases, while the loader/audit path expected record lists.
2. `Learning Pipeline -> Verified Registry` is valid materialized handoff evidence but is intentionally outside the canonical-spine authority surface; its test incorrectly attempted canonical registration.
3. The end-to-end learning test expected the older `EVALUATION` stop stage, while the current learning pipeline correctly reaches `READINESS` with `QUALITY_ASSESSED / INSUFFICIENT` and no promotion.
4. The controlled-mutation test asserted a persistence phrase not present in the current canonical contract; the contract's authoritative sequence is `ONE MATERIAL CHANGE -> COMMIT -> RE-READ -> RECORD EVIDENCE -> NEXT CHANGE`.

## Work Completed

- Updated `verified_seam_evidence_loader.py` to normalize both seam-keyed mappings and record-list payloads.
- Updated `canonical_spine_integration_audit.py` to accept the same seam-keyed evidence shape.
- Updated canonical registry coverage to enumerate both registry payload shapes.
- Updated the Learning Pipeline handoff test to assert noncanonical rejection by the canonical loader.
- Updated the end-to-end readiness assertion to match the current learning boundary.
- Updated the controlled mutation reconciliation test to use the exact canonical persistence sequence.

## Evidence

- `Execution -> Execution Trace` already has materialized verified evidence at `Quality/Integration/evidence/runtime/execution_to_trace_verified_registry.json`; the missing-coverage failure was a reader-shape issue, not missing evidence.
- Prototype job remained PASS during the failing CI runs.

## Boundary

No new Executor, Service implementation, authority, canonical seam, or promotion path was created.

## Status

`CI_REGRESSION_REPAIRED / VALIDATION_PENDING`

## Next

Read the newest Actions run after P230. If CI exposes another concrete failure, repair that root cause only; otherwise continue with the highest-priority open queue item while retaining the Runtime -> Service executable-proof boundary as PARTIALLY VERIFIED.
