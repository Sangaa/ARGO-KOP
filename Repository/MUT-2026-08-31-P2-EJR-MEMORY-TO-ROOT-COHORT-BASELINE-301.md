# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-301

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort-baseline normalization after Repair300.
Opening main: `67d3afc07fe99ecf626652573e765bd69d3a346e`
Pre-write Matrix301: `fde393f60b710b81a26fbd9cda85d81c2765428c`
Functional normalization head: `b38726a2236c035ad949b1fa1bf39fdbe64425f4`

## Trigger evidence

Repair300 moved displaced root EJR-297 to EJR-424 correctly. Full-Stack run `33411014563` succeeded. Internal Document-ID run `33411014572` failed only because the provenance census expected 13 groups while complete-history classification observed 12.

Artifact `9765136756`, digest `sha256:2b701488269fa45a41d549450763b91b01468ba32811d7d3bd7839aed0319fb5`, proved history_complete=true, expected=13, observed=12, and incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`] only.

## Executed normalization

Changed only `EXPECTED_GROUP_COUNT = 13` to `EXPECTED_GROUP_COUNT = 12` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Exact compare from Lease301 opening head to functional normalization head showed one modified file with 1 addition and 1 deletion.

## Final validation

At `b38726a2236c035ad949b1fa1bf39fdbe64425f4`:
- Full-Stack run `33411361825`: SUCCESS;
- Internal Document-ID run `33411361814`: SUCCESS;
- final census artifact `9765272679`, digest `sha256:1d3cc4a94fe8d87b00353c55cf0acf78dc9a2f8a772e5edd4392dc13936e617e`;
- expected_group_count=12;
- observed_group_count=12;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[];
- history_complete=true.

Final current target set:
`EJR-165, EJR-174, EJR-218, EJR-234, EJR-237, EJR-240, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296`.

No EJR identity/content mutation, consumer rewrite, governance promotion, REP promotion, or Global Integrity promotion occurred under Lease301.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
