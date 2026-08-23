# EJR-324 — GitHub Actions GT-017 Artifact Evidence Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent: EJR-323

## Objective
Determine what GitHub Actions artifact metadata and downloaded artifact contents can prove, and what claims remain dependent on other evidence surfaces.

## Training run
Run: `32548603868`
Workflow: `Full-Stack Repository Audit`
Event: `pull_request`
Discovery key: PR head SHA `2378f1bdfad2ba93dad09597950f1219ea6d819f`
Execution identity SHA: `400a50414a31c0e8537a06f46ff4bf580945874c`

## GT-017A — Artifact metadata

The run exposes four artifacts:
- `ci-execution-identity` — id `9469322269`, digest `sha256:679632aa55f5628498898c2f62c35c47c043f90f8af070a0aef78cbfccdd711d`
- `ci-impact-correlation` — id `9469322132`, digest `sha256:f1b0398ea95a843089e0b2b3fe4d36d3b93d938f37b2ace9a2b8dcf67f961128`
- `runtime-evidence` — id `9469321973`, digest `sha256:94cc6871bf4a34d8c057d08ab875d26825e4d8ff5e3b8957b7a84c5fd9e80dea`
- `full-stack-audit-report` — id `9469321798`, digest `sha256:ba8f8a73e84967779a44f50ef887e029ebad9fe4d8a61f1fc62d85ec87d6e77f`

The metadata associates every artifact with workflow run `32548603868` and its PR head SHA `2378...`.

Evidence classification: `RUN-BOUND ARTIFACT METADATA`.

## GT-017B — Artifact content

Downloaded `ci-execution-identity.zip` and inspected its JSON content. It states:
- workflow: `Full-Stack Repository Audit`
- run_id: `32548603868`
- event: `pull_request`
- ref: `refs/pull/25/merge`
- github_sha: `400a50414a31c0e8537a06f46ff4bf580945874c`
- checkout_sha: `400a50414a31c0e8537a06f46ff4bf580945874c`
- before: `11cf36f121958d31cb212d138f91024d75e7ec41`

Evidence classification: `EXECUTION-IDENTITY PAYLOAD`.

## GT-017C — Independent artifact correlation

Artifact metadata and artifact content converge on the same run identity:

`artifact id 9469322269 → run 32548603868 → event/ref → execution SHA 400a...`

This is stronger than a filename-only observation because the artifact object itself is run-associated and the payload independently declares the execution identity.

## GT-017D — CI impact correlation artifact

Downloaded `ci-impact-correlation` and inspected its payload. It reports:
- base: `11cf36f121958d31cb212d138f91024d75e7ec41`
- head: `400a50414a31c0e8537a06f46ff4bf580945874c`
- changed_path_count: `1`
- mapped_path_count: `0`
- overall: `POLICY_UNRESOLVED`
- promotion: `NO_AUTO_PROMOTION`
- affected path: `EJR/PROBES/HERMUZ-LAYERED-CHANNEL-LAW-20260822.md`

Important: this artifact provides evidence of the CI impact-correlation calculation and its unresolved policy result. It does not by itself prove that P6 passed or that the changed path is eligible for promotion.

## Knowledge Delta KD-017 — Artifact metadata is run-bound evidence

Classification: `VERIFIED`

Artifact metadata exposes a direct association to the workflow run and PR head lineage.

Reusable rule:
`Treat artifact metadata as run-bound evidence only after verifying the run association; do not infer execution identity from artifact filename alone.`

## Knowledge Delta KD-018 — Artifact payload can independently assert execution identity

Classification: `VERIFIED`

The `ci-execution-identity` payload independently declares run_id, event, ref, github_sha, and checkout_sha. When correlated with artifact metadata and run metadata, it creates a multi-surface identity chain.

Reusable rule:
`Use artifact payload as a corroborating execution-identity source, not as a substitute for run metadata.`

## Knowledge Delta KD-019 — Artifact evidence has claim boundaries

Classification: `VERIFIED`

The CI impact artifact can prove what its correlation calculation reported (`POLICY_UNRESOLVED` / `NO_AUTO_PROMOTION`) but cannot upgrade that result into PASS. Artifact evidence must preserve the semantics and conclusion emitted by the producer.

Reusable rule:
`Evidence transport does not change evidence meaning.`

## Evidence graph learned

`Run ID`
`  ↓`
`Artifact metadata`
`  ↓`
`Artifact content`
`  ↓`
`Execution identity / correlation result`

This graph is a corroboration chain. It does not eliminate the need for direct run/job evidence when the target claim concerns workflow execution state.

## P6 consequence

Artifacts materially improve the evidence chain, but P6 remains `IMPLEMENTED / EXECUTION EVIDENCE PENDING` until the canonical P6 contract is satisfied by the correct execution identity and all required gates. In particular, the observed CI impact artifact explicitly reports `POLICY_UNRESOLVED` and `NO_AUTO_PROMOTION`; this is evidence against automatic promotion, not evidence of P6 PASS.

## Safety

- Read-only training against existing run/artifacts.
- No workflow mutation.
- No dispatch.
- No rerun.
- No production logic mutation.

## Next task

`GT-018 — Evidence hierarchy and cross-surface contradiction testing.`

Use existing evidence only to test what ARGO should do when run metadata, artifact metadata, artifact payload, status surfaces, and repository state appear incomplete or semantically different. Record precedence rules and contradiction handling before any P6 decision.

Session rule: Execute → document → read-back → verify → close.
