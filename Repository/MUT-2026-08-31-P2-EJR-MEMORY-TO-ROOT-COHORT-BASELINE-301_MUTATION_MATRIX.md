# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 301

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-301
Opening main: `67d3afc07fe99ecf626652573e765bd69d3a346e`
Execution role: HERMUZ
Functional normalization head: `b38726a2236c035ad949b1fa1bf39fdbe64425f4`
Predecessor Repair300: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE

## Evidence and mutation boundary

Repair300 left only deterministic cohort drift: expected=13, observed=12, history_complete=true, incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`] and no member-specific incomplete group. Artifact `9765136756`, digest `sha256:2b701488269fa45a41d549450763b91b01468ba32811d7d3bd7839aed0319fb5`.

Lease301 executed exactly one functional change:
- `Quality/Integration/ejr_memory_to_root_provenance_census.py`
- `EXPECTED_GROUP_COUNT = 13` → `EXPECTED_GROUP_COUNT = 12`.

Exact compare proved one file modified, 1 addition, 1 deletion.

## Validation closure

At `b38726a2236c035ad949b1fa1bf39fdbe64425f4`:
- Full-Stack `33411361825`: SUCCESS;
- Internal Document-ID `33411361814`: SUCCESS;
- final artifact `9765272679`, digest `sha256:1d3cc4a94fe8d87b00353c55cf0acf78dc9a2f8a772e5edd4392dc13936e617e`;
- expected=12;
- observed=12;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[];
- history_complete=true.

Final 12-member cohort:
`EJR-165, EJR-174, EJR-218, EJR-234, EJR-237, EJR-240, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296`.

No EJR identity/content mutation, consumer/reference rewriting, unrelated test change, governance/REP promotion, or Global Integrity promotion occurred under Lease301.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
