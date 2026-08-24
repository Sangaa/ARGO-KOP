# EJR-322 — GitHub Connector GT-014 PR Lifecycle Capability

Date: 2026-08-24
Protocol: GOV-017 / HERMUZ session protocol
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first

## Objective

Extend GT-013 from branch-scoped sequential file mutation into the pull-request lifecycle: create a disposable branch, create one isolated probe file, create a draft PR against `main`, inspect the PR metadata, enumerate changed files, inspect the exact patch, and close the PR without merging.

## Probe

Branch: `probe/hermuz-gt014-20260824-v1`

Probe file: `Quality/Integration/.hermuz_gt014_probe`

Create commit: `c1df6b127aefd70643aad519c8bf16e1200f86cd`

Read-back blob SHA: `265ccfe78a3b3366e5c4902203002f79ec72e8fa`

PR: #27

## Observed Capabilities

1. Draft PR creation succeeded with explicit head and base branches.
2. PR metadata inspection returned state, draft state, head SHA, base SHA, commit count, and changed-file count.
3. Changed-file enumeration returned the exact probe path.
4. Per-file patch inspection returned the expected one-line addition.
5. PR close succeeded without merge.
6. Final PR state was `closed`, `merged = false`.

## Important Connector Observation

The first PR-create response reported `mergeable = false`; a subsequent metadata read reported `mergeable = true`. Therefore mergeability is treated as a dynamic GitHub state and must not be cached from the creation response.

The normalized metadata also exposed a non-null `merge_commit_sha` while `merged = false` and `merged_at = null`. This field is therefore not accepted as evidence of an actual merge. Merge truth is determined from explicit `merged` / `merged_at` state.

## Safety Boundary

No merge was performed. The probe did not modify production logic. The PR was intentionally closed after create/inspect verification.

The connector surface used in this cycle does not expose a branch-deletion operation, so the disposable probe branch remains as a non-production training artifact. This is recorded rather than falsely claiming branch cleanup.

## Learning

PR lifecycle evidence must be read back after creation. `state`, `draft`, `merged`, `merged_at`, and mergeability are distinct fields with different semantics. A connector must not infer merge from the presence of `merge_commit_sha` alone.

## Closure

`create branch → create probe → read-back → create draft PR → inspect PR → enumerate files → inspect patch → close PR → verify closed/unmerged`

GT-014 is closed for the exercised PR create/inspect/close capability path. Merge remains a separate capability class and was deliberately not executed.
