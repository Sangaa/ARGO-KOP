# HORUS Session Record 017 — 2026-08-24

## Objective
Advance the HORUS truth audit from causal isolation to counterfactual reasoning. The goal is to determine what can legitimately be inferred about a learning strategy when the decisive alternative condition cannot be directly observed in the same historical event.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H087 — Counterfactuals must be grounded in observable causal structure
A counterfactual is useful only when its assumed change is connected to a mechanism or intervention that can be justified from the evidence. Imaginative alternatives are not evidence.

### DEC-H088 — Historical counterfactuals are weaker than controlled counterfactuals
"What would have happened without guidance?" inferred from a historical event is weaker than an actual matched condition in which guidance was removed or controlled.

### DEC-H089 — Counterfactual claims require explicit assumptions
HORUS must list the assumptions required to move from observed history to an unobserved alternative. Hidden assumptions cannot be counted as evidence.

### DEC-H090 — Counterfactual stability matters
If a conclusion changes drastically under small reasonable changes to its assumptions, the conclusion is fragile and must not be promoted as strong attribution.

### DEC-H091 — Use negative-space evidence carefully
A behavior that occurs only when an external pathway is present can indicate dependency, but only when alternative explanations for the pathway's presence are controlled.

### DEC-H092 — Counterfactuals should narrow claims, not inflate them
When counterfactual evidence is weak, the correct response is to reduce the scope of the conclusion rather than invent a stronger narrative.

## Counterfactual reasoning model

`Observed Case`
→ `Causal Model`
→ `Counterfactual Intervention`
→ `Assumptions`
→ `Predicted Alternative`
→ `Consistency Check`
→ `Sensitivity to Assumptions`
→ `Claim Scope`

## New findings

### F-H017-01 — The missing alternative condition is itself a source of uncertainty
If we observed success with guidance but never observed the same decision boundary without guidance, the difference between the two conditions cannot be treated as measured fact.

### F-H017-02 — Counterfactual reasoning can expose hidden assumptions
Asking "would ARGO have selected X without retrieval?" forces the analysis to state assumptions about memory, available information, task difficulty, and strategy space that might otherwise remain invisible.

### F-H017-03 — Sensitivity analysis is an anti-overclaim mechanism
If plausible assumptions produce materially different counterfactual conclusions, the strongest defensible result is a fragile or unresolved attribution.

### F-H017-04 — Counterfactual consistency can prioritize experiments
When several competing origins imply different counterfactual outcomes, the most valuable future experiment is the one that directly tests the assumption responsible for the largest disagreement.

### F-H017-05 — Dependency is not equivalent to origin
Showing that behavior depends on retrieval does not automatically prove that retrieval created the strategy originally. A strategy may have originated elsewhere and later become retrieval-dependent.

### F-H017-06 — Origin and execution dependencies must remain separate
HORUS must distinguish:
- `Origin dependency` — what caused the strategy to arise.
- `Execution dependency` — what the system needs to reproduce or execute the strategy later.

## Counterfactual claim scale

- `CF0 — Speculative`: unsupported alternative story.
- `CF1 — Assumption-bound`: plausible but heavily dependent on explicit assumptions.
- `CF2 — Evidence-grounded`: constrained by observed causal structure and supporting evidence.
- `CF3 — Experimentally anchored`: counterfactual supported by a controlled intervention or matched comparison.

This scale measures counterfactual grounding, not probability of truth.

## Handoff lesson for ARGO/HERMUZ

> **Never confuse what happened with what would have happened. A counterfactual becomes useful only when its assumptions are visible, testable, and tied to an observable causal structure.**

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

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / COUNTERFACTUAL-CAUSAL FRONTIER ACTIVE

**Next action:** apply the origin-versus-execution dependency distinction to the strongest historical candidate and identify whether any current claim silently assumes that later retrieval dependence proves original strategy origin.

**Highest-risk error:** using an imagined counterfactual as though it were an observed control condition.

**Epistemic status:** Analytical / non-canonical.
