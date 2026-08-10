# CORE-000A — Platform Glossary

---

Document ID: CORE-000A

Version: 1.2.0

Status: Official / Revalidated / Integrity Hold

Classification: Core Reference

Owner: ARGO KOP

Last Audit: 2026-08-10

Review Type: Repository Re-Audit / Targeted Platform Glossary Review

---

# Purpose

This glossary defines the canonical terminology used throughout the ARGO KOP repository.

A glossary definition establishes the governed meaning of a term within ARGO's declared scope. It does not grant the glossary authority to silently reinterpret another canonical document.

If a source intentionally uses a term differently within a declared local scope, that source's scope and authority must be preserved and the difference must be recorded rather than normalized away.

# Terminology Rules

- Exact terms shall be preserved where the distinction matters.
- Different terms shall not be treated as synonyms merely because their general meanings overlap.
- A glossary definition shall not silently replace a source's own explicit definition.
- A definition is not the same thing as an interpretation, inference or commentary.
- If a term is ambiguous, conflicting or insufficiently defined, ARGO shall record the ambiguity and investigate it rather than silently choosing a preferred meaning.
- Historical usage is evidence, not permanent authority.
- External model explanations may support analysis but do not become canonical definitions automatically.
- Where a term is defined by a higher-authority source, the glossary shall reference that authority rather than inventing a competing meaning.

# Definition Integrity

For each material term, ARGO should be able to distinguish:

`Term → Definition → Scope → Authority → Usage → Related Terms`

Where appropriate, a definition should also identify:

- source/provenance;
- effective version;
- related or contrasting terms;
- known scope limitations;
- superseded definitions.

An unresolved contradiction between definitions is an integrity finding, not an invitation to invent a hidden meaning.

---

# Interpretation and Provenance Boundary

A glossary may normalize terminology for discoverability, but it shall not manufacture semantic equivalence.

When a term is encountered in a source, preserve:

```text
Observed Term
    ↓
Source Wording
    ↓
Declared Scope
    ↓
Source Authority
    ↓
Glossary Mapping
    ↓
Confirmed / Distinct / Ambiguous
```

A glossary mapping remains provisional when the source authority or intended scope has not been verified.

A glossary entry shall not be used as evidence that an implementation, architecture, process or capability exists merely because the entry names it.

# Authority Conflict Rule

If the glossary definition conflicts with a higher-authority canonical source, the conflict shall be recorded and escalated through the applicable governance path.

The glossary shall not silently overwrite the higher-authority source, and the higher-authority source shall not be silently rewritten to match the glossary.

# Terminology Change Rule

Changing a material definition requires review of known consumers, related terms, indexes and dependent documents where applicable.

A rename or terminology clarification is not automatically semantic equivalence. Where identity or meaning changes, revalidation is required.

---

# ARGO

The governed cognitive engineering platform and methodology for reasoning, knowledge organization, learning, decision making and controlled evolution.

ARGO is independent of any specific AI model.

# KOP

Knowledge Operating Platform.

The platform implementing the ARGO methodology.

# Repository

The structured knowledge base containing governed documentation, architecture, decisions, knowledge, memory, and learning records.

The Repository is the Single Source of Truth for governed ARGO platform artifacts.

# Governance

The collection of rules, authorities, controls and processes that regulate reasoning, documentation, review, authorization and repository evolution.

# Architecture

The structural design describing ARGO components, boundaries, relationships, dependencies and evolution.

# Core

The foundational identity and operating principles of the platform.

# Knowledge

Information or understanding captured for reuse and governed according to its declared source, scope, evidence and authority.

Knowledge is version controlled and traceable.

# Decision

A documented engineering, architectural, governance or operational choice supported by identified evidence and reasoning.

# Fact

Information directly verified through reliable evidence within a declared scope.

# Assumption

A proposition accepted temporarily for reasoning while verification remains required.

Assumptions shall never be presented as facts.

# Hypothesis

A proposed explanation requiring investigation and evidence before acceptance.

# Operational Reality

The actual observed behavior of users, processes, systems and workflows within a declared context.

Operational reality has priority over unsupported theoretical assumptions.

# Verified Assessment

An assessment explicitly stating, as applicable:

- Inspection Scope
- Evidence Level
- Confidence Level
- Repository Coverage
- Assessment Type
- Known Limitations

# Confidence Level

High

Evidence and verification are sufficiently complete for the declared scope.

Medium

Partial verification exists, with identified limitations.

Low

Evidence is limited, preliminary or materially incomplete.

Confidence describes evidence quality; it does not itself grant authority.

# Canonical

The governed version currently recognized as authoritative for its declared scope.

Canonical status does not make a document permanently correct or immune from review.

# Archive

Historical material preserved for traceability.

Archived documents are not current canonical authority unless explicitly designated otherwise by governance.

# Implementation

A specific AI environment or software environment operating under ARGO governance.

Examples may include:

- ChatGPT
- Gemini
- Other compatible models or independent implementations

Implementations may evolve or be replaced without changing ARGO itself.

# Engineering Review

A structured examination of repository content, relationships and evidence intended to detect contradictions, improve consistency, validate assumptions and support controlled evolution.

# Repository Drift

Any inconsistency between the governed repository definition and the actual repository contents, including missing artifacts, contradictory definitions, broken references, unauthorized changes or stale indexes.

# Interpretation

A reasoned reading of source material that goes beyond its directly stated wording.

Interpretation must remain explicitly labeled and must not be presented as the source's own meaning.

# Inference

A conclusion derived from available evidence rather than directly stated by the source.

Inference must remain distinguishable from fact, definition and source wording.

# Commentary

Explanatory material intended to assist understanding.

Commentary may clarify but does not silently replace canonical source content.

# Scope

The declared domain within which a knowledge object, rule, definition or decision applies.

Current ARGO knowledge scopes include:

- SESSION
- USER
- PROJECT
- DEPLOYMENT
- SHARED_CANDIDATE
- PLATFORM

Scope is not equivalent to authority.

# Authority

The governed basis that determines whether a rule, definition, decision or knowledge object may be treated as authoritative within its declared scope.

Authority is not created merely by age, repetition, confidence, usefulness, model output or storage location.

---

# Self-Explaining Terminology

ARGO should be understandable without a privileged interpreter.

If a core term cannot be applied from its canonical definition, scope and relationships, the terminology system should be reviewed for ambiguity, missing definitions, conflicting authority or unnecessary complexity.

The appropriate response to a terminology defect is clarification and validation, not an unmarked interpretive tradition.

# Integrity Status

This document underwent a targeted repository re-audit on 2026-08-10.

The review applies specifically to the glossary and its terminology-governance boundaries. It does not certify the entire Core folder or repository.

Core remains under `INTEGRITY HOLD` until the remaining canonical Core artifacts and relevant cross-layer relationships are revalidated.

---

# Related Documents

- `Core/CORE-004_CORE_PRINCIPLES.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Memory/MEM-001_MEMORY_MODEL.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`

# Guiding Statement

**A term must mean what its governing source establishes within its declared scope. Preserve distinctions, expose uncertainty, label interpretation, and never create authority through explanation alone.**

---

# End of Document
