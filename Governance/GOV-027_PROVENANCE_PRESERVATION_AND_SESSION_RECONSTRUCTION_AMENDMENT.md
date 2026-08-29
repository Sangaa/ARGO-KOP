# GOV-027 — Provenance, Preservation & Session Reconstruction Amendment

Document ID: GOV-027
Date: 2026-08-27
Parent Contract: `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
Status: `CANONICAL AMENDMENT / EFFECTIVE`
Authority: HERMUZ Governance Protocol amendment
Identity migration: from colliding historical `GOV-013_AMENDMENT_001_PROVENANCE_RECONSTRUCTION_2026-08-27.md`; authority/status unchanged.

## 1. Purpose

This amendment strengthens GOV-013 using the analytical boundary discovered during the HORUS → HERMUZ handoff and subsequent HERMUZ review.

It does not grant HORUS authority and does not convert analytical output into governance merely because it is preserved in the repository.

## 2. Provenance Preservation Rule

For material knowledge crossing execution identities, the repository MUST preserve, where applicable:

`SOURCE_ID → SOURCE_IDENTITY → CLAIM → SOURCE_EVIDENCE → EVIDENCE_STATE → VERIFIED_BY → VERIFICATION_METHOD → VERIFICATION_DATE → AUTHORITY_STATE → CHECKPOINT`

A verifier establishes the state of the evidence it actually examined. It does not automatically establish the truth of the source's interpretation.

The following states MUST remain distinct:

`HORUS-REPORTED`
`HERMUZ-VERIFIED`
`INDEPENDENTLY-VALIDATED`

These are provenance/verification states, not an automatic promotion chain.

## 3. Preservation Is Not Truth

`PRESERVED ≠ VERIFIED ≠ VALIDATED ≠ GOVERNANCE`

> **Preservation proves preservation, not truth.**

A claim being stored in `main`, an Engineering Journal, a Knowledge Package, a matrix, or another shared memory surface does not by itself increase its evidence state or authority state.

## 4. Knowledge, Evidence and Authority Separation

`KNOWLEDGE → PROVENANCE → EVIDENCE → VALIDATION → AUTHORITY → ACTION`

The repository is the source of preserved/reconstructable state. It is not automatically the source of truth for every claim stored within it.

Evidence determines what is supported; provenance identifies where the claim/evidence came from; authority determines what the system is permitted to do with the supported result.

## 5. Evidence Report Contract

Material session reports SHOULD use:

```text
SESSION
RE-ENTRY
WORK
EVIDENCE
PROVENANCE
CANDIDATES
UNPROVEN
MUTATIONS
VERIFICATION
AUTHORITY
NEXT
CLOSE
```

`PROVENANCE` is mandatory whenever material claims cross execution identities or analytical surfaces.

## 6. Session Reconstruction Invariant

Session memory MUST NOT be a required dependency for safe continuation.

A continuation state is reconstructable only when the repository preserves enough information to recover, as applicable:

`Repository State + Provenance + Evidence State + Authority + Uncertainty + Checkpoint`

## 7. Re-entry / Reconstruction Test

Before this amendment is treated as fully operationally validated, HERMUZ MUST test the rule using a controlled reconstruction case containing at least one deliberate distinction between source claim, supporting evidence, verifier observation, independent validation status and authority status.

The reconstruction executor MUST determine the safe next action from repository evidence without relying on unavailable session memory.

A successful reconstruction proves reconstructability for the tested case only. It does not prove universal meta-learning or universal knowledge transfer.

## 8. No Automatic Promotion

No analytical output from HORUS, HERMUZ, another execution identity, an external evaluator, or a previous session may become Governance Authority solely because it was repeated, preserved, rephrased, committed, read back successfully, or verified for transport integrity.

Promotion requires the applicable independent validation and governance gate.

## 9. Scope and Non-Effects

This amendment changes governance/session-control behavior only. It does NOT alter Runtime behavior, create a Model, authorize HORUS to mutate Canonical state, declare KTP-029 independently validated, declare Meta-Learning proven, or convert repository presence into truth.

## 10. Effective Checkpoint

`P352 → Provenance State → Authority Separation → Protocol Amendment → Re-entry Test → Session Reconstruction → Independent Validation`

The controlled Room71 reconstruction test later supplied bounded operational validation; universal capability remains outside that bounded proof.
