# Branch Family Disposition — Historical Probe / Training Surfaces

Date: 2026-08-29

Leases:
- `R71-20260829-BRANCH-HYGIENE-093` — `probe/actions-trigger-20260822`
- `R71-20260829-BRANCH-HYGIENE-094` — `probe/github-channel-write-read-20260821`
- `R71-20260829-BRANCH-HYGIENE-095` — `probe/hermuz-execution-observation-20260822`
- `R71-20260829-BRANCH-HYGIENE-096` — `probe/hermuz-gt012-20260824`
- `R71-20260829-BRANCH-HYGIENE-097` — `probe/hermuz-gt012-20260824-v2`
- `R71-20260829-BRANCH-HYGIENE-098` — `probe/hermuz-gt012-20260824-v3`
- `R71-20260829-BRANCH-HYGIENE-099` — `probe/hermuz-gt012-20260824-v4`
- `R71-20260829-BRANCH-HYGIENE-100` — `probe/hermuz-gt012-20260824-v5`
- `R71-20260829-BRANCH-HYGIENE-101` — `probe/hermuz-gt012-20260824-v6`
- `R71-20260829-BRANCH-HYGIENE-102` — `probe/hermuz-gt012-20260824-v7`
- `R71-20260829-BRANCH-HYGIENE-103` — `probe/hermuz-gt012-20260824-v8`
- `R71-20260829-BRANCH-HYGIENE-104` — `probe/hermuz-gt012-20260824-v9`
- `R71-20260829-BRANCH-HYGIENE-105` — `probe/hermuz-gt012-20260824-v10`
- `R71-20260829-BRANCH-HYGIENE-106` — `probe/hermuz-gt012-20260824-final`
- `R71-20260829-BRANCH-HYGIENE-107` — `probe/hermuz-gt013-20260824-v1`
- `R71-20260829-BRANCH-HYGIENE-108` — `probe/hermuz-gt014-20260824-v1`
- `R71-20260829-BRANCH-HYGIENE-109` — `probe/hermuz-layered-channel-law-20260822`
- `R71-20260829-BRANCH-HYGIENE-110` — `probe/hermuz-observation-law-20260822`
- `R71-20260829-BRANCH-HYGIENE-111` — `training/gt012b-git-object-lifecycle-20260823`

## Fully ancestral probe/training refs

The original GT012 ref, GT012 v2-v9, GT012 final, layered-channel-law, and `training/gt012b-git-object-lifecycle-20260823` compare as strictly behind current main with `ahead_by=0` and no changed files.

Disposition:
`FULLY_ANCESTRAL_TO_MAIN / NO_UNMERGED_WORK / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Net-zero experiment refs

`probe/github-channel-write-read-20260821`, `probe/hermuz-execution-observation-20260822`, `probe/hermuz-gt012-20260824-v10`, `probe/hermuz-gt013-20260824-v1`, and `probe/hermuz-observation-law-20260822` have historical commits but no net changed-file delta against current main.

Disposition:
`HISTORICAL_PROBE_COMMIT_LINEAGE / ZERO_NET_TREE_DELTA / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Explicit marker-only probe refs

`probe/actions-trigger-20260822` leaves one text probe whose content says its purpose is connector write-capability verification only and explicitly states `No ARGO production logic or governance artifact.`

`probe/hermuz-gt014-20260824-v1` leaves a one-line hidden integration marker: `GT-014 PR lifecycle probe`.

Disposition:
`HISTORICAL_PROBE_MARKER_ONLY / NON_PRODUCTION_NON_AUTHORITY / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Coordination boundary

This classification preserves branch history as training/tool evidence while preventing probe fixtures from being mistaken for production architecture, governance, or current verification authority.

## Learning

A branch may contain meaningful experimental history while having zero current tree delta. Commit history and current promotion payload are separate questions; preserve the former without manufacturing the latter.
