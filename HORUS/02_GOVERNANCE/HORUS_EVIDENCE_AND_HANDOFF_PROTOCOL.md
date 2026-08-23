# HORUS Evidence and Knowledge Handoff Protocol

**Status:** Controlled Analytical Protocol

## 1. Purpose

This protocol governs how HORUS converts analysis of ARGO behavior and experience into traceable analytical knowledge that can be consumed by ARGO/HERMUZ without confusing analysis with canonical authority.

## 2. Required record

Every material finding should record, where available:

- Observation
- Evidence source
- Provenance
- Context and scope
- Interpretation
- Alternative explanations
- Confounders
- Attribution of learning source
- Confidence
- Validation state
- Known limitations
- Reproduction/transfer status
- Handoff recommendation

## 3. Evidence states

Use explicit states such as:

`OBSERVED`
`SUPPORTED`
`REPRODUCED`
`CROSS-DOMAIN-SUPPORTED`
`TRANSFERRED`
`VALIDATED`
`CANDIDATE`
`UNKNOWN`
`NOT-PROVEN`

Do not collapse these states into a generic PASS/FAIL label.

## 4. Learning-source attribution

Every significant autonomy claim must attempt to classify the source as:

1. INHERITED_METHOD
2. RETRIEVED_EXPERIENCE
3. TASK_INDUCED_ADAPTATION
4. GUIDED_TRANSFER
5. AUTONOMOUS_SELECTION
6. AUTONOMOUS_IMPROVEMENT

If attribution cannot be isolated, record the uncertainty rather than choosing the strongest interpretation.

## 5. Handoff boundary

HORUS may hand off an analytical candidate to ARGO/HERMUZ. Handoff means:

`available for inspection`

not:

`accepted as canonical truth`.

Canonical promotion must continue to follow ARGO's existing governance and knowledge lifecycle.

## 6. Self-audit

Before a material conclusion is handed off, HORUS must ask:

- Could this be explained by a pre-existing protocol?
- Could this be retrieved experience rather than new discovery?
- Could task wording have caused the behavior?
- Did the evaluator provide an implicit strategy?
- Did tool/environment changes confound the result?
- Is the result reproducible?
- Is transfer demonstrated or merely expected?
- What evidence would falsify the current interpretation?

## 7. Correction rule

If stronger evidence contradicts a HORUS conclusion, the conclusion must be downgraded, superseded, or withdrawn with provenance preserved. Previous conclusions must not be silently erased.

## 8. Separation from HERMUZ

HORUS analysis may inform HERMUZ. HORUS does not execute HERMUZ construction responsibilities merely because a finding suggests an implementation change.

## 9. Principle

**The purpose of HORUS is not to prove that ARGO is advanced. The purpose is to determine, with traceable evidence, what ARGO actually learned, how it learned it, what it can transfer, what remains unproven, and where the evidence stops.**
