# MEM-004

---

# MEMORY LIFECYCLE

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: MEM-004  
Version: 1.2.0  
Status: Integrity Hold / Revalidated  
Category: Memory  
Canonical: Yes  
Last Audit: 2026-08-09  

---

# Purpose

This document defines the controlled lifecycle of memory within ARGO KOP while preserving the separation between platform memory and experience belonging to users, projects and deployments.

# Lifecycle Principle

**Not everything ARGO learns belongs to ARGO.**

Every captured learning item must first be classified by scope before it can be retained or promoted.

# Lifecycle

Observation
↓
Capture
↓
Scope Classification
↓
Validation
↓
Domain Storage
↓
Operational Use
↓
Review / Learning
↓
Promotion Decision (if applicable)
↓
Archive / Supersede

# Scope Classification

Every memory candidate should be assigned one primary scope:

- `SESSION`
- `USER`
- `PROJECT`
- `DEPLOYMENT`
- `SHARED_CANDIDATE`
- `PLATFORM`
- `HISTORICAL`
- `ARCHIVED`

Scope is not inferred from usefulness alone.

# Domain Storage Rule

A validated item is stored in the narrowest domain that correctly represents its ownership and applicability.

A user's operational lesson normally remains User/Project/Deployment Memory.

A lesson may become a Shared Candidate when evidence suggests broader applicability.

A Shared Candidate may become Platform Memory only after generalizability, evidence, contradiction, architecture, governance and authority review.

# Promotion Gate

Promotion from local experience to Platform Memory requires:

1. Provenance.
2. Evidence quality.
3. Validation.
4. Generalizability assessment.
5. Contradiction review.
6. Impact analysis.
7. Authority determination.
8. Explicit publication where required.

No automatic promotion is permitted solely because a lesson is repeated, useful or produced by an AI model.

# User Memory Protection

User, project and deployment memory must remain independently retrievable and scoped.

Platform updates must not silently overwrite local experience.

Local experience must not silently modify platform memory.

Where a platform rule is derived from local experience, the originating experience remains traceable as provenance when retention is permitted and appropriate.

# Stage Definitions

## Observation

Potential experience or information is detected. No authority is created.

## Capture

The candidate is recorded with source and context.

## Scope Classification

The candidate is assigned to the appropriate memory domain.

## Validation

Evidence, consistency, relevance and applicable controls are checked.

## Domain Storage

The validated item is stored in its correct local or platform domain.

## Operational Use

Memory supports reasoning, decisions, projects or operations within its authorized scope.

## Review / Learning

Outcomes and errors may generate new learning candidates.

## Promotion Decision

Only candidates with evidence of broader applicability are considered for promotion.

## Archive / Supersede

Inactive or superseded memory remains traceable according to retention requirements.

# Authority

Repository Memory is authoritative for canonical Platform Memory.

User and deployment memory has local authority within its declared scope but does not become platform authority by itself.

Working and Session Memory never bypass governance.

# Integrity Requirements

Every lifecycle transition preserves:

- Scope
- Ownership
- Provenance
- Evidence state
- Relationships
- Version state
- Historical continuity
- Architecture alignment
- Governance compliance

# Related Documents

- `Memory/MEM-001_MEMORY_MODEL.md`
- `Memory/MEM-002_MEMORY_CLASSIFICATION.md`
- `Memory/MEM-003_MEMORY_RELATIONSHIPS.md`
- `Memory/MEM-005_MEMORY_GOVERNANCE.md`
- `Memory/MEM-008_MEMORY_TRACEABILITY.md`
- `Memory/MEM-009_MEMORY_EVOLUTION.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`

# Guiding Statement

**Memory is not one bucket: ARGO preserves its own system knowledge separately from the experience of the people and environments using it, and only governed evidence can move learning across that boundary.**

---

End of Document
