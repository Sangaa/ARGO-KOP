# MUT — MEMORY_TO_ROOT Cohort Baseline Normalization — Lease 310

Date: 2026-08-31
Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Priority: P2 Internal Document-ID Audit

## Executed normalization
Functional head `6633c038d7fea8f73bc990f097311afebbbd677e` changed only:
`EXPECTED_GROUP_COUNT = 10` → `9` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Exact compare from matrix head showed one changed file with +1/-1 only.

## Validation
- Internal Document-ID Audit run `33417436428`: SUCCESS.
- Final census artifact `9767575237`: `expected_group_count=9`, `observed_group_count=9`, `classification_complete=true`, `decision=CENSUSED`, `incomplete_group_ids=[]`.
- Current cohort: EJR-165, EJR-234, EJR-237, EJR-240, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296.
- Full-Stack run `33417436519`: SUCCESS.

Priority 2 and Phase 1 remain OPEN. Global Integrity remains HOLD.
