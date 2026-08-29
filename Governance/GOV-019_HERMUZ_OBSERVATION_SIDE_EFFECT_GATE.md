# GOV-019 — HERMUZ Observation & Side-Effect Gate

Document ID: GOV-019
Status: Canonical Governance Addendum / Proposed integration into GOV-013
Purpose: prevent ARGO from treating newly observed execution effects as automatically intended behavior.
Identity migration: from colliding historical path `GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md`; authority/status unchanged.

## 1. Core Rule

When an operation, execution, mutation, workflow, or external interaction produces an observable effect in a repository surface not previously included in the expected model, HERMUZ MUST NOT immediately classify that effect as either required behavior or harmless noise.

It MUST first ask:

1. **What exactly changed?**
2. **Why did this effect appear here rather than only in the expected location?**
3. **What causal path could connect the triggering action to this surface?**
4. **Was this surface expected by the design, contract, workflow, or platform law?**
5. **Is the effect required, supportive, incidental, or unintended?**
6. **Could the effect be a side effect, propagation effect, generated artifact, audit trace, cache/index effect, or governance/documentation consequence?**
7. **Could the effect indicate an undocumented dependency or hidden integration seam?**
8. **What evidence distinguishes intended behavior from collateral behavior?**

## 2. Effect Classification

Every material newly observed effect MUST be classified provisionally as one of:

- **INTENDED** — explicitly required or evidenced by the governing contract.
- **EXPECTED PROPAGATION** — not the primary target, but a documented consequence of the operation.
- **INCIDENTAL / BENIGN** — causally related but not required for correctness.
- **UNINTENDED / RISK** — undesirable or potentially harmful consequence.
- **UNKNOWN / UNCLASSIFIED** — insufficient evidence to classify.

`UNKNOWN` is preferable to inventing intent.

## 3. Observation Expansion Rule

If an effect appears in a new surface, HERMUZ MUST expand the observation boundary before proposing a fix.

The search should include, where applicable:

`trigger → event → state mutation → generated artifact → runtime trace → cache/index → audit evidence → downstream consumer → governance/documentation effect`

The absence of an expected effect and the presence of an unexpected effect are separate questions and MUST NOT be conflated.

## 4. Causal Verification

A newly observed effect is not evidence of causality merely because it followed an operation in time.

Where practical, establish:

`Before State → Trigger → Intermediate Event → Effect → Reproduction → Cleanup/Reverse Test`

A controlled reproduction or reverse test should be preferred when safe.

## 5. Side-Effect Escalation

If an unexpected effect is repeatable and materially changes repository state, execution evidence, authority, relationships, security/integrity boundaries, or user-visible behavior, it becomes a mandatory investigation item before the triggering work is considered fully understood.

## 6. Learning Requirement

If the effect reveals an undocumented platform or repository law, record the law as candidate learning and test it against another independent example before promoting it as reusable knowledge.

## 7. Boundary Rule

An observed effect MUST NOT be promoted into canonical relationship, runtime verification, or architectural intent solely because it exists.

`Observed ≠ Intended ≠ Required ≠ Safe`

## 8. Relation to GOV-013

This addendum extends the Prior-Learning Retrieval, Three-Search, Evidence Discipline, Safe Mutation, Integration Verification, Learning Promotion, and Session Closure rules of GOV-013.

Until formally merged into the body of GOV-013, this document is a canonical governance addendum for the current diagnostic workstream and must be loaded whenever the investigation concerns unexpected repository/execution effects.
