# HORUS Session Record 018 — 2026-08-24

## Objective
Advance the HORUS truth audit by separating three questions that are often collapsed into one: whether a strategy existed, whether ARGO selected it, and whether ARGO understood why it worked. The goal is to prevent successful execution from being mistaken for selection, and selection from being mistaken for understanding.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H093 — Existence, selection, and understanding are separate claims
Evidence that a strategy was available does not prove ARGO selected it. Evidence that ARGO selected it does not prove ARGO understood its causal validity.

### DEC-H094 — Availability is not agency
A strategy appearing in memory, retrieval results, tools, examples, or the environment establishes availability, not authorship or selection.

### DEC-H095 — Selection requires decision-boundary evidence
A claim that ARGO selected among alternatives requires evidence that alternatives were available or representable and that the observed choice was attributable to ARGO rather than an externally imposed path.

### DEC-H096 — Understanding requires counterfactual competence or equivalent evidence
A successful explanation or execution does not by itself establish understanding. Stronger evidence requires the system to use the underlying principle appropriately when relevant surface details change, or otherwise demonstrate a validated causal model.

### DEC-H097 — Transfer must be mechanism-sensitive
Transfer to a new context is stronger evidence of abstraction when the transferable invariant is the causal principle rather than superficial similarity. Surface-level reuse must not be mislabeled as conceptual understanding.

### DEC-H098 — Failure under changed conditions is diagnostically valuable
If a strategy transfers only when surface cues remain similar, the result may indicate pattern reuse rather than mechanism-level understanding.

## Three-layer evidence model

HORUS now records:

`Strategy Existence`
→ `Strategy Selection`
→ `Strategy Understanding`

with separate evidence requirements.

### Layer 1 — Existence
Questions:
- Was the strategy available?
- When did it first become observable?
- What provenance supports its existence?

### Layer 2 — Selection
Questions:
- What alternatives existed?
- Were they accessible at the decision boundary?
- Was the choice constrained or externally specified?
- Is there evidence ARGO selected rather than merely executed?

### Layer 3 — Understanding
Questions:
- Can ARGO identify the invariant principle?
- Can it distinguish causal features from surface features?
- Can it adapt the principle when surface conditions change?
- Can it predict relevant consequences before execution?

## New findings

### F-H018-01 — Successful execution is the weakest of the three claims
Execution can be produced by retrieval, imitation, direct guidance, or fixed procedural pathways. It establishes that the behavior occurred, not who selected it or whether its mechanism was understood.

### F-H018-02 — Selection is stronger than execution but weaker than understanding
If evidence shows ARGO compared meaningful alternatives and chose one under controlled conditions, selection becomes supported. That still does not establish a causal model of why the selected strategy works.

### F-H018-03 — Understanding should survive meaningful surface change
A strategy that works only when the original surface pattern remains intact provides weaker evidence of abstraction than a strategy that adapts correctly when irrelevant surface details change while the causal structure remains stable.

### F-H018-04 — Counterfactual prediction is a strong understanding signal when validated
If ARGO can predict what should change when a causal factor is manipulated, and those predictions are independently validated, this is stronger evidence than retrospective explanation alone.

### F-H018-05 — Wrong transfer can expose the boundary of learned knowledge
A systematic failure under a controlled context change can reveal which feature ARGO actually learned. Failure is therefore evidence about representation, not merely lack of capability.

### F-H018-06 — Understanding must not be inferred from language fluency
A coherent explanation can be generated from retrieved text, learned linguistic patterns, or post-hoc rationalization. Explanation quality therefore requires independent behavioral or predictive corroboration.

## Claim ladder

- `E0 — Executed`: behavior occurred.
- `E1 — Available`: strategy provenance/availability established.
- `E2 — Selected`: controlled evidence supports ARGO's choice among alternatives.
- `E3 — Abstracted`: behavior transfers across meaningful surface changes while preserving the relevant mechanism.
- `E4 — Mechanistically supported`: validated predictions/manipulations show that the system tracks the relevant causal structure.

These are evidence states, not capability labels or claims of consciousness.

## Handoff lesson for ARGO/HERMUZ

> **Do not confuse doing the right thing with choosing the method, and do not confuse choosing the method with understanding why it works. Test the three claims separately.**

This is analytical knowledge only; no implementation mutation is implied.

## Current capability posture

No capability promotion.

- Learning framework: strongly evidenced.
- Learning behavior: supported.
- Strategy availability: case-dependent and provenance-sensitive.
- Independent strategy selection: not proven globally; testable case-by-case.
- Mechanism-level understanding: not proven.
- Strategy improvement: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / EXISTENCE-SELECTION-UNDERSTANDING FRONTIER ACTIVE

**Next action:** take the strongest historical candidate and score it independently at E0–E4. Identify the highest layer actually supported and the exact evidence gap preventing the next promotion.

**Highest-risk error:** interpreting a successful, fluent, or repeatable execution as proof that ARGO selected and understood the underlying strategy.

**Epistemic status:** Analytical / non-canonical.
