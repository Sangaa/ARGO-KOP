# Branch Family Disposition — KRS P257–P266

Date: 2026-08-29
Baseline inspected: `main@98d78edab9cac1ab14b0e831d1c1c3ed0e585a61`

Leases:
- `R71-20260829-BRANCH-HYGIENE-059` — `hermuz/krs002-mainline-p257`
- `R71-20260829-BRANCH-HYGIENE-060` — `hermuz/krs005-bounded-equivalence-p264`
- `R71-20260829-BRANCH-HYGIENE-061` — `hermuz/krs006-heterogeneous-pilot-p266`
- `R71-20260829-BRANCH-HYGIENE-062` — `hermuz/krs005-operational-advantage-p265`
- `R71-20260829-BRANCH-HYGIENE-063` — `hermuz/krs-reconciliation-p262`

## Ancestral branches

Git comparison establishes `ahead_by=0` for:
- `hermuz/krs002-mainline-p257`;
- `hermuz/krs005-bounded-equivalence-p264`;
- `hermuz/krs006-heterogeneous-pilot-p266`.

These branches are fully ancestral to current main and therefore contain no unmerged branch-only work.

Disposition for each:
`FULLY_ANCESTRAL_TO_MAIN / NO_UNMERGED_WORK / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Assessment-only branches

`hermuz/krs005-operational-advantage-p265` contains only the P265 mutation matrix and operational-advantage assessment. The assessment explicitly states:
- `ASSESSMENT / NO MIGRATION`;
- repository-wide migration is not authorized;
- source retirement is not authorized;
- runtime consumer change is not authorized;
- compression is not proven.

Disposition:
`HISTORICAL_BOUNDED_KRS_ASSESSMENT / NO_MIGRATION_AUTHORITY / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

`hermuz/krs-reconciliation-p262` contains only a three-class compression pilot and its matrix. The pilot explicitly states `ASSESSMENT / NOT CANONICAL`, concludes that no repository-wide compression is proven, and preserves governance/learning surfaces rather than flattening them into one representation.

Disposition:
`HISTORICAL_NONCANONICAL_COMPRESSION_ASSESSMENT / NO_REPOSITORY_WIDE_COMPRESSION_PROVEN / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Learning

The KRS family already contains its own safety boundary: structured Knowledge Objects showed bounded retrieval/addressability value, but neither byte compression nor repository-wide migration was proven. Preserve that distinction; do not turn pilot usefulness into migration authority.
