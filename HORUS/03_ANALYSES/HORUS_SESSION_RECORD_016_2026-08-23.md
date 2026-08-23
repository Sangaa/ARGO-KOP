# HORUS Session Record 016 — 2026-08-23

## Objective
Apply the decisive-test frontier one step deeper by defining causal isolation and the minimum evidence needed to interpret an intervention. The aim is to prevent a failed control, side effect, or altered task difficulty from being mistaken for evidence about autonomous strategy origin.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H081 — Intervention effect is not automatically causal attribution
A change after removing a suspected pathway is evidence about the intervention only if the intervention was valid and competing side effects are controlled or bounded.

### DEC-H082 — Manipulation checks precede interpretation
HORUS must verify that the intended factor changed as planned before interpreting the outcome as evidence about that factor.

### DEC-H083 — Task equivalence must be assessed
Removing retrieval or guidance may inadvertently change task difficulty, available information, latency, or error feedback. Such changes can alter behavior without identifying the causal source of the original strategy.

### DEC-H084 — Use matched controls where feasible
The strongest comparison preserves task demands while varying only the suspected causal pathway as closely as practical.

### DEC-H085 — Robustness is stronger than one boundary condition
If an autonomy claim survives multiple reasonable controls and task-preserving variations, attribution becomes stronger within the tested scope. It still does not justify unlimited generalization.

### DEC-H086 — Failed experiments must preserve diagnostic value
A failed manipulation is not a failed learning record. It should identify which causal question remains unresolved and what must change in the next test.

## Causal-isolation model

`Target Hypothesis`
→ `Suspected Cause`
→ `Manipulation`
→ `Manipulation Check`
→ `Task-Equivalence Check`
→ `Observed Difference`
→ `Alternative Side-Effect Audit`
→ `Causal Interpretation`

If either the manipulation check or task-equivalence check fails, the result cannot be promoted to strong causal evidence.

## New findings

### F-H016-01 — Removing help can create a new task
If retrieval or guidance is removed, the resulting condition may no longer represent the original task without help; it may represent a harder or qualitatively different task. The difference must be measured before interpreting the outcome.

### F-H016-02 — Behavioral disappearance is ambiguous without control integrity
A strategy disappearing after intervention can mean dependency on the removed pathway, but it can also mean increased task difficulty, loss of necessary information, or measurement failure.

### F-H016-03 — Matched variation is the bridge between observation and causality
When feasible, compare conditions that differ in the suspected pathway while remaining as similar as possible in task demand, information, evaluation, and measurement.

### F-H016-04 — Robustness can be graded
A result surviving one control is weaker than a result surviving several independently justified controls. HORUS will record robustness separately from basic support.

### F-H016-05 — Causal isolation is local
Even a strong intervention result establishes a dependency relationship under the tested conditions. It does not establish a universal mechanism for every ARGO learning event.

## Robustness scale

- `R0 — Uncontrolled`: no meaningful causal isolation.
- `R1 — Single control`: one relevant alternative pathway tested.
- `R2 — Matched control`: suspected pathway varied while major task factors are preserved.
- `R3 — Multi-control`: multiple plausible alternatives and side effects tested.
- `R4 — Cross-context robustness`: causal interpretation survives meaningful context variation within the defined scope.

Robustness is an evidence-quality dimension, not a probability of truth.

## Handoff lesson for ARGO/HERMUZ

> **When changing one factor changes the outcome, first prove that you changed only the factor you intended. A causal claim begins with a valid comparison, not with a surprising result.**

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

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / CAUSAL-ISOLATION FRONTIER ACTIVE

**Next action:** apply the causal-isolation model to the strongest historical autonomy candidate and determine whether the existing evidence contains a valid manipulation check and task-equivalence basis. If not, classify the missing control rather than inferring autonomy.

**Highest-risk error:** interpreting an intervention-induced behavioral change as proof of causal dependency when the intervention also changed task difficulty or observability.

**Epistemic status:** Analytical / non-canonical.
