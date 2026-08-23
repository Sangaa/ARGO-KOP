# HORUS Session Record 012 — 2026-08-23

## Objective
Execute the next HORUS truth-audit step: define the distinction between evidence that a learning event is reproducible and evidence that its origin is independently attributable. Strengthen the historical-case procedure without promoting any autonomy capability.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H057 — Reproducibility and attribution are orthogonal
A behavior can be highly reproducible while its origin remains unresolved. Reproducibility therefore cannot substitute for attribution evidence.

### DEC-H058 — Controlled repetition must preserve the causal question
Repeating an event while unintentionally preserving the same guidance, retrieval path, or task constraint can reproduce the behavior without testing independent origin.

### DEC-H059 — Change one causal dimension at a time where feasible
When testing origin, the strongest experiments alter one relevant factor while holding other factors as stable as practical. This is an analytical design principle, not a requirement that historical evidence satisfy laboratory standards.

### DEC-H060 — Historical reconstruction and prospective testing have different evidentiary roles
Historical evidence can discover candidate events and establish what happened. Prospective controlled tests are often stronger for separating competing causes. Neither should be silently substituted for the other.

### DEC-H061 — Provenance continuity is required for inherited/retrieved explanations
If a strategy is claimed to be inherited or retrieved, the chain connecting the earlier artifact/experience to the later behavior must be demonstrated as far as the available evidence permits.

### DEC-H062 — Autonomous origin requires positive residual evidence
After alternatives are tested, HORUS must identify what positive observation remains specifically supportive of autonomous origin. Autonomy cannot be inferred only from the failure to explain the event otherwise.

## Analytical model: two-dimensional evidence

HORUS now records candidate cases on two separate dimensions:

**Behavioral Evidence Strength**
- Occurrence
- Reproducibility
- Retention
- Transfer

**Origin Evidence Strength**
- Prior-state reconstruction
- Guidance exclusion/control
- Retrieval provenance
- Alternative-cause testing
- Counterfactual strength
- Positive agency signal

A case can therefore be `Behavior Strong / Origin Weak`, `Behavior Strong / Origin Strong`, or any other combination.

## New findings

### F-H012-01 — Strong behavior with weak origin is a valid and useful state
A case may be an excellent demonstration of learning-like behavior while remaining insufficient to identify how the strategy originated. This should not be treated as a failed experiment.

### F-H012-02 — Repetition can become circular
If the same prompt, same retrieval state, same evaluator signal, and same task structure are repeated, repeated success may only demonstrate stability of the whole pipeline. It does not isolate ARGO's contribution.

### F-H012-03 — Origin evidence needs an independent signal
The most valuable future cases are those where the evidence for agency is not derived from the same behavior being explained. Examples include a pre-decision diagnosis, explicit comparison among viable strategies, or a changed-context choice where the relevant principle had not been supplied.

### F-H012-04 — Prospective testing can resolve historical ambiguity
If a historical case is `Unresolved`, that status can guide a new controlled experiment designed around the exact competing explanations. The historical uncertainty is preserved rather than rewritten.

### F-H012-05 — A clean negative result can improve the theory
If a proposed autonomous behavior disappears when guidance or retrieval is removed, that is evidence against autonomous origin and valuable evidence about the actual dependency structure.

## Candidate evaluation matrix

| Dimension | Question | Status vocabulary |
|---|---|---|
| Occurrence | Did the event happen? | Observed / Unresolved |
| Reproducibility | Does it recur? | Strong / Moderate / Weak / Unknown |
| Retention | Does it persist? | Supported / Unresolved |
| Transfer | Does it survive meaningful context change? | Supported / Unresolved |
| Prior state | What was available before choice? | Reconstructed / Partial / Unknown |
| Guidance | Was strategy supplied or narrowed? | Controlled / Present / Unknown |
| Retrieval | Can prior origin be traced? | Traced / Partial / Unknown |
| Alternatives | Were competing causes tested? | Tested / Partial / Not tested |
| Counterfactual | Is there a meaningful comparison? | Strong / Moderate / Weak / None |
| Positive agency | Is there independent evidence of selection? | Supported / Weak / None |
| Overall origin | What can be claimed? | Supported / Weakened / Unresolved / Ruled Out |

## Handoff lesson for ARGO/HERMUZ

> **A repeatable behavior is evidence about behavior. It becomes evidence about autonomous origin only when the experiment or record separates ARGO's choice from the surrounding pipeline.**

This is analytical knowledge only; no implementation mutation is implied.

## Current capability posture

No capability promotion.

- Learning behavior: supported.
- Behavioral reproducibility: case-dependent and testable.
- Autonomous strategy origin: unresolved.
- Independent strategy selection: not proven.
- Strategy improvement: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / TWO-DIMENSIONAL EVIDENCE FRONTIER ACTIVE

**Next action:** select the first high-quality historical case and score behavioral evidence separately from origin evidence, then identify the single missing observation with the highest potential to discriminate between competing origins.

**Highest-risk error:** treating repeated success of the entire pipeline as repeated proof of autonomous agency.

**Epistemic status:** Analytical / non-canonical.
