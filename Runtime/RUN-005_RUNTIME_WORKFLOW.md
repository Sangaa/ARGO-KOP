# RUN-005

---

# RUNTIME WORKFLOW

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: RUN-005
Version: 1.3.1
Status: Validated / Integrity Hold
Category: Runtime
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1
Latest Official Release: 1.0.0
Last Audit: 2026-08-10

---

# Purpose

Defines the governed Runtime Workflow executed by ARGO KOP from repository synchronization through an approved engineering operation, including governed interaction with external connectors and evidence sources.

# Workflow Overview

Receive / Select Repository State

↓

Synchronize and Validate

↓

Load Current Context

↓

Resolve Required Interfaces / Dependencies

↓

Acquire Authorized External Evidence when required

↓

Determine Valid Engineering Target

↓

Execute Approved Operation

↓

Validate Result

↓

Persist Validated Change

↓

Re-read Affected State

↓

Continue only if the next operation is deterministically safe

# Repository Intake

The current repository state becomes the active evidence source after synchronization.

Historical context may explain prior decisions but cannot override current repository reality.

External evidence does not become repository authority merely because it is available.

# Repository Scan

The workflow loads the repository structures and canonical artifacts required for the current operation. It MUST NOT claim that every file was scanned when only a relevant subset was inspected.

# Interface and Connector Resolution

When an operation depends on an external system, device, model, API, file source or other connector, the runtime MUST resolve the applicable interface contract before execution.

The resolution sequence is:

Connector

↓

Interface Contract

↓

Authorization / Provenance

↓

Dependency Validation

↓

Runtime Consumption

An available connector does not imply authorization to act through it.

An interface contract does not imply that its implementation is validated.

# External Evidence

When authorized external evidence is required, the runtime shall preserve, as applicable:

- source identity;
- acquisition context;
- timestamp;
- transformation / normalization history;
- quality or confidence information;
- authorization state;
- execution status.

Observation, extracted signal, interpretation, model output and verified fact MUST remain distinguishable.

If execution status is unknown, the runtime MUST NOT report successful external execution without evidence establishing success.

# Engineering Priority

Priority is determined from current repository evidence, folder status, dependencies, architecture, governance and the active engineering objective.

Hard-coded priority lists are advisory only and MUST NOT override explicit repository authority or current dependencies.

# Folder Execution

For each selected folder:

1. Load applicable README / canonical documents / folder status.
2. Resolve dependencies and authority.
3. Resolve required interfaces and external dependencies, if applicable.
4. Identify the exact required change.
5. Preserve unrelated content.
6. Apply the smallest safe complete-file update when replacement is required.
7. Validate references, metadata and consistency.
8. Re-read the resulting artifact.
9. Record the commit / revision.

# Validation

Validate as applicable:

- Repository integrity
- Architecture consistency
- Governance compliance
- Cross-references
- Folder completion state
- Version alignment
- Dependency integrity
- Interface contract alignment
- Authorization / provenance requirements
- External execution state
- Resulting file content

# Continuation Rule

Continuation is conditional, not unconditional.

The runtime MAY continue automatically when:

- the previous operation passed required validation;
- the next target is known;
- dependencies are resolvable;
- applicable interfaces are resolvable;
- required authorization is established;
- no authority conflict exists;
- no material ambiguity exists.

The runtime MUST stop or enter `HOLD` / `FAULT` when any required gate fails.

# Stop Conditions

Stop when:

- repository corruption exists;
- architecture conflict exists;
- governance conflict exists;
- required dependency is missing;
- required interface contract is missing or ambiguous;
- required authorization is missing;
- canonical identity is ambiguous;
- external execution result is materially unknown for a required action;
- validation fails;
- the requested operation cannot be executed safely.

# Runtime Rules

Repository Reality > Historical Claims

Repository Authority > Runtime Assumptions

Validated Evidence > Unverified External Output

Validation > Automatic Continuation

Preserve unrelated content

No undocumented dependency

No unsafe write after failed validation

No automatic promotion of external experience into canonical knowledge

# Learning and Memory Boundary

Runtime observations, external evidence and user-specific experience may be captured for the applicable Session / User / Project memory domain.

They MUST NOT become canonical ARGO platform knowledge merely because the runtime consumed them.

Learning candidates require the applicable validation and promotion gates defined by the Learning and Memory architecture.

# Related Documents

- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-002_INITIALIZATION.md`
- `Runtime/RUN-003_CONFIGURATION.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-007_RUNTIME_SECURITY.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/INTF-010_INTEGRATIONS.md`
- `PROJECT_BOOTSTRAP.md`

---

# Guiding Statement

Deterministic engineering requires governed continuation, explicit interface boundaries, validated evidence and controlled execution—not unconditional automation.

---

End of Document
