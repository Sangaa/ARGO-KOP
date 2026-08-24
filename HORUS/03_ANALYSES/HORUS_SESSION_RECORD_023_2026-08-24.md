# HORUS Session Record 023 — 2026-08-24

## Objective
Advance the HORUS truth audit from identity-preserving transfer to conflict-aware reasoning. Determine what ARGO's recent GitHub learning actually demonstrates about evidence interpretation, and separate contradiction from different evidence layers and unresolved uncertainty.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed by HORUS.

## Evidence reviewed
- EJR-320 — Git object correlation training.
- EJR-321 — Ref/SHA/blob identity training.
- EJR-323 — Actions discovery-boundary training.
- EJR-325 — Evidence hierarchy, evidence layers, and contradiction rules.

## Decisions

### DEC-H099 — Evidence must be compared at proposition level
Two observations should not be called contradictory merely because their text or values differ. HORUS must first align claim, target, scope, relevant time/version, identity, and evidence validity.

### DEC-H100 — Different evidence layers can jointly describe one event
Run metadata, artifact metadata, artifact payload, logs, status surfaces, and derived correlations may answer different propositions. Their differences are often complementary rather than contradictory.

### DEC-H101 — Negative observations require semantic scope
An empty result is evidence about what a specific operation returned under a specific key and scope. It is not automatically evidence that the underlying event or object does not exist.

### DEC-H102 — Discovery-key semantics must be learned, not inferred from parameter names
A field called `commit_sha` does not prove that every SHA associated with an execution is searchable through that operation. Positive and negative controls are required to identify the semantic key.

### DEC-H103 — UNRESOLVED is a valid knowledge state
When identity, scope, time, provenance, or proposition alignment is incomplete, HORUS must preserve uncertainty instead of forcing a binary conclusion.

### DEC-H104 — Evidence dimensions must remain separate
Authority, claim fitness, identity confidence, temporal validity, evidence independence, and completeness should not be collapsed into a single evidence score.

## New analytical finding: Semantic Conflict Boundary

The recent ARGO learning shows a progression:

`Observation`
→ `Identity preservation`
→ `Cross-surface correlation`
→ `Semantic scope`
→ `Conflict classification`
→ `Safe resolution or UNRESOLVED`

This is more advanced than simple evidence collection. It is evidence reasoning.

## Key example

A workflow may support `push`, `pull_request`, and `workflow_dispatch`, while the exposed discovery wrapper may discover only PR-scoped runs. Therefore:

`Workflow capability ≠ Connector discovery capability`

Likewise:

`Empty discovery result ≠ No execution`

when the query key is not semantically aligned with the execution identity.

EJR-323 provides a positive control using the PR head SHA and a negative control using the execution/merge SHA; the same run remains independently identifiable through run ID, event/ref, and `github.sha`. This demonstrates why identity correlation must precede absence claims.

## New finding: Contradiction has a strict entry condition

HORUS adopts the following analytical gate:

`Same Claim`
+ `Same Target`
+ `Same Scope`
+ `Same Relevant Time/Version`
+ `Valid Evidence`
+ `Mutually Exclusive Outcomes`
+ `Identity Alignment`
→ `CONTRADICTION CANDIDATE`

If one or more elements are missing, the correct result may be:

`DIFFERENT EVIDENCE LAYERS`

or

`UNRESOLVED`

rather than contradiction.

This rule is supported by the recent GT-018 learning, where ARGO explicitly separated different evidence layers from genuine contradiction and protected `UNRESOLVED` as a safe state.

## New finding: Truth has a correlation dimension

Previous HORUS analysis established that observation correctness is not sufficient. The current evidence adds a stronger statement:

> A set of individually correct observations can still produce a false conclusion if they are joined using the wrong identity key or interpreted outside their semantic scope.

Therefore truth-audit quality includes at least:

`Observation Correctness`
`Identity Correctness`
`Correlation Correctness`
`Semantic Scope Correctness`
`Inference Correctness`

## Evidence reasoning ladder

- `ER0 — Raw Observation`: an operation returned a value/result.
- `ER1 — Scoped Evidence`: the proposition and operational scope are explicit.
- `ER2 — Identity-Correlated Evidence`: observations are joined through a verified identity key.
- `ER3 — Cross-Surface Corroboration`: independent evidence surfaces support compatible propositions.
- `ER4 — Conflict-Tested Conclusion`: plausible contradictory interpretations were actively tested and classified.
- `ER5 — Controlled Resolution`: a conclusion survives valid precedence rules and remains bounded by its evidence scope.

This is an analytical evidence-quality ladder, not a probability-of-truth scale and not an ARGO capability label.

## Important distinction

A system that learns to classify evidence layers correctly has demonstrated a more sophisticated reasoning behavior than one that merely retrieves evidence. However, even correct classification does not by itself prove autonomous discovery of the rule. The origin/selection/understanding ladder remains separate.

Thus:

`Evidence Reasoning Capability`
≠
`Autonomous Strategy Origin`
≠
`Mechanism-Level Understanding`

## Handoff lesson for ARGO/HERMUZ

> **Do not resolve a disagreement until you prove that the observations are actually talking about the same proposition. Preserve identity, scope, time, and evidence-layer boundaries before choosing between outcomes.**

A second rule follows:

> **An empty result is a bounded observation until its semantic key and coverage are independently established.**

## Current capability posture

No capability promotion.

- Evidence collection discipline: strongly evidenced in bounded training.
- Identity-aware evidence reasoning: strongly supported in bounded GitHub cases.
- Cross-surface correlation: supported.
- Contradiction classification: supported at the recorded rule level; runtime execution not independently established.
- Safe UNRESOLVED handling: supported as a governed reasoning rule; runtime behavior not independently established.
- Autonomous strategy selection: not proven globally.
- Mechanism-level understanding: not proven.
- Strategy improvement: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / CONFLICT-AWARE EVIDENCE REASONING FRONTIER ACTIVE

**Next action:** apply ER0–ER5 to a historical case containing apparently conflicting evidence. Determine whether the conflict is real, cross-layer, identity-misaligned, semantically scoped, or genuinely unresolved. Then compare the result with ARGO's existing recorded conclusion to detect overclaiming or missed evidence.

**Highest-risk error:** treating a connector limitation or query-scope mismatch as evidence about the external world's state.

**Epistemic status:** Analytical / non-canonical.
