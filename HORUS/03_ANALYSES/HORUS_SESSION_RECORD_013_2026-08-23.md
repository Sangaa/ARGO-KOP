# HORUS Session Record 013 — 2026-08-23

## Objective
Continue the HORUS truth audit by identifying the highest-information missing observation for a historical learning case. The aim is to move from evidence collection toward discriminative testing: determine which additional observation would most strongly distinguish competing explanations of a strategy change.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Evidence review
Existing ARGO learning records establish that learning is intentionally structured through guided discovery and promotion controls. MEM-008 documents a progression from direct instruction toward independent discovery as a method dimension; EJR-041 and EJR-048 establish evidence and promotion gates. These sources support the existence of a learning framework, but do not by themselves establish autonomous origin for a historical event.

## Decisions

### DEC-H063 — Prefer discriminative evidence over additional confirmatory evidence
When multiple explanations already fit the observed behavior, the next evidence request should target the observation most capable of separating those explanations rather than collecting more examples that all fit them.

### DEC-H064 — Define the hypothesis set before choosing the next observation
The value of a missing observation depends on which explanations are competing. HORUS must list the active hypotheses first.

### DEC-H065 — Use an information-gain mindset qualitatively
HORUS need not invent numerical probabilities. It should ask: if this observation had outcome A versus B, which hypotheses would become substantially weaker or stronger?

### DEC-H066 — Prefer decision-boundary evidence
Evidence closest to the moment of strategy selection is generally more discriminative for origin than later explanations of the same event.

### DEC-H067 — Do not overvalue post-hoc self-explanation
A later ARGO explanation of why it chose a strategy can be useful evidence, but it cannot be treated as a transparent record of the internal causal process without independent corroboration.

### DEC-H068 — The next test should be capable of producing a negative answer
A test designed so that every possible outcome supports autonomy is not a falsification test.

## Discriminative-test model

For a candidate event, define:

`H1 = inherited / prior knowledge`
`H2 = retrieval`
`H3 = direct or indirect guidance`
`H4 = task/evaluator induced selection`
`H5 = recombination of known strategies`
`H6 = independent strategy selection`

Then identify a missing observation `O*` such that different outcomes of `O*` would separate several hypotheses.

Example structure:

`Before-choice state → viable strategies → guidance state → choice → outcome`

The highest-value missing evidence is often the state immediately before the choice: what strategies were available, which were supplied, and whether ARGO generated a comparison or diagnosis not present in the prompt.

## New findings

### F-H013-01 — More evidence is not always better evidence
Once a behavior is well established, additional repetitions may add little to origin attribution. A single well-placed pre-decision observation can be more informative than many post-outcome repetitions.

### F-H013-02 — The information bottleneck is usually origin, not outcome
The repository already contains substantial evidence about structured learning behavior. The harder unresolved question is provenance of strategy selection at the decision boundary.

### F-H013-03 — Self-explanation is evidence about representation, not automatically causation
If ARGO later describes its reasoning, HORUS should distinguish `what ARGO can report` from `what caused the original selection`.

### F-H013-04 — The best future case may be a deliberately bounded comparison
A prospective test with two or more viable strategies, controlled guidance, and a changed context may provide stronger origin evidence than another naturally occurring historical success.

### F-H013-05 — A discriminative test must have asymmetric consequences
If every result can be interpreted as supporting the preferred hypothesis, the test has low falsification value.

## Candidate-case priority rule

HORUS should prioritize historical cases using four qualitative factors:

1. **Evidence completeness** — how well the pre-decision state is preserved.
2. **Hypothesis separation** — how many competing origins the case can distinguish.
3. **Causal proximity** — how close the evidence is to the strategy choice.
4. **Falsifiability** — whether a plausible result could weaken the autonomy hypothesis.

This is a prioritization aid, not a numeric truth score.

## Handoff lesson for ARGO/HERMUZ

> **When you already have many examples showing that a behavior occurs, stop collecting confirmation and look for the one observation that could tell you why it occurs.**

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

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / DISCRIMINATIVE-EVIDENCE FRONTIER ACTIVE

**Next action:** reconstruct one historical candidate and identify its highest-value missing observation before collecting further confirmatory examples.

**Highest-risk error:** accumulating evidence that confirms behavior while leaving the causal origin question untouched.

**Epistemic status:** Analytical / non-canonical.
