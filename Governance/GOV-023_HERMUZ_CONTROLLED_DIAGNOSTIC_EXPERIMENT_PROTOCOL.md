# GOV-023 — HERMUZ Controlled Diagnostic Experiment & Observation Protocol

Document ID: GOV-023
Status: Proposed Canonical Governance Artifact — pending governance review
Category: Governance / Engineering / Diagnostic Method
Parent Operating Contract: `GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
Identity migration: from colliding historical `GOV-015_HERMUZ_CONTROLLED_DIAGNOSTIC_EXPERIMENT_PROTOCOL.md`; Proposed status unchanged.

## 1. Purpose

This protocol defines the reusable diagnostic experiment used when prior ARGO knowledge does not adequately explain a material problem, before modifying ARGO methodology or production architecture.

It is also the mandatory pre-flight and post-flight model for any new diagnostic test intended to inspect repository behavior, connector capability, execution surfaces, or unexpected effects.

The protocol is diagnostic-first. It does not grant production authority and does not promote experiment evidence into architectural/runtime evidence automatically.

## 2. Entry Gate

Before designing a new experiment:

`Problem Definition → Prior-Learning Retrieval → Prior-Evidence Review → Bounded Simulation → Verified Gap → Controlled Experiment`

A new experiment is justified only when prior learning fails to explain or safely resolve the observed problem, or when a new test is required to validate an unresolved hypothesis.

## 3. Fresh-Baseline Rule

When historical evidence may contaminate interpretation, create a fresh controlled experiment from a known repository state/ref.

Record baseline commit/ref, pre-existing relevant objects, experiment branch/ref, exact mutation, expected primary effect, observation surfaces and cleanup plan.

Historical experiments remain learning/evidence, not automatic ground truth for the fresh experiment.

## 4. Layered Test Model

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

The experiment must record the first layer at which a result differs from prediction.

## 5. Blind Repository Sweep

After a controlled mutation, search broadly for its unique marker and observable traces, not only in the expected path.

A negative search result is not proof of absence when the search surface has different indexing, ref, permissions, timing, or coverage semantics.

Use at least the applicable retrieval diversity required by GOV-013 §5, then perform direct verification where an authoritative identity is known.

## 6. Observation Context

Every observation must be interpreted with:

`Object + Repository + Ref + Commit + Observation Surface + Index State + Identifier + Permissions + Timing`

`NOT FOUND` must not be promoted to `ABSENT` without sufficient independent evidence.

## 7. Effect-Surface / Causal Review Gate

If an operation produces an observed change outside its expected primary result, do not label it a side effect and stop.

Required sequence:

`Observed Change → Locate Affected Layer → Trace Back to Trigger/Operation → Identify Intermediate Mechanism → Explain Why It Was Not Predicted → Update Model → Classify Effect`

Final classification may be EXPECTED/REQUIRED, EXPECTED/PROPAGATED, INCIDENTAL/BENIGN, UNACCEPTABLE/RISK, or UNKNOWN/REQUIRES INVESTIGATION.

## 8. No-Side-Effect-by-Default Rule

An unexpected effect is not random or irrelevant merely because it was not part of the original objective. Temporal coincidence alone does not prove causation, but a materially relevant observed change requires causal investigation before dismissal.

## 9. Execution Boundary Rule

A test may prove only the surface it actually observes.

`Direct Read ≠ Search Proof`
`Commit Evidence ≠ Workflow Evidence`
`Workflow PASS ≠ Relationship Authority`
`Synthetic Evidence ≠ Production Evidence`
`PR Existence ≠ Execution Identity`

## 10. Controlled Mutation Rule

Diagnostic writes must use an isolated branch/ref whenever practical.

`Pre-check → Isolated Change → Immediate Read-back → Layered Observation → Causal Analysis → Cleanup → Post-cleanup Verification → Evidence Capture`

## 11. Test-Effectiveness Gate

Before accepting a new diagnostic test as reusable methodology, verify a defined hypothesis, pre-specified expected observation, sufficient isolation, enumerated observation surfaces, negative/blind search where relevant, causal review of unexpected effects, cleanup, reproducible discriminatory value, limitations and repository read-back.

A successful test is not automatically an effective test.

## 12. Promotion Gate

A diagnostic method may be proposed for permanent methodology only after:

`Experiment Result → Reproducibility / Material Value → Limitation Review → Existing-Protocol Conflict Check → Canonical Documentation → Governance Review`

## 13. Closure Record

Every completed diagnostic experiment must leave hypothesis, baseline, layers tested, observations, unexpected effects, causal explanation status, limitations, cleanup state, production impact, learning classification and next experiment/safe continuation point.

## 14. Relationship to GOV-013

GOV-023 supplements GOV-013. It does not override prior-learning retrieval, safe mutation, integration verification, learning promotion, post-change verification or session closure rules.
