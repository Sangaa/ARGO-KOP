# HORUS-004 — Knowledge Validation & Handoff

Status: FOUNDATION
Purpose: control promotion of HORUS analysis into ARGO shared knowledge

## Knowledge lifecycle

`OBSERVED → INTERPRETED → CANDIDATE → SUPPORTED → VALIDATED → INTEGRATED → HANDOFF-ELIGIBLE`

Alternative terminal states are:

- SUPERSEDED
- CONTRADICTED
- UNRESOLVED

## Validation gate

Before handoff, HORUS should establish, where the evidence permits:

1. the source experiences and observations;
2. the reasoning that produced the candidate;
3. why it is not merely duplicated prior knowledge;
4. its applicability boundary;
5. at least one meaningful attempt to falsify or limit it;
6. compatibility or explicit conflict with existing knowledge;
7. evidence quality and confidence;
8. whether the learning is useful for ARGO, HERMUZ, both, or neither.

## Handoff record

Every handoff-eligible learning must retain:

- HORUS knowledge ID;
- source experience IDs or references;
- originating analysis;
- evidence state;
- confidence;
- applicability boundary;
- known counterexamples;
- target ARGO/HERMUZ consumer;
- reason for handoff;
- supersession/conflict status if applicable.

## Routing rule

Handoff must preserve the distinction:

- **ARGO-facing learning** — improves cognition, retrieval, reasoning, transfer or self-learning.
- **HERMUZ-facing engineering knowledge** — improves construction, verification or implementation practice.
- **Shared knowledge** — valid for both, with separate consumer interpretations recorded.

## No silent promotion

HORUS must never convert an interpretation into canonical ARGO knowledge merely because the interpretation is elegant, repeated in one context, or useful to the current analysis.
