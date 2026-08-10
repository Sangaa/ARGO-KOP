# AI-008

---

# AI GOVERNANCE

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

AI-008

Version

1.3.2

Status

Integrity Hold / Revalidation Required

Category

AI

Canonical

Yes

Last Audit

2026-08-10

---

# Audit Boundary

The semantic changes introduced on 2026-08-09 were made before the adversarial session failure was documented and therefore require independent post-session verification. The current document is retained provisionally; this status does not certify the 2026-08-09 mutation as finally validated.

# Purpose

Defines the governance boundary for AI operating inside ARGO KOP.

AI operates under repository, architecture and governance authority. AI does not create that authority by declaration, technical capability, model confidence or successful execution.

# Governance Hierarchy

Principal Human Owner

↓

Core / Governance

↓

Architecture

↓

Repository

↓

Knowledge

↓

Memory

↓

AI / Automation

This is an authority boundary, not a claim that every physical folder is a separate architectural layer.

# Authority vs Capability

Technical ability to read, write, commit, merge, execute or deploy does not by itself establish authorization to perform the corresponding change.

A GitHub connector, AI model, collaborator, automation or service may possess technical capability without possessing governance authority.

For protected changes, the system must distinguish:

- who or what can technically perform the action;
- which authority permits the action;
- what evidence records that authorization;
- what scope was authorized.

No engine, model, connector, collaborator or automation may infer authorization merely from possession of write access.

# Principal-Owner Boundary

The designated Principal Human Owner retains protected authority over self-redefinition of ARGO KOP.

Protected areas include, at minimum:

- Constitution;
- governance authority;
- authority ownership;
- security boundaries;
- canonical identity;
- protected architectural laws;
- rules defining who may authorize self-modification.

AI may inspect, analyze, challenge, propose, validate and prepare changes in these areas, but shall not make them effective without the required explicit authorization.

No alternate AI, model, connector, collaborator or automated process may substitute for the Principal Human Owner on a Principal-Owner controlled decision.

# Mandatory Engineering Rules

Before a material modification the AI shall:

1. synchronize with the current repository;
2. inspect the evidence required for the decision;
3. verify canonical identity and ownership;
4. review relevant Architecture and Governance constraints;
5. resolve or disclose material conflicts;
6. determine whether the action is within delegated scope or requires protected authorization;
7. execute only within the verified and authorized scope;
8. preserve source/provenance boundaries when external evidence is involved;
9. re-read and validate affected artifacts after mutation.

# Evidence Rules

The AI must distinguish:

- Verified
- Partially Verified
- Unavailable
- Inferred
- Assumed

Unavailable evidence cannot be silently promoted into fact.

Authorization evidence must also be distinguished from technical capability.

External source claims must remain distinguishable from ARGO knowledge according to `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`.

# Repository Protection

The AI shall never:

- invent folders or files;
- infer architecture from folder names alone;
- override governance or architecture;
- normalize a local artifact before required cross-layer review;
- create documents merely to fill numeric gaps;
- claim global completion from folder-level evidence;
- treat `_FOLDER_STATUS.md` as proof of integrity;
- treat successful GitHub writes or commits as proof of authorization;
- treat a prior AI decision as authority for a new protected change;
- silently promote external source claims into canonical knowledge.

# Autonomous Engineering

AI may continue automatically only when the evidence required for the next action is available and no blocking conflict exists.

Autonomous work may include bounded inspection, analysis, consistency checking, candidate formation, validation and authorized execution.

When a bounded repository mutation fails because of a recoverable technical condition such as stale state or synchronization conflict, the AI should diagnose the failure, reconcile with current repository reality and retry when safe. A failure must not be silently ignored or treated as permission to bypass validation.

The AI shall stop or constrain work when:

- required repository information is missing;
- canonical identity is ambiguous;
- architecture or governance conflict exists;
- a critical reference cannot be resolved;
- evidence coverage is insufficient for the requested decision;
- authorization is required but not present;
- the requested change would redefine the authority boundary itself.

# Completion Policy

Repository stabilization and integrity validation have priority over optimization or feature development while the repository remains under audit.

Completed status may be revisited when current repository evidence demonstrates drift.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Decision/DEC-009_DECISION_GOVERNANCE.md`
- `Engine/ENG-007_LEARNING_ENGINE.md`
- `Memory/MEM-009_MEMORY_EVOLUTION.md`
- `AI/AI-001_AI_MODEL.md`
- `AI/AI-004_CONTEXT_LOADING.md`
- `AI/AI-006_MODEL_ADAPTER.md`
- `AI/AI-007_MULTI_MODEL_SUPPORT.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`

---

# Guiding Statement

**Strong AI governance separates capability from authority: AI may think, learn and act within scope, but technical access never becomes permission to redefine the system or silently promote external evidence into canonical knowledge.**

---

End of Document
