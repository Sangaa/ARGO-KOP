# MUT-2026-08-31-P2-EJR-217-TO-411-IDENTITY-REPAIR-257

Status: CLOSED / SUCCESSOR-VERIFIED / ONE-RECORD REPAIR / RESUME-SAFE
Scope: One-record Priority-2 identity repair: displaced root EJR-217 → EJR-411.

## Authority
- Disposition255 retained the earlier Memory EJR-217 and classified the later root allocation displaced.
- Vacancy256 was CLOSED / EXECUTION-VERIFIED before allocation and proved EJR-411 vacant across complete reachable history.
- Repair257 preserved the then-current MEMORY_TO_ROOT baseline 26 inside the repair lease.

## Functional mutation
Prewrite: `f177d6fa7e078f496937e8459499d8b516d39cbc`.
Functional repair: `bd0b833ed006118352dc1139f83de0a4e63a4194`.

The bounded mutation:
1. retained `Memory/Engineering_Journal/EJR-217_2026-08-14_P34_SESSION_CLOSURE.md` unchanged;
2. removed `EJR/EJR-217_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md`;
3. created `EJR/EJR-411_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md` preserving semantic body/date/chronology and changing only record path/H1 identity;
4. performed no consumer rewrite because zero direct consumer obligations were established;
5. did not change the census baseline inside the repair.

Compare prewrite→repair proved only the root rename/H1 identity change plus the repair Mutation Matrix state update.

## Repair-head verification
At exact repair head `bd0b833ed006118352dc1139f83de0a4e63a4194`, Real Mutation Matrix run `33368357951` succeeded. Internal-ID run `33368357858` passed audit/chronology/lineage/provenance stages and failed only at the deterministic MEMORY_TO_ROOT census.

Repair-head artifact `9749113045`, digest `sha256:354c7181f8b881e302828a3d7a311f7e06c9295ed4a14e2b58b78b19538d9558`, proved expected=26, observed=25, history_complete=true, decision=PARTIAL, and sole incompleteness `__COHORT_COUNT_DRIFT__`; EJR-217 and EJR-411 were absent from target_ids. This failure is preserved as legitimate repair evidence.

## Successor verification
Lease258 separately changed only `EXPECTED_GROUP_COUNT = 26` → `25` at `e6111ec33574601d3e979451dedcb3e44d4a0c65`.

Exact successor verification:
- Internal-ID `33368587229`: SUCCESS
- Full-Stack `33368587218`: SUCCESS
- Runtime `33368587225`: SUCCESS
- M2 `33368587254`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to the census-only successor diff.

Final census artifact `9749193758`, digest `sha256:6d3886048bed192173aab7f8a6edacf565af83501691e8305caca6026c303c5f`, proved expected=25, observed=25, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], with EJR-217/EJR-411 absent from target_ids.

## Boundary
Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide reconciliation and global graph validation remain OPEN; Global Integrity remains HOLD.
