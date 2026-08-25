# EJR-273 — GT-067 Fixture Contract Reconciliation

**Date:** 2026-08-25
**Protocol:** GOV-013 HERMUZ Session Build Protocol
**Scope:** Evidence reasoning integration-test fixtures
**Mutation class:** Documentation-only

## Trigger

GT-067 previously reported nine runtime-test failures. Before changing production semantics, the `EvidenceObservation` constructor and the affected fixtures were inspected directly.

## Verified contract

`EvidenceObservation` is a frozen dataclass. Its constructor defines `semantic_status` as a real field with default `OBSERVED`, followed by optional execution/provenance identity fields.

## Verified fixture defect pattern

The affected execution-occurrence tests define `semantic_status` inside a shared `common` dictionary and then pass another explicit `semantic_status` value in the same constructor call.

Representative pattern:

```python
common = dict(..., semantic_status="VERIFIED_OCCURRENCE")
capability = EvidenceObservation(..., semantic_status="VERIFIED_CAPABILITY", **common)
```

This is a Python constructor invocation error (`multiple values for keyword argument 'semantic_status'`). It occurs before the semantic assertion can execute.

The same pattern is present in the capability/occurrence fixtures for the affected execution tests. Therefore the observed failure is classified as a fixture-construction defect, not a failure of `classify_execution_occurrence()` semantics.

## Important negative finding

The constructor contract itself should NOT be changed to accommodate the malformed fixtures. Doing so would alter the evidence model merely to make tests execute.

The safe repair boundary is the fixture layer: each fixture must provide `semantic_status` exactly once.

## Provenance relevance

This finding preserves the distinction established by GT-064 through GT-066:

- execution identity is composite evidence;
- execution capability is not execution occurrence;
- an unresolved or malformed observation must not be promoted to a verified occurrence;
- test-construction failure must not be interpreted as semantic contradiction or CI failure.

## Decision

**GT-067 = ROOT CAUSE VERIFIED / FIXTURE CONTRACT MISMATCH**

Production evidence semantics: **UNCHANGED**

No production-code mutation performed.

## Next safe mutation

Repair only the affected test fixtures by removing duplicated constructor arguments so each `EvidenceObservation` receives one explicit `semantic_status` value. Then execute the focused test set and classify each resulting failure independently as:

1. fixture/runtime failure,
2. semantic failure,
3. provenance failure, or
4. verified pass.

Do not broaden the mutation to production semantics until the focused test run demonstrates a semantic defect.
