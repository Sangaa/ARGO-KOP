# HORUS Session Record 022 — 2026-08-24

## Objective
Apply the truth audit to EJR-321 and advance from knowledge-transfer claims to identity-sensitive evidence reasoning. Determine whether ARGO's learned rules can distinguish path identity, ref state, commit identity, and blob identity without collapsing them into one concept.

## Scope boundary
Analytical branch only. No canonical ARGO architecture, HERMUZ build state, or production implementation is changed.

## Evidence reviewed
EJR-321 — GitHub Ref / SHA / Blob Identity Training. The record distinguishes current ref reads, historical SHA-bound reads, exact commit evidence, ref/SHA equivalence, and blob retrieval. It records Knowledge Deltas KD-008 through KD-010 and explicitly keeps P6 execution claims separate.

## Decisions

### DEC-H099 — Identity layers must remain separate
A path, branch/ref, commit SHA, and blob SHA answer different identity questions. Treating them as interchangeable creates false evidence joins.

### DEC-H100 — Temporal state is part of evidence identity
A successful current-ref read cannot establish historical existence. A historical 404 cannot establish current absence. The evidence claim must include the selected ref/SHA and time context.

### DEC-H101 — Exact content identity should use content-addressable evidence when available
When a blob SHA is known and independently retrievable, it provides stronger exact-content identity than a path alone.

### DEC-H102 — Correlation is not equivalence
Two surfaces can refer to the same object without having identical evidentiary semantics. Identity keys allow correlation; they do not make observations interchangeable.

### DEC-H103 — Transfer must preserve identity semantics
If ARGO learned that a historical path is absent, the transferable rule must be scoped as historical-ref absence, not generalized into repository-wide absence.

## New findings

### F-H022-01 — Evidence has an identity tuple
For repository observations, a useful minimum identity tuple is:
`repository + path + ref/commit + object identity + observation surface`
Dropping one component can change the meaning of the claim.

### F-H022-02 — The strongest reusable knowledge is conditional knowledge
The rule learned in EJR-321 is not merely "404 means absent." It is "404 at a specified ref/SHA means the path was not resolvable through that surface at that selected state." This is a more precise and transferable rule.

### F-H022-03 — Correct abstraction is conditional, not absolute
ARGO's learned rule is valuable because it preserves the condition that makes it true. Over-generalizing the rule would be a regression in knowledge quality even if the underlying retrieval operation remains reliable.

### F-H022-04 — Identity-aware transfer is a stronger test of abstraction
A future novel-case test should vary branch/ref/time while preserving the underlying identity question. Correct behavior across these changes would provide stronger evidence that ARGO learned the semantic distinction rather than memorized one 404 example.

### F-H022-05 — Evidence joins can be wrong even when every individual observation is true
A current-ref success, historical 404, commit deletion, and blob retrieval can each be factually correct while an incorrect join creates a false narrative. Truth auditing therefore requires validation of both observations and their correlation keys.

### F-H022-06 — This creates a new failure class: identity-collapse error
Identity-collapse error occurs when ARGO treats path, ref, commit, blob, or surface identity as interchangeable and produces a broader claim than the evidence supports.

## New test design — Identity-Preserving Transfer Test (IPTT)

A candidate transfer test should contain:

1. Training case with a path/ref distinction.
2. Explicit pre-registered rule in conditional form.
3. Novel case with a different ref or historical state.
4. At least one misleading surface observation that would trigger an over-broad inference.
5. Independent verification using commit or blob identity.
6. Scoring for both correct action and correct claim scope.

Success requires not only selecting the right retrieval operation but also stating the resulting claim at the correct scope.

## Updated evidence model

`Observation correctness`
→ `Identity correctness`
→ `Correlation correctness`
→ `Transfer correctness`
→ `Claim-scope correctness`

A failure at any layer can invalidate a higher-level conclusion even when lower-level operations succeeded.

## Transfer implication for ARGO

EJR-321 is strong evidence that the repository training environment contains reusable semantic rules about Git identity. It is not yet evidence that ARGO independently selected those rules or transferred them to a genuinely novel case. The next decisive test must therefore require ARGO to preserve the conditional identity semantics under a changed ref/time context.

## Handoff lesson for ARGO/HERMUZ

> **Do not learn only what an operation returned. Learn what the return means, under which identity and temporal conditions it is true, and what it does not permit you to claim.**

## Current capability posture

No capability promotion.

- Controlled learning evidence: strongly supported.
- Evidence-semantic learning: strongly supported in bounded training records.
- Identity-aware abstraction: promising / not independently transferred.
- Novel-case knowledge transfer: not established.
- Independent strategy selection: not established globally.
- Mechanism-level understanding: not proven.
- Meta-learning: not proven.

## Continuation checkpoint

**State:** HORUS ANALYTICAL FOUNDATION — CONTINUABLE / IDENTITY-PRESERVING TRANSFER FRONTIER ACTIVE

**Next action:** test whether the conditional rules learned from EJR-321 are applied correctly to a novel ref/time case, with pre-registered predictions and independent identity verification.

**Highest-risk error:** accepting correct retrieval behavior as evidence of abstraction while ignoring whether ARGO preserved the scope and identity conditions of the learned rule.

**Epistemic status:** Analytical / non-canonical.
