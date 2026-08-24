# EJR-271 — GT-065 Execution State Reconciliation

**Date:** 2026-08-24
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Scope:** Training / CI provenance only
**Mutation class:** Documentation-only

## Objective

Continue GT-064 by testing whether the CI execution SHA can be bound to a concrete Git object state and therefore to the filesystem state that could have produced the CI artifact.

## Evidence observed

PR #27 in `Sangaa/ARGO-KOP` is closed and not merged. Its metadata records:

- `base_sha = bc0ab35b5051a436d44f42b5fff9413659ede083`
- `head_sha = c1df6b127aefd70643aad519c8bf16e1200f86cd`
- `merge_commit_sha = 412f0ff10dc33b9411a9a2195fad146d5af81881`

The execution-side commit previously identified as `checkout_sha` is:

- `execution_sha / checkout_sha = aa9b0665c932a91a15868c417928d311b8a24a5c`
- commit message: `Merge c1df6b127aefd70643aad519c8bf16e1200f86cd into ee368e58cb54b3c24f9535bf549ebebccf046cf4`
- parents:
  - `ee368e58cb54b3c24f9535bf549ebebccf046cf4`
  - `c1df6b127aefd70643aad519c8bf16e1200f86cd`
- `tree_sha = 9e41a3668d2023208a82d3e6940219c4e9ec4d2e`

The execution tree contains the probe file:

`Quality/Integration/.hermuz_gt014_probe`

with blob SHA:

`265ccfe78a3b3366e5c4902203002f79ec72e8fa`

and blob content:

`GT-014 PR lifecycle probe`

## Reconciliation result

The execution SHA is therefore not an opaque identifier. It resolves to a real Git commit, with explicit parents, a concrete tree, and a concrete blob representing filesystem content.

However, the currently available connector surface did **not** provide a direct historical read proving that `refs/pull/27/merge` pointed to `aa9b0665c932a91a15868c417928d311b8a24a5c` at the exact CI execution time. The commit-to-workflow lookup for this SHA also returned no workflow runs through the available filtered surface.

Therefore the evidence boundary is:

`execution SHA → commit → parents → tree → blob = VERIFIED`

but:

`historical execution_ref → execution SHA → CI run/artifact = NOT FULLY RECONCILED`

## Verdict

**GT-065 = PARTIAL / EXECUTION-STATE-IDENTIFIED-BUT-RUN-BINDING-INCOMPLETE**

This is not a CI failure and not evidence that the SHA is invalid. It is a provenance completeness boundary.

## Architectural learning

A CI evidence record must preserve at minimum:

- `source_head_sha`
- `base_sha`
- `pr_merge_commit_sha`
- `execution_ref`
- `execution_sha`
- `checkout_sha`
- `tree_sha`
- artifact identity / run identity when available

`commit_sha` alone is insufficient to establish CI execution identity.

A Git object graph can establish the filesystem state represented by an execution commit, but it does not by itself prove that a particular CI run or artifact executed from that commit unless the run/ref binding is independently evidenced.

## Session boundary

No production logic was changed. This entry records the verified evidence and the remaining provenance gap only.

**Next safe priority:** recover or independently establish the historical CI run/artifact binding to `refs/pull/27/merge` and `aa9b0665c932a91a15868c417928d311b8a24a5c` before declaring CI provenance closed.
