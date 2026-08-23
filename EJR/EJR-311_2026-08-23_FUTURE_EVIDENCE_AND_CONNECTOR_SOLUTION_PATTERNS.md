# EJR-311 — Future Evidence & Connector Solution Patterns

Date: 2026-08-23
Status: CLOSED / REUSABLE-LEARNING CAPTURED
Classification: Future Solution Patterns / Generative Learning
Scope: GitHub Actions / Connector abstraction / P6 evidence architecture
Production impact: NONE

## 1. Purpose

Preserve useful solution ideas that emerged during P6 investigation even when they are not selected for the current implementation.

ARGO must retain both successful and rejected approaches when they reveal reusable reasoning, failure modes, alternative architectures, or future recovery paths.

This record is a learning artifact, not an authorization to implement any listed pattern.

## 2. Pattern A — Dedicated Actions Capability Surface

### Status
`ACCEPTED / IMPLEMENTED / LIVE E2E PENDING`

### Principle
Repository access, Actions invocation, and execution observation are separate capabilities and should not be silently collapsed into one connector.

### Reusable form
```text
Repository Connector
        +
Actions Control/Observation Connector
```

### Useful operations
- workflow-run discovery with branch/event/head-SHA filters;
- exact workflow-run retrieval;
- workflow dispatch;
- run-job discovery;
- job-log retrieval;
- future artifact discovery/download.

### Why it is valuable
It prevents a narrow repository Contents surface from being mistaken for the full external execution surface.

### Current ARGO evidence
EJR-310 records the implementation and explicitly preserves the live E2E boundary.

## 3. Pattern B — Check-Run / Commit-Centric Discovery

### Status
`FUTURE-CANDIDATE / NOT IMPLEMENTED`

### Idea
Use commit-associated check runs as an additional read-only discovery route when workflow-run collection discovery is unavailable or incomplete.

Conceptual path:
```text
HEAD SHA
   ↓
check-runs
   ↓
CI check identity
   ↓
associated execution evidence
```

### Value
Provides a second independent discovery mechanism and may reduce dependence on a single Actions collection endpoint.

### Constraint
A check run must not automatically be treated as equivalent to a workflow run. The relationship and provenance must be verified before promotion.

## 4. Pattern C — Evidence Publication as a Fallback Channel

### Status
`FUTURE-CANDIDATE / ARCHITECTURALLY USEFUL`

### Idea
When direct execution observation is unavailable, allow the execution environment to publish a signed/structured evidence payload into an independently readable evidence surface.

Conceptual path:
```text
Execution
   ↓
Evidence Publication
   ↓
Observable Storage
   ↓
ARGO
```

### Important refinement
The preferred publication target is an execution-native artifact or other non-mutating evidence surface, not an automatic commit to `main`.

### Why
The idea preserves the useful insight of the proposed out-of-band solution while avoiding repository-state mutation as a side effect of CI observation.

## 5. Pattern D — Artifact-First Evidence Recovery

### Status
`FUTURE-CANDIDATE / STRONGLY RECOMMENDED FOR FUTURE ACTIONS EXTENSION`

The current canonical workflow already emits execution artifacts such as runtime evidence and CI execution identity.

Future Actions connector capability should therefore consider:
- list artifacts for a known run;
- retrieve artifact metadata;
- download an artifact;
- validate artifact provenance against run ID and head SHA.

### Preferred chain
```text
Run ID
  ↓
Artifacts
  ↓
Execution identity
  ↓
Runtime evidence
```

This is preferable to writing evidence back into the source branch because it preserves the executed commit boundary and avoids CI recursion.

## 6. Pattern E — Repository Self-Commit Evidence

### Status
`REJECTED AS PRIMARY P6 PATTERN / RETAINED AS FAILURE-LEARNING`

### Original idea
Have the workflow create `.argo/evidence/p6_latest_execution.json`, commit it, and push it back to the repository.

### Why it was rejected
The approach can create a new repository mutation from inside the workflow and can recursively trigger push-based workflows. It also blurs the distinction between the SHA being tested and the later SHA containing the evidence file.

### Reusable lesson
A failed implementation does not make the underlying evidence-publication idea useless. Preserve the concept, but move publication toward artifacts or a dedicated non-recursive evidence channel.

## 7. Pattern F — Multi-Channel Evidence Convergence

### Status
`FUTURE ARCHITECTURAL CANDIDATE`

Instead of relying on one observation channel, converge independent evidence paths:

```text
                 ┌→ workflow-runs
HEAD / Run ID ───┼→ check-runs
                 ├→ jobs / logs
                 └→ artifacts
                         ↓
                 Evidence Convergence
                         ↓
                    P6 Judgment
```

### Rule
Independent channels increase confidence only when their provenance is actually independent and their identities can be correlated. Duplicate representations of the same inaccessible source do not constitute independent evidence.

## 8. Pattern G — Capability Ladder for Connector Diagnosis

Future connector investigations should distinguish at least:

1. capability exists in provider API;
2. capability is exposed by the connector;
3. capability is invocable;
4. resulting state can be discovered;
5. exact state can be read downstream;
6. absence is actually proven.

This extends the P6 learning already recorded in EJR-294 and EJR-310.

## 9. Pattern H — Exact-ID Before World-State Claims

If a connector can read an exact workflow run, job, or log when an identifier is supplied, that proves observation capability but does not prove discovery capability.

Therefore:

`Exact-ID Observation ≠ Collection Discovery`

and:

`No Discovery ≠ No Resource`

This rule should be reused in future connector audits.

## 10. Pattern I — Evidence Publication Must Preserve Provenance

Any future evidence-publication mechanism should carry, at minimum:

- provider;
- repository;
- workflow identity;
- run identity;
- event;
- ref;
- head SHA;
- execution status/conclusion;
- creation/completion timestamps where available;
- publication channel;
- provenance relationship to the source execution.

A self-authored statement must not be promoted to authoritative execution evidence merely because it contains a plausible run ID.

## 11. Pattern J — Solution Ideas Are Learning Objects

A candidate solution should be preserved even when rejected if it contains reusable knowledge about:

- a new capability;
- a hidden connector boundary;
- a better evidence path;
- a failure mode;
- a side effect;
- a safer alternative;
- a future architecture;
- or a diagnostic method.

Classification should distinguish:

`WORKING / IMPLEMENTED / FUTURE-CANDIDATE / REJECTED-BUT-LEARNED / SUPERSEDED`

This follows the generative-learning principle that novelty is not truth, but failed novelty can still be valuable training evidence.

## 12. Explicit Non-Claims

This record does not establish:

- that GitHub Actions live execution is currently verified from ARGO;
- that the current token has all required Actions permissions;
- that check-runs provide sufficient provenance for P6;
- that artifact retrieval is currently exposed by the conversational connector;
- that any future candidate should be implemented without a new gap analysis.

## 13. Future Reuse Trigger

Revisit these patterns when one of the following occurs:

- direct Actions invocation remains blocked;
- run discovery remains unavailable after E2E connector testing;
- exact run IDs become available but downstream evidence remains inaccessible;
- artifact evidence becomes the preferred execution authority;
- a new connector/provider exposes similar capability gaps;
- P6 or another execution-evidence problem requires a non-mutating fallback.

## 14. Learning Classification

`REUSABLE-LEARNING`

The current preferred architecture remains the dedicated Actions capability surface. The other patterns are retained as future candidates or rejected implementations with preserved learning value.

## 15. Closure

This record intentionally preserves successful, candidate, and rejected solution paths so future ARGO sessions can reason from accumulated experience rather than rediscovering the same design space.

`CLOSED — DOCUMENTED — FUTURE PATTERNS PRESERVED`

End of EJR-311
