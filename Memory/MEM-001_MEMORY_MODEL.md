# MEM-001

---

# MEMORY MODEL

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: MEM-001  
Version: 1.2.0  
Status: Integrity Hold / Revalidated  
Category: Memory  
Canonical: Yes  
Last Audit: 2026-08-09  

---

# Purpose

This document defines the canonical memory model of ARGO KOP.

A fundamental architectural separation applies:

> **ARGO Platform Memory is the memory of the ARGO system; User, Session and Deployment Memory stores experience accumulated while ARGO is used.**

These domains may exchange learning candidates through governed promotion, but they are never treated as one undifferentiated memory pool.

# Memory Domains

## 1. Platform Memory

Stores validated knowledge required to define and operate ARGO itself, including applicable constitutional, architectural, governance, cognitive and system-level learning.

Platform Memory is repository-controlled and may become canonical only through the applicable authority process.

## 2. User Memory

Stores experience belonging to a specific user, including user-specific working patterns, preferences, project history and lessons.

User Memory remains owned/scoped to that user or deployment and does not become platform memory merely because ARGO learned from it.

## 3. Project / Deployment Memory

Stores contextual experience belonging to a project, organization or deployment environment.

It may be reusable locally without becoming a platform-wide rule.

## 4. Session / Working Memory

Temporary execution context. It may generate learning candidates but has no canonical authority.

## 5. Shared Learning Candidates

Potentially generalizable experience extracted from user, project, deployment or external-model feedback. It remains non-canonical until independently reviewed and promoted.

# Memory Layers

Working Memory
↓
Session Memory
↓
User / Project / Deployment Memory
↓
Shared Learning Candidate
↓
Validation & Scope Review
↓
Platform Memory (only when authorized)
↓
Historical / Archived Memory

# Promotion Rule

Experience must never move silently from a local memory domain into Platform Memory.

Promotion requires, as applicable:

- evidence;
- validation;
- generalizability assessment;
- contradiction and impact review;
- provenance;
- authority check;
- explicit publication when protected authority is affected.

# Demotion / Localisation Rule

A platform rule must not be copied into every user's memory as if it were personal experience. Runtime implementations may expose platform knowledge to users, but provenance and scope remain distinguishable.

# Memory Rules

- Repository authority remains authoritative for canonical platform memory.
- User memory remains distinct from platform memory.
- Project and deployment experience remains scoped to its owner/environment unless promoted.
- Temporary context never bypasses governance.
- Learning may be autonomous; canonical authority acquisition is not.
- Historical states remain traceable.
- Memory changes preserve provenance and affected relationships.

# Lifecycle

Capture → Classify → Validate → Scope Review → Store in Correct Domain → Operational Use → Learn → Review → Promote if justified → Archive when inactive

# Repository Integrity

Memory shall preserve:

Traceability

Context

Scope / Ownership

Provenance

History

Relationships

Architecture Alignment

Governance Compliance

# Related Documents

- `Memory/MEM-004_MEMORY_LIFECYCLE.md`
- `Memory/MEM-005_MEMORY_GOVERNANCE.md`
- `Memory/MEM-008_MEMORY_TRACEABILITY.md`
- `Memory/MEM-009_MEMORY_EVOLUTION.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`
- `Core/CORE-003_CONSTITUTION.md`

# Guiding Statement

**ARGO remembers what belongs to ARGO, users retain what belongs to their experience, and shared learning crosses that boundary only through evidence, scope review and governed promotion.**

---

End of Document
