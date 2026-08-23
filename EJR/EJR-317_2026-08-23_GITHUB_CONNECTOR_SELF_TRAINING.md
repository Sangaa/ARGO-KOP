# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before further P6 planning.

## Current completed training

The training record has now reached GT-007F. Training remains read-first and evidence-scoped.

### GT-007F — Git-object surfaces and PR head/base correlation
Operations: `fetch` (Git tree endpoint), `fetch_blob`, `compare_commits`
Targets: `Sangaa/ARGO-KOP`, base commit `8af28e47428f6550f92581f795428a433eb97be0`, PR #25 head `2378f1bdfad2ba93dad09597950f1219ea6d819f`.

Hypothesis: Git-object surfaces can establish repository structure, exact blob identity, and commit ancestry independently of Actions Run-ID discovery; PR head/base identity can then be correlated with this lineage.

Observed behavior:
- The Git tree endpoint for commit `8af28e47428f6550f92581f795428a433eb97be0` returned a recursive repository tree including workflow files and their blob SHAs. This demonstrates that the connector can expose Git tree/object identity through its approved fetch surface.
- `fetch_blob` successfully retrieved the exact blob content for `AI/README.md` using its SHA `e921632ae70806ce7ee1ef40bf2a5d25536a8d67`.
- `compare_commits` between base `8af28e47428f6550f92581f795428a433eb97be0` and PR #25 head `2378f1bdfad2ba93dad09597950f1219ea6d819f` returned `status=diverged`, `ahead_by=2`, `behind_by=34`, `total_commits=2`, `merge_base=942271c4830b059258e6f2fc1b364f084df7c92f`, and `files=[]`.

Interpretation:
1. Git tree and blob surfaces provide object-level evidence that is independent of PR review and Actions observation.
2. A known blob SHA can be used as an exact content identity, allowing content retrieval without path-based ambiguity.
3. Commit comparison can establish ancestry and divergence even when the returned file list is empty.
4. `status=diverged` with `ahead_by=2` and `behind_by=34` is materially different from a simple linear "PR is two commits ahead" interpretation. The comparison must retain both sides of the relation.
5. `files=[]` from this comparison is scoped to the returned comparison payload and must not be interpreted as proof that the two refs contain no differences.
6. PR head/base identity can therefore be correlated to commit lineage, but the comparison result must be interpreted using its status, ahead/behind counts, and merge base together.

Reuse rule:
`PR metadata → exact head/base SHA → compare refs → inspect merge-base/divergence → use tree/blob identity for exact object evidence → correlate with Actions evidence when available`.

Training classification: READ + GIT-OBJECT-LINEAGE + EVIDENCE-CLASSIFICATION.
Canonical mutation involved: NO.

## Behavioral laws added by GT-007F

21. Git tree, blob, and commit comparison are independent evidence surfaces from PR and Actions.
22. Blob SHA is an exact content identity and can be used for content verification independently of path discovery.
23. Commit comparison must preserve `status`, `ahead_by`, `behind_by`, and `merge_base`; a single count is insufficient to describe lineage.
24. Empty `files` in a comparison response is scoped to the connector response and is not proof of zero repository differences.
25. PR head/base correlation must be SHA-based before execution evidence is attached to a change lineage.

## P6 implication after GT-007F

The current evidence model is now broader:

`PR → head/base SHA → Git lineage → status/PR evidence → Actions evidence`

This does not remove the Actions Run-ID gap, but it prevents P6 from treating Run-ID discovery as the only available lineage evidence. The Actions run remains the authoritative execution layer when available; Git/PR evidence is corroborating lineage, not a substitute for execution proof.

## Next task

`GT-007G — Train branch/ref discovery and exact ref-to-commit resolution, then map the resulting evidence to the P6 branches already identified.`

Required order:
`Inventory → safe read-only training → evidence classification → update EJR → derive P6 evidence plan → smallest justified probe → document → close session.`

No P6 promotion is authorized by this record.

## Model handoff

Every future model/session must read GOV-017 and EJR-317 before connector-dependent work, reuse validated observations, and perform freshness checks only where needed.
