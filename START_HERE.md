# START HERE

ARGO KOP is a repository-first cognitive engineering platform.

Do not begin by assuming that folder names, previous sessions, ZIP snapshots, or remembered structure represent current repository reality.

## Recommended Entry Sequence

**START HERE**

↓

**README**

↓

**VISION**

↓

**PROJECT BOOTSTRAP**

↓

**PROJECT STATUS**

↓

**SYSTEM MAP**

↓

**PLATFORM IDENTITY / MANIFEST**

↓

**MASTER INDEX**

↓

**REPOSITORY RELATIONSHIP MAP**

↓

**ARCHITECTURE / LIFECYCLE / COGNITION / MODELS / INTERFACES / RUNTIME / ENGINE**

↓

**Relevant Project or Engineering Domain**

---

## First Rule

**Inspect the current repository before proposing structural changes.**

The repository is the current evidence source. Session memory, historical snapshots, and prior claims may provide context but cannot override inspected repository content.

If required content is unavailable, record the evidence gap rather than filling it by assumption.

## Current Phase

ARGO KOP is currently under **Connected-Baseline Integrity Validation**, moving from bounded seam-evidence construction into repository-wide connectivity proof.

The latest closed checkpoint is **EJR-110 — Canonical Execution Trace Producer and Pipeline Wiring (2026-08-12)**.

The canonical-spine scanner treats same-file endpoint co-occurrence as a candidate `PARTIAL` signal and returns bounded repository-relative candidate artifact locations. The gap-map layer preserves that provenance without changing the seam state. Verified seam promotion remains gated by complete, materialized contract/test/trace evidence through the registry and canonical audit.

The current high-value finding is the **Execution → Execution Trace → Outcome** seam. Provenance guards now exist at execution and outcome evaluation boundaries, and a bounded canonical execution-trace producer has now been materialized and proven capable of feeding the learning pipeline in an executable integration test. The live application-executor → producer invocation path remains unproven, so the broader seam is still **PARTIAL / UNPROVEN LIVE PRODUCER PATH**, not `CONNECTED`.

## Current Connectivity Chain

```text
Canonical Spine Evidence Scanner
        ↓
Candidate Seam Records + Bounded Provenance
        ↓
Concrete Artifact Inspection
        ↓
Contract + Executable Test + Trace
        ↓
Verified Seam Evidence Loader
        ↓
Verified Seam Evidence Registry
        ↓
Canonical Spine Integration Audit
        ↓
Full Repository Connectivity / End-to-End Audit
        ↓
GAP MAP + Candidate Provenance
        ↓
Highest-Value Seam Fixes
        ↓
Regression Test
        ↓
Re-Audit
```

For the current Execution/Outcome path, the focused construction chain is:

```text
Decision
   ↓
Actual Execution Entrypoint
   ↓
Canonical Execution Trace Producer
   ↓
Execution Trace (canonical trace_id)
   ↓
Outcome Producer
   ↓
Outcome Evaluation
   ↓
Feedback Quality
   ↓
Learning Readiness
   ↓
Existing Promotion Gate
```

The governing question is no longer merely whether individual artifacts exist or work independently. The current question is whether the repository behaves as one connected system, with evidence-backed seams from source through execution to outcome.

## Current Next Target

**Locate the actual execution entrypoint and wire it to the canonical execution-trace producer only if the existing architecture supports that connection. Then prove the resulting trace ID reaches the actual outcome path.**

The required proof is:

**Actual Execution → Producer Invocation → Canonical Trace Creation → Trace ID Propagation → Actual Outcome Creation → Outcome Evaluation → Executable Integration Test → Trace/Evidence Artifact**

The producer added in EJR-110 is deliberately bounded: it records a completed execution result; it is not an executor and it does not grant authorization.

Candidate provenance is a navigation aid only. It is not verification evidence and must not be promoted by itself.

The GAP MAP may carry candidate file locations so the next review step can go directly from a gap to the artifacts that caused it to become a candidate. Candidate locations never change `MISSING` or `PARTIAL` into `CONNECTED`.

No seam should be promoted merely because a plausible contract name, test name, trace label or same-file keyword co-occurrence exists. Candidate evidence must be inspected as a coherent relationship and must be materialized repository files.

The connectivity audit must look for, at minimum:

- files that exist but are not connected;
- contracts that have no real runtime consumer;
- tests that do not exercise a real path;
- traces that do not reach an outcome;
- completed layers whose seams are missing;
- paths that start but do not terminate;
- paths that terminate without evidence;
- components that exist but are unreachable;
- learning paths that do not return correctly to Memory/State;
- execution traces that are defined but are not actually propagated into downstream outcomes;
- producers that exist only as test utilities without a real runtime caller.

Do not expand features or architecture merely because the loader, registry, scanner, gap-map or producer is implemented.

## Required Resumption Sequence

1. Load current repository state.
2. Load the verified seam registry.
3. Confirm the latest checkpoint and inspect its changed artifacts.
4. Enumerate actual seam candidates from repository artifacts.
5. Use same-file scanner results and bounded candidate provenance only to prioritize inspection.
6. Inspect contract + executable test + trace together.
7. Locate the actual runtime execution entrypoint.
8. Determine whether it can invoke the canonical trace producer without creating a parallel runtime architecture.
9. Validate trace identity propagation from execution into outcome.
10. Populate the registry only with complete evidence sets.
11. Run the canonical spine integration audit.
12. Generate the GAP MAP while preserving bounded candidate provenance.
13. Expand to repository-wide connectivity / end-to-end audit.
14. Fix the highest-value missing seams.
15. Run regression tests.
16. Re-run the audit.
17. Close the checkpoint.

## Future Engineering Capability Targets

These are **future capability targets, not current execution work**. They must not interrupt the connected-baseline audit.

### Programming and Mathematics Learning Capability

After the connectivity baseline is sufficiently proven, ARGO is expected to acquire implementation capability through a governed learning path:

**Source / Book → Extract Knowledge → Verify Understanding → Practice → Test → Apply → Record Reusable Knowledge**

The learning path should cover programming fundamentals, data structures and algorithms, relevant programming languages, software architecture and testing, followed by mathematics required by the target projects. Learning must be evidence-backed and application-driven rather than quantity-driven.

### Future Project A — Android Applications

Target capability path:

**Programming Fundamentals → Kotlin → Android Development → Architecture → Testing → Real Application Project**

The project begins only when the relevant learning and connectivity gates justify implementation.

### Future Project B — Roblox Game Development + AI

Target capability path:

**Luau → Roblox Studio → Game Architecture → Gameplay Systems → State / Networking → AI Integration → Testing → Optimization**

The intended outcome is to help develop Roblox games and later integrate AI into game experiences through explicit, testable paths between game state, AI input, inference/decision, game action and player feedback.

These future projects are retained as governed capability targets so that current repository work does not lose the intended destination, while avoiding premature feature or architecture expansion.

## Engineering Priority Rule

**Priority is construction quality, connectivity, evidence and reusable learning—not file count.**

A smaller set of correctly connected, tested and documented artifacts is higher-value than a larger set of superficially modified files.

Every substantial session should be treated as potentially closable: preserve what was actually established, record evidence boundaries, identify unresolved work, and leave a deterministic resumption point.

## Before You Modify Anything

1. Read the applicable bootstrap requirements.
2. Enumerate the relevant repository scope.
3. Read the files involved in the proposed change.
4. Verify identities and authority ownership.
5. Trace affected references and consumers.
6. Distinguish verified evidence from inferred or unavailable evidence.
7. Make the smallest justified change.
8. Re-read every changed artifact after writing.
9. Revalidate affected indexes, status claims, and relationships.
10. Check whether the change propagates into upstream or downstream consumers.

## Review Loop

Use the following operational loop during repository review:

**Read Reality → Detect Contradiction → Prove the Contradiction → Correct → Review Impact → Re-read → Verify No New Contradiction → Continue**

Do not mark a change complete merely because the write succeeded.

## Ready State

You are ready to work when you understand:

**what the repository currently contains, what is authoritative, what is historical, what remains uncertain, which relationships your work may affect, and which future capabilities must not be allowed to distract from the current build gate.**

---

End of Document
