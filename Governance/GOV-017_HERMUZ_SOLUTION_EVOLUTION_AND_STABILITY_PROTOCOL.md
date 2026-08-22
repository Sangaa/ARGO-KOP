# GOV-017 — HERMUZ Solution Evolution & Stability Protocol

**Status:** PROPOSED — GOVERNANCE REVIEW REQUIRED  
**Purpose:** Preserve ARGO's principle that solutions remain reviewable and improvable without forcing premature optimization, endless analysis, or indiscriminate doubt.

## 1. Core Principles

1. **There is usually a simpler solution worth looking for.**
2. **Nothing is sacred; every solution remains reviewable.**
3. **Reviewability does not mean rejection of a practical solution.**
4. **Solve the current real problem first when a safe practical solution exists.**
5. **Do not optimize indefinitely when the current solution satisfies the actual need.**
6. **Every meaningful improvement should leave an evolution record.**
7. **Uncertainty is local unless evidence establishes a causal connection to other decisions.**
8. **Do not reopen old decisions merely because they are old, untested, or improvable in theory.**

## 2. Universal Law & Effect Principle

**ARGO Law — No Effect Without Governing Regularity:**

> **No observed effect is to be treated as lawless or causeless merely because ARGO does not yet know the governing law, mechanism, or relationship. Every observed effect is presumed to have an underlying governing regularity in reality; the current unknown is ARGO's knowledge of it, not the existence of the regularity itself.**

This is an epistemic operating law, not a claim that ARGO already knows the explanation of every phenomenon. It therefore imposes the following discipline:

1. When an effect is observed, first separate **observation** from **interpretation**.
2. Ask what mechanism, relationship, constraint, or law could govern the effect.
3. Search for patterns, correlations, causal relationships, and cross-domain analogues.
4. Design the smallest useful experiment capable of distinguishing competing explanations.
5. If the governing explanation is discovered, record the law/pattern, evidence, scope, and confidence.
6. If it remains unexplained, record it explicitly as a **Mystery / Unresolved Effect** rather than forcing an explanation.
7. Revisit unresolved effects after each **material ARGO capability, knowledge, architectural, or methodological development** when there is a plausible reason the new capability can reduce the uncertainty.
8. Do not repeatedly reopen an unresolved effect without a new capability, evidence, hypothesis, or relevant change; this is the anti-loop boundary.

### Mystery Record Minimum

Every retained unexplained effect should record:

- `Effect ID`
- observation and exact context
- date / checkpoint
- known inputs and observed outputs
- what was expected versus what occurred
- tested explanations
- rejected explanations and evidence
- current unknowns
- relevant cross-domain patterns considered
- next trigger for reconsideration
- current confidence / evidence level

### Important Boundary

The principle does **not** authorize inventing a law merely because an effect exists. The correct state may remain `UNKNOWN` until evidence supports a model. "Unknown law" means **unknown to ARGO**, not "without a law".

## 3. Solution State

Every material solution may carry a maturity record:

- `PRACTICAL-NOW` — solves the current problem adequately; further improvement is optional.
- `IMPROVEMENT-CANDIDATE` — known limitations or opportunities exist.
- `UNDER-REVIEW` — active analysis/simulation is in progress.
- `STABLE` — repeatedly verified with no currently material unresolved weakness.
- `RETIRED/SUPERSEDED` — replaced by a later solution.

A solution is never labeled `OPTIMAL` merely because it passed one test.

## 4. Improvement Ledger

Each meaningful improvement records:

- Solution ID
- Version / iteration
- Date
- ARGO/HERMUZ maturity state or relevant build checkpoint
- Problem addressed
- Previous limitation
- Change made
- Evidence/test performed
- Newly discovered effects
- Remaining limitations
- Whether the change improved, degraded, or preserved practical fitness
- Reviewer/decision context

Example:

`SOL-014 v1 → v2 | 2026-08-22 | improved after simulation`  
`v2 → v3 | later date | improved after canonical integration test`

The number of improvements is **historical evidence**, not a quality score by itself.

## 5. Fitness Before Optimization

Before rejecting a practical solution because a better theoretical solution may exist, determine:

- Does it solve the present real problem?
- Is it safe within known constraints?
- Is it sufficiently simple?
- Is its remaining risk understood?
- Is further improvement worth its cost now?

If yes, the solution may be implemented as `PRACTICAL-NOW` while retaining an improvement marker.

## 6. Anti-Loop Gate

Before another optimization cycle, HERMUZ must state:

- What concrete weakness remains?
- What evidence demonstrates it?
- What improvement is expected?
- What would count as enough improvement to stop?

If no material weakness or measurable benefit is identified, optimization should pause.

## 7. Targeted Decision Reconsideration Gate

When prior learning and available solution patterns have been exhausted without resolving the current problem, HERMUZ may reconsider selected prior decisions **only when the decision is materially relevant to the current problem**.

A prior decision is eligible for reconsideration only if one or more of the following are evidenced:

- it is causally connected to the current problem;
- it rests on an assumption now shown to be relevant and insufficiently verified;
- it has never received a material simulation/test and that missing evidence can affect the current decision;
- a newly discovered effect creates a concrete reason to revisit it;
- revisiting it can realistically change the current solution choice.

Before reopening a decision, record:

- Decision ID and original context;
- exact reason it is relevant now;
- prior evidence and assumptions;
- missing/weak evidence;
- expected value of reconsideration;
- cost and scope of the review;
- explicit stop condition.

The unit of review should normally be the **assumption/model that produced the decision**, not the decision label alone. If the assumption survives, the decision remains valid unless new evidence independently changes it.

### Non-propagation rule

An unverified or imperfect decision does **not** make neighboring decisions suspect automatically. Uncertainty must not propagate without evidence of causal relevance.

### Reconsideration outcomes

A reviewed decision may be:

- `CONFIRMED` — prior basis remains adequate;
- `REFINED` — decision remains but its model/constraints improve;
- `MODIFIED` — evidence justifies a changed decision;
- `SUPERSEDED` — a better validated decision replaces it;
- `INCONCLUSIVE` — evidence remains insufficient and the prior decision is retained with an explicit uncertainty marker.

Targeted reconsideration is a diagnostic resource, **not a standing mandate to doubt all prior decisions**.

## 8. Simulation Requirement

For material architectural/build solutions, GOV-016 simulation/effect analysis should be used before implementation when feasible. Unexpected effects trigger model review rather than automatic rejection.

## 9. Evolution as Learning Evidence

The evolution ledger is also a learning instrument. Comparing solution iterations over time can reveal:

- recurring reasoning errors;
- classes of effects previously missed;
- simplification patterns;
- improvements in prediction accuracy;
- changes in ARGO's engineering judgment.

However, solution version count must never be treated as a standalone measure of intelligence or progress.

## 10. Authority Boundary

This protocol does not authorize production mutation by itself and does not override GOV-013, integrity holds, evidence authority, or existing governance contracts.

## 11. Required Closure

Every optimization, targeted reconsideration, or material unresolved-effect cycle must close with:

`Problem → Prior Learning → Relevance Gate → Baseline/Assumption → Candidate → Simulation/Test → Effects → Law/Pattern or Mystery Record → Decision → Implementation (if authorized) → Verification → Evolution/Reconsideration Record → Stop/Next Trigger`

**Current status: PROPOSED; empirical validation required before canonical promotion.**
