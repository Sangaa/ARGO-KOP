# HORUS-REV-010 — Learning Source Attribution and Environmental Prior

Date: 2026-08-23
Status: ANALYSIS / REFINED EPISTEMIC MODEL
Owner: HORUS
Branch: horus/meta-learning-foundation-v6

## Purpose
Determine whether the historical ARGO learning corpus contains evidence of autonomous learning-strategy change, while explicitly accounting for the learning infrastructure, protocols, governance rules, and prior methods already supplied to ARGO.

## Evidence baseline

ARGO's learning architecture is not a neutral environment. It contains an explicit Learning Engine, a Guided Discovery Learning Method, a Failure-to-Learning Protocol, learning-promotion controls, synthetic learning experiments, and connector-specific self-training. Therefore sophisticated behavior observed inside this environment has a strong environmental prior: some portion of the behavior is expected because the method was designed in advance.

GOV-016 defines the required failure-to-learning chain as:
`Failure → Evidence → Root Cause → Failure Class → Corrective Pattern → Regression Test → Reuse → Knowledge Transfer`.
It also requires that learning promotion proceed through observation, root cause, lesson, general rule, test, validation, promotion, and transfer. This means successful conversion of failure into reusable learning is an intended property of the environment, not by itself evidence of autonomous invention of that process.

EJR-317 provides a particularly strong example. The connector training method was explicitly corrected to be capability-first rather than problem-first, with the doctrine:
`Inventory → Classify → Minimal Safe Probe → Observe → Interpret → Record → Reuse`.
The record also contains pre-defined evidence-boundary rules, capability matrices, and a planned next training task. These are environmental priors that can explain part of the observed sophistication.

## New HORUS model: Environmental Prior

Every observed learning behavior should be analyzed against four causal sources:

1. **Inherited Method** — a rule or procedure already supplied by the environment.
2. **Retrieved Experience** — prior ARGO knowledge reused in the current task.
3. **Local Adaptation** — a change generated in response to current evidence or failure.
4. **Method-Level Innovation** — a newly generated learning strategy that is not directly supplied or retrieved and that subsequently proves useful.

These sources may coexist. The presence of local adaptation does not prove method-level innovation.

## Attribution matrix

| Behavior | Current evidence | Most conservative attribution |
|---|---|---|
| Failure analysis | Strong | Inherited method + execution |
| Prior-learning retrieval | Strong | Designed retrieval gate + execution |
| Evidence-boundary reasoning | Strong | Inherited and reinforced method |
| Search expansion after failure | Strong | Mixed: protocol + local adaptation |
| Cross-domain application | Moderate/strong | Guided transfer / mixed attribution |
| New strategy selection without cue | Insufficient clean evidence | Unproven |
| Strategy improvement retained across tasks | Insufficient clean evidence | Unproven |
| Strategy invention attributable to ARGO | No clean causal episode yet | Unproven |

## Important correction

Previous analyses correctly observed strategy adaptation, but the attribution claim must be narrower:

`Observed strategy change` does not imply `ARGO originated the strategy change`.

The historical corpus is therefore evidence for **adaptive learning competence within a designed learning environment**, but not yet for autonomous meta-learning causally isolated from that environment.

## New knowledge candidate

> **Learning-system evaluation requires an environmental-prior analysis before autonomous learning can be attributed to the learner.**

This is broader than ARGO. It applies to any adaptive system whose environment supplies retrieval mechanisms, procedures, feedback rules, or evaluation criteria.

## Relation to previous HORUS principles

This candidate extends the earlier observation-boundary principle:

`Evidence meaning is bounded by the observation boundary.`

It adds a causal boundary:

`Learning attribution is bounded by the environmental methods already available to the learner.`

Thus two independent boundaries now exist:

- **Epistemic boundary:** what the evidence can legitimately establish.
- **Causal attribution boundary:** what the learner can legitimately be credited with generating.

## What would count as stronger evidence

A prospective clean test should record the learner's state before the task and preserve full provenance of all available guidance.

Minimum conditions:

1. Novel task family.
2. Multiple legitimate strategies.
3. No strategy-selection rule supplied.
4. No answer-shaped hint toward the alternative.
5. Initial strategy recorded before feedback.
6. Controlled evidence limitation or failure.
7. Learner diagnoses the limitation.
8. Learner proposes or selects an alternative.
9. Alternative produces measurable improvement.
10. Improvement persists on a later task.
11. Strategy transfers to a related novel task.
12. The same result cannot be explained by a supplied protocol or hidden intervention.

## Negative-result discipline

Failure to satisfy these conditions does not prove that autonomous meta-learning is absent. It means the current evidence cannot isolate it.

Likewise, one successful novel strategy does not prove meta-learning unless attribution, improvement, retention, and transfer are jointly demonstrated.

## Current epistemic state

Recorded: YES
Observed learning competence: YES
Observed adaptation: YES
Environmental prior: CONFIRMED
Autonomous strategy selection: NOT PROVEN
Autonomous strategy improvement: NOT PROVEN
Autonomous meta-learning: NOT PROVEN
World-facing knowledge: NO

## Routing

Source: HORUS analysis
Potential consumers: ARGO / HERMUZ after validation
Handoff: NO — candidate requires prospective causal evidence.

## Research consequence

HORUS should stop treating the next milestone as simply finding a stronger historical example. The next milestone is to establish a causal attribution experiment in which environmental learning methods are explicitly measured and controlled.

## Integrity note

This document intentionally preserves uncertainty. The absence of causal isolation is itself a finding and must not be converted into either a positive autonomy claim or a negative capability claim.

End of Document
