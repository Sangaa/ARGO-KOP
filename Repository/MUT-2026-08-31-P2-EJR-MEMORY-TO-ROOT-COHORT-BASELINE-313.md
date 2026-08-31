# Lease 313 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization

Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

## Trigger
Repair 312 reduced the deterministic MEMORY_TO_ROOT_EJR ambiguity cohort from 9 to 8 with no member-specific incomplete IDs.

## Executed mutation
Changed only `EXPECTED_GROUP_COUNT = 9` → `EXPECTED_GROUP_COUNT = 8` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.
Exact compare: one file, +1/-1.

## Verification
Functional baseline head: `79553ce51075f711a2e5b16de663d3b30b0b26d4`.
Internal Document-ID Audit: SUCCESS.
Provenance artifact: expected=8, observed=8, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].
Full-Stack Repository Audit: SUCCESS.

## Outcome
Current deterministic cohort baseline is 8. Priority 2 and Phase 1 remain OPEN. Global Integrity remains HOLD.
