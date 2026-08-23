# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before further P6 planning.

## Current completed training

The training record has now reached GT-007D. Training remains read-first and evidence-scoped.

### GT-007D — Pull Request metadata vs change evidence
Operations: `fetch_pr`, `get_pr_diff`, `fetch_pr_patch`
Target: `Sangaa/ARGO-KOP#25`

Hypothesis: PR metadata, PR diff, and PR patch are separate evidence surfaces and should not be treated as interchangeable.

Observed behavior:
- `fetch_pr` returned authoritative PR metadata: PR #25 is closed, not merged, base `main`, head `probe/hermuz-layered-channel-law-20260822`, head SHA `2378f1bdfad2ba93dad09597950f1219ea6d819f`, with `commits=2`, `changed_files=0`, and `additions/deletions=0`.
- `get_pr_diff` returned an empty diff.
- `fetch_pr_patch` returned an empty patch list.

Interpretation:
1. PR metadata can exist even when no code-change payload is returned by diff/patch surfaces.
2. `commits=2` must not be interpreted as `changed_files>0`.
3. Empty diff/patch is evidence about the PR change surface returned by these operations; it is not evidence that the PR never existed or that no execution occurred.
4. For lineage work, use `fetch_pr` first to bind base/head identity, then use diff/patch only when actual change evidence is required.

Reuse rule:
`PR metadata → bind head/base/merge state → inspect change surface → correlate commit/evidence channels`.

Training classification: READ + PR-LINEAGE + EVIDENCE-CLASSIFICATION.
Canonical mutation involved: NO.

## Behavioral laws added by GT-007D

14. PR metadata and PR change payloads are separate evidence surfaces.
15. A PR can report commits while exposing zero changed files and an empty diff/patch; do not infer code change from commit count alone.
16. Empty PR diff/patch must remain scoped to that PR-change surface and must not be promoted to execution absence.

## Next task

`GT-007E — Train PR discussion/review surfaces and correlate review evidence with commit lineage.`

Required order:
`Inventory → safe read-only training → evidence classification → update EJR → derive P6 evidence plan → smallest justified probe → document → close session.`

No P6 promotion is authorized by this record.

## Model handoff

Every future model/session must read GOV-017 and EJR-317 before connector-dependent work, reuse validated observations, and perform freshness checks only where needed.
