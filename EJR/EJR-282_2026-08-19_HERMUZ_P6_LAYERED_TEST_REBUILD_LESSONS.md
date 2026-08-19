# EJR-282 — HERMUZ P6 Layered Test Rebuild Lessons

Date: 2026-08-19
Status: GOVERNANCE / DESIGN DECISION
Authority: GOV-013 + GOV-014

## Finding
P6 exposed a structural testing weakness. P1–P5 primarily expose direct command/assertion outcomes, while P6 combines functional testing, CI observation, SHA binding, impact correlation, evidence classification and reconciliation.

A missing or stale CI observation was therefore easily confused with a failed functional test. Successful historical execution was also at risk of being rejected wholesale when only its freshness relative to the current HEAD was stale.

## Required Testing Rule
Any test containing multiple execution/evidence layers MUST expose each layer as an independently testable boundary with an explicit result.

Required pattern:

1. Functional test → PASS/FAIL.
2. Invocation/evidence capture → PRESENT/MISSING/INVALID.
3. Identity correlation → CURRENT/STALE/MISMATCH.
4. Artifact/read-back → VALID/INVALID/MISSING.
5. Reconciliation/classification → explicit state.

A failure at one layer MUST NOT be reported as failure of another layer.

## P6 Rebuild Direction
P6 must be rebuilt/reviewed against the simpler P1–P5 testing model while preserving its multi-layer nature. The layered chain should be inspectable stage-by-stage:

P6-A Functional Deterministic Test
→ P6-B CI Invocation/Evidence Capture
→ P6-C SHA/Scope Correlation
→ P6-D Artifact Read-back
→ P6-E Evidence Classification/Reconciliation

Each stage must have its own regression fixture and failure boundary.

## Evidence Classification Rule
Historical successful execution remains valid as execution evidence but may be classified `VALID_EXECUTION_STALE_BASELINE` when it does not bind to the current HEAD. It must not be relabeled as execution failure.

## Observability Rule
A connector query returning zero records is `NO_OBSERVATION`, not `NO_EXECUTION`, unless the query surface is proven complete for the trigger type being inspected.

## Construction Rule
Do not add triggers, rerun old jobs, or alter unrelated workflow logic to compensate for an unproven observability gap. First isolate the layer producing the ambiguity.

## Review Rule
For every layered test, reviewers must be able to answer independently:
- Did the test execute?
- Did the intended target execute?
- Which commit/range was tested?
- Was the evidence captured?
- Is the evidence current or stale?
- Did read-back succeed?
- What exact state is justified?

## Future Prevention
This rule applies beyond P6 to any future test that combines execution, evidence, correlation, artifacts, or reconciliation. Layered tests are to be designed for fault localization first, compactness second.

## Disposition
P6 remains open for structural review/rebuild. No promotion is authorized solely from existing historical success evidence.
