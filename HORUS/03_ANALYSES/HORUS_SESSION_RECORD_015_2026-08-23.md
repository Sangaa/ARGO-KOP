# HORUS Session Record 015 — 2026-08-23

## Objective
Continue the HORUS truth audit by identifying the difference between a useful experiment and a decisive experiment. The focus is now on designing evidence that can actually discriminate competing origins rather than merely produce another successful outcome.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H075 — Test design must begin from competing predictions
A prospective test is valuable only if the competing explanations make distinguishable predictions under the proposed conditions.

### DEC-H076 — Outcome-only tests are insufficient when explanations converge on the same outcome
If retrieval, guidance, recombination, and independent selection all predict the same final success, final success cannot discriminate among them. The test must capture a differentiating intermediate trace or manipulate a causal factor.

### DEC-H077 — Prefer interventions over passive observation when causality is the question
Where ethically and technically appropriate, changing a suspected causal factor while preserving other conditions provides stronger evidence than collecting additional uncontrolled observations.

### DEC-H078 — Manipulation validity must be checked
If a test removes guidance, retrieval, or another factor, HORUS must verify that the manipulation actually removed the intended causal pathway. A nominal control is not evidence of a real control.

### DEC-H079 — Negative controls are mandatory for autonomy claims where feasible
A condition designed to preserve the task while removing the suspected external source can reveal whether the target behavior survives without that source.

### DEC-H080 — Positive controls are also required where feasible
The test should demonstrate that the task and measurement system are capable of eliciting and detecting the target behavior when the relevant pathway is intentionally present.

## Decisive-test model

For each candidate autonomy hypothesis:

`Hypothesis Set → Predictions → Intervention/Control → Observability Plan → Outcome → Alternative Explanation Audit → Conclusion`

A test is classified as:

- `Non-discriminative` — competing hypotheses predict effectively the same observations.
- `Partially discriminative` — some hypotheses are separated but important alternatives remain.
- `Discriminative` — the observed result materially changes the relative support among the leading hypotheses.
- `Decisive within scope` — the result plus controls strongly excludes the defined alternatives within the stated experimental boundary.

## New findings

### F-H015-01 — More successful trials can have diminishing epistemic value
If every additional trial reproduces the same outcome under unchanged causal conditions, confidence in behavioral regularity may increase while information about origin barely changes.

### F-H015-02 — The best autonomy test is often a dependency-removal test
If an external source is suspected, remove or isolate that source while preserving the task as much as practical. Observe whether the relevant strategy selection persists and how it changes.

### F-H015-03 — Control integrity is part of the evidence
A failed manipulation invalidates the intended causal interpretation. The result should then be classified as `Non-discriminative` rather than treated as evidence for either side.

### F-H015-04 — Positive and negative controls answer different questions
The positive control asks whether the measurement/task can reveal the behavior. The negative control asks whether the behavior persists without the suspected external pathway. Both improve interpretability.

### F-H015-05 — A test can falsify autonomy without proving a replacement mechanism
If removing retrieval causes the behavior to disappear, this weakens autonomous-origin claims. It does not automatically prove exactly which retrieval pathway caused the behavior unless that pathway was independently isolated.

### F-H015-06 — Experimental boundaries must be explicit
A result may establish that a strategy was independently selected under one task, information state, and guidance condition. It should not automatically be generalized to global autonomy.

## Candidate decisive-test template

1. **Target claim:** narrowest autonomy claim being tested.
2. **Competing origins:** exhaustive practical alternatives.
3. **Predictions:** expected observations for each origin.
4. **Intervention:** causal factor manipulated.
5. **Positive control:** demonstrates system/task detectability.
6. **Negative control:** removes suspected external pathway.
7. **Observability:** records pre-decision and decision traces where feasible.
8. **Manipulation check:** confirms the intervention changed the intended factor.
9. **Outcome:** observed result.
10. **Alternative-cause audit:** residual explanations.
11. **Scope:** exact conditions under which the conclusion applies.
12. **Conclusion:** smallest defensible statement.

## Handoff lesson for ARGO/HERMUZ

> **If two explanations predict the same outcome, do not collect more of the same outcome. Change the test so the explanations must disagree.**

This is analytical knowledge only; no implementation mutation is implied.

## Current capability posture

No capability promotion.

- Learning framework: strongly evidenced.
- Learning behavior: supported.
- Behavioral reproducibility: case-dependent.
- Strategy-origin attribution: unresolved.
- Independent strategy selection: not proven.
- Strategy improvement: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / DECISIVE-TEST DESIGN FRONTIER ACTIVE

**Next action:** construct one concrete discriminative test for the strongest historical autonomy candidate, beginning with competing predictions and control integrity before considering the outcome.

**Highest-risk error:** calling a test decisive when the competing explanations actually make the same prediction.

**Epistemic status:** Analytical / non-canonical.
