# EJR-274 — GT-067 Fixture Repair and Execution Boundary

**Date:** 2026-08-25
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Scope:** Evidence reasoning integration-test fixtures
**Mutation class:** Test-fixture-only

## Prior-learning gate

Before mutation, the current canonical GOV-013 protocol, current `PROJECT_BOOTSTRAP.md`, the current test file, and prior validator-repair learning in EJR-280 were inspected.

Relevant reusable learning from EJR-280: repair the narrow validation/fixture boundary rather than weakening the governed semantic contract; preserve the core safety assertions and avoid broad rewrites. 

## Pre-mutation findings

The current `EvidenceObservation` contract defines `semantic_status` once, with default `OBSERVED`. The affected execution-occurrence fixtures previously placed `semantic_status="VERIFIED_OCCURRENCE"` in the shared `common` mapping and then supplied an explicit `semantic_status="VERIFIED_CAPABILITY"` for the capability observation. This causes Python constructor failure before the semantic assertion executes.

The defect is therefore confined to fixture construction.

## Mutation performed

Updated only:

`Quality/Integration/test_evidence_reasoning_classification.py`

The repair removes `semantic_status` from the shared `common` mapping in the four affected execution-occurrence tests and supplies exactly one explicit semantic status to each constructed observation:

- capability → `VERIFIED_CAPABILITY`
- occurrence → `VERIFIED_OCCURRENCE`

No production function, dataclass field, provenance rule, or classification semantics were changed.

## Verification after mutation

Post-write read-back confirms the affected fixtures now pass `semantic_status` exactly once and retain their intended execution identity / target-commit bindings.

New commit:
`6557eb73880a85408c468e092e04e794ba769852`

New file blob SHA:
`8b0efbbd83f9f0ad4d87b0a76779b34e5162e357`

The available GitHub Actions connector reports no workflow runs and no combined status entries for the new commit. This is an execution-evidence boundary, not evidence of test failure.

## Current verdict

**GT-067 = FIXTURE ROOT CAUSE VERIFIED / MINIMAL FIX APPLIED / EXECUTION PENDING**

The fixture construction defect is resolved at source. The semantic result of the focused test set remains unverified until an authoritative runtime execution is available.

## Integrity boundary

Do not mark the focused tests as passing based on static inspection alone.

Do not promote the production semantic model based on the repaired fixture state.

Do not classify the absence of current workflow runs as CI failure.

## Next safe action

Obtain authoritative execution of the focused test file on commit `6557eb73880a85408c468e092e04e794ba769852`, then inspect run identity, checkout SHA, job result and test output. If execution is unavailable through the connector, record the capability boundary and do not infer the test result.
