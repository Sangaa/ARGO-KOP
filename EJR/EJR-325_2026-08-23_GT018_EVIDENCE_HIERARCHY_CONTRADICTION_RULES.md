# EJR-325 — GT-018 Evidence Hierarchy, Evidence Layers & Contradiction Rules

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING + IMPLEMENTATION RECORD
Protocol: GOV-013 + GOV-017 + CELM-001
Parent: EJR-324

## Objective

Convert the verified GT-017 GitHub Actions artifact evidence into explicit ARGO reasoning rules answering:

1. Which evidence has priority?
2. When is a difference a `CONTRADICTION`?
3. When are observations `DIFFERENT EVIDENCE LAYERS`?
4. When must the engine remain `UNRESOLVED`?

## Prior-learning retrieval

Existing relevant authority and learning were inspected before mutation:

- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `PROJECT_BOOTSTRAP.md`
- `Governance/GOV-013_BASELINE_AUTHORITY_RECONCILIATION_2026-08-14.md`
- `EJR/EJR-324_2026-08-23_GITHUB_ACTIONS_GT017_ARTIFACT_EVIDENCE_TRAINING.md`
- `Engine/ENG-001_REASONING_ENGINE.md`
- `PROJECT_STATUS.md`
- `Repository/REP-001_MASTER_INDEX.md`

Three-search retrieval for an existing exact `CONTRADICTION / DIFFERENT EVIDENCE LAYERS / UNRESOLVED` rule did not find a dedicated canonical rule. Existing artifacts contained the component principles but not the combined inference procedure. This was therefore treated as a verified model gap rather than permission to invent a replacement architecture.

## GT-018A — Priority is claim-dependent

Rule established:

`Evidence precedence is claim-dependent, not globally fixed.`

For normative claims, applicable higher-authority ARGO governance has priority.

For identity/state/execution/provenance claims, direct current evidence of the target claim is preferred, followed by independent corroboration, inspectable derived evidence, canonical declarations, historical evidence, and finally inference/assumption.

Authority and evidence fitness remain separate dimensions.

## GT-018B — DIFFERENT EVIDENCE LAYERS

Use `DIFFERENT EVIDENCE LAYERS` when observations concern different propositions, stages or dimensions of the same event/object and can coexist.

Example from GT-017:

`run metadata → artifact metadata → artifact payload → correlation result`

An artifact may prove run association while a job result is still required to prove execution success. A correlation artifact may report `POLICY_UNRESOLVED` without contradicting the fact that the workflow run exists.

Reusable rule:

`Different layer ≠ contradiction.`

## GT-018C — CONTRADICTION

Use `CONTRADICTION` only when:

`Same Claim + Same Target + Same Scope + Same Relevant Time/Version + Valid Evidence + Mutually Exclusive Outcomes`

A contradiction is a finding, not a resolution. After classification, ARGO must apply legitimate authority/evidence precedence and trace propagation.

## GT-018D — UNRESOLVED

Use `UNRESOLVED` when the engine cannot safely reach one conclusion because identity, scope, time, provenance or proposition alignment is incomplete, or because a genuine same-claim contradiction remains without legitimate precedence.

`UNRESOLVED` means insufficient evidence for safe resolution; it is not synonymous with contradiction.

## GT-018E — No scalar evidence score

Do not combine authority, recency, directness, confidence and independence into one scalar score. A low-authority source cannot become normative authority by being newer, more detailed or more numerous.

Required dimensions remain separate:

`Authority / Claim Fitness / Identity Confidence / Temporal Validity / Evidence Independence / Completeness`

## Implementation

### Candidate governance rule created

`Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md`

Status:

`Candidate / Evidence-Backed / Controlled Promotion Pending`

The document explicitly preserves the existing Constitution/Governance authority boundary and does not claim canonical authority yet.

### Reasoning Engine integration

`Engine/ENG-001_REASONING_ENGINE.md` was updated from `3.1.1` to `3.1.2` and now contains operational rules for:

- claim-dependent evidence precedence;
- evidence-layer separation;
- contradiction qualification;
- contradiction-versus-resolution separation;
- `UNRESOLVED` safety boundary;
- derived-evidence semantics;
- search-failure boundary;
- bounded reference to GOV-018 candidate learning.

## Verification

1. GOV-018 was written successfully on `main`.
2. GOV-018 was directly re-read from current `main` and its SHA verified.
3. ENG-001 was updated with the smallest sufficient canonical-engine mutation.
4. ENG-001 was directly re-read from current `main`.
5. ENG-001 version `3.1.2` and the new evidence-conflict procedure were verified in the read-back.

## Evidence boundary

This checkpoint proves that the reasoning rules are recorded in the repository and integrated into the canonical reasoning-engine specification.

It does not prove repository-wide semantic integration, runtime execution of the new inference logic, or formal promotion of GOV-018 to canonical Governance authority.

## Knowledge Delta

**KD-020 — Evidence precedence is claim-dependent**

Classification: `VERIFIED`

ARGO must first identify the claim type before deciding which evidence has priority.

**KD-021 — Different evidence layers are not contradictions**

Classification: `VERIFIED`

Observations at different stages/dimensions of an evidence chain may coexist and should be correlated rather than forced into one status.

**KD-022 — Contradiction requires proposition alignment**

Classification: `VERIFIED`

Textual difference is insufficient. Contradiction requires same claim, target, scope, relevant time/version and mutually exclusive outcomes supported by valid evidence.

**KD-023 — UNRESOLVED is a protected reasoning state**

Classification: `VERIFIED`

When safe resolution is not justified, ARGO must preserve the discrepancy and missing evidence instead of guessing or promoting.

## Session closure

Session rule executed:

`Execute → Document → Read-back → Verify → Close`

Next safe continuation:

`GT-019 — controlled test cases for evidence-layer classification and contradiction resolution, using existing GitHub evidence without production mutation.`
