# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-301

Status: OPEN / BASELINE NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort-baseline normalization after Repair300.
Opening main: `67d3afc07fe99ecf626652573e765bd69d3a346e`
Pre-write Matrix301: `fde393f60b710b81a26fbd9cda85d81c2765428c`

## Trigger evidence

Repair300 moved displaced root EJR-297 to EJR-424 correctly. Full-Stack run `33411014563` succeeded. Internal Document-ID run `33411014572` failed only because the provenance census expected 13 groups while complete-history classification observed 12.

Artifact `9765136756`, digest `sha256:2b701488269fa45a41d549450763b91b01468ba32811d7d3bd7839aed0319fb5`, proves:
- history_complete=true;
- expected_group_count=13;
- observed_group_count=12;
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`];
- no member-specific incomplete group.

## Authorized state transition

Change only `EXPECTED_GROUP_COUNT = 13` to `EXPECTED_GROUP_COUNT = 12` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No EJR identity/content mutation, consumer rewrite, governance promotion, REP promotion, or Global Integrity promotion is authorized under Lease301.

## Closure gate

Lease301 closes only after exact diff verification, Full-Stack SUCCESS, Internal Document-ID SUCCESS, and final artifact inspection proving a complete 12/12 CENSUSED cohort with zero incomplete groups.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
