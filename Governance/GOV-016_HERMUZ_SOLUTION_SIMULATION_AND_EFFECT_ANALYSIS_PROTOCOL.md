# GOV-016 — HERMUZ Solution Simulation and Effect Analysis Protocol

Status: PROPOSED — GOVERNANCE REVIEW REQUIRED

## Purpose
Before recommending or implementing a material solution to an ARGO/KOP build problem, HERMUZ should simulate the proposed solution within a bounded model and inspect its expected effects before changing the canonical repository.

This protocol is a reasoning and risk-control instrument. It does not authorize production mutation by itself.

## Core Principle
A solution must be evaluated as a causal operation, not only as a fix for the immediate symptom.

`Problem → Prior Learning → Candidate Solutions → Bounded Simulation → Primary Effect → Secondary Effects → Causal Analysis → Trade-offs → Decision`

An unexpected effect is not dismissed as "side effect" or "chance". It is treated first as evidence that the operational model may be incomplete. The mechanism producing the effect must be investigated before acceptance or rejection.

## Mandatory Gates

### Gate 0 — Prior Learning Retrieval
Retrieve and review relevant previous solutions, failures, lessons, experiments, constraints, and known repository state before inventing a new solution.

### Gate 1 — Candidate Definition
State the problem, objective, assumptions, constraints, candidate solution, and success criteria explicitly.

### Gate 2 — Bounded Simulation
Model or test the candidate without modifying canonical production state whenever practical. Define the simulation boundary and baseline before execution.

### Gate 3 — Layered Effect Sweep
Inspect at least:
- direct target effect;
- dependent components;
- repository state/history;
- generated artifacts/evidence;
- execution/runtime surfaces where applicable;
- governance/relationship surfaces;
- unexpected repository-wide changes.

### Gate 4 — Causal Effect Review
For every observed change ask:
1. What operation produced it?
2. What mechanism connects the operation to the change?
3. Was that mechanism represented in the original model?
4. Was the effect required, expected propagation, incidental, unacceptable, or unresolved?

Unexplained effects remain `UNRESOLVED`; they are not silently accepted.

### Gate 5 — Alternative Comparison
Compare the candidate against simpler alternatives and the known prior solution. Do not call a solution "optimal" merely because it works. Evaluate correctness, scope, complexity, reversibility, governance impact, evidence quality, and residual risk.

### Gate 6 — Decision Boundary
Only after simulation/effect analysis may HERMUZ recommend production mutation. If uncertainty remains material, preserve the current state and record the gap.

### Gate 7 — Post-Execution Verification
If the solution is subsequently implemented, repeat layered observation and compare predicted versus actual effects. Unexpected effects reopen model review.

## Anti-Pattern
`Symptom → Quick Fix → PASS → Close`

This is insufficient because a locally successful fix may introduce downstream effects that contaminate later reasoning.

## Required Output
Each material solution simulation should leave a durable record containing:
- problem and context;
- prior-learning sources reviewed;
- candidate and alternatives;
- simulation boundary/baseline;
- predicted effects;
- observed effects;
- unexpected effects;
- causal explanations and unresolved gaps;
- decision and rationale;
- production status;
- post-execution verification plan/results.

## Relationship to Existing Governance
GOV-016 complements GOV-013 and GOV-015. GOV-013 remains the session operating contract. GOV-015 governs controlled diagnostic experiments when prior knowledge cannot adequately diagnose the problem. GOV-016 governs evaluation of proposed solutions before material implementation.

GOV-016 does not grant authority to bypass existing integrity holds, repository governance, authorization boundaries, or evidence promotion rules.

## Learning Objective
The protocol is intended to strengthen deep reasoning by requiring HERMUZ to explore the behavior of a proposed solution before committing to it, reducing shallow local fixes that solve one step while creating confusion or failure in later steps.

## Promotion Rule
This document remains PROPOSED until repeated application demonstrates that the method improves solution quality without creating unnecessary process overhead. Promotion requires evidence and governance review.
