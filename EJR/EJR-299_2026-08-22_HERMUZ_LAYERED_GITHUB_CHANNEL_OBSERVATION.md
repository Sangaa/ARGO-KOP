# EJR-299 — HERMUZ Layered GitHub Channel Observation Experiment

## Classification
Diagnostic learning record. No production semantic promotion.

## Objective
Test GitHub connectivity and observation boundaries using a fresh isolated experiment, then search blindly for effects across repository surfaces. The experiment was designed to reduce contamination from historical probes and to locate secondary effects by layer.

## Experimental design
A fresh branch was created from `main` at baseline `942271c4830b059258e6f2fc1b364f084df7c92f`.

Layers:
1. Connectivity/read — read a known canonical repository file.
2. Write — create one unique marker file on the isolated branch.
3. Direct observation — read the exact marker from the exact branch/ref.
4. Blind repository search — search the unique marker and distinctive terms without supplying the branch/ref.
5. Change observation — inspect the resulting commit and its changed-file evidence.
6. PR observation — open a non-draft PR and observe PR/head SHA/diff metadata.
7. Execution observation — attempt workflow/run discovery for the exact head SHA through the exposed connector surface.
8. Secondary-effect analysis — compare which surfaces changed and trace each to the operation that caused it.
9. Cleanup — delete the marker, close the PR without merge, and reset the probe branch to the original main SHA.

## Observed facts
- Write succeeded and produced commit `11cf36f121958d31cb212d138f91024d75e7ec41`.
- Direct read from the probe branch succeeded and returned the marker/blob SHA `7bb5ff0c36400b911ad1b77b52919ea02a6aaae9`.
- Blind repository search for the exact marker returned no results.
- Blind repository search for the distinctive experiment phrase also returned no results.
- Direct commit observation succeeded and exposed commit identity, parent, tree, changed file, blob, and patch.
- PR #25 was created successfully with one changed file and head SHA `11cf36f121958d31cb212d138f91024d75e7ec41`.
- Workflow discovery through the available commit/run helper did not yield a run for the head SHA.
- Direct attempts to access unlisted Actions/status API endpoints through the generic fetch surface were rejected as unsupported endpoints. This is evidence about connector exposure, not evidence that GitHub execution did not occur.
- The marker was deleted, PR #25 was closed without merge, and the probe branch was force-reset to the original `main` SHA.

## Causal interpretation
The experiment demonstrates that one repository mutation can produce observable effects across distinct surfaces: object/file state, commit identity, PR state, and potentially execution state. These surfaces are not equivalent observation channels.

A negative blind search cannot be promoted to object absence when direct authoritative observation proves the object exists under a specific ref. Likewise, inability to discover a workflow run through the exposed connector does not prove that no workflow execution occurred.

The experiment also validates the new side-effect rule: every newly observed effect must be traced back to the operation that produced it. An unexpected effect is first evidence of an incomplete process/model description, not a "random side effect" to be ignored.

## Learning
The correct unit of investigation is not only `operation -> intended result`; it is:

`operation -> causal chain -> observable surfaces -> secondary effects -> explanation of each transition`.

Future probes must be layered before execution so that any newly observed effect can be localized to the layer that produced it.

## P6 impact
No P6 logic, relationship status, runtime authority, or production evidence was promoted by this experiment.

## Closure
Status: CLOSED — DIAGNOSTIC LEARNING CAPTURED.
Production impact: NONE.
Main branch content: untouched by the probe.
Probe branch: reset to baseline SHA after cleanup.
PR #25: closed, not merged.
