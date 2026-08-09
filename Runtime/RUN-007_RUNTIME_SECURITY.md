# RUN-007

---

# RUNTIME SECURITY

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: RUN-007
Version: 1.2.1
Status: Validated / Integrity Hold
Category: Runtime
Canonical: Yes
Priority: Critical
Development Baseline: 3.3.0
Latest Official Release: 1.0.0
Last Audit: 2026-08-09

---

# Purpose

Defines the Runtime Security model of ARGO KOP.

Runtime Security protects repository integrity during execution while preserving authority boundaries, external connector boundaries, authorization state, provenance, and traceability.

# Security Principles

- Repository First
- Least Authority
- Explicit Validation
- Deterministic Execution
- Complete Traceability
- Governed Recovery
- No Hidden State
- Explicit External Authorization
- Provenance Preservation

Security controls execution; it does not redefine repository authority.

# Protected Assets

- Repository Structure
- Canonical Documents
- Repository Tree
- Architecture
- Governance
- Knowledge
- Memory
- Engineering History
- Runtime Configuration
- External Connector Credentials / Tokens where applicable
- Connector Provenance and Execution Evidence

# Runtime Validation

Before every write or security-sensitive engineering operation verify, as applicable:

- repository synchronized;
- repository integrity;
- architecture validity;
- governance validity;
- current repository baseline;
- canonical references;
- engineering target;
- required dependencies;
- applicable interface contract;
- authorization scope;
- source / connector provenance;
- expected execution boundary.

# Runtime Access Rules

Runtime may:

- read repository and applicable context;
- read Governance and Architecture;
- modify authorized engineering targets;
- generate or update canonical documents when authorized;
- update status records when the evidence supports the change;
- consume external evidence through an authorized interface;
- request an external action only within an established authorization scope.

Runtime shall never:

- invent repository files, folders or relationships;
- bypass Governance or Architecture;
- modify unrelated canonical artifacts without justification;
- treat historical completion as current authorization;
- treat connector availability as authorization;
- allow a connector to grant itself authority;
- treat external observations as canonical facts without validation;
- continue unsafe writes after a failed validation gate.

# External Connector Security

External systems, APIs, devices, files and AI providers are security boundaries, not authorities.

The security sequence is:

Connector

↓

Interface Contract

↓

Authentication where required

↓

Authorization Scope

↓

Provenance / Acquisition Context

↓

Execution

↓

Execution Result / Evidence

Authorization shall be explicit where the operation requires it.

Credentials and tokens MUST NOT be treated as permission to perform actions outside their defined scope.

A successful authentication MUST NOT be interpreted as authorization for every operation available through the provider.

# External Evidence Security

The runtime shall preserve, where materially available:

- source identity;
- acquisition timestamp;
- acquisition context;
- transformation history;
- quality / confidence indicators;
- authorization state;
- execution state;
- material errors or limitations.

The following remain distinct:

Observation ≠ Interpretation

Interpretation ≠ Fact

Model Output ≠ Canonical Knowledge

External Evidence ≠ Repository Authority

# Execution Status

External actions may result in:

- `SUCCESS`
- `FAILURE`
- `PARTIAL`
- `TIMEOUT`
- `DENIED`
- `UNKNOWN`

`UNKNOWN` MUST NOT be silently converted into `SUCCESS`.

When the external system does not provide reliable confirmation, the runtime shall report the uncertainty and preserve the evidence needed for later reconciliation.

# Security Events

Generate or preserve security evidence for:

- repository mismatch;
- repository corruption;
- architecture conflict;
- governance conflict;
- baseline/version mismatch;
- folder status inconsistency;
- unauthorized target;
- missing authorization;
- connector authentication failure;
- authorization denial;
- provenance failure;
- unexpected connector response;
- execution interruption;
- unknown external execution state;
- recovery event.

# Recovery

If a security violation or material integrity failure is detected:

1. Stop unsafe engineering.
2. Preserve current state and evidence.
3. Enter `HOLD` or `FAULT` as appropriate.
4. Resolve the underlying repository, authority, interface or security issue.
5. Revalidate before resuming.

Automatic recovery MUST NOT silently discard evidence or override authority.

# Learning and Memory Boundary

Security-relevant observations may be retained as operational evidence and may contribute to applicable Session / User / Project memory.

They MUST NOT become canonical ARGO platform rules merely because they were observed during runtime.

Learning candidates remain subject to the applicable validation and promotion gates.

# Engineering Integrity

Every engineering action should remain:

- deterministic;
- traceable;
- recoverable;
- reviewable;
- repository compliant;
- architecture compliant;
- governance compliant;
- authorization compliant.

# Related Documents

- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-008_RUNTIME_STATE.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/INTF-010_INTEGRATIONS.md`
- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`

---

# Guiding Statement

Runtime Security protects execution by protecting repository reality, enforcing least authority, preserving external provenance, and maintaining governed recovery.

---

End of Document
