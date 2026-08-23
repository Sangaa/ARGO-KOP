# GOV-017 — HERMUZ Connector Self-Learning Protocol

Status: `PROPOSED — GOVERNANCE REVIEW REQUIRED`
Version: `1.0.0`
Scope: `Connector capability discovery, simulated tool training, runtime planning`
Primary case: `GitHub connector`

---

## 1. Purpose

ARGO MUST learn the capabilities and limits of the active external communication connector before designing a material investigation, execution plan, test strategy, or solution that depends on that connector.

The connector is not merely a transport path to a repository. It is an operational environment with its own capability surface, wrappers, filters, permissions, error behavior, pagination rules, mutation authority, and observation boundaries.

Therefore the correct order is:

`Connector Discovery → Capability Inventory → Capability Classification → Bounded Tool Training → Behavioral Evidence → Connector Knowledge Model → Repository Inspection → Execution Plan`

The repository remains the object of engineering work, but the connector must first be understood as part of the operating environment.

---

## 2. Foundational Rule

> **ARGO MUST inspect the tool it will use before assuming what the tool can reveal or change.**

A connector capability MUST NOT be inferred solely from:

- the provider's public API documentation;
- a repository implementation;
- a similarly named operation;
- an earlier session's memory;
- one successful or failed probe;
- the absence of a result from a filtered wrapper.

The active session surface is itself evidence and MUST be characterized independently.

---

## 3. Five Distinct Capability Layers

ARGO MUST distinguish at least:

1. **Provider Capability** — what the external provider/API can do.
2. **Connector Implementation** — what the repository-side connector implements.
3. **Connector Contract** — what the repository/interface declares.
4. **Session Exposure** — what the current AI/tool environment actually exposes as callable operations.
5. **Observed Behavior** — what the exposed operation actually returns or changes under controlled use.

These are not interchangeable:

`Provider Capability ≠ Connector Implementation ≠ Connector Contract ≠ Session Exposure ≠ Observed Behavior`

A capability may exist at one layer and be unavailable at another.

---

## 4. Mandatory Connector Boot Sequence

At the start of a new material session, before selecting a solution path, HERMUZ SHOULD perform the following bounded discovery:

### C0 — Identify Connector

Record:
- connector/provider identity;
- authenticated account or installation where observable;
- target repository/account scope;
- read/write/administrative permissions where observable;
- known restrictions and wrapper-specific limits.

### C1 — Inventory Available Operations

Enumerate the complete exposed operation surface available to the session, grouped by capability family.

For GitHub this includes, where exposed:
- repository discovery;
- repository metadata;
- files/blobs/trees/commits/refs;
- branches and comparisons;
- pull requests and reviews;
- issues/comments/reactions;
- statuses/checks;
- Actions workflows/runs/jobs/logs/artifacts;
- account/installation metadata;
- search and discovery;
- mutation operations;
- retry/re-execution operations.

The inventory MUST distinguish **available**, **not exposed**, **unknown**, and **not applicable**.

### C2 — Classify Operations

Each operation SHOULD be classified as:

`READ | WRITE | EXECUTE | OBSERVE | DISCOVER | MUTATE | RETRY | ADMIN`

and additionally by:

`DIRECT | FILTERED WRAPPER | DERIVED | DOWNSTREAM`

### C3 — Behavioral Training

Before relying on an unfamiliar operation, HERMUZ SHOULD perform the smallest safe simulation or read-only probe that can establish its actual behavior.

Training SHOULD test:
- accepted parameters;
- result shape;
- filtering behavior;
- scope limitations;
- pagination behavior;
- identifier requirements;
- error classification;
- mutation side effects where safe;
- relationship to neighboring operations.

Destructive or production mutations MUST NOT be used merely for training.

### C4 — Capability Map

Persist a connector capability map containing:

`Operation → Purpose → Parameters → Scope → Classification → Observed Behavior → Limits → Evidence Quality → Reusable Guidance`

### C5 — Plan Against the Map

Only after C0–C4 may HERMUZ select the connector operations used for repository analysis or execution.

If a required capability is not exposed, HERMUZ MUST search the complete available surface for an alternative evidence channel before declaring an external boundary.

---

## 5. Training as Simulation, Not Blind Probing

Connector training is a controlled learning activity, not repeated trial-and-error.

Each training case SHOULD contain:

- training ID;
- operation;
- hypothesis;
- minimal input;
- expected behavior;
- actual behavior;
- interpretation;
- limitation discovered;
- reuse rule;
- whether canonical mutation was involved.

A failed training case is valuable when it distinguishes among:

`Wrong Operation | Wrong Parameter | Wrapper Limitation | Permission Boundary | Provider Rejection | Missing Identifier | Filtering | Pagination | Runtime Exposure | Unknown`

---

## 6. Evidence Rules

ARGO MUST distinguish:

`No Result` from `No Execution`.

It MUST also distinguish:

`Endpoint Exists` from `Endpoint Is Exposed`;

`Operation Exists in Code` from `Operation Is Callable`;

`Capability Exists` from `Capability Was Observed`.

An empty result from a filtered wrapper MUST NOT be generalized to the underlying provider unless the wrapper's scope is known and sufficient.

---

## 7. Self-Learning Output

Connector training MUST produce reusable knowledge, not only a session-local conclusion.

At minimum, durable learning SHOULD preserve:

- capability inventory;
- tested operations;
- observed restrictions;
- successful usage patterns;
- failed usage patterns;
- misleading operation names or wrappers;
- evidence-channel substitutions;
- safe alternatives;
- prohibited assumptions;
- implications for future session boot;
- regression cases for important connector laws.

This connects directly to `CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT`:

`Observation → Hypothesis → Training → Validation → Connector Knowledge → Reuse`

---

## 8. Connector Knowledge Must Affect Architecture

Validated connector knowledge MUST be allowed to change:

- investigation order;
- evidence-source selection;
- test design;
- simulation strategy;
- mutation strategy;
- failure classification;
- session bootstrap;
- runtime planning;
- regression coverage.

The connector knowledge layer is therefore part of ARGO's operational intelligence, not an optional troubleshooting note.

---

## 9. GitHub-Specific Training Requirement

For the currently connected GitHub surface, HERMUZ SHOULD maintain a reusable inventory covering as much of the exposed  operation surface as practical, grouped at least into:

`Account/Installation → Repositories → Git Objects → Branches → Commits → PRs → Reviews → Issues → Search → Status/Checks → Actions Runs → Jobs → Logs → Artifacts → Mutations → Retry/Execution`

The training record MUST explicitly identify wrapper-specific limitations discovered during P6 work, including the distinction between:

- commit-to-workflow-run helper scope;
- generic fetch restrictions;
- downstream run/job/artifact operations;
- unavailable workflow-dispatch or general run-discovery exposure;
- repository-side implementation versus session exposure.

This section is a training target, not a claim that every provider endpoint must be exposed.

---

## 10. Relation to Session Boot

This protocol extends the repository-first boot model.

The preferred sequence becomes:

`Connector Boot → Connector Capability Learning → Repository Boot → Problem Classification → Prior Learning → Evidence Plan → Simulation → Execution → Verification → Learning Transfer → Session Closure`

A new session SHOULD NOT repeat connector discovery from zero if a current, validated capability model exists. It SHOULD verify the model's identity/version and run only the required freshness checks.

---

## 11. Promotion Boundary

Connector observations become reusable rules only after validation and appropriate governance review.

`Training Record ≠ Canonical Rule`

A connector limitation observed once remains scoped to its evidence until reproduced or otherwise validated.

Repeated evidence may justify promotion into a connector law, regression test, boot requirement, or architecture rule through the applicable governance path.

---

## 12. Anti-Patterns

The following are prohibited as reasoning shortcuts:

- `Unknown tool surface → assume unavailable`;
- `Provider API docs → assume session callable`;
- `Repository code exists → assume session exposure`;
- `Empty filtered result → assume no execution`;
- `One failed probe → redesign architecture`;
- `Known operation name → assume identical semantics`;
- `Repeated probe → learning` without a new hypothesis;
- `Missing downstream ID → invent an ID`;
- `Connector limitation → mutate repository logic` without architectural evidence.

---

## 13. Current P6 Application

The P6 investigation exposed the need for this protocol.

The current validated chain is:

`GitHub REST capability → Actions Connector contract → Actions Connector implementation → session exposure → observed execution`

The first three layers have been verified for `list_workflow_runs(head_sha=...)`; session exposure has not.

Therefore the immediate P6 problem must be analyzed using the complete connector capability map rather than repeated Actions-only probes.

The connector-learning program MUST be used to search for alternative evidence channels before declaring the execution boundary final.

---

## 14. Required Training Artifact

A durable GitHub connector training record SHOULD accompany the first implementation of this protocol and be refreshed when the exposed connector surface materially changes.

Recommended record:

`EJR/EJR-317_2026-08-23_GITHUB_CONNECTOR_SELF_TRAINING.md`

The training record is evidence and learning, not a replacement for provider documentation.

---

## 15. Safety

This protocol does not grant additional repository authority.

All canonical mutations remain governed by existing constitutional, governance, authorization, integrity, and session protocols.

Connector learning MUST prefer read-only training. Any write training requires explicit bounded scope, reversibility, read-back, and session closure.

---

End of Document
