# EJR-298 — HERMUZ Effect-Surface / Side-Effect Learning

Date: 2026-08-22
Status: Closed — Learning Captured
Scope: Diagnostic / Governance learning

## Trigger

During the GitHub channel investigation, repeated observation showed that repository operations can leave or expose evidence across multiple surfaces. This raises a second-order question: if execution or mutation produces effects in additional surfaces, are those effects intended, required propagation, incidental traces, or unintended side effects?

## Prior Learning Applied

The investigation used the Prior-Learning Retrieval Gate and the previously learned distinction between repository state, observation surface, search visibility, execution identity, and runtime evidence.

## New Rule

The existence of a downstream effect must never be treated as proof of intent or architectural necessity.

The investigation sequence must become:

`Trigger → Expected Primary Effect → Search for Secondary Effects → Causal Hypothesis → Effect Classification → Controlled Reproduction → Required/Incidental/Unintended decision`

## Effect Classes

INTENDED / EXPECTED PROPAGATION / INCIDENTAL-BENIGN / UNINTENDED-RISK / UNKNOWN-UNCLASSIFIED.

UNKNOWN is the safe default when causality or intent is not established.

## Why This Matters to P6

A newly observed GitHub surface may represent execution evidence, generated evidence, indexing/cache behavior, audit trace, downstream integration, or an unintended mutation. P6 must not promote any of these into relationship or runtime authority solely because the effect exists.

## Governance Mutation

Created `Governance/GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md` as a canonical addendum pending formal incorporation into GOV-013.

## Verification

The new addendum was read back after creation. SHA: `67a435ee24c17f065257095cf2deb73b024e5d1d`.

## Closure

No P6 relationship promotion.
No runtime verification promotion.
No production runtime mutation.
Learning is retained as reusable governance guidance.
