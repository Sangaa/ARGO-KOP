# RUN-005

---

# RUNTIME WORKFLOW

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: RUN-005
Version: 1.2.0
Status: Validated / Integrity Hold
Category: Runtime
Canonical: Yes
Priority: Critical
Development Baseline: 3.2.1
Latest Official Release: 1.0.0
Last Audit: 2026-08-08

---

# Purpose

Defines the governed Runtime Workflow executed by ARGO KOP from repository synchronization through an approved engineering operation.

# Workflow Overview

Receive / Select Repository State

↓

Synchronize and Validate

↓

Load Current Context

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

# Repository Scan

The workflow loads the repository structures and canonical artifacts required for the current operation. It MUST NOT claim that every file was scanned when only a relevant subset was inspected.

# Engineering Priority

Priority is determined from current repository evidence, folder status, dependencies, architecture, governance and the active engineering objective.

Hard-coded priority lists are advisory only and MUST NOT override explicit repository authority or current dependencies.

# Folder Execution

For each selected folder:

1. Load applicable README / canonical documents / folder status.
2. Resolve dependencies and authority.
3. Identify the exact required change.
4. Preserve unrelated content.
5. Apply the smallest safe complete-file update when replacement is required.
6. Validate references, metadata and consistency.
7. Re-read the resulting artifact.
8. Record the commit / revision.

# Validation

Validate as applicable:

- Repository integrity
- Architecture consistency
- Governance compliance
- Cross-references
- Folder completion state
- Version alignment
- Dependency integrity
- Resulting file content

# Continuation Rule

Continuation is conditional, not unconditional.

The runtime MAY continue automatically when:

- the previous operation passed required validation;
- the next target is known;
- dependencies are resolvable;
- no authority conflict exists;
- no material ambiguity exists.

The runtime MUST stop or enter `HOLD` / `FAULT` when any required gate fails.

# Stop Conditions

Stop when:

- repository corruption exists;
- architecture conflict exists;
- governance conflict exists;
- required dependency is missing;
- canonical identity is ambiguous;
- validation fails;
- the requested operation cannot be executed safely.

# Runtime Rules

Repository Reality > Historical Claims

Repository Authority > Runtime Assumptions

Validation > Automatic Continuation

Preserve unrelated content

No undocumented dependency

No unsafe write after failed validation

# Related Documents

- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-002_INITIALIZATION.md`
- `Runtime/RUN-003_CONFIGURATION.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-009_RECOVERY.md`
- `PROJECT_BOOTSTRAP.md`

---

# Guiding Statement

Deterministic engineering requires governed continuation, not unconditional automation.

---

End of Document
