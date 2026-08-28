# P384 — Exact-HEAD CI Reconciliation After REL-009 Gate Repair

Date: 2026-08-28
Status: `CLOSED / VERIFIED / ISOLATED / EXECUTION-PENDING / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P383. P383 recorded a source-level repair of the REL-009 negative integrity gate at exact head `5893f77b79348abddbd9a9ff4c96eceffff03977`, after CI had exposed a deterministic conflict between the historical lexical gate and the intentionally governed B07 consumer seam.

## CURRENT OBSERVATION
The repaired head was re-queried through the commit-associated workflow observation channel. No workflow run is currently observable for exact head `5893f77b79348abddbd9a9ff4c96eceffff03977`.

The PR remains open and points to that head. This does not establish a failure of the repair, nor does it establish a pass.

## ANALYSIS
The correct classification is `NO OBSERVATION / EXECUTION-PENDING`.

No second code mutation is justified merely to provoke another run. Rewriting the repair, adding redundant tests, or weakening the gate without a new observation would destroy the evidence discipline established in P383.

The previous pre-fix CI result remains valid evidence for the old head only. It cannot be transferred to the repaired head.

## EVIDENCE STATE
- Pre-fix integrity failure at `83c26b6...`: `PROVEN BY CI`
- Architectural cause: `PROVEN BY INSPECTION`
- Repair at `5893f77...`: `PROVEN BY SOURCE`
- CI result for repaired exact head: `UNOBSERVED`
- Repair PASS: `UNPROVEN`
- Repair FAIL: `UNPROVEN`
- B07 behavioral closure: `UNPROVEN`
- B08 real-provider dispatch: `UNPROVEN`
- Canonical mutation: `NONE`
- Promotion: `NOT JUSTIFIED`

## KNOWLEDGE DELTA
**KD-070 — Evidence is exact-head scoped: a CI result belongs to the commit that produced it and must not be projected onto a later repair commit.**

**KD-071 — Once a deterministic failure has been repaired, the absence of a new observation is a state of incomplete evidence, not evidence of either success or failure.**

## CHECKPOINT
`P384 → obtain observable CI result for exact repaired HEAD 5893f77... → inspect all relevant jobs → if green, execute/verify B07 matrix → address current-SHA/read-before-write contract gap → B07 closure → controlled B08 observation.`

## CLOSE
`CLOSED / VERIFIED / ISOLATED / EXECUTION-PENDING / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
