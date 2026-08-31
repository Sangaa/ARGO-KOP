# GOV-013B — HERMUZ TOOL-SURFACE / DECISION-BOUNDARY GATE

**Platform:** ARGO KOP (Knowledge Operating Platform)
**Document ID:** GOV-013B
**Version:** 1.0.0
**Status:** Approved Candidate / Canonical Promotion Pending CI
**Category:** Governance / Engineering Operating Protocol
**Authority:** Supplements GOV-013; does not replace higher ARGO authority
**Date:** 2026-08-25
**Learning Provenance:** EJR-405 / P221

## 1. Purpose

Prevent an AI or human engineer from converting a connector/tool result into a repository-state conclusion when the tool surface may be narrower than the question being asked.

## 2. Governing Rule

**A tool result is evidence about what that tool surface returned; it is not automatically a complete fact about repository state.**

Before a material decision is based on a GitHub result, the engineer MUST establish that the selected tool/endpoint is capable of answering the question being asked.

## 3. Mandatory Sequence

`Question → Tool Capability/Scope Check → Evidence Retrieval → Independent Cross-Surface Validation → Boundary Identification → Prior-Learning Retrieval → Decision`

Where a suitable independent GitHub surface exists, material negative findings MUST be corroborated before being treated as verified negatives.

## 4. CI / Actions Rule

For a material CI question:

- A commit-specific workflow query returning zero runs does **not** by itself prove that no relevant run exists.
- Check an appropriate repository Actions/workflow-run surface when available.
- When a candidate run exists, inspect `Run → Job → Step → Log`.
- A workflow headline is insufficient for Full-Stack closure.
- Required Jobs/Steps and relevant logs must be reconciled before declaring PASS.

## 5. Failure and Success Symmetry

The same discipline applies in both directions:

- `No run found` is not automatically `CI absent`.
- `Workflow green` is not automatically `repository verified`.
- `One job passed` is not automatically `full-stack passed`.
- `One failure found` is not automatically `root cause proven` until the failure boundary is traced and the correction is revalidated.

## 6. Rule-Defect Detection

If repeated execution shows that an existing ARGO rule, matrix, validator, or retrieval method systematically produces a conclusion inconsistent with repository evidence, the engineer MUST evaluate the rule/method itself as a possible control defect.

Do not blindly obey a locally convenient rule when higher-quality current evidence demonstrates that its assumptions are incomplete. Resolve the conflict through authority and documented learning; do not bypass governance silently.

## 7. No-Transition Rule

A material checkpoint cannot advance on an uncorroborated tool result when the required evidence surface is available but has not been inspected.

## 8. Learning Promotion

If this pattern repeats, promote the learning into the governing protocol, validator, workflow gate, or tool-use guidance rather than relying on session memory.

## 9. Provenance

This rule originates from P220, where a narrow commit-specific workflow lookup initially suggested that no CI run existed, while a broader Actions surface exposed the actual run and job log. The discovered failure was a protected mutation without a pre-existing Mutation Matrix.

## 10. Closure

This addendum is not considered fully promoted until:

`Pre-Write Matrix → Artifact Created → Read-Back → Required CI/Integration Evidence → Reconciliation → Canonical Promotion Decision`

# End of GOV-013B
