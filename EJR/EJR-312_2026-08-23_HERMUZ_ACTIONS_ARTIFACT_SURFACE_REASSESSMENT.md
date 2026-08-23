# EJR-312 — HERMUZ Actions Artifact Surface Reassessment

Date: 2026-08-23
Status: CLOSED / REUSABLE-LEARNING CAPTURED
Classification: Connector Capability Discovery / P6 Evidence
Production impact: NONE

## 1. Trigger

During continuation of the P6 build, the previously preserved future pattern `Artifact-First Evidence Recovery` was rechecked against the currently exposed GitHub connector surface before authorizing any new repository mutation.

## 2. Finding

The GitHub connector already exposes two relevant Actions artifact operations:

- `fetch_workflow_run_artifacts(repo_full_name, run_id, name=None)`
- `download_workflow_artifact(repo_full_name, artifact_id, file_name=None)`

Therefore artifact observation is not merely a future connector-design idea. The capability is already exposed at the connector layer.

## 3. Critical Boundary

The artifact surface still requires a real `run_id` first.

Therefore:

`Artifact Observation Available ≠ Run Discovery Available`

and:

`Artifact Capability ≠ Current-HEAD Execution Evidence`

The discovery gap remains upstream of artifact retrieval.

## 4. Architectural Consequence

No new artifact connector implementation is justified in this cycle.

The correct chain is now:

```text
Run-ID Discovery
      ↓
fetch_workflow_run_artifacts
      ↓
artifact identity
      ↓
download_workflow_artifact
      ↓
execution evidence
      ↓
provenance validation
      ↓
P6 judgment
```

This is preferable to repository self-commit evidence because artifacts do not require mutation of the source branch and do not alter the SHA being evaluated.

## 5. Relation to EJR-311

EJR-311 classified Artifact-First Evidence Recovery as a future candidate. This reassessment refines that classification:

`FUTURE ARCHITECTURAL PATTERN → CONNECTOR CAPABILITY ALREADY PRESENT`

The remaining unknown is operational access to a real run ID, not artifact API design.

## 6. Decision

- Do not add duplicate artifact operations.
- Do not modify the canonical workflow merely to create repository evidence.
- Preserve artifact retrieval as a preferred downstream evidence path.
- Continue investigation at the Run-ID discovery / Actions invocation boundary.

## 7. Non-Claims

This record does not establish:

- that a current `main` run has been discovered;
- that artifact retrieval has been exercised against a live current run;
- that artifact contents are sufficient by themselves for P6 promotion;
- that current Actions permissions permit all operations.

## 8. Learning

A connector audit must inspect the complete exposed capability surface before implementing a capability that was only assumed to be missing.

`KNOWN CAPABILITY ≠ VERIFIED LIVE EXECUTION`

`DOWNSTREAM OBSERVATION ≠ UPSTREAM DISCOVERY`

## 9. Closure

`CLOSED — CAPABILITY REASSESSED — NO REDUNDANT MUTATION — NEXT GAP REMAINS RUN-ID DISCOVERY / INVOCATION`

End of EJR-312
