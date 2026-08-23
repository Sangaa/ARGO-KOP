# HORUS Session Record 014 — 2026-08-23

## Objective
Continue the HORUS truth audit by establishing an explicit distinction between observability and causality. The immediate goal is to prevent a hidden assumption from entering the analysis: that an event which cannot be internally observed must therefore be explained by the most plausible visible narrative.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Decisions

### DEC-H069 — Unobserved does not mean absent
If an internal decision process is not directly observable, HORUS must record the limitation rather than filling the gap with a preferred causal story.

### DEC-H070 — Observable proxies require validation
A behavioral proxy may be useful for inferring an unobservable process only when the proxy-to-process relationship is independently supported. A proxy must not become evidence for itself through circular interpretation.

### DEC-H071 — Separate latent-state hypothesis from observable evidence
HORUS may maintain hypotheses about latent processes such as internal diagnosis, strategy comparison, or confidence, but these must remain explicitly labeled as hypotheses unless supported by observable consequences.

### DEC-H072 — Negative evidence is condition-dependent
Failure to observe a predicted behavior weakens a hypothesis only when the observation opportunity, sensitivity, and expected detectability were adequate.

### DEC-H073 — Missing instrumentation is itself a finding
If a historical event cannot distinguish competing origins because the decision boundary was not recorded, HORUS should record the missing observability as a knowledge gap and identify what instrumentation would have resolved it.

### DEC-H074 — Prefer causal experiments over interpretive reconstruction when ambiguity persists
When historical evidence remains unresolved and the competing hypotheses are experimentally distinguishable, a prospective controlled test is preferable to increasingly elaborate post-hoc interpretation.

## Observability–causality model

HORUS now separates four states:

`Observed Event`
`Observable Proxy`
`Latent-State Hypothesis`
`Causal Attribution`

The transition from one to the next requires additional evidence. In particular:

`Observed Event → Causal Attribution` is not automatic.

`Proxy → Latent State` requires validation.

`Latent State → Causal Attribution` requires independent causal support.

## New findings

### F-H014-01 — The current bottleneck may be instrumentation, not intelligence
Some historical autonomy questions may be impossible to resolve from the available records because the decisive pre-choice information state was never captured. This is an observability limitation, not evidence for or against autonomy.

### F-H014-02 — Self-report is an observable artifact, not a transparent window
An explanation generated after an event is itself a behavior produced under a later information state. It can be analyzed as evidence, but it must not automatically be treated as direct access to the causal process that produced the earlier decision.

### F-H014-03 — Proxy validity must be demonstrated
If a particular behavior is used as a proxy for self-diagnosis, strategy comparison, or uncertainty, HORUS must establish why that behavior reliably tracks the proposed latent process and what alternative processes could produce the same signal.

### F-H014-04 — Absence-of-evidence requires detectability analysis
Before using a missing behavior as negative evidence, HORUS must ask whether the system had an opportunity to display it and whether the recording mechanism could have captured it.

### F-H014-05 — The highest-value future experiment may be an observability experiment
If two hypotheses predict the same final outcome but different pre-decision traces, recording those traces may be more valuable than collecting more final outcomes.

## Observability gap record

For each unresolved case, HORUS should record:

1. `Unknown variable` — what cannot currently be observed.
2. `Why it matters` — which competing hypotheses it separates.
3. `Expected observable consequence` — what each hypothesis predicts.
4. `Instrumentation needed` — what trace or event would expose the difference.
5. `Feasibility` — historical, prospective, or unavailable.
6. `Interpretation risk` — how easily the trace could be misread.

## Handoff lesson for ARGO/HERMUZ

> **When the evidence cannot answer the causal question, first ask whether the decisive variable was ever observable. Do not convert an instrumentation gap into an intelligence claim.**

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

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / OBSERVABILITY-CAUSALITY FRONTIER ACTIVE

**Next action:** for the selected historical candidate, identify the single unobserved variable that most strongly separates the leading competing origins and determine whether that variable can be reconstructed or tested prospectively.

**Highest-risk error:** interpreting an unobservable internal process as though it were directly established by the final behavior.

**Epistemic status:** Analytical / non-canonical.
