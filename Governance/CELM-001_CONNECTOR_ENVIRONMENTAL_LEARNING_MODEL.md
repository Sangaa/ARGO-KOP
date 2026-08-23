# CELM-001 — Connector Environmental Learning Model

Status: ACTIVE / ARCHITECTURAL LEARNING
Date: 2026-08-23
Scope: ARGO KOP connector environments, initially GitHub

## 1. Purpose

ARGO must learn the environment through which it operates before using that environment to plan or execute repository work.

A connector is not merely a transport mechanism. It is an environmental boundary with its own provider capabilities, implementation choices, exposed operations, dependencies, filters, transformations, errors, and observation limits.

## 2. Core analogy

ARGO treats a new connector environment as an inhabited world:

- ARGO KOP is the home.
- The external provider is the surrounding environment.
- The connector is the boundary/bridge between home and environment.
- Exposed operations are accessible territory.
- Capability knowledge is the map.
- Controlled probes are exploration.
- Behavioral rules are learned environmental laws.
- Repository mutations are expansion and therefore require prior boundary knowledge.

ARGO must not confuse the environment with its home, nor assume that an observed boundary is the provider's boundary.

## 3. Environmental learning sequence

`Identify Provider → Inventory Connector → Map Exposure → Study Scope → Map Dependencies → Safe Training → Build Behavioral Model → Build Evidence Model → Define Boundaries → Plan Work → Execute`

This sequence applies before connector-dependent planning whenever the connector is new, materially changed, or insufficiently understood.

## 4. Five-layer separation

Every connector-dependent observation must distinguish:

1. Provider capability — what the external provider supports.
2. Connector implementation — what the connector code implements.
3. Connector contract — what the connector declares or guarantees.
4. Session exposure — what the current model can actually invoke.
5. Observed behavior — what the invoked operation actually returned.

No layer may be inferred solely from another layer.

## 5. Tool understanding model

For every important operation, ARGO should learn:

- purpose and scope
- accepted inputs
- provider endpoint or underlying operation when observable
- upstream object dependencies
- downstream objects reachable
- filtering and query restrictions
- response transformation
- pagination behavior
- error classes
- permission behavior
- empty-result semantics
- positive evidence semantics
- negative-evidence limits
- correlations required with other tools

The goal is not merely to know how to call a tool, but to know what conclusions its output can legitimately support.

## 6. Evidence semantics

ARGO must distinguish at minimum:

`NO DATA`
`NO MATCH`
`FILTERED`
`NOT EXPOSED`
`NOT AUTHORIZED`
`INVALID INPUT`
`PROVIDER ERROR`
`CONNECTOR ERROR`
`SESSION LIMITATION`
`UNKNOWN`

An empty response is never automatically interpreted as absence in the external world.

## 7. Safe expansion rule

Read-only capability learning precedes mutation learning. Mutation is allowed only after the relevant scope, dependency, evidence, and failure behavior are sufficiently understood and the governing build protocol authorizes the action.

For uncertain capabilities, ARGO must prefer:

`discover → read → correlate → document → then mutate`

rather than guessing or widening the connector surface unnecessarily.

## 8. Training record requirement

Each learned behavior must be persisted as reusable knowledge containing:

`Tool → Input → Layer → Observation → Interpretation → Evidence strength → Boundary → Reuse rule`

Training results must survive the session and be available to later models.

## 9. Operational learning / Knowledge Delta

Connector knowledge must continue to grow during real work. A tool invocation made for a substantive repository task is also a learning opportunity.

When actual use reveals an error, limitation, unexpected capability, filtering rule, dependency, better invocation pattern, or any other behavior not represented accurately in the current model, ARGO must record a `Knowledge Delta` rather than silently adapting its plan.

A Knowledge Delta must contain:

`KD-ID → Tool → Previous Knowledge → Action → Expected Behavior → Observed Behavior → Difference → Layer → Evidence → Evidence Strength → Classification → Impact → Follow-up → Reusable Rule`

Knowledge Delta classification must distinguish at least:

`KNOWN`
`NEW OBSERVATION`
`POSSIBLE BUG`
`CONNECTOR LIMITATION`
`PROVIDER BEHAVIOR`
`MODEL MISUNDERSTANDING`
`UNRESOLVED`

A difference is not promoted to architectural truth until its layer and evidence strength are understood. Repeated or high-impact deltas should trigger targeted re-testing or knowledge-model review.

## 10. Revalidation rule

A later session should reuse validated knowledge and perform only targeted freshness checks unless there is evidence that the provider, connector implementation, contract, exposure surface, or behavior has changed.

Operational learning may override a prior assumption only after the delta is classified and supported by evidence. The latest observation must not silently erase historical knowledge; it should extend, refine, or invalidate it explicitly.

## 11. Current instantiation: GitHub

GitHub is the first fully trained connector environment under this model. `GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md` governs the active training program and `EJR-317_2026-08-23_GITHUB_CONNECTOR_SELF_TRAINING.md` stores the current behavioral observations.

The current P6 investigation must use CELM knowledge before declaring an external boundary. In particular, GitHub Actions Run-ID discovery must be analyzed against all relevant connector layers and independent evidence surfaces rather than against a single Actions wrapper.

## 12. Architectural consequence

CELM is a reusable ARGO architecture pattern, not a GitHub-specific workaround. A future connector should instantiate the same environmental-learning process before ARGO relies on it for substantive work.
