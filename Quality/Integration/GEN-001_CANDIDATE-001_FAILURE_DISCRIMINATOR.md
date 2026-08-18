# GEN-001 Candidate 001 — Minimal Failure Discriminator

Status: `VALIDATED_GENERATED_KNOWLEDGE / BOUNDED SCOPE`
Class: `VALIDATED_GENERATED_KNOWLEDGE`
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

### Case C — Prospective Controlled Test
A deterministic validator injected four bounded states: subject-only failure, channel-only failure, composite failure and no failure. The discriminator returned the corresponding classification for each case in CI.

Workflow: `GEN-001 Candidate Training`
Run: `32058801487`
Job: `95474138297`
Conclusion: `SUCCESS`

## Validation Result

`VALIDATED_GENERATED_KNOWLEDGE`

The candidate has passed bounded prospective validation as a failure-triage decision procedure.

## Limits

Validation is bounded to test-failure triage. It does not prove the heuristic is optimal in every production environment, nor does it grant permission to modify canonical behavior automatically.

## Reuse Value

Use as a default **triage heuristic** for material test failures when the failure layer is uncertain:

`Discriminate first → Mutate second`

Further domain-specific validation is required before broader governance promotion.

## Promotion Recommendation

Keep as `VALIDATED_GENERATED_KNOWLEDGE` until repeated use demonstrates stable benefit across additional failure classes. Do not promote automatically to an ARGO-Native Rule.

---

End of Candidate 001
