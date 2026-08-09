# KNW-002

---

# KNOWLEDGE CLASSIFICATION

---

Platform: ARGO KOP  
Document ID: KNW-002  
Version: 1.2.1  
Status: Integrity Hold / Revalidated  
Category: Knowledge  
Canonical: Yes  
Last Audit: 2026-08-09  

---

# Purpose

This document defines the classification dimensions used throughout ARGO KOP so knowledge remains discoverable, attributable, correctly scoped and reusable without confusing subject matter with ownership or authority.

# Classification Dimensions

Knowledge classification uses separate dimensions.

## Subject Classification

Describes **what the knowledge is about**.

Primary classes may include:

Architecture

Governance

Repository

Platform

Business

Operational

Project

Technical

Reference

Historical

Research

Decision

## Domain / Scope Classification

Describes **where the knowledge belongs**.

- `SESSION`
- `USER`
- `PROJECT`
- `DEPLOYMENT`
- `SHARED_CANDIDATE`
- `PLATFORM`

Subject classification and domain classification shall not be conflated.

Example: a `Technical` knowledge item may belong to a `USER` or `PROJECT` domain and does not become Platform knowledge merely because it is technically useful.

# Knowledge States

Classification does not determine authority.

A classified item may be:

- `CANDIDATE`
- `VALIDATED`
- `AUTHORIZED`
- `CANONICAL`
- `HOLD`
- `REJECTED`

`VALIDATED` does not automatically mean `CANONICAL`.

# Ownership

Every governed knowledge object shall identify its owner or owning scope.

User-owned, project-owned and deployment-specific knowledge remains attributable to that scope unless explicitly promoted.

# Source and Provenance

Every material knowledge object shall preserve its source/provenance as applicable.

Sources may include:

Repository Documents

Operational Experience

User Experience

Project Records

Validated External Sources

AI Model Outputs

AI Model Outputs are candidate evidence or source material and do not receive canonical authority automatically.

For connected AI, tools, databases and other external sources, `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md` defines the semantic source/provenance boundary. Classification consumes those source and evidence semantics; it does not redefine source authority or provenance rules.

# Primary Knowledge Classes

## Architecture

Platform Structure, Layer Models, Dependencies, Integration and Architectural Decisions.

## Governance

Policies, Standards, Naming, Versioning, Traceability and Compliance.

## Repository

Repository Structure, Navigation, Ownership, Lifecycle and Repository Standards.

## Platform

Knowledge describing governed platform behavior, capabilities and canonical platform concepts.

## Business

Business Processes, Rules, Entities, Relationships and Concepts.

## Operational

Daily Operations, Execution Procedures, Operational Standards, Experience and Lessons.

## Project

Knowledge specific to a project. Project knowledge does not redefine platform knowledge without applicable governance and promotion.

## Technical

Implementation guidance, technology references, engineering practices and integrations.

## Reference

Definitions, indexes, catalogs, mappings and reference tables.

## Historical

Archived knowledge, past decisions, repository history and historical versions.

## Research

Validated external findings, comparative studies, analysis and future opportunities.

## Decision

Governed engineering, architectural, repository or policy decisions.

# Classification Rules

Every governed knowledge object should have, as applicable:

- one primary subject classification;
- optional secondary classifications;
- one declared domain/scope;
- owner;
- source/provenance;
- evidence state;
- status;
- version;
- repository location;
- relationships.

Repository location is a storage fact, not a substitute for knowledge domain or authority.

When source/provenance information is supplied by an external model or connector, the source claim must remain distinguishable from ARGO's resulting knowledge classification and interpretation.

# Reclassification

Knowledge may be reclassified when new evidence, ownership changes, project boundaries, deployment context or broader validation changes its appropriate scope.

Reclassification shall preserve traceability and shall not silently rewrite historical meaning.

# Promotion Candidate

Knowledge that appears reusable beyond its original scope may be marked `SHARED_CANDIDATE`.

Promotion toward `PLATFORM` requires evidence, validation, contradiction review, impact analysis, applicable privacy/confidentiality review, authority and provenance.

Promotion shall not be inferred from source reliability, model agreement, transport success or connector availability alone.

# Repository Validation

Knowledge reviews shall verify, as applicable:

Classification Accuracy

Domain / Scope Accuracy

Ownership

Provenance

Evidence State

Relationships

Repository Alignment

Architecture Alignment

Governance Compliance

Promotion Status

# Reviewability

This classification system is itself reviewable. If a simpler classification preserves the same or better clarity, traceability and governance protection, it may replace the current model through the applicable governance process.

# Related Documents

- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `Knowledge/KNW-005_KNOWLEDGE_GOVERNANCE.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Memory/MEM-001_MEMORY_MODEL.md`
- `Memory/MEM-005_MEMORY_GOVERNANCE.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`
- `Repository/REP-001_MASTER_INDEX.md`

# Guiding Statement

**Classify what the knowledge means, where it belongs, who owns it, what evidence supports it, and what authority it has. Never collapse these questions into one label.**

---

End of Document
