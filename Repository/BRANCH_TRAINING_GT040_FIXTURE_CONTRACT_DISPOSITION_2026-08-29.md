# Branch Disposition — training/GT-040-fixture-contract

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-115`

## Evidence

The branch contains three training/proposal records rather than a production promotion unit:

1. `GT-041_FIXTURE_CONTRACT_BOUNDARY` — `BRANCH-ISOLATED / INVESTIGATION`; explicitly says no production implementation change is authorized from the fixture-failure evidence alone.
2. `GT-042_DOCUMENT_OBJECT_BLOB_ARCHITECTURE_PLAN` — `TRAINING-RECORDED / POST-TRAINING PRIORITY`; proposes backend-independent Document Object/BLOB research and explicitly forbids repository-wide migration from the note.
3. `GT-050_TEST_ARCHITECTURE_P6_DOMAIN_SEPARATION_PROPOSAL` — `PROPOSAL RECORDED / IMPLEMENTATION DEFERRED`; proposes L0 shared capability, L1 integrity, L2 evidence/provenance, L3 P6 integration separation and explicitly does not authorize immediate test migration or production adapter changes.

Current main already contains later evidence relevant to these proposals: P6 canonical/layered/reconciliation/runtime-lineage regressions are present in the Full-Stack workflow, while KRS/compression assessments independently concluded that repository-wide compression/migration is not proven.

## Disposition

`HISTORICAL_TRAINING_AND_ARCHITECTURE_PROPOSAL_SURFACE / VALUABLE_CANDIDATE_LEARNING / NO_PRODUCTION_OR_MIGRATION_AUTHORITY / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

Specific lessons may be re-read and adopted through a fresh governed decision. The branch itself is not a current promotion unit.

## Learning retained

- Fixture drift must be separated from production-contract failure.
- Git Blob semantics are a backend reference model, not the ARGO domain model.
- Layered test architecture should separate shared capabilities, repository integrity, evidence/provenance and P6 integration.
- Attractive representation changes do not justify legacy migration without measured advantage and clean baseline evidence.

## Boundary

This classification preserves the training branch as evidence and closes only its branch-hygiene/wholesale-merge question. It does not claim every proposal has been fully implemented or invalidated.
