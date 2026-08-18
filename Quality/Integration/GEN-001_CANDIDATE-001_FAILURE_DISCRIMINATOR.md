# GEN-001 Candidate 001 — Minimal Failure Discriminator

Status: `VALIDATION COMPLETE / GENERATED KNOWLEDGE CANDIDATE`
Class: `GENERATED_HYPOTHESIS`
Not an ARGO-Native Rule.

## Generated Hypothesis

**When a material test fails unexpectedly, the first corrective action should be the smallest discriminator experiment that separates a defect in the subject under test from a defect in the test/execution channel. Only then should the subject or test channel be modified.**

## Why This Candidate Is Not Merely Inherited

The inherited knowledge separately states that bad idea, implementation, test and execution-channel failures must be distinguished. The new candidate adds an operational decision heuristic: **use the smallest information-separating experiment before changing either side**.

## Derivation

`Failure classification requirement`
+
`Observed M3 logic PASS + CI FAIL`
+
`Observed multi-Matrix workflow with zero Jobs`
+
`Need to avoid changing correct system logic because of channel evidence`
+
`→ Minimal discriminator before corrective mutation`

## Novelty Check

Repository search was performed for the exact operational principle and for equivalent wording. No canonical rule with this specific "minimal discriminator" decision procedure was identified in the inspected scope.

## Validation Cases

### Case A — M3
The reconciliation harness printed `PASS`, while the CI step failed because `pytest` was undeclared. The smallest discriminator was inspecting the failing CI step/log before modifying reconciliation logic. Root cause: test-channel dependency.

### Case B — Multi-Matrix
The proposed three-Matrix run returned `jobs=[]`, so no test job executed. The smallest discriminator was checking workflow/job state before modifying Matrix semantics. Root cause: workflow execution/loading boundary, not Matrix evaluation.

Both cases support the candidate's predicted behavior: distinguish the layer before mutating the subject.

## Validation Result

`RETROSPECTIVELY SUPPORTED`

## Limits

Retrospective support is not sufficient for ARGO-Native promotion. A prospective controlled experiment must demonstrate that the discriminator selects the correct failure layer for injected subject faults and injected channel faults.

## Promotion Recommendation

Remain `GENERATED_HYPOTHESIS` until prospective validation and reuse are demonstrated.

---

End of Candidate 001
