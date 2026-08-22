# EJR-295 — HERMUZ Actions Identity Discovery Experiment

Date: 2026-08-22
Status: CLOSED / DIAGNOSTIC LEARNING CAPTURED
Classification: Architectural Learning / Connector Capability Boundary
Production impact: NONE

## Purpose

Test the hypothesis that the previously exercised GitHub Actions observation frame was narrower than the actual environment, and distinguish workflow execution from the ability to discover its run identity.

## Prior-learning gate

Before experimentation, prior evidence was reviewed:
- EJR-279: prior Actions evidence boundary.
- EJR-293: mandatory prior-learning retrieval gate.
- EJR-294: blind Actions boundary expansion; exact-ID run/job/log observation was proven on a public control repository.

## Controlled experiment

A real changed-file PR probe was created on an isolated branch. PR #22 was initially draft, then a real marker file was added, the PR was transitioned to ready-for-review, and the resulting head SHA was tested through the connector's workflow-run and status observation surfaces.

Observed:
- PR became ready-for-review successfully.
- Head SHA: b4ede2a2a2ec5857aa45bc01e18981cb4a00a820.
- `fetch_commit_workflow_runs` returned an empty workflow-run list.
- `get_commit_combined_status` returned an empty status list.
- The marker was read back successfully before cleanup.
- PR #22 was closed without merge.
- Probe marker was deleted from the isolated branch.

## Failed hypothesis

Hypothesis: draft-state or pull-request state might explain the missing Actions observation.

Result: not supported by this probe. The PR was a real changed-file PR and was transitioned to ready-for-review, yet the same connector surfaces still returned no run/status evidence.

## Revised model

The experiment does NOT prove that GitHub Actions did not execute.

It establishes only:

`READY_FOR_REVIEW + CHANGED_FILE + CONNECTOR QUERY -> NO OBSERVED RUN/STATUS`

Therefore:

`NO OBSERVED RUN != NO RUN EXISTS`

and the unresolved problem remains specifically **run identity discovery / observation**, not demonstrated workflow absence.

## Learning

The environment must be modeled as separate layers:

1. world capability;
2. connector exposure;
3. invocation capability;
4. execution occurrence;
5. run identity discovery;
6. downstream observation by exact identifier;
7. authoritative world-state conclusion.

A failure at layer 5 must not be promoted to a conclusion about layer 4.

## P6 impact

No P6 logic, relationship, Runtime evidence, or governance state was promoted. P6 remains execution-verification-pending.

## Reusable experiment pattern

`Prior Learning -> State Hypothesis -> Controlled Probe -> Exact Identifier Capture -> Downstream Observation -> Falsify/Refine -> Cleanup -> Record Learning`

## Closure

Experiment closed after read-back and cleanup. No production logic was changed and the probe PR was not merged.

End of EJR-295
