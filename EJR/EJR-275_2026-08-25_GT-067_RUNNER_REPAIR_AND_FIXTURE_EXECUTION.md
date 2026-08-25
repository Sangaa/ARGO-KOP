# EJR-275 — GT-067 Runner Repair and Fixture Execution

**Date:** 2026-08-25
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Scope:** `Quality/Integration/test_evidence_reasoning_classification.py` and GT-018 CI execution
**Mutation class:** Test-fixture reconciliation + execution evidence

## Starting state

Commit `c1033254cdb00cc4ace309bca3d42a7cb8d8695f` corrected GT-018 discovery from `unittest` to `pytest` while preserving the canonical `PYTHONPATH`.

That execution produced real pytest discovery but failed 5 of 21 tests. The failure boundary was inside fixture construction, not the production evidence classifier.

## Root cause confirmed by runtime evidence

The five failures were:

- one fixture omitted the required `evidence_layer` constructor field;
- four fixtures placed `evidence_independence` in a shared dictionary and supplied it again explicitly, producing duplicate-key constructor errors.

The failure occurred before the affected semantic assertions could execute.

## Prior-learning retrieval

Relevant prior learning was searched through:

1. exact constructor/field identifiers;
2. GT-039 / GT-040 provenance regression artifacts;
3. reverse semantic searches for provenance, independence and evidence-layer contracts.

The retrieved learning confirms that the evidence model and provenance semantics are established boundaries. No production-model change was justified.

## Safe mutation

Commit:
`a691c0cbff49b8d1a571948986af90b82d4a8ded`

Only `Quality/Integration/test_evidence_reasoning_classification.py` was changed. The repair reconciled the affected fixtures with the existing `EvidenceObservation` constructor contract. Production semantic functions were unchanged.

Read-back diff confirms the mutation is confined to fixture construction lines.

## Execution evidence

Full-Stack Repository Audit run:
`32809526519`

Head SHA:
`a691c0cbff49b8d1a571948986af90b82d4a8ded`

Conclusion: **success**

The GT-018 step completed successfully, followed by all downstream mutation-matrix, relationship, repository-audit and runtime-evidence steps.

The canonical Runtime Prototype and Integration Tests workflow for the same commit also completed its integrity, prototype and integration jobs successfully.

## Result

`GT-067 = VERIFIED`

`GT-068 = VERIFIED`

`Production semantic model = UNCHANGED`

`Runtime evidence = PRESENT`

`False-green boundary = CLOSED`

## Learning

A correct test runner is necessary but insufficient for evidence identity. Once discovery is repaired, fixture-construction failures must be distinguished from semantic failures. A test that cannot construct its observation object has not yet tested the evidence model.

The combined chain is now:

`pytest discovery > 0`

→ `GT-018 focused assertions execute`

→ `all focused assertions PASS`

→ `downstream audit executes`

→ `runtime evidence emitted`

→ `commit-bound execution evidence verified`
