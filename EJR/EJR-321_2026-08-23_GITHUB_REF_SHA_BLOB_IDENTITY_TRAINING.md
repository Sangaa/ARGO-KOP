# EJR-321 — GitHub Ref / SHA / Blob Identity Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent: EJR-320

## Objective

Train ARGO to distinguish current branch/ref state, historical SHA-bound state, and exact blob identity. This cycle also tests what can and cannot be inferred when a historical path no longer exists at a selected ref.

No production mutation was performed.

## GT-014A — Current branch/ref read

Operation:
`fetch_file(path=Governance/CELM-001_CONNECTOR_ENVIRONMENTAL_LEARNING_MODEL.md, ref=main)`

Observed:
- file resolves on `main`;
- blob SHA: `4fa403d8d9f8d75b1626fe57939d703d5b76ce28`;
- current content includes Operational Learning / Knowledge Delta and GitHub connector training rules.

Evidence class:
`CURRENT-REF FILE STATE`

## GT-014B — Historical SHA-bound read

Operation:
`fetch_file(path=Governance/CELM-001_CONNECTOR_ENVIRONMENTAL_LEARNING_MODEL.md, ref=2378f1bdfad2ba93dad09597950f1219ea6d819f)`

Observed:
`404 Not Found`.

This is consistent with the historical commit metadata: commit `2378f1bdfad2ba93dad09597950f1219ea6d819f` predates CELM-001 and records deletion of a different diagnostic file.

Evidence classification:
`HISTORICAL-REF ABSENCE`

Important boundary: this does not mean CELM-001 is absent from the repository today. It means the selected path cannot be resolved at that historical SHA through this connector surface.

## GT-014C — Historical diagnostic path

The exact diagnostic path from commit `2378f1bdfad2ba93dad09597950f1219ea6d819f` was queried at the PR base SHA and at the historical branch ref.

Both direct path reads returned 404.

The commit object itself independently records that the path was deleted in that commit.

Learning:
A path may be visible in a commit's diff as a historical change object while not being directly retrievable from a later branch/ref after deletion or branch removal. Exact commit evidence can therefore outlive direct ref-based path resolution.

## GT-014D — Ref versus SHA equivalence test

Operation:
`fetch_file(path=EJR/EJR-319_2026-08-23_GITHUB_CONNECTOR_GT011C_CAPABILITY_EQUIVALENCE.md, ref=main)`

and the same path at commit:
`1b783254889d01f57193f7fc991ac4307d5ff9fc`

Observed:
- both reads returned identical content;
- both reported blob SHA `35582f564a234bf1514fcba338dc5d687f5ea1b0`.

Evidence classification:
`REF/SHA CONTENT EQUIVALENCE FOR THIS OBJECT`

Learning:
When a branch/ref currently resolves to a commit containing an unchanged blob, branch-bound and SHA-bound retrieval can produce the same exact blob identity. This must be verified, not assumed.

## GT-014E — Blob identity retrieval

Operation:
`fetch_blob(blob_sha=4fa403d8d9f8d75b1626fe57939d703d5b76ce28)`

Observed:
The connector returned the exact CELM-001 content for the specified blob SHA.

Evidence classification:
`CONTENT-ADDRESSABLE OBJECT EVIDENCE`

Learning:
Blob retrieval is independent of branch naming. It establishes content identity by blob SHA once the blob identifier is known.

## Knowledge Delta KD-008 — Ref state is time-dependent

Classification: `NEW OBSERVATION`

Observed:
The same repository can yield successful file retrieval on `main` while the same path returns 404 at an older SHA.

Reusable rule:
`Never use current-ref success to infer historical-ref existence, and never use historical-ref absence to infer current repository absence.`

## Knowledge Delta KD-009 — Commit evidence can outlive direct path retrieval

Classification: `NEW OBSERVATION`

Observed:
The diagnostic path is absent through direct ref reads, while the exact commit object retains the deletion evidence.

Reusable rule:
`When a ref-bound path disappears, use exact commit/diff evidence to establish historical change rather than guessing another ref.`

## Knowledge Delta KD-010 — Blob identity is stronger than path identity for exact content

Classification: `NEW OBSERVATION`

Observed:
The same content returned from `main` and a historical commit shared the same blob SHA, and direct blob retrieval reproduced that content.

Reusable rule:
`For exact content identity, correlate path/ref observations to blob SHA; do not treat a path alone as immutable identity.`

## Behavioral laws added

77. A branch/ref is a moving or historical name; it is not itself immutable content identity.
78. A commit SHA identifies a historical Git object and provides a stable correlation key for that object.
79. A blob SHA identifies content independently of branch naming.
80. Ref-bound path absence is scoped to that ref and time point.
81. Historical diff evidence can remain available even when direct path retrieval no longer resolves.
82. Ref/SHA equivalence must be verified by content/blob identity when used as evidence.
83. Exact content claims should prefer blob identity when the blob SHA is known.

## P6 boundary

This training does not alter P6 status and does not establish Actions execution evidence.

The result strengthens the future P6 correlation model by separating:

`workflow/run identity → commit SHA → ref state → file/blob content`

from:

`status surface → execution evidence`

No mutation, workflow change, or P6 promotion was performed.

## Next task

`GT-015 — Connector capability inventory and Actions-specific surface mapping.`

Focus:
- enumerate the currently exposed GitHub Actions operations;
- inspect each operation's contract and dependency order;
- distinguish run discovery from run inspection;
- determine which known provider capabilities are implemented but not session-exposed;
- build the Actions capability map before any P6 execution probe.
