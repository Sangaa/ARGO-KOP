# EJR-141 — Connected Spine Reasoning Packet Repair

Date: 2026-08-12

## Trigger

CI Run #86 failed 17 integration tests while 50 passed. The dominant symptom was an early `HOLD` path: downstream tests received no `execution` or `outcome`, and evidence capture consequently returned `HOLD`.

## Root Cause

`Cognition/reasoning_packet_classifier.py` requires a packet shaped as:

- `context`
- `knowledge`

`Runtime/Execution/connected_spine_runner.py` previously flattened the fixture context and knowledge into one dictionary before calling `classify()`. The classifier therefore returned `REASONING_PACKET_INCOMPLETE` before the real spine could reach decision, execution, outcome, and evidence seams.

## Repair

The runner now passes an explicit reasoning packet:

`{"context": fixture["context"], "knowledge": fixture["knowledge"]}`

Conflict detection continues to receive the original governed context directly, preserving the intended boundary between the classifier envelope and cognition-state analysis.

## Expected Effect

This should unblock the downstream execution/outcome/evidence integration tests that were failing as a consequence of the premature classifier hold.

## Verification Status

Repair committed as `a7484e02a8a5a9f6aeb54cab6c133512022525e2`.

CI certification is intentionally not claimed until the workflow runs against this commit.

## Next Step

Inspect CI results. If the failure cluster moves downstream, use that new failure boundary as the next construction priority rather than masking it.
