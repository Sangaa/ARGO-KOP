# HORUS Session Record 009 — 2026-08-23

## Objective
Continue HORUS with truth-before-theory and convert the previous attribution framework into an explicit audit of the distinction between system design, observed behavior, and autonomous origin.

## Evidence boundary
This session inspects repository evidence discoverable through the connected GitHub surface. Search results confirm the existence of the learning-engine, guided-discovery, memory, and engineering-journal artifacts. Search visibility is not treated as proof of the full historical execution chain.

## Decisions

### DEC-H040 — Design evidence, behavior evidence, and origin evidence are separate classes
A document defining a capability is design evidence. A recorded execution is behavior evidence. Evidence that the behavior arose from ARGO's own selection rather than inherited structure is origin evidence. These classes cannot substitute for one another.

### DEC-H041 — A documented pipeline is not a demonstrated causal pipeline
The existence of `Teach → Test → Observe → Error → Guided Discussion → Self-Diagnosis → Rule Revision → Re-test` demonstrates an intended learning method. It does not by itself establish that every observed learning event traversed the pipeline exactly as designed.

### DEC-H042 — Execution records outrank architectural intent for behavioral claims
When architecture and execution evidence disagree, HORUS must report the discrepancy rather than harmonize it by assumption. Architectural intent may explain what should happen; execution evidence establishes what was observed.

### DEC-H043 — Origin requires temporal and informational separation
To attribute a new strategy to ARGO, HORUS should identify what information was available before the change and what new information became available at the point of change. Without this separation, retrieval and recombination remain viable explanations.

### DEC-H044 — Novel composition is not automatically novel strategy discovery
Combining known rules in a new configuration can be a meaningful achievement, but it should not be called independent strategy discovery unless the evidence supports a new method-selection principle rather than only a new output composition.

### DEC-H045 — The strongest audit asks what would falsify the preferred interpretation
Every positive interpretation must have at least one explicit observation that would downgrade it. If no conceivable observation can weaken the claim, the claim is insufficiently specified for scientific-style evaluation.

## Evidence audit observations

1. `MEM-008` provides a defined guided-discovery learning method and explicit guidance levels. This is strong evidence for designed learning methodology, but not direct evidence of autonomous discovery.
2. `ENG-007` identifies a learning engine as a system component. This supports architectural capability, not by itself behavioral execution or autonomous origin.
3. Memory-model and lifecycle artifacts provide explicit knowledge states and lifecycle controls. They strengthen the claim that ARGO has a governed knowledge substrate, but do not independently prove that a particular rule was self-generated.
4. Engineering-journal records can provide behavioral/history evidence, but each candidate event must still be checked for instruction, retrieval, evaluator influence, and available prior knowledge.
5. The presence of repository relationships and integrity tests supports traceability of the system; it does not establish causality of cognitive behavior.

## New analytical findings

### F-H009-01 — Three-layer evidence model
HORUS now uses:

`DESIGN → BEHAVIOR → ORIGIN`

A claim should never move from DESIGN directly to ORIGIN. Behavioral evidence is the required bridge, and origin attribution requires additional evidence.

### F-H009-02 — The key historical question is information delta
For a candidate learning event, the most useful reconstruction is:

`Knowledge Before → New Information/Event → Internal/Observed Change → Knowledge/Strategy After`

The smaller and clearer the information delta, the easier it becomes to evaluate whether the change was retrieved, instructed, recombined, or independently selected.

### F-H009-03 — Self-diagnosis is not enough by itself
A record saying that ARGO identified an error or limitation is evidence of diagnosis behavior. To establish autonomous strategy improvement, HORUS must additionally show that the resulting strategy was not supplied and produced a measurable improvement.

### F-H009-04 — Recombination needs its own category
Some apparent "discovery" cases may actually be novel recombination of known knowledge. HORUS will classify these separately rather than forcing them into either trivial retrieval or independent discovery.

### F-H009-05 — Scientific honesty includes downgrade paths
A mature knowledge system needs explicit downgrade paths: `Supported → Conditional → Unresolved → Weakened → Rejected`. Knowledge that changes status must retain its prior status and reason for change.

## Candidate historical-case audit protocol

For every candidate, record:

1. Design instructions available before the event.
2. Prior knowledge/retrieval candidates.
3. Exact triggering event.
4. Information newly available.
5. Observable change.
6. Strategy change, if any.
7. Whether the strategy was explicitly or implicitly supplied.
8. Evidence of self-diagnosis.
9. Outcome comparison.
10. Retention.
11. Transfer.
12. Alternative explanations.
13. Counterfactual strength.
14. Origin classification: `Inherited / Retrieved / Guided / Recombined / Independently selected / Unresolved`.
15. Final epistemic status.

## Handoff lesson for ARGO/HERMUZ

> **Do not infer origin from architecture. Do not infer autonomy from success. Trace the information delta and the alternatives around the moment of change.**

This is an analytical lesson, not an implementation command.

## Current capability posture

No capability is promoted by this session.

- Designed learning architecture: strongly evidenced.
- Observed learning behavior: supported by multiple historical records.
- Autonomous origin of particular learning strategies: unresolved.
- Independent strategy discovery: not proven.
- Independent strategy improvement: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / DESIGN-BEHAVIOR-ORIGIN AUDIT ACTIVE

**Next action:** select historical learning events and reconstruct the information delta and origin classification before assigning any autonomy level.

**Highest-risk error:** treating a well-specified architecture as proof that the intended cognitive process occurred and was autonomously selected.

**Epistemic status:** Analytical / non-canonical.
