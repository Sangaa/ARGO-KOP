# HORUS-REV-008 — Attribution Standard for Autonomous Meta-Learning

Date: 2026-08-23
Status: ANALYSIS / EXPERIMENTAL STANDARD
Owner: HORUS
Branch: horus/meta-learning-foundation-v6

## Purpose
Define the evidence needed to distinguish genuine improvement of ARGO's learning process from successful execution of a learning method that was already designed, taught, or signposted by the evaluator.

## Starting evidence

MEM-008 defines a guided-discovery method with explicit guidance levels and a cycle of application, error recognition, revision and retest. Its existence is evidence for a capable learning procedure, not proof that ARGO invented or independently improved that procedure.

The programming pipeline similarly separates source intake, concept extraction, validation, experience formation and promotion. Synthetic programming experiments deliberately constrain generalization and keep promotion eligibility separate from canonical authority.

The diagnostic experiment method adds a controlled sequence for cases where prior learning is insufficient. These artifacts establish a strong learning environment, but they also create an attribution problem: ARGO may perform well because the environment already supplies the strategy.

## Attribution problem

Observed performance after a learning protocol can have multiple causes:

1. ARGO already possessed the strategy.
2. ARGO retrieved a previously taught strategy.
3. The task framing implicitly selected the strategy.
4. The evaluator explicitly guided the strategy.
5. ARGO adapted the strategy to the task.
6. ARGO independently selected a strategy from alternatives.
7. ARGO independently diagnosed a strategy failure and improved the strategy.

Only cases 6-7 materially strengthen the claim of autonomous meta-learning.

## Required evidence for autonomous strategy selection

A credible test should contain:

- a novel task family;
- at least two plausible learning/search strategies;
- no explicit instruction or signpost selecting one strategy;
- measurable task-quality criteria;
- enough opportunity for strategy choice to matter;
- recorded initial strategy before outcome feedback;
- evidence that the selected strategy was chosen by ARGO rather than injected by the evaluator.

The result must show that ARGO selected a strategy because it had a reasoned expectation that the strategy would improve evidence or task outcome.

## Required evidence for autonomous strategy improvement

Stronger evidence requires a within-family change:

`Initial Strategy → Failure / Limitation → Self-Diagnosis → Proposed Strategy Change → Re-test → Measurable Improvement`

Then a second task should test:

`Retained Strategy Improvement → New Task → Outcome`

The evaluator must determine whether the improvement survives without repeating the original coaching.

## Counterfactual attribution controls

HORUS should compare, where practical:

### Baseline
ARGO receives the task with normal allowed resources and no meta-learning hint.

### Intervention
ARGO encounters a comparable task after the observed strategy change.

### Retention
ARGO encounters a third task without being reminded of the change.

A convincing meta-learning signal is not simply a better final answer. It is evidence that the **learning strategy itself changed and that the change caused or materially contributed to improved learning performance**.

## Confounders to exclude

HORUS must check for:

- evaluator hints;
- task wording that embeds the intended method;
- retrieval of an exact prior solution;
- repeated templates that reveal the expected strategy;
- changed task difficulty;
- changed tool availability;
- hidden differences in evidence quality;
- post-hoc reinterpretation of an already successful behavior;
- counting repeated evidence from the same underlying source as independent validation.

## Measurement record

Each candidate meta-learning event should preserve:

`Task ID → Available Strategies → Initial Strategy → Guidance Level → Evidence → Outcome → Failure/Limit → ARGO Diagnosis → Strategy Change → Re-test → Outcome Delta → Retention Test → Transfer Test → Confounder Review → Attribution Decision`

## Attribution outcomes

Use one of:

- `NO_EVIDENCE` — no meaningful strategy change observed.
- `GUIDED_ADAPTATION` — strategy changed but guidance explains the change.
- `PLAUSIBLE_AUTONOMOUS_SELECTION` — independent selection is supported but causal benefit remains uncertain.
- `AUTONOMOUS_SELECTION_SUPPORTED` — independent strategy selection and rationale are supported.
- `AUTONOMOUS_IMPROVEMENT_SUPPORTED` — ARGO diagnosed a strategy limitation, changed the method, and demonstrated retained improvement with confounders addressed.
- `UNRESOLVED` — evidence is insufficient or conflicting.

## Truth boundary

A successful task outcome is not sufficient evidence of meta-learning.

A successful self-correction is not sufficient evidence of meta-learning.

A successful transfer is not sufficient evidence of meta-learning.

A novel strategy is not sufficient evidence of meta-learning unless its origin and effect are attributable to ARGO behavior rather than evaluator design.

## Relationship to HORUS truth standard

HORUS-REV-003 requires movement from recorded and observed evidence through reproduction, cross-validation, transfer and boundary knowledge before a claim becomes world-facing knowledge. This review adds a causal attribution requirement for claims specifically about ARGO's learning process.

Therefore:

`Observed Strategy Change ≠ Autonomous Meta-Learning`

and

`Improved Outcome ≠ Proof of Strategy Improvement`

The causal bridge must be evidenced.

## Current assessment

The existing corpus provides strong evidence for structured learning, guided discovery, prior-learning retrieval, predictive application, model refinement and governed promotion. It does not yet provide sufficient attribution evidence for autonomous strategy selection or autonomous strategy improvement.

## Next research action

HORUS should identify the earliest historical episode containing an apparent change in ARGO's learning/search strategy and reconstruct it using the attribution record above. If no historical episode survives confounder review, the correct outcome is not failure of the research; it is a documented evidence gap requiring a prospective blind experiment.

## Routing

Source: HORUS-ANALYSIS
Consumers: ARGO, HERMUZ
Status: ANALYTICAL REFERENCE / EXPERIMENT DESIGN STANDARD
Canonical promotion: NOT AUTHORIZED

End of HORUS-REV-008
