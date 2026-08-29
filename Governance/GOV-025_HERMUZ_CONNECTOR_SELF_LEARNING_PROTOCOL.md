# GOV-025 — HERMUZ Connector Self-Learning Protocol

Document ID: GOV-025
Status: `PROPOSED — GOVERNANCE REVIEW REQUIRED`
Version: `1.0.0`
Scope: `Connector capability discovery, simulated tool training, runtime planning`
Primary case: `GitHub connector`
Identity migration: from colliding historical `GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md`; Proposed status unchanged.

## 1. Purpose

ARGO MUST learn the capabilities and limits of the active external communication connector before designing a material investigation, execution plan, test strategy, or solution that depends on that connector.

Correct order:

`Connector Discovery → Capability Inventory → Capability Classification → Bounded Tool Training → Behavioral Evidence → Connector Knowledge Model → Repository Inspection → Execution Plan`

## 2. Foundational Rule

> **ARGO MUST inspect the tool it will use before assuming what the tool can reveal or change.**

A connector capability MUST NOT be inferred solely from provider documentation, repository implementation, similarly named operations, earlier memory, one probe, or absence from a filtered wrapper.

## 3. Five Distinct Capability Layers

ARGO MUST distinguish:

1. Provider Capability.
2. Connector Implementation.
3. Connector Contract.
4. Session Exposure.
5. Observed Behavior.

`Provider Capability ≠ Connector Implementation ≠ Connector Contract ≠ Session Exposure ≠ Observed Behavior`

## 4. Mandatory Connector Boot Sequence

### C0 — Identify Connector
Record connector/provider identity, target scope, permissions where observable, restrictions and wrapper-specific limits.

### C1 — Inventory Available Operations
Enumerate the complete exposed operation surface, including repository discovery, metadata, git objects, branches/commits/PRs/issues, search, statuses/checks, Actions runs/jobs/logs/artifacts, mutations and retry/execution where exposed.

Distinguish `available`, `not exposed`, `unknown`, and `not applicable`.

### C2 — Classify Operations
Classify each operation as `READ | WRITE | EXECUTE | OBSERVE | DISCOVER | MUTATE | RETRY | ADMIN` and `DIRECT | FILTERED WRAPPER | DERIVED | DOWNSTREAM`.

### C3 — Behavioral Training
Before relying on an unfamiliar operation, perform the smallest safe simulation/read-only probe to establish parameters, result shape, filtering, scope, pagination, identifiers, errors, side effects and neighboring-operation relationships.

### C4 — Capability Map
Persist:

`Operation → Purpose → Parameters → Scope → Classification → Observed Behavior → Limits → Evidence Quality → Reusable Guidance`

### C5 — Plan Against the Map
Only after C0–C4 may HERMUZ select connector operations for material repository analysis/execution. Search for alternative evidence channels before declaring a required capability unavailable.

## 5. Training as Simulation, Not Blind Probing

Each training case should include training ID, operation, hypothesis, minimal input, expected/actual behavior, interpretation, limitation, reuse rule and canonical-mutation status.

A failed training case should distinguish among wrong operation/parameter, wrapper limitation, permission, provider rejection, identifier, filtering, pagination, exposure and unknown states.

## 6. Evidence Rules

Distinguish:

`No Result` from `No Execution`;
`Endpoint Exists` from `Endpoint Is Exposed`;
`Operation Exists in Code` from `Operation Is Callable`;
`Capability Exists` from `Capability Was Observed`.

An empty filtered result MUST NOT be generalized to the provider without sufficient scope evidence.

## 7. Self-Learning Output

Connector training must produce reusable knowledge: capability inventory, tested operations, restrictions, successful/failed patterns, wrapper traps, substitutions, safe alternatives, prohibited assumptions, boot implications and regressions.

`Observation → Hypothesis → Training → Validation → Connector Knowledge → Reuse`

## 8. Connector Knowledge Must Affect Architecture

Validated connector knowledge may alter investigation order, evidence-source selection, test/simulation/mutation strategy, failure classification, session bootstrap, runtime planning and regression coverage.

## 9. GitHub-Specific Training Requirement

Maintain a reusable inventory across Account/Installation → Repositories → Git Objects → Branches → Commits → PRs → Reviews → Issues → Search → Status/Checks → Actions Runs → Jobs → Logs → Artifacts → Mutations → Retry/Execution where exposed.

Training must preserve wrapper-specific limitations learned during P6, including commit-to-run helper scope, generic fetch restrictions, downstream run/job/artifact operations and session exposure differences.

## 10. Relation to Session Boot

Preferred sequence:

`Connector Boot → Connector Capability Learning → Repository Boot → Problem Classification → Prior Learning → Evidence Plan → Simulation → Execution → Verification → Learning Transfer → Session Closure`

Do not repeat discovery from zero when a current validated capability map exists; perform freshness checks instead.

## 11. Promotion Boundary

`Training Record ≠ Canonical Rule`

Connector observations become reusable rules only after validation and applicable governance review.

## 12. Anti-Patterns

Prohibited shortcuts include assuming unknown tools unavailable, provider docs imply session callable, repository code implies exposure, empty result means no execution, one failed probe justifies redesign, repeated probing equals learning, invented downstream IDs, or connector limitations justify unrelated repository mutation.

## 13. P6 Learning Boundary

The P6 investigation established the need to separate provider capability, connector contract/implementation, session exposure and observed execution. Future execution planning should use the complete capability map rather than repeated narrow probes.

## 14. Required Training Artifact

A durable GitHub connector training record should accompany application of this candidate and be refreshed when exposure materially changes.

## 15. Safety

This protocol grants no additional repository authority. Connector learning should prefer read-only training; writes require explicit scope, reversibility, read-back and closure.
