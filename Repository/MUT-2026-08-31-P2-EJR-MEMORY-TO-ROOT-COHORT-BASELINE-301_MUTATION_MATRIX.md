# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 301

Status: OPEN / PRE-WRITE GATE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-301
Opening main: `67d3afc07fe99ecf626652573e765bd69d3a346e`
Execution role: HERMUZ
Predecessor Repair300: functional identity repair complete; normalization pending.

## Evidence for deterministic normalization

Repair300 atomically displaced legitimate root EJR-297 content to reserved successor EJR-424 while retaining Memory EJR-297 unchanged.

Functional repair evidence:
- Full-Stack run `33411014563`: SUCCESS;
- Internal Document-ID run `33411014572`: FAILURE only at MEMORY_TO_ROOT provenance census;
- census artifact `9765136756`, digest `sha256:2b701488269fa45a41d549450763b91b01468ba32811d7d3bd7839aed0319fb5`;
- history_complete=true;
- expected_group_count=13;
- observed_group_count=12;
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`];
- no member-specific incomplete group exists.

Current 12-member target set reported by the artifact:
`EJR-165, EJR-174, EJR-218, EJR-234, EJR-237, EJR-240, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296`.

## Authorized mutation

Baseline-only normalization:
- `Quality/Integration/ejr_memory_to_root_provenance_census.py`
- change exactly `EXPECTED_GROUP_COUNT = 13` to `EXPECTED_GROUP_COUNT = 12`.

Forbidden under Lease301:
- EJR identity/content mutation;
- consumer/reference rewriting;
- unrelated test changes;
- relationship/governance/REP promotion;
- Global Integrity promotion.

Required validation:
- functional diff limited to one census file and one constant change;
- Full-Stack SUCCESS;
- Internal Document-ID SUCCESS;
- final census expected=12, observed=12, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], history_complete=true.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
