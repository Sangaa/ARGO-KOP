# AI-006

---

# MODEL ADAPTER

Platform: ARGO KOP
Document ID: AI-006
Version: 1.2.2
Status: Integrity Hold / Revalidation Required
Category: AI
Canonical: Yes
Last Audit: 2026-08-10

---

# Audit Boundary

The semantic changes introduced on 2026-08-09 were made before the adversarial session failure was documented and therefore require independent post-session verification. The current document is retained provisionally; this status does not certify the 2026-08-09 mutation as finally validated.

# Purpose

Defines the model-adapter boundary that allows ARGO to operate with different AI models without making any model, vendor, API, operating system or deployment environment part of ARGO's identity.

The adapter is an interoperability boundary, not a source of authority.

# Objectives

The Model Adapter shall:

- provide model independence;
- normalize engineering interaction;
- preserve repository consistency;
- support multiple AI providers and local engines;
- support future standalone ARGO runtimes;
- preserve deterministic governance behavior where practical;
- reduce platform dependency;
- allow transport and packaging to evolve without changing the ARGO knowledge model.

# Adapter Philosophy

AI models may differ.

Transport mechanisms may differ.

Operating environments may differ.

**ARGO identity, authority and repository semantics shall not depend on any of them.**

# Interoperability Boundary

The adapter shall expose a stable logical contract independent of transport.

Possible transport mechanisms include, but are not limited to:

- file exchange;
- structured package exchange;
- API;
- command-line or local process integration;
- plugin/connector integration;
- message or queue transport;
- future embedded or standalone runtime interfaces.

No transport is canonical merely because it is implemented first.

# Portable Session Exchange

The preferred cross-platform exchange unit is a **portable session package** containing, as applicable:

- session identity;
- source model / instance;
- ARGO context or context reference;
- repository baseline / commit;
- task objective;
- verified findings;
- errors and corrections;
- lessons learned;
- rejected/deferred learning;
- improvement candidates;
- unresolved questions;
- repository impact;
- handoff status;
- evidence references;
- reviewer information;
- ingestion status.

The package format shall be machine-readable where practical and remain human-inspectable where practical.

The exchange package is a transport artifact, not repository authority.

# Transport Neutrality

ARGO shall not require one specific API, operating system, cloud service, application or vendor to exchange session learning.

A future implementation may replace file-based exchange with an API, or an API with local/embedded exchange, without changing the semantic contract of the learning handoff.

# Adapter Responsibilities

- normalize model interaction;
- load ARGO context;
- identify repository baseline;
- apply applicable repository rules;
- preserve authority boundaries;
- normalize session handoff data;
- validate required exchange fields;
- support transport conversion;
- preserve traceability across transport boundaries;
- report unavailable or incomplete evidence.

# Knowledge Source Semantic Boundary

`Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md` defines the semantic model for source identity, provenance, evidence states and source-versus-ARGO knowledge distinction used by model adapters.

AI-006 consumes these semantics but does not redefine or grant authority through them. Transport success, adapter availability or model output remains evidence/input and does not by itself establish canonical knowledge.

# Adapter Non-Responsibilities

The adapter shall not:

- redefine Constitution;
- grant authority to a model;
- convert external model restrictions into ARGO rules;
- invent repository content;
- silently change canonical ownership;
- treat transport success as learning acceptance;
- treat a model response as repository truth.

# Model Switching

Switching AI providers shall not require repository restructuring merely because the provider changed.

Switching transport shall not require changing the learning semantics.

Changing repository authority or architecture remains a governed change independent of adapter implementation.

# Future Standalone Runtime

ARGO may eventually operate as an independent platform with its own runtime, memory, knowledge, decision, learning, interface and integration services.

The current adapter boundary shall therefore remain implementation-neutral so that external model sessions can later become optional connectors rather than architectural dependencies.

# Validation Requirements

Before an exchange is accepted, verify as applicable:

- source identity;
- repository baseline;
- exchange completeness;
- evidence references;
- authority requirements;
- affected relationships;
- transport integrity;
- post-ingestion validation.

The semantic interpretation of source identity, provenance and evidence-state transitions shall remain aligned with `MOD-011`; this reference does not transfer canonical authority to the adapter.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `AI/AI-001_AI_MODEL.md`
- `AI/AI-007_MULTI_MODEL_SUPPORT.md`
- `AI/AI-008_AI_GOVERNANCE.md`
- `Interfaces/INTF-004_API.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Memory/Engineering_Journal/SESSION_LEARNING_HANDOFF_TEMPLATE.md`
- `Core/CORE-003_CONSTITUTION.md`

# Guiding Statement

**Models, transports and environments may change; ARGO's identity, authority and learning semantics remain independent of them.**

---

End of Document
