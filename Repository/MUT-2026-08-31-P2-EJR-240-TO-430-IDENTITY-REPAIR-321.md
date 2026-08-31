# Repair 321 — Root EJR-240 → EJR-430 Identity Repair

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31

## Authorization
Lease319 retained the earlier Memory EJR-240 allocation and classified the later root EJR-240 record as displaced. Lease320 run `33422684323` proved EJR-430 VACANT with complete history.

## Executed mutation
Atomic functional commit `dce9b40c7d013d3d7600812d7d9728ba4cafcb18`:
- renamed root `EJR-240_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md` to `EJR-430_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md`;
- changed only its first-H1 identity;
- updated the two live semantic-provenance mentions in `EJR-416` from EJR-240 to EJR-430;
- preserved Memory EJR-240 at blob `a09c33622adfd3f258d1e1f8f4af628d3506b317`.

Exact functional compare from `b8278ecac0b9e1c87ef0e47629ec633a4775ce58` to repair head shows only the root rename/H1 change and the two EJR-416 provenance substitutions.

## Verification
- old root EJR-240 path: absent;
- successor EJR-430 path: present, blob `3b9c4a4b46ae0f445d7cbe8a5e848b3630e62b5b`;
- Memory EJR-240 blob unchanged;
- EJR-416 provenance self-consistent with EJR-430;
- Full-Stack run `33422982316`: SUCCESS;
- Internal-ID run `33422982303`: all tests/stages passed except the deterministic MEMORY_TO_ROOT census emission.

Repair-head census artifact `9769651317`, digest `sha256:c4473dcfebc970091519bd8a2c479e793d5ae1d431fbdc379b19e08331b34a71`, proved:
- expected_group_count: 7
- observed_group_count: 6
- history_complete: true
- decision: PARTIAL
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`] only
- remaining target_ids: EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296

## Outcome
Repair321 is functionally correct. The expected 7→6 cohort drift is preserved as evidence and must be normalized only under a separate rebaseline lease. Priority 2 remains OPEN; Phase 1 remains OPEN; Global Integrity remains HOLD.