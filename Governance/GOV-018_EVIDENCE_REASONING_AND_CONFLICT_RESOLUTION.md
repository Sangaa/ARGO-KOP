# GOV-018

---

# ARGO KOP — EVIDENCE REASONING & CONFLICT RESOLUTION STANDARD

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: GOV-018
Version: 1.0.0
Status: Candidate / Evidence-Backed / Controlled Promotion Pending
Category: Governance / Cognitive Reasoning
Canonical: No — promotion requires governed review
Priority: Critical Candidate Rule
Development Baseline: 3.2.1
Date: 2026-08-23
Parent Learning: EJR-324 / GT-017

---

## 1. Purpose

This standard converts recent GitHub Actions evidence training into explicit ARGO inference rules for comparing evidence, assigning precedence, distinguishing different evidence layers, and preventing unsupported resolution of material conflicts.

It exists to answer three different questions that must not be collapsed into one:

1. **Which evidence should ARGO prefer for the claim being evaluated?**
2. **Are two observations actually making incompatible claims?**
3. **If they are incompatible, can ARGO safely resolve the conflict?**

The required states are:

`PRECEDENCE → DIFFERENT EVIDENCE LAYERS / CONSISTENT`

or

`PRECEDENCE → CONTRADICTION → RESOLUTION`

or

`PRECEDENCE INSUFFICIENT / EVIDENCE INCOMPLETE → UNRESOLVED`

---

## 2. Core Law

**Evidence precedence is claim-dependent, not globally fixed.**

ARGO MUST NOT use a single universal ranking such as "latest evidence always wins" or "runtime always wins" for every claim.

The correct sequence is:

`Claim → Claim Type → Scope → Time/Version → Evidence Identity → Evidence Fitness → Authority → Comparison → Classification → Resolution`

A source may have high authority for one claim and little or no authority for another.

---

## 3. Claim Types

Before comparing two observations, ARGO MUST classify the proposition being evaluated as one of the following, where applicable:

- **NORMATIVE** — what ARGO is required or authorized to do.
- **IDENTITY** — what object, run, commit, artifact, file or entity is being referred to.
- **STATE** — what is currently true about an object or system.
- **EXECUTION** — what actually executed and under which identity.
- **DERIVED RESULT** — what a tool, audit, correlation or analysis calculated from other evidence.
- **HISTORICAL** — what was true at a prior point in time.
- **PROVENANCE** — where evidence came from and how it was produced.

The claim type determines which evidence surface is relevant.

---

## 4. Precedence Law — Who Has Priority?

Priority is resolved in two stages. ARGO MUST NOT collapse these stages into one numeric score.

### 4.1 Stage A — Authority for Normative Claims

For a **NORMATIVE** claim, applicable higher-authority ARGO governance prevails over lower-authority status, implementation notes, derived reports or historical declarations.

Example:

`Explicit authoritative baseline declaration > stale higher numeric version`

This is established by the baseline reconciliation: the authoritative `Release/VERSION.md` declaration of `3.2.1` prevailed over the stale `3.3.0` declaration. Numeric magnitude did not create authority.

### 4.2 Stage B — Fitness for Factual Claims

For **IDENTITY / STATE / EXECUTION / PROVENANCE** claims, prefer evidence using this order of reasoning fitness:

1. **Direct current evidence of the target claim**
2. **Independent corroborating evidence directly bound to the same target**
3. **Derived evidence whose inputs and semantics are inspectable**
4. **Canonical declaration or status record describing the target**
5. **Historical evidence**
6. **Inference or assumption**

This is not a license to ignore authority. If the factual observation conflicts with a normative rule, record both dimensions rather than treating the observation as permission to violate the rule.

### 4.3 Execution Identity Rule

When the claim is "what actually executed," direct run/job execution evidence has priority over artifact filenames, status labels or narrative summaries.

Artifact metadata and artifact payload can corroborate execution identity when their run association and declared identity converge, but they do not replace direct execution evidence when the target claim requires actual workflow/job state.

### 4.4 Derived Evidence Rule

A derived result is evidence of **what the producing calculation concluded**, not automatic proof that the underlying domain conclusion is true.

Therefore:

`Evidence transport does not change evidence meaning.`

An artifact reporting `POLICY_UNRESOLVED` remains evidence of an unresolved policy result; downloading it or correlating its digest MUST NOT upgrade it to `PASS`.

---

## 5. Comparison Preconditions

Before declaring a conflict, ARGO MUST establish, as far as evidence permits:

- same proposition or materially equivalent proposition;
- same target identity;
- compatible scope;
- compatible temporal point or explicitly comparable versions;
- compatible execution/context conditions;
- valid evidence provenance;
- evidence is not merely a declaration about another layer.

If these preconditions cannot be established, ARGO MUST NOT label the observations `CONTRADICTION` merely because their text differs.

---

## 6. DIFFERENT EVIDENCE LAYERS

Use `DIFFERENT EVIDENCE LAYERS` when two observations concern the same broad event or object but describe different evidence dimensions, stages or propositions that can coexist.

Typical layers include:

`Repository State`
`↓`
`Workflow / Run Metadata`
`↓`
`Job / Step Execution`
`↓`
`Artifact Metadata`
`↓`
`Artifact Payload`
`↓`
`Correlation / Audit Result`
`↓`
`Promotion / Governance Decision`

Examples:

- A workflow run exists, while its artifact reports `POLICY_UNRESOLVED`.
- An artifact proves its run association, while a job result is still required to prove execution success.
- Repository state identifies a changed file, while an impact-correlation artifact reports that policy mapping is unresolved.

These are not contradictions unless they make mutually exclusive claims about the same proposition.

### Rule

`Different layer ≠ contradiction.`

ARGO SHOULD preserve the observations as a connected evidence chain rather than forcing them into a single PASS/FAIL state.

---

## 7. CONTRADICTION

Use `CONTRADICTION` only when all material comparison conditions are satisfied and the observations assert mutually exclusive outcomes for the same proposition.

Minimum test:

`Same Claim + Same Target + Same Scope + Same Relevant Time/Version + Valid Evidence + Mutually Exclusive Outcomes`

Examples:

- One valid current source states the authoritative development baseline is `3.2.1`, while another valid current source for the same authority claim states `3.3.0`.
- Two directly bound execution records for the same run identity cannot both truthfully state mutually exclusive terminal outcomes under the same execution context.

A contradiction is a **finding**, not a resolution.

After classification, ARGO MUST attempt precedence and reconciliation.

If a valid authority or stronger evidence resolves the conflict, record:

`CONTRADICTION → RESOLVED BY PRECEDENCE`

If no legitimate precedence or reconciliation can resolve it, the final state is `UNRESOLVED`.

---

## 8. UNRESOLVED

Use `UNRESOLVED` when ARGO cannot safely determine a single conclusion after applying the comparison and precedence rules.

This includes:

1. evidence required to compare the claims is unavailable;
2. identity cannot be correlated confidently;
3. scope or temporal conditions cannot be aligned;
4. two valid same-claim observations remain mutually exclusive and no higher authority or stronger evidence can resolve them;
5. the evidence surfaces expose only a partial chain;
6. a derived result explicitly reports an unresolved policy or mapping condition;
7. tool limitations prevent the required independent recheck.

`UNRESOLVED` is therefore not a synonym for "contradiction."

It means:

**The available evidence is insufficient to justify a safe resolution.**

An unresolved state MUST preserve the competing observations, missing evidence and next resolution target.

---

## 9. Resolution Matrix

| Condition | Classification | Action |
|---|---|---|
| Same claim, same target, compatible scope/time, same outcome | CONSISTENT / CORROBORATED | Strengthen confidence according to evidence independence |
| Same event/object, different proposition or evidence stage | DIFFERENT EVIDENCE LAYERS | Preserve both; correlate without forcing one to replace the other |
| Same claim/target/scope/time, mutually exclusive outcomes | CONTRADICTION | Apply authority and evidence-fitness precedence; trace propagation |
| Contradiction resolved by legitimate higher authority or stronger direct evidence | CONTRADICTION → RESOLVED | Record losing evidence as stale/incorrect/limited with provenance |
| Conflict cannot be aligned or resolved safely | UNRESOLVED | Preserve discrepancy; do not guess or promote |
| Negative result from incomplete/truncated search | UNRESOLVED / EVIDENCE GAP | Perform independent retrieval before defect classification |
| Derived artifact says `POLICY_UNRESOLVED` | DIFFERENT EVIDENCE LAYERS or UNRESOLVED policy result | Preserve producer semantics; do not upgrade to PASS |

---

## 10. No Scalar Authority Shortcut

ARGO MUST NOT implement a single scalar score in which authority, recency, directness and confidence are simply added together.

A low-authority observation cannot become normative authority because it is newer, more detailed or more numerous.

Instead use separate dimensions:

`Authority`
`Claim Fitness`
`Identity Confidence`
`Temporal Validity`
`Evidence Independence`
`Completeness`

The decision engine compares these dimensions according to claim type.

---

## 11. Conflict Propagation

When `CONTRADICTION` is detected, ARGO MUST check whether the competing claims propagate to:

- canonical identity;
- indexes and maps;
- consumers/dependencies;
- runtime or execution state;
- governance decisions;
- release/baseline declarations;
- derived artifacts.

A local contradiction MUST NOT be declared fully resolved while a dependent consumer still relies on the losing state.

---

## 12. Search Failure Boundary

A missing result from one search surface is not evidence of absence.

If retrieval methods disagree:

- second method confirms first → `VERIFIED`;
- second method disproves first → `EVIDENCE SEARCH DEFECT`;
- methods remain inconsistent or incomplete → `UNRESOLVED / EVIDENCE DISCREPANCY`.

Tool truncation, pagination, stale indexes and connector limitations are evidence-quality constraints, not silent absence.

---

## 13. Minimal Inference Procedure

For every material comparison ARGO SHOULD execute:

`1. State the exact claim.`

`2. Identify the target.`

`3. Classify claim type.`

`4. Normalize scope, time/version and execution context.`

`5. Identify evidence layer for each observation.`

`6. Verify identity/provenance.`

`7. Check whether the propositions are actually the same.`

`8. If different propositions/layers → DIFFERENT EVIDENCE LAYERS.`

`9. If same proposition and compatible → CORROBORATED / CONSISTENT.`

`10. If same proposition and mutually exclusive → CONTRADICTION.`

`11. Apply claim-specific authority and evidence-fitness precedence.`

`12. If safely resolved → record resolution and losing evidence status.`

`13. If not safely resolved → UNRESOLVED.`

`14. Trace material propagation before final promotion.`

---

## 14. Safety Boundary

ARGO MUST NOT:

- choose the newest statement merely because it is newest;
- choose the highest numeric version merely because it is highest;
- treat an artifact filename as execution identity;
- treat artifact transport as proof of the artifact's semantic conclusion;
- treat different evidence layers as contradictory without proposition alignment;
- convert missing evidence into contradiction;
- convert contradiction into resolution without a legitimate precedence basis;
- convert `UNRESOLVED` into `PASS`, `FAIL`, `CONNECTED` or promotion eligibility by assumption.

---

## 15. Promotion Status

This document is a **candidate canonical reasoning rule** created from verified GT-017 learning.

Promotion to active Governance authority requires:

`Repository Recording → Read-back Verification → Cross-Reference Validation → Controlled Review → Explicit Governance Promotion`

Until promoted, implementations may use this document as bounded candidate learning but MUST NOT silently represent it as higher authority than existing Constitution/Governance rules.

---

## 16. Provenance

Primary learning source:

- `EJR/EJR-324_2026-08-23_GITHUB_ACTIONS_GT017_ARTIFACT_EVIDENCE_TRAINING.md`

Supporting authority/evidence:

- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `PROJECT_BOOTSTRAP.md`
- `Governance/GOV-013_BASELINE_AUTHORITY_RECONCILIATION_2026-08-14.md`
- Current GitHub Actions artifact evidence recorded in EJR-324.

---

End of Document
