# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before further P6 planning.

## Current completed training

The training record has now reached GT-007G. Training remains read-first and evidence-scoped.

### GT-007G — Branch/ref discovery and exact ref-to-commit resolution
Operations: `search_branches`, `fetch_file(ref=...)`
Target: `Sangaa/ARGO-KOP`

Hypothesis: branch discovery and exact ref reads can establish the identity of P6-related branches and bind a symbolic branch name to the exact repository content currently reachable through that ref.

Observed behavior:
- `search_branches(query="p6")` returned seven P6-related branches, including `fix/p6-head-binding-20260819`, `fix/p6-actions-pr-trigger-20260819`, `fix/p6-pr-trigger-main-20260819`, three `revalidate/p4-p6-execution-boundary...` variants, and `revalidate/p6-execution-evidence-20260819`.
- A direct REST-style `fetch` attempt against `/branches/{branch}` was rejected by the connector as an unapproved public GitHub endpoint. This is a connector-surface restriction, not evidence that the branch does not exist.
- The dedicated `fetch_file` surface accepted `ref="fix/p6-head-binding-20260819"` and returned `PROJECT_STATUS.md` from that branch, with blob SHA `69394d0140af7d27aee5e42caeec9172c88ece50`.
- The branch's `PROJECT_STATUS.md` explicitly states that `Sangaa/ARGO-KOP` on `main` is the primary repository source of truth, while the branch is a historical/development ref. Therefore branch-local evidence must not silently override the main authority boundary.

Interpretation:
1. Branch discovery is a distinct capability and can surface multiple historical/revalidation lines that would be missed by looking only at main.
2. Symbolic ref resolution is reliable through the dedicated file-read surface when a known file is selected, but the generic REST fetch surface has narrower endpoint allowlisting.
3. Branch existence and branch content are separate evidence facts; discovering a branch does not establish its current commit identity unless a ref-to-content operation resolves it.
4. A branch-local status document may itself declare `main` as the authority source; therefore reading a branch is not equivalent to promoting that branch as canonical.
5. The connector's endpoint restriction must be classified as a surface limitation, not as a GitHub repository absence.

Reuse rule:
`Discover refs → select exact ref → read a known repository artifact at that ref → record content SHA/authority claims → compare to main or other lineage only when needed`.

Training classification: READ + BRANCH/REF-DISCOVERY + AUTHORITY-CLASSIFICATION + ERROR-CLASSIFICATION.
Canonical mutation involved: NO.

## Behavioral laws added by GT-007G

42. Branch discovery and branch content resolution are separate evidence operations.
43. A discovered branch is not execution evidence and is not automatically canonical authority.
44. Generic fetch endpoint rejection must be classified as connector allowlisting behavior when the dedicated operation succeeds.
45. A branch-local artifact may explicitly defer authority to `main`; authority claims must therefore be read, not inferred from the ref being queried.
46. Ref identity should be bound to exact content evidence before using a branch in lineage analysis.

## P6 implication after GT-007G

The P6 evidence model now includes a ref layer:

`P6 branch discovery → exact ref/content evidence → PR/commit lineage → Actions execution evidence`

This improves pre-Run-ID lineage and prevents the investigation from confusing historical P6 branches with the current canonical `main` baseline. It does not prove Actions execution and does not close the Run-ID discovery gap.

## Next task

`GT-007H — Train Actions read-only surfaces using any already-known real workflow-run/job identifiers; if no real identifier is available, inventory and classify the exposed Actions operations without fabricating IDs.`

Required order:
`Inventory → safe read-only training → evidence classification → update EJR → derive P6 evidence plan → smallest justified probe → document → close session.`

No P6 promotion is authorized by this record.

## Model handoff

Every future model/session must read GOV-017 and EJR-317 before connector-dependent work, reuse validated observations, and perform freshness checks only where needed.
