# KNW-004

---

# KNOWLEDGE LIFECYCLE

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: KNW-004  
Version: 1.3.1  
Status: Integrity Hold / Revalidated  
Category: Knowledge  
Canonical: Yes  
Last Audit: 2026-08-09  

---

# Purpose

This document defines the lifecycle of knowledge objects within ARGO KOP.

It does not define the lifecycle of the platform itself, repository documents as artifacts, projects or decisions.

The lifecycle explicitly separates knowledge belonging to the platform from knowledge belonging to a user, project or deployment.

# Knowledge Scope Classification

Before validation, every knowledge candidate should be assigned the narrowest applicable scope:

- `SESSION` — temporary working context;
- `USER` — experience, preferences or lessons belonging to a user;
- `PROJECT` — knowledge specific to a project;
- `DEPLOYMENT` — knowledge specific to an operating environment;
- `SHARED_CANDIDATE` — proposed reusable knowledge supported across contexts;
- `PLATFORM` — governed ARGO knowledge accepted as canonical.

Scope may be changed only through an explicit promotion or reclassification event.

# Lifecycle

Observation

↓

Capture

↓

Scope Classification

↓

Validation

↓

Classification & Ownership

↓

Domain Storage

↓

Relationship Validation

↓

Operational Use

↓

Review / Learning

↓

Promotion or Reclassification Decision

↓

Authorized Update / Archive

# Stage Definitions

## Observation

Information is discovered.

No repository authority.

## Capture

A knowledge candidate is documented with available provenance and evidence state.

Awaiting validation.

For external AI, tools, databases and other connected sources, source identity and provenance shall remain distinguishable from ARGO's interpretation.

## Scope Classification

The candidate is assigned the narrowest applicable knowledge domain. Scope is not inferred from usefulness alone.

## Validation

Evidence is reviewed.

Governance, architecture, repository alignment and claim-specific sufficiency are checked.

Source provenance and evidence state are validated where applicable.

## Classification & Ownership

The knowledge object receives its category, owner, relationships and applicable repository location.

Source ownership, ARGO ownership and authority are not conflated.

## Domain Storage

Validated knowledge is stored in the memory/knowledge domain appropriate to its scope. User or project knowledge does not become platform knowledge merely because it is stored in the repository.

## Relationship Validation

The object is connected to relevant authorities, evidence, consumers and related knowledge.

Relationship existence must be validated; a path or textual reference alone is insufficient.

For source-derived knowledge, provenance must remain traceable through the relationship chain.

## Operational Use

Knowledge may be consumed by projects, runtime, reasoning, documentation and operational processes within its applicable scope and authority boundaries.

## Review / Learning

Accuracy, completeness, relevance, consistency and practical outcomes are periodically checked. Errors and successful outcomes may produce new learning candidates.

## Promotion or Reclassification Decision

A knowledge object may remain local, be superseded, be reclassified, or be proposed for broader reuse.

Promotion from `USER`, `PROJECT` or `DEPLOYMENT` toward `SHARED_CANDIDATE` or `PLATFORM` requires evidence, broader applicability assessment, contradiction review, impact analysis and the authority applicable to the target scope.

Source reliability, model agreement or transport availability do not substitute for validation or authority.

## Authorized Update / Archive

Approved improvements are incorporated with traceability. Superseded knowledge becomes historical where retention is required.

# Knowledge Validation

Knowledge shall be accepted for its declared scope only after applicable:

- Evidence Verification
- Architecture Alignment
- Governance Compliance
- Repository Review
- Relationship Validation
- Ownership / Scope Check
- Provenance Verification
- Approval or Authorization appropriate to the target state

`VALIDATED` does not automatically mean `CANONICAL`.

# Cross-Lifecycle Boundary

`KNW-004` is the **knowledge-object lifecycle**.

It interacts with:

- `CORE-009` — platform evolution lifecycle.
- `REP-006` — repository artifact lifecycle.
- `GOV-005` — document artifact lifecycle.
- `Memory/MEM-001_MEMORY_MODEL.md` — memory domains.
- `Memory/MEM-004_MEMORY_LIFECYCLE.md` — memory lifecycle.
- `Memory/MEM-005_MEMORY_GOVERNANCE.md` — memory ownership and authority.
- `Memory/MEM-009_MEMORY_EVOLUTION.md` — memory learning and promotion.
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md` — source identity, provenance and evidence semantics.

These lifecycles are complementary.

A knowledge object can be in a knowledge lifecycle stage while the file representing it has a separate document lifecycle state, the repository is in another lifecycle stage, and its source experience remains in a user/project memory domain.

No one of these states automatically proves the others.

# Repository Integrity

Knowledge lifecycle shall preserve:

Architecture

Governance

Repository Structure

Knowledge Relationships

Traceability

Version History

Scope and Ownership

Source Provenance

# Lifecycle Events

Create

Validate

Classify

Integrate

Use

Review

Learn

Promote

Reclassify

Revise

Archive

Every material event shall be recorded where the applicable traceability authority requires it.

# Reviewability

This lifecycle is itself reviewable. If a rule is shown to be incorrect, contradictory or unnecessarily complex, it may be revised through the applicable governance process.

# Related Documents

- `Models/MOD-001_KNOWLEDGE_MODEL.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md`
- `Knowledge/KNW-005_KNOWLEDGE_GOVERNANCE.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`
- `Core/CORE-003_CONSTITUTION.md`

# Guiding Statement

**Knowledge evolves through evidence and experience, but its scope, ownership, provenance and authority must remain explicit throughout the lifecycle.**

---

End of Document