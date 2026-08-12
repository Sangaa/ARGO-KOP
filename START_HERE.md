# START HERE

ARGO KOP is a repository-first cognitive engineering platform.

Do not begin by assuming that folder names, previous sessions, ZIP snapshots, or remembered structure represent current repository reality.

## Recommended Entry Sequence

START HERE → README → VISION → PROJECT BOOTSTRAP → PROJECT STATUS → SYSTEM MAP → PLATFORM IDENTITY / MANIFEST → MASTER INDEX → REPOSITORY RELATIONSHIP MAP → ARCHITECTURE / LIFECYCLE / COGNITION / MODELS / INTERFACES / RUNTIME / ENGINE → Relevant Project or Engineering Domain

## First Rule

**Inspect the current repository before proposing structural changes.**

The repository is the current evidence source. Session memory, historical snapshots, and prior claims cannot override inspected repository content.

If required content is unavailable, record the evidence gap rather than filling it by assumption.

## External Advisory Boundary

External model reviews (including Gemini, Copilot, or any other model) are **advisory and test-only inputs**. They have no authority to modify ARGO KOP architecture, construction priorities, governance decisions, seam certification, or build direction.

External findings must be treated as claims to analyze against repository evidence. They may reveal contradictions, suggest risks, or motivate a targeted external test, but they do not become engineering decisions automatically.

If an external test is needed and cannot be executed from the repository-side environment, request a **specific bounded test** and analyze the returned report before deciding whether any repository change is justified.

## Current Phase

ARGO KOP is currently under **Connected-Baseline Integrity Validation**, moving from bounded seam-evidence construction into repository-wide connectivity proof.

The latest closed checkpoint is **EJR-136 — Execution Trace → Outcome Evaluation Seam (2026-08-12)**.

The controlled runtime path contains a real cross-stage runner, governed execution entrypoint, canonical execution-trace production, canonical outcome production, and a reusable explicit-target persistence adapter. A thin evidence-capture adapter reuses that persistence path to capture the exact runtime-produced trace without introducing another storage layer. Runtime-to-outcome lineage is explicitly verified and returns `HOLD` when identity cannot be established. The controlled path remains side-effect-free and must not be interpreted as autonomous production execution.

EJR-121 hardened the registry boundary: complete-looking evidence is not enough to become `CONNECTED`; a record must carry an explicit `verification_status == VERIFIED` from the upstream evidence/verifier chain.

EJR-122 applies the same explicit verification gate at the canonical audit boundary. The audit also requires the referenced contract, test and trace artifacts to be real repository-relative regular files.

EJR-123/EJR-124 preserve bounded candidate provenance in the canonical GAP MAP and explicitly prevent candidate provenance from promoting a seam.

EJR-125 adds one further guard at the promotion boundary: the trace reference must be a materialized repository-relative JSON execution-trace record matching the minimum canonical shape emitted by the runtime trace producer.

EJR-126 proves that the actual `connected_spine_runner.run()` output can produce a registry-ready evidence set through the existing thin capture path, but the temporary test target is **not** canonical repository evidence and does not itself certify a `CONNECTED` seam.

EJR-127 makes runtime/outcome lineage verification an explicit prerequisite for registry promotion; the registry must not receive a merely complete-looking record.

EJR-128 establishes the smallest governed repository-backed evidence boundary: `capture_repository_evidence()` may write only beneath `Quality/Integration/evidence/runtime/`, using the existing explicit-target persistence adapter. Temporary test targets remain valid for tests, but permanent runtime evidence must use the governed boundary and must not silently mutate canonical Memory.

EJR-129 corrected the integration proof to use the governed boundary's own path-composition contract: callers provide only a boundary-relative filename, and the returned canonical repository-relative path is used for downstream evidence loading. This prevents a false-positive proof caused by duplicating the governed root in the caller.

EJR-136 adds an executable `Execution Trace → Outcome Evaluation` seam proof. The real `connected_spine_runner.run()` output is consumed by the existing Outcome Evaluator; exact `execution_trace_id` continuity is asserted, and an orphaned evidence trace is required to fail with `OUTCOME_PROVENANCE_BROKEN`. This proves the executable provenance relationship in the controlled integration environment but does not, by itself, certify the canonical seam as repository-wide `CONNECTED`.

## Current Connectivity Chain

```text
Canonical Spine Evidence Scanner
        ↓
Candidate Seam Records + Bounded Provenance
        ↓
Concrete Artifact Inspection
        ↓
Contract + Executable Test + Canonical Runtime Trace
        ↓
Runtime Trace / Outcome Lineage Verification
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

## Current Execution / Outcome Target

```text
Cognition
   ↓
Reasoning
   ↓
Decision Proposal
   ↓
Authorization
   ↓
Execution Plan
   ↓
Decision Trace Producer
   ↓
Governed Execution Entrypoint
   ↓
Canonical Execution Trace Producer
   ↓
Execution Trace ID
   ↓
Canonical Outcome Producer
   ↓
Runtime Outcome Lineage Verification
   ↓
Outcome Evaluation
   ↓
Feedback Quality
   ↓
Learning Readiness
   ↓
Existing Promotion Gate
```

The exact controlled path from `connected_spine_runner.run()` through Outcome Evaluation is executable and test-proven. Its exact runtime-produced trace can also be captured through the thin evidence-capture adapter and persisted/re-read through the existing explicit-target persistence adapter without silently mutating canonical Memory.

It is not yet a complete canonical-spine certification because the complete evidence set still needs to be assembled from the actual runtime artifacts, passed through the loader/verifier boundaries, materialized into the verified seam registry, and audited as one evidence set.

## Current Next Target

**Run CI on the new Execution Trace → Outcome Evaluation seam proof. Inspect the result and repair the smallest demonstrated gap. If the complete evidence chain is satisfied, perform the canonical audit before promoting the seam. Then move to the next highest-value seam rather than repeatedly polishing one seam.**

Do not create another persistence layer.

The evidence loader and canonical audit require the trace artifact itself to be a repository-relative JSON execution-trace record with minimum identity fields. This prevents an arbitrary existing file from being treated as trace evidence merely because a path exists.

The registry and canonical audit additionally require an explicit `verification_status == VERIFIED`; neither may infer verification from path existence, candidate provenance, or record shape.

Required proof:

**connected_spine_runner.run() → execution_trace_id → Outcome Producer → execution_trace_ids → Outcome Evaluation → Feedback Quality → Learning Readiness → runtime lineage verification → thin capture → governed repository evidence target → verified registry → Canonical Audit**

Passing the loader is still not semantic certification. A synthetic trace fixture may test the loader boundary, but it cannot substitute for evidence that the trace was produced by the actual runtime path.

The current execution path is intentionally controlled/simulated. `side_effect=False` remains the boundary until a separate governed decision authorizes any future real side-effect capability.

The Outcome Producer maps controlled `SIMULATED` execution to `INCONCLUSIVE` with `UNKNOWN` confidence. It must never manufacture `SUCCESS` merely because the runner completed.

Only complete contract + runtime consumer + executable test + actual trace/outcome evidence, with explicit upstream verification, may support `CONNECTED` promotion.

Candidate provenance is a navigation aid only. It is not verification evidence and must not be promoted by itself.

## Audit Requirements

The connectivity audit must look for:

- files that exist but are not connected;
- folders or files required by the architecture but missing;
- contracts with no real runtime consumer;
- tests that do not exercise a real path;
- traces that do not reach an outcome;
- completed layers whose seams are missing;
- paths that start but do not terminate;
- paths that terminate without evidence;
- unreachable components;
- learning paths that do not return correctly to Memory/State;
- execution traces defined but not propagated into downstream outcomes;
- producers or entrypoints that exist only as test utilities without a real runtime caller;
- controlled execution results that bypass the canonical Outcome Producer;
- outcome evidence that is not tied to the exact execution trace that produced it;
- trace references that point to arbitrary files instead of materialized execution-trace records;
- permanent evidence writes that bypass an explicit governed target;
- duplicate, stale or historical structures that no longer have a justified current role.

Do not expand features or architecture merely because a loader, registry, scanner, gap-map, producer, entrypoint, capture adapter or persistence adapter exists.

## Required Resumption Sequence

1. Load current repository state.
2. Load the verified seam registry.
3. Confirm the latest checkpoint and inspect its changed artifacts.
4. Inspect the latest GitHub Actions result when one was triggered by the previous checkpoint.
5. Enumerate actual seam candidates.
6. Use bounded candidate provenance only to prioritize inspection.
7. Inspect contract + executable test + trace together.
8. Inspect `connected_spine_runner.py` and its exact downstream consumers.
9. Confirm the canonical Outcome Producer and its trace lineage.
10. Validate `execution_trace_id` → `execution_trace_ids` propagation.
11. Validate Outcome Evaluation and lineage.
12. Reuse the existing explicit-target persistence adapter and the thin evidence-capture adapter; do not invent a second persistence path.
13. Validate runtime trace/outcome lineage before preparing any registry record.
14. Validate that any proposed trace evidence matches the canonical runtime execution-trace shape.
15. Use the governed repository evidence boundary for permanent runtime evidence; reject traversal or out-of-bound targets.
16. Ensure callers pass only a boundary-relative filename and consume the returned canonical repository-relative evidence path.
17. Determine whether the complete evidence set justifies verified-registry promotion.
18. Run the canonical spine integration audit.
19. Generate the GAP MAP and preserve bounded candidate provenance for unresolved seams.
20. Expand to repository-wide connectivity / end-to-end audit when the current seam set is mature enough.
21. Inventory missing folders/files and orphaned or duplicate structures.
22. Rank all gaps by dependency, seam value and construction impact—not file count.
23. Fix the highest-value missing seams.
24. Run regression tests.
25. Re-run the audit.
26. Close the checkpoint.

## Future Engineering Capability Targets

These are **future capability targets, not current execution work**. They must not interrupt the connected-baseline audit.

### Programming and Mathematics Learning Capability

After the connectivity baseline is sufficiently proven:

**Source / Book → Extract Knowledge → Verify Understanding → Practice → Test → Apply → Record Reusable Knowledge**

The learning path should cover programming fundamentals, data structures and algorithms, relevant programming languages, software architecture and testing, followed by mathematics required by the target projects. Learning must be evidence-backed and application-driven rather than quantity-driven.

### Future Project A — Android Applications

**Programming Fundamentals → Kotlin → Android Development → Architecture → Testing → Real Application Project**

### Future Project B — Roblox Game Development + AI

**Luau → Roblox Studio → Game Architecture → Gameplay Systems → State / Networking → AI Integration → Testing → Optimization**

These future projects are retained as governed capability targets without allowing premature feature expansion to interrupt the current build gate.

## Engineering Priority Rule

**Priority is construction quality, connectivity, evidence and reusable learning—not file count.**

A smaller set of correctly connected, tested and documented artifacts is higher-value than a larger set of superficially modified files.

Every substantial session should be treated as potentially closable: preserve what was actually established, record evidence boundaries, identify unresolved work, and leave a deterministic resumption point.

## Before You Modify Anything

1. Read applicable bootstrap requirements.
2. Enumerate the relevant repository scope.
3. Read files involved in the proposed change.
4. Verify identities and authority ownership.
5. Trace affected references and consumers.
6. Distinguish verified evidence from inferred/unavailable evidence.
7. Make the smallest justified change.
8. Re-read every changed artifact after writing.
9. Revalidate affected indexes, status claims and relationships.
10. Check upstream/downstream impact.

## Review Loop

**Read Reality → Detect Contradiction → Prove the Contradiction → Correct → Review Impact → Re-read → Verify No New Contradiction → Continue**

Do not mark a change complete merely because the write succeeded.

## Ready State

You are ready to work when you understand what the repository currently contains, what is authoritative, what is historical, what remains uncertain, which relationships your work may affect, and which future capabilities must not distract from the current build gate.

---

End of Document
