# EJR-417 — P4 REL-009 Consumer Boundary Gate

Date: 2026-08-17
Status: `CLOSED / SAFETY-GATE-EXECUTION-VERIFIED / RELATIONSHIP-REMAINING-OPEN`

## 1. Execution Identity

- Session / EJR: `EJR-236`
- Starting HEAD/SHA: `9a3d2e314662cff7f9e7d6586c40bc6dc53f06ff`
- Scope: P4 safety/control construction for unresolved `REL-009`
- Objective: prevent speculative promotion and create a reusable executable boundary gate.

## 2. Governing Controls

- `GOV-013` Hermuz session build protocol.
- `GOV-014` controlled mutation/current-state/read-back.
- `GOV-015` execution documentation and knowledge transfer.
- Canonical relationship registry `REP-014`.

## 3. Execution

- Added side-effect-free safety test: `Quality/P4/test_rel009_consumer_boundary.py`.
- Added a dedicated P4 workflow, then removed it after GitHub did not produce a workflow run; the gate was integrated into the already-proven `Full-Stack Repository Audit` workflow instead.
- Preserved `setup-python@v5` after detecting and correcting an accidental temporary drift to v4 during integration.
- Added `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md`.
- Hardened the gate after CI failures caused by brittle wording assertions; the final workflow checks the canonical relationship state and the canonical RUN-010 evidence boundary using stable assertions.

## 4. Execution Evidence

Successful Full-Stack workflow:

- Workflow: `333498182`
- Run: `32046636097`
- Job: `95435955639`
- HEAD: `9f3c7ddd8ac82427251b8add97bd1550cf3bb554`

Verified stages:

- P4 REL-009 consumer boundary safety gate: `SUCCESS`
- Repository-wide audit: `SUCCESS`
- Real runtime evidence emission: `SUCCESS`
- Audit evidence upload: `SUCCESS`
- Runtime evidence upload: `SUCCESS`

## 5. Evidence Boundary

### Proven

- `REL-009` remains `REVALIDATION REQUIRED` in `REP-014`.
- `RUN-010` explicitly describes the execution chain as a relationship description and does not claim universal runtime-path execution.
- A repository-controlled safety gate exists and executes successfully in the proven Full-Stack CI channel.
- The gate is side-effect free and does not create runtime evidence.

### Not Proven

- A callable consumer path `RUN-010 → SRV-009`.
- Independent runtime trace proving that path.
- Any basis for promoting `REL-009` to `VERIFIED`.

## 6. Failures and Recovery

- The initial dedicated P4 workflow produced no observable workflow run and was removed rather than treated as a valid execution channel.
- A temporary `setup-python@v4` drift was detected during integration and restored to the existing `setup-python@v5` configuration.
- Initial boundary assertions were too dependent on literal wording and failed despite correct repository evidence.
- The final gate was reduced to stable canonical evidence assertions and then passed in CI.
- A transient connector error occurred during matrix creation; the mutation was retried through the governed path without speculative content changes.

## 7. Learning Extraction

Observation: safety gates are useful only when their own execution path is reliable and their assertions target stable canonical evidence.

Root Cause: a logically correct boundary can still produce false CI failures when the test asserts paraphrased or layout-sensitive wording.

Lesson: safety gates should assert stable canonical facts, not model-written interpretations or fragile paraphrases.

General Rule: `SAFETY GATE PASS ≠ RELATIONSHIP VERIFIED`; the gate certifies only that the repository has not silently crossed the current evidence boundary.

Reusable Test Rule: use stable identity/state assertions for repository boundary gates, and keep the positive promotion evidence separate from the negative safety gate.

Boundary: none of this establishes runtime connectivity and none of it authorizes canonical relationship promotion.

### Learning Classification

`REUSABLE-LEARNING`

Promotion to `DEFAULT-PRACTICE` is deferred until the same safety-gate pattern is exercised successfully in a later relationship review.

## 8. Transfer Decision

- New reusable safety test: installed and CI-verified.
- New P4 evidence matrix: installed and updated with execution evidence.
- Full-Stack CI integration: verified.
- Knowledge transfer: recorded in this EJR and the P4 matrix so future models can discover the negative boundary directly from repository artifacts.
- Regression coverage: active for this relationship boundary.

## 9. Closure Gate

- [x] Execution Evidence
- [x] Verification
- [x] Documentation
- [x] Learning Assessment
- [x] Transfer Decision
- [x] Next Safe Entry

## 10. Next Safe Entry

Search for independent callable-consumer source evidence and runtime execution evidence for `RUN-010 → SRV-009`. The safety gate may block promotion, but it must never be used as positive relationship proof.

---

End of EJR-236
