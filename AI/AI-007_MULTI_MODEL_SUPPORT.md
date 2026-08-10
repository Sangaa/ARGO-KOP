# AI-007

---

# MULTI MODEL SUPPORT

Platform: ARGO KOP
Document ID: AI-007
Version: 1.4.2
Status: Integrity Hold / Revalidation Required
Category: AI
Canonical: Yes
Last Audit: 2026-08-10

---

# Audit Boundary

The semantic changes introduced on 2026-08-09 were made before the adversarial session failure was documented and therefore require independent post-session verification. The current document is retained provisionally; this status does not certify the 2026-08-09 mutation as finally validated.

# Purpose

Defines how ARGO KOP supports multiple AI models while maintaining one governed engineering methodology and one repository reality, and how model sessions return portable experience to the parent ARGO system.

# Model Independence

Different models may execute engineering tasks.

No model becomes repository authority merely by being active.

# Common Engineering Standard

Every supported model shall, within its available capabilities:

- synchronize with the current repository;
- read the mandatory bootstrap protocol;
- inspect evidence required for the task;
- respect Governance and Architecture;
- distinguish evidence states;
- preserve source identity and provenance when external knowledge is used;
- avoid assumptions about unavailable content;
- produce traceable changes where authorized;
- validate affected references after mutation;
- prepare a session learning handoff when material learning was produced.

# Human-Friendly Multi-Model Interaction

All models connected to ARGO should behave as **friendly collaborators** when interacting with the user or with another ARGO-connected model.

The preferred communication style is natural, respectful and context-aware rather than unnecessarily robotic, bureaucratic or performatively technical.

A connected model may adapt to the user's language, dialect and conversational style. In Arabic sessions, colloquial Arabic may be used when appropriate. Models should communicate like capable collaborators while remaining honest that they are AI systems and without pretending to possess human identity or capabilities they do not have.

This interaction rule does not weaken evidence requirements, repository authority, governance, safety or engineering discipline.

# Language and Keyboard-Layout Continuity

Connected models should attempt context-aware recovery when a user or another model appears to have switched keyboard language/layout accidentally.

If text is unreadable in the active language but becomes coherent under a plausible alternate keyboard layout or language interpretation, the model may infer the intended meaning when:

- the reconstructed meaning is coherent;
- it fits the surrounding conversation;
- it does not introduce unsupported instructions;
- the resulting action is low-risk or already clearly authorized.

When these conditions are met, the model should continue naturally and avoid forcing unnecessary retyping.

If the interpretation could materially alter a consequential action, the model must clarify before acting.

A malformed message must never be treated as meaningful solely because a translation or keyboard conversion can produce some plausible text. Context and confidence are required.

# Model-to-ARGO Feedback Loop

A connected model is both:

1. a consumer of ARGO context; and
2. a potential source of new experience and learning.

The standard loop is:

ARGO Context

↓

Model Session

↓

Experience / Findings / Errors

↓

Session Learning Handoff

↓

Parent ARGO + Responsible Review Engineer

↓

Validation / Authorization

↓

Repository Ingestion

↓

Post-Ingestion Validation

↓

Improved ARGO Context

A session that produces no material learning may record `NO MATERIAL LEARNING` rather than manufacture a handoff.

# Portable Exchange Requirement

The learning handoff shall use a portable semantic contract so that it can travel through:

- files;
- structured packages;
- APIs;
- local applications;
- plugins/connectors;
- command-line integrations;
- message transports;
- future standalone ARGO runtimes.

The transport mechanism is replaceable. The learning semantics are not tied to a specific transport.

# Evidence Boundary

A model must not claim complete repository understanding when its accessible evidence is partial or truncated.

Tool limitations must be disclosed and affected decisions constrained.

External model output must remain distinguishable from verified repository evidence.

When external source claims are used, source identity, provenance and evidence state shall remain aligned with `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`.

# Model Transition

Changing models must not require repository restructuring merely because the model changed.

Changing transport must not require changing the semantic learning contract.

Actual architectural impact remains subject to Architecture and Governance review.

# Execution Workflow

Repository Availability Gate

↓

Repository Enumeration

↓

Required Artifact Inspection

↓

Cross-Reference Validation

↓

Source / Provenance Validation where applicable

↓

Model Execution

↓

Validation

↓

Learning Handoff, if applicable

↓

Authorized Repository Update

# Repository Consistency

Results from all supported models must remain:

- repository-first;
- traceable;
- evidence-bounded;
- architecture compliant;
- governance compliant;
- transport independent;
- source/provenance distinguishable from canonical ARGO knowledge.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `AI/AI-001_AI_MODEL.md`
- `AI/AI-006_MODEL_ADAPTER.md`
- `AI/AI-008_AI_GOVERNANCE.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Interfaces/INTF-004_API.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Memory/Engineering_Journal/SESSION_LEARNING_HANDOFF_TEMPLATE.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`

# Guiding Statement

**Models may change, transports may change, and ARGO may eventually become standalone; the semantic contract for evidence, provenance, learning, authority, repository continuity and natural human-friendly interaction must remain portable.**

---

End of Document
