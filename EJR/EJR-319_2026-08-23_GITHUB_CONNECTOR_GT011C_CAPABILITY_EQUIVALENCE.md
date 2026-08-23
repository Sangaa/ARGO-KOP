# EJR-319 — GitHub Connector Self-Training: GT-011C Capability Equivalence & Boundaries

Date: 2026-08-23
Protocol: GOV-017
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first, not P6-first

## Objective

Determine whether operations that appear equivalent actually produce equivalent evidence, and record boundaries between metadata retrieval, change evidence, collaboration evidence, and execution observation. The probes were selected to expand general GitHub Connector knowledge, not to solve P6.

## Probe GT-011C-01 — PR metadata vs full PR retrieval

Operations:
- `get_pr_info`
- `fetch_pr`

Target: `Sangaa/ARGO-KOP` PR #25.

Observed:
- Both operations resolved the same PR identity and refs.
- `get_pr_info` explicitly reports metadata only and does not include actual code changes.
- `fetch_pr` returns a normalized full PR snapshot and exposes the diff/comments fields; for PR #25 those fields were empty.
- PR #25 is closed and unmerged, with base `main`, head `probe/hermuz-layered-channel-law-20260822`, and two commits.

Learning:
1. Similar retrieval targets do not imply identical evidence surfaces.
2. Metadata is not a substitute for change content.
3. An empty diff from a full PR retrieval must be interpreted together with changed-file evidence; it is not proof that the PR mechanism is broken.
4. Tool documentation/contract is part of capability semantics.

## Probe GT-011C-02 — Changed-file enumeration before per-file patch retrieval

Operation:
`list_pr_changed_filenames`

Target: PR #25.

Observed:
- The connector returned an empty filename list.
- This is consistent with the full PR snapshot reporting `changed_files=0`, `additions=0`, and `deletions=0`.
- No per-file patch retrieval was attempted because the connector contract requires an exact returned path before `fetch_pr_file_patch`.

Learning:
1. Some operations are intentionally staged: enumerate first, retrieve exact child resource second.
2. Empty enumeration can be a valid state and should stop dependent child probes rather than trigger guessed paths.
3. A connector that requires validated identifiers reduces false-positive probing.

## Probe GT-011C-03 — PR discussion vs reactions

Operations:
- `fetch_pr_comments`
- `get_pr_reactions`

Target: PR #25.

Observed:
- PR comments returned an empty list.
- PR reactions returned an empty list.

Learning:
1. Comments and reactions are independent collaboration surfaces.
2. Empty collaboration collections are successful observations of those surfaces only.
3. Absence of comments/reactions says nothing about CI execution.

## Capability equivalence matrix

| Apparent equivalence | Actual distinction | Evidence class |
|---|---|---|
| `get_pr_info` vs `fetch_pr` | metadata-only vs richer normalized PR/change/discussion surface | PR metadata vs change/discussion |
| `fetch_pr` vs `list_pr_changed_filenames` | full normalized PR snapshot vs explicit changed-path enumeration | change scope |
| changed filenames vs per-file patch | collection/discovery vs exact child-resource retrieval | change content |
| PR comments vs PR reactions | discussion text vs reaction state | collaboration |
| commit status vs Actions run | status/check surface vs execution-run identity/details | CI/status vs execution |
| run discovery vs run jobs | finding a run ID vs inspecting a known run | CI discovery vs CI inspection |
| repository search vs exact repository retrieval | candidate discovery vs canonical identity | discovery vs identity |

## Boundary laws learned

1. **Metadata is not content.**
2. **Collection discovery is not child-resource retrieval.**
3. **Successful empty collection is evidence of an empty observed surface, not evidence of global absence.**
4. **A downstream operation that requires an exact ID/path cannot safely become an upstream discovery mechanism.**
5. **Different evidence classes must remain separate even when they concern the same GitHub object.**
6. **A connector wrapper can intentionally expose a narrower or normalized contract than the provider API.**
7. **Tool documentation and parameter contracts must be inspected before interpreting a result.**
8. **Control probes using unrelated IDs are useful only for classifying boundary behavior and must never be attributed to the target resource.**
9. **No guessed path, ID, branch, or run identifier is permitted when the next operation requires an exact identifier.**
10. **Capability equivalence must be demonstrated, not inferred from naming similarity.**

## P6 independence check

These probes were intentionally selected from PR and collaboration surfaces rather than Actions because the purpose was to test capability equivalence generally. The results are reusable knowledge for future problem mapping but do not change P6 status.

## Current training state

GT-011C-01 — COMPLETED
GT-011C-02 — COMPLETED
GT-011C-03 — COMPLETED

Capability-first GitHub training — IN PROGRESS
P6-specific selection criterion — OFF
P6 promotion — NONE
Production logic mutation — NONE

## Next task

`GT-012 — General read/write boundary and mutation-safety training.`

Focus:
- distinguish read capability from mutation capability;
- map write preconditions and identity requirements;
- use an isolated disposable artifact if a mutation probe is required;
- verify read-back and final state after every mutation;
- record mutation behavior without modifying production logic.

Session rule: Execute → document → read-back → verify → close.
