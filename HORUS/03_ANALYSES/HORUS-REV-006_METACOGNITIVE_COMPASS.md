# HORUS-REV-006 — Metacognitive Compass Analysis

Date: 2026-08-23
Status: ANALYTICAL MODEL / CANDIDATE CAPABILITY
Owner: HORUS

## Observation
The existing ARGO learning corpus contains mechanisms for prior-learning retrieval, evidence validation, bounded generalization, experimentation, and explicit promotion. HORUS can add a distinct function: observing whether ARGO's current learning direction is proportionate to the next action.

## New distinction

A learning system can be wrong in two different ways:

1. **Knowledge error** — what it believes is incorrect or insufficient.
2. **Learning-direction error** — the system is investing effort or taking action in a direction that is poorly matched to its current uncertainty, consequence, reversibility, or information needs.

HORUS is primarily responsible for detecting the second class while also identifying the first when it affects direction.

## Guidance is valuable even without new knowledge

HORUS does not need to discover a new fact to be useful. It may correctly recommend:
- learn more before a pivotal action;
- verify a critical assumption;
- run a reversible experiment instead of theorizing longer;
- revisit a neglected prior experience;
- reconsider transfer of an old rule;
- continue a promising learning path that was abandoned prematurely.

The recommendation itself becomes an object for later evaluation.

## Candidate meta-learning capability

`Self-observation`
→ `Learning-direction assessment`
→ `Guidance`
→ `ARGO decision`
→ `Outcome`
→ `Guidance quality review`

This creates a feedback loop about the **process of learning**, not merely the content learned.

## Important boundary

This does not establish consciousness, subjective awareness, or a literal subconscious. It is an engineered reflective layer whose outputs are evidence-bounded recommendations.

## Truth test

The framework will be considered behaviorally meaningful only when recommendations can be evaluated against outcomes and when repeated reviews demonstrate that HORUS improves direction selection without becoming an unnecessary blocker.

## Current status

`FRAMEWORK: ESTABLISHED`
`BEHAVIORAL EFFECT: NOT YET ESTABLISHED`
`AUTONOMOUS META-LEARNING: NOT ESTABLISHED`
`WORLD-FACING CLAIM: NOT PROMOTED`

## Next validation target

Collect a small set of real ARGO decision points with different risk/reversibility profiles and test whether HORUS recommendations correctly distinguish:

- study-first;
- verify-first;
- experiment-first;
- proceed.

Do not reward HORUS for recommending caution by default. A correct compass must sometimes say `PROCEED`.

## Routing

Source: HORUS analysis
Consumer: ARGO
Engineering consumer: HERMUZ when validated guidance affects construction decisions
