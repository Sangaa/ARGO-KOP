# GT-041 — Fixture Contract Boundary

## Status
BRANCH-ISOLATED / INVESTIGATION

## Scope
Training-only investigation of the integration-test failures reproduced in the ARGO Runtime Prototype and Integration Tests workflow.

## Evidence
- Original failing job: `97395585982`
- Rerun job: `97405504648`
- Both reproduced the same 9-test failure family.
- Failure signatures include duplicate keyword arguments for `semantic_status` and `evidence_independence`, plus missing required `evidence_layer`.
- `EvidenceObservation` defines `evidence_layer` and `evidence_independence` as required fields and `semantic_status` as a defaulted field.

## Boundary Decision
No production implementation change is authorized from this evidence alone. The suspected drift is in test-fixture construction and must be separated from production-contract behavior.

## Isolation
Branch: `training/GT-040-fixture-contract`
Base: `main`

## Next Safe Step
Inventory every affected constructor call, classify each as duplicate-field, missing-required-field, or legitimate semantic override, then apply the smallest fixture-only correction and compare CI results against the baseline.

## Rule
A rerun is not a fix. A reduced failure set after a controlled fixture mutation is causal evidence only when the same test surface and failure signatures are compared.
