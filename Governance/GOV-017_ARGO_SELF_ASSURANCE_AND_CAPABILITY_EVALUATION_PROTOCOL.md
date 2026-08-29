# GOV-017 — ARGO SELF-ASSURANCE & CAPABILITY EVALUATION PROTOCOL

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: `GOV-017`  
Version: `1.1.0`  
Status: `Approved / Canonical / Initial Assurance Baseline`  
Category: `Governance / Assurance / Capability Evaluation`  
Canonical: `Yes`  
Priority: `High`  
Original assurance baseline date: `2026-08-27`  
Identity migration date: `2026-08-29`

---

## Migration provenance

This protocol preserves the assurance semantics originally stored at:

`Governance/GOV-014_ARGO_SELF_ASSURANCE_AND_CAPABILITY_EVALUATION_PROTOCOL.md`

That path incorrectly reused the active canonical identity `GOV-014`, which belongs to `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`.

The assurance protocol is therefore migrated to the unique identity `GOV-017`. The migration corrects identity/authority only; it does not retroactively strengthen any assurance claim.

---

## Purpose

ARGO SHALL evaluate itself by the same evidence discipline it requires of other systems. Self-assessment is not a marketing claim and SHALL NOT be inferred from documentation volume, successful isolated tests, or internal confidence alone.

## Core Rule

> **ARGO SHALL NOT claim a capability merely because it can describe, design, or attempt that capability. The capability must be classified by evidence.**

## Required evidence classes

1. **Internal evidence** — repository, contracts, tests, CI, runtime and governed mutation evidence.
2. **External evidence** — users, customers, independent benchmarks, market evidence, competitor comparison, deployments and external validation.
3. **Observability boundary** — explicitly distinguish absent evidence from evidence that the available connector cannot observe.

## Capability states

- `VERIFIED` — sufficient current evidence exists.
- `DEMONSTRATED` — repeated evidence exists, but coverage or independence is incomplete.
- `PARTIAL` — meaningful evidence exists but material gaps remain.
- `UNRESOLVED` — evidence is insufficient to decide.
- `NOT OBSERVABLE` — the relevant evidence surface cannot currently be observed.
- `NOT TESTED` — no adequate test has been executed.
- `CONTRADICTED` — credible evidence conflicts with the claim.

## Minimum record for every material capability

`Claim → Evidence → Test/Observation → Result → Confidence → Limitations → Last verified HEAD`

## Required capability domains

- repository access and mutation;
- connector capability discovery;
- evidence/provenance integrity;
- relationship/graph validation;
- policy/governance correlation;
- CI execution and observability;
- runtime reachability;
- self-diagnosis;
- controlled self-correction;
- learning/reuse;
- regression resistance;
- product readiness;
- external validation;
- market position.

## Self-evaluation requirements

ARGO SHALL publish strengths, weaknesses, unknowns, failed cases, unobservable boundaries, and unsupported claims together. A self-score without evidence is non-authoritative.

Internal success SHALL NOT be treated as proof of market superiority, product-market fit, customer value, or competitive advantage.

## Independence boundary

A self-assurance result produced by the same model/session that implemented the assessed change is not independent merely because a different ARGO role label was used.

Use `GOV-015` evidence labels:

- `SELF_REVIEWED_NOT_INDEPENDENT`;
- `CROSS_ROLE_REVIEW_NOT_PROVEN_INDEPENDENT`;
- `INDEPENDENTLY_VALIDATED` only when distinct evidence supports the independence claim.

External evidence entering ARGO remains subject to its applicable provenance/authentication/qualification boundary before it can support an external-validation claim.

## Review cadence

Self-assurance SHALL be refreshed at material architecture milestones, release-readiness gates, and when significant evidence boundaries change.

## Initial conclusion preserved from 2026-08-27

ARGO demonstrates a healthy self-critical engineering pattern: it can inspect, test, detect contradictions, record reusable learning, revise governed rules, and re-verify. However, formal self-proof and external market validation remain incomplete.

Therefore the bounded assurance classification remains:

**Healthy Self-Critical Maturity / Not Yet Market-Proven Product.**

This classification is historical/current context, not proof that every current subsystem is independently validated.

## Non-goals

This protocol does not authorize:

- uncontrolled self-modification;
- relationship promotion;
- runtime mutation;
- marketing claims;
- provider-authenticity claims;
- cognitive-benefit claims without controlled evidence;
- authority escalation from an internal score.

---

## Related governance

- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER_PROTOCOL.md`
- `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`

---

End of GOV-017
