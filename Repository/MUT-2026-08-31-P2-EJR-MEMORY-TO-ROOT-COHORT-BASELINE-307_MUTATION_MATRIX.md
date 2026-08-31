# Mutation Matrix — Lease 307 — MEMORY_TO_ROOT Baseline 11 → 10

Status: OPEN / PRE-MUTATION
Date: 2026-08-31

| Path | Mutation | Protected impact | Reversible |
|---|---|---:|---:|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | `EXPECTED_GROUP_COUNT = 11` → `10` | evidence-tool baseline only | yes |

## Preconditions

- Repair306 post-state verified.
- Full-Stack SUCCESS on repair head.
- Census artifact inspected: observed=10; only `__COHORT_COUNT_DRIFT__` incomplete marker.

## Guardrails

- No identity mutation.
- No workflow-policy mutation.
- No relationship/authority promotion.
- Exact compare required after write.

## Rollback

Restore expected count to 11 if validation shows any non-drift inconsistency.
