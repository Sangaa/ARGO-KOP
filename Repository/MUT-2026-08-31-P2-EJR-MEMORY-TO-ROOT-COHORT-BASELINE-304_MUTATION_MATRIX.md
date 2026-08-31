# Mutation Matrix 304 — MEMORY_TO_ROOT Cohort Baseline 12→11

Status: OPEN / PRE-MUTATION
Date: 2026-08-31

Prerequisite Repair303 evidence:
- root EJR-218 atomically displaced to EJR-425;
- Full-Stack SUCCESS on repair head `74cc1f6211c4a3ea20b06b541ca56891f6545ce9`;
- deterministic census: expected 12, observed 11;
- only incomplete marker: `__COHORT_COUNT_DRIFT__`.

Allowed mutation: change only `EXPECTED_GROUP_COUNT = 12` to `EXPECTED_GROUP_COUNT = 11` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Forbidden: any identity/content/reference rewrite, authority promotion, or unrelated test change.

Required validation: exact diff inspection, Internal Document-ID Audit SUCCESS, Full-Stack Repository Audit SUCCESS, artifact expected=observed=11 with classification_complete=true.

Global Integrity remains HOLD.
