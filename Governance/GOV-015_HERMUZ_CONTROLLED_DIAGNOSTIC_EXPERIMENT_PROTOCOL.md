# GOV-015

## HERMUZ — CONTROLLED DIAGNOSTIC EXPERIMENT & OBSERVATION PROTOCOL

Status: Proposed Canonical Governance Artifact — pending governance review
Category: Governance / Engineering / Diagnostic Method
Parent Operating Contract: `GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`

### 1. Purpose

This protocol defines the reusable diagnostic experiment used when prior ARGO knowledge does not adequately explain a material problem, before modifying ARGO methodology or production architecture.

It is also the mandatory pre-flight and post-flight model for any new diagnostic test intended to inspect repository behavior, connector capability, execution surfaces, or unexpected effects.

The protocol is diagnostic-first. It does not grant production authority and does not promote experiment evidence into architectural/runtime evidence automatically.

### 2. Entry Gate

Before designing a new experiment:

`Problem Definition → Prior-Learning Retrieval → Prior-Evidence Review → Bounded Simulation → Verified Gap → Controlled Experiment`

A new experiment is justified only when prior learning fails to explain or safely resolve the observed problem, or when a new test is required to validate an unresolved hypothesis.

### 3. Fresh-Baseline Rule

When historical evidence may contaminate interpretation, create a fresh controlled experiment from a known repository state/ref.

Record:
- baseline commit/ref;
- pre-existing relevant objects;
- experiment branch/ref;
- exact mutation;
- expected primary effect;
- observation surfaces;
- cleanup plan.

Historical experiments remain learning/evidence, not automatic ground truth for the fresh experiment.

### 4. Layered Test Model

Every material diagnostic experiment should separate observation into layers where applicable:

`L0 Connectivity / Authority`
`L1 Read`
`L2 Write / Mutation`
`L3 Direct Observation`
`L4 Blind Repository Search`
`L5 Commit / Change Surface`
`L6 PR / Event Surface`
`L7 Execution / Workflow Surface`
`L8 Secondary Effects`
`L9 Cleanup / Post-State Verification`

The experiment must record the first layer at which a result differs from prediction. This narrows the causal boundary before deeper interpretation.

### 5. Blind Repository Sweep

After a controlled mutation, search broadly for its unique marker and observable traces, not only in the expected path.

A negative search result is not proof of absence when the search surface has different indexing, ref, permissions, timing, or coverage semantics.

Use at least the applicable retrieval diversity required by GOV-013 §5, then perform direct verification where an authoritative identity is known.

### 6. Observation Context

Every observation must be interpreted with its context:

`Object + Repository + Ref + Commit + Observation Surface + Index State + Identifier + Permissions + Timing`

`NOT FOUND` must not be promoted to `ABSENT` without sufficient independent evidence.

### 7. Effect-Surface / Causal Review Gate

If an operation produces an observed change outside its expected primary result, do not label it a "side effect" and stop.

Treat the unexpected change as evidence that the current process/model may be incomplete.

Required sequence:

`Observed Change → Locate Affected Layer → Trace Back to Trigger/Operation → Identify Intermediate Mechanism → Explain Why It Was Not Predicted → Update Model → Classify Effect`

Final classification may be:
- EXPECTED / REQUIRED
- EXPECTED / PROPAGATED
- INCIDENTAL / BENIGN
- UNACCEPTABLE / RISK
- UNKNOWN / REQUIRES INVESTIGATION

"UNKNOWN" is a valid controlled state; it must not be converted into intent or absence by assumption.

### 8. No-Side-Effect-by-Default Rule

An unexpected effect is not treated as random or irrelevant merely because it was not part of the original design objective.

Temporal coincidence alone does not prove causation, but an observed change following a controlled operation requires causal investigation before dismissal when the effect is materially relevant.

The purpose is to discover omitted mechanisms in the operation's actual behavior.

### 9. Execution Boundary Rule

A test may prove only the surface it actually observes.

Examples:

`Direct Read ≠ Search Proof`
`Commit Evidence ≠ Workflow Evidence`
`Workflow PASS ≠ Relationship Authority`
`Synthetic Evidence ≠ Production Evidence`
`PR Existence ≠ Execution Identity`

No lower-level evidence may silently promote a higher-level state.

### 10. Controlled Mutation Rule

Diagnostic writes must use an isolated branch/ref whenever practical. Do not intentionally place experimental markers or mutations on `main` merely for convenience.

Each mutation requires:

`Pre-check → Isolated Change → Immediate Read-back → Layered Observation → Causal Analysis → Cleanup → Post-cleanup Verification → Evidence Capture`

### 11. Test-Effectiveness Gate

Before accepting a new diagnostic test as reusable ARGO methodology, verify:

1. the test had a defined hypothesis;
2. the expected observation was specified before execution;
3. the experiment was isolated sufficiently to control contamination;
4. observation surfaces were explicitly enumerated;
5. blind/negative search was attempted where relevant;
6. unexpected effects were investigated causally;
7. cleanup was verified;
8. the test exposed a reproducible boundary, law, or failure mode;
9. limitations and connector/tool boundaries were recorded;
10. the result was documented and read back from the repository.

A successful test is not automatically an effective test. Effectiveness requires evidence that the test discriminates between competing explanations or materially narrows the unknown.

### 12. Promotion Gate

A diagnostic method may be proposed for permanent ARGO methodology only after:

`Experiment Result → Reproducibility / Material Value → Limitation Review → Existing-Protocol Conflict Check → Canonical Documentation → Governance Review`

Do not modify a specialized ARGO methodology merely because one experiment succeeded or one connector returned an unexpected result.

### 13. Closure Record

Every completed diagnostic experiment must leave a compact closure record containing:

- hypothesis;
- baseline;
- layers tested;
- observations;
- unexpected effects;
- causal explanation status;
- limitations;
- cleanup state;
- production impact (normally NONE);
- learning classification;
- next experiment or safe continuation point.

### 14. Relationship to GOV-013

GOV-015 supplements GOV-013. It does not override its Prior-Learning Retrieval Gate, Three-Search Rule, Safe Mutation Rules, Integration Verification, Learning Promotion Gate, Post-Change Verification, or Session Closure Rule.

When a diagnostic experiment is performed under a HERMUZ session, the experiment and its closure are part of the session evidence/checkpoint chain.
