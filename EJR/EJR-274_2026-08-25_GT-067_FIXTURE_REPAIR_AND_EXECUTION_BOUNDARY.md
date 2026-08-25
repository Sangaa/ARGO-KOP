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

Post-write read-back confirmed the affected fixtures pass `semantic_status` exactly once and retain their intended execution identity / target-commit bindings.

Repair commit:
`6557eb73880a85408c468e092e04e794ba769852`

## New execution evidence review

A subsequent repository-wide `Full-Stack Repository Audit` run on `main` completed successfully at run `32806800284`. Its job passed the repository audit gates, including the GT-018 evidence reasoning classification step.

However, the job log shows that the GT-018 command was:

`python -m unittest Quality/Integration/test_evidence_reasoning_classification.py -v`

and reported:

`Ran 0 tests in 0.000s`
`OK`

Therefore this is **not** authoritative evidence that the repaired GT-067 test cases passed. It is evidence that the workflow command itself exited successfully while executing zero discovered tests in that invocation.

The same run also produced successful P6 boundary regressions and a repository-wide audit, but those results must not be substituted for the focused GT-067 execution result.

The workflow configuration for `runtime-prototype-tests.yml` separately defines integration execution using `pytest -q Quality/Integration`, and is triggered by `workflow_dispatch`, relevant path pushes, and relevant pull requests. This establishes a distinct authoritative execution channel that must be checked for the repaired commit rather than inferred from the full-stack audit result.

## Reconciliation result

Current evidence supports:

`fixture defect → root cause verified → minimal fixture repair applied → repository read-back verified`

It does **not** yet support:

`repaired fixture → focused tests executed → semantic assertions passed`

The distinction is deliberate. A green workflow containing a zero-test invocation is not a passing test result.

## Current verdict

**GT-067 = FIXTURE ROOT CAUSE VERIFIED / MINIMAL FIX APPLIED / EXECUTION NOT YET PROVEN**

## Integrity boundary

Do not mark the focused tests as passing based on the full-stack audit's `OK` result.

Do not classify `Ran 0 tests` as a semantic pass.

Do not classify absence of a run returned by a connector's SHA-filtered surface as CI failure.

Do not promote the production semantic model based on fixture repair alone.

## Next safe action

Locate the authoritative `runtime-prototype-tests` execution for repair commit `6557eb73880a85408c468e092e04e794ba769852` (or a later execution whose checkout SHA is explicitly proven to contain that repair), then verify:

1. run identity;
2. execution ref;
3. checkout SHA;
4. focused test discovery count;
5. focused test result;
6. artifact/log evidence.

Only then classify GT-067 semantically.
