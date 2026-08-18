# Multi-Channel / Multi-Source Regression Corpus

Status: `VERIFIED TRAINING ASSET / REUSABLE`
Authority Boundary: `TEST ONLY / NO CANONICAL MUTATION`

## Purpose

Preserve the M1-M5 multi-channel training sequence as a repeatable regression corpus for future ARGO changes.

## Corpus

- **M1** — One User / Multi-Task / Read-Only: identity, context, state and failure isolation.
- **M2** — Proposal Write Isolation: workspace boundaries, read-back and no implicit canonical merge.
- **M3** — Controlled Reconciliation: explicit decisions, conflict objects, no automatic merge.
- **M4** — Multi-User / Multi-Task: authorization and channel-collision isolation.
- **M5** — Multi-Source Intake: source/schema provenance preservation and conflict quarantine.

## Evidence

M1: `Run 32056078246` — SUCCESS.
M2: `Run 32057350530` — SUCCESS.
M3: `Run 32057745976 / Job 95471684377` — SUCCESS after correcting undeclared pytest dependency to stdlib regression execution.
M4: `Run 32057977008` — SUCCESS.
M5: `Run 32058008592 / Job 95472511808` — SUCCESS.

## Regression Principle

Every future material ARGO change should be evaluated for whether it could break one of these boundaries:

`Identity → Context → State → Proposal Isolation → Conflict Handling → Authorization → Provenance`

The corpus is a training and regression surface, not a production orchestration engine.

## Non-Claims

The corpus does not prove production asynchronous concurrency, external connector reliability, production authentication, automatic canonical merge, or production-scale throughput.

## Failure Learning

Any new corpus failure MUST follow GOV-016 and preserve distinction between:

`Subject Failure ≠ Test Failure ≠ Execution Channel Failure ≠ Governance Failure`

---

End of Document
