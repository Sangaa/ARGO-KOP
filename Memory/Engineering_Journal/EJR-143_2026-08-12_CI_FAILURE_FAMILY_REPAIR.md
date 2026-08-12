# EJR-143 — CI Failure Family Repair

Date: 2026-08-12

## Trigger

CI integration run reported 10 failures / 57 passes.

## Root causes identified

1. Valid but inconclusive feedback was being marked `QUALITY_REJECTED`. Quality assessment and learning readiness are separate boundaries; an assessed INCONCLUSIVE result must remain assessed but not learning-ready.
2. Repository evidence loader silently dropped incomplete candidates, allowing callers to misread omission as successful loading. It now rejects unverified/incomplete candidates explicitly.
3. Canonical seam coverage did not include the real `Execution -> Outcome` producer handoff exercised by end-to-end evidence tests. The seam is now explicit in the canonical seam list; this does not itself certify it CONNECTED.
4. Repository-backed evidence tests referenced contract/test paths without materializing them in their temporary repository root. The tests now create those bounded artifacts before asking the audit/loader to verify them.
5. The reasoning-packet and outcome-confidence repairs from the preceding checkpoints are present on `main` and are exercised by the next CI run.

## Changes

- `Runtime/Learning/feedback_quality_gate.py`
- `Quality/Integration/canonical_spine_gap_map.py`
- `Quality/Integration/verified_seam_evidence_loader.py`
- `Quality/Integration/test_repository_evidence_to_registry.py`
- `Quality/Integration/test_repository_evidence_canonical_audit.py`

## Boundary Rules Preserved

- `QUALITY_ASSESSED` does not imply learning readiness.
- `READY_FOR_PROMOTION_REVIEW` does not perform promotion.
- Verified evidence is required before CONNECTED.
- Candidate provenance never promotes a seam.
- Repository audit still requires real contract/test/trace artifacts and a valid execution-trace JSON artifact.

## Verification State

The preceding CI run was still 10 failed / 57 passed. These changes require a fresh CI run. No success is claimed until that run reports it.

## Next Action

Run CI. Triage only the remaining failure families. If green, proceed to the next highest-value connectivity gap and eventually the full repository connectivity audit.
