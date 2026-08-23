# EJR-320 — Git Object Correlation Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent: EJR-319

## Objective
Train the connector on correlation across PR identity, commit SHA, commit object, comparison surface, and status surface.

This cycle is independent of P6 execution evidence and uses an existing diagnostic PR/commit. No production mutation was performed.

## GT-013A — PR identity → head SHA

`get_pr_info(PR #25)` returned:
- PR state: closed
- merged: false
- base: main
- base SHA: `942271c4830b059258e6f2fc1b364f084df7c92f`
- head branch: `probe/hermuz-layered-channel-law-20260822`
- head SHA: `2378f1bdfad2ba93dad09597950f1219ea6d819f`
- commits: 2
- changed_files: 0

Learning: PR metadata exposes a stable identity bridge into the Git object graph through base/head refs and SHAs.

## GT-013B — SHA → exact commit object

`fetch_commit(head_sha)` returned the exact commit object. The commit message is `probe: cleanup layered channel law marker` and the diff shows deletion of the diagnostic marker file.

Learning: SHA-bound commit retrieval can establish exact commit identity and its file-level diff without relying on PR metadata.

## GT-013C — Commit SHA → combined status surface

`get_commit_combined_status(head_sha)` returned an empty status list with no connector error.

Evidence classification:
`STATUS-SURFACE OBSERVATION`

Important boundary: empty status list means no statuses were returned by this status surface for the specified SHA. It does not prove that no CI execution occurred, because status and Actions run surfaces are distinct evidence layers.

## GT-013D — Base/head SHA → comparison

`compare_commits(base_sha, head_sha)` returned:
- status: `ahead`
- ahead_by: 2
- behind_by: 0
- total_commits: 2
- files: []

The empty `files` result is therefore scoped to this connector's comparison response and must not be interpreted as proof that the two commits contain no historical file changes; the exact head commit independently reports a deletion.

## Layer model learned

`PR identity → refs/SHAs → exact commit → status surface`

and independently:

`base/head SHAs → comparison surface`

These surfaces overlap in identity but are not interchangeable evidence sources.

## Knowledge Delta KD-006 — Empty comparison files vs exact commit diff

Classification: `NEW OBSERVATION` + `UNRESOLVED CONNECTOR SEMANTICS`

Observed: comparison returned `files: []`, while exact commit retrieval returned a concrete file deletion.

Learning: the connector's compare response must not be assumed to expose the same file-level semantics as exact commit diff retrieval. Before using compare `files` as evidence, ARGO must determine whether the field is intentionally summarized, filtered, or transformed.

Reusable rule: `Never substitute compare.files for exact commit evidence until compare-file semantics are independently validated.`

## Knowledge Delta KD-007 — Status absence is not execution absence

Classification: `NEW OBSERVATION`

Observed: combined commit status returned an empty status list.

Learning: status checks are a separate evidence surface from Actions workflow execution. Empty status output cannot settle an Actions execution question.

Reusable rule: `For execution claims, correlate status evidence with the appropriate Actions run/job evidence rather than treating an empty status surface as a universal negative.`

## Behavioral laws added

71. PR refs provide an identity bridge into the Git object graph.
72. Exact SHA retrieval is authoritative for the selected commit object.
73. Status and Actions execution are separate evidence surfaces.
74. Compare output has its own semantics and must be validated independently.
75. An empty comparison file list cannot override exact commit evidence without understanding connector transformation.
76. Cross-surface correlation must preserve the identity key (SHA/ref/object ID) used to join observations.

## Safety / P6 boundary

- No production ARGO file was mutated.
- No workflow was changed.
- No P6 execution claim was made.
- Existing PR #25 and its head commit were used only for read-only training.

## Next task

`GT-014 — Ref-bound file/blob retrieval and branch-vs-SHA identity training. Determine whether exact ref reads, branch reads, and blob reads expose distinct evidence semantics; record Knowledge Deltas before any return to P6.`
