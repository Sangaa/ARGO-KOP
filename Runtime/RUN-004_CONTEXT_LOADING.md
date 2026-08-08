# RUN-004

---

# CONTEXT LOADING

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: RUN-004
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

Defines the Runtime Context Loading mechanism. Context Loading ensures engineering decisions are based on current synchronized repository evidence rather than temporary conversation history.

Context Loading is mandatory before each engineering operation whose correctness depends on repository state.

# Context Priority

Repository Reality

↓

PROJECT_BOOTSTRAP.md

↓

Repository Tree / Canonical Index

↓

Current Folder Context

↓

Canonical Documents

↓

Applicable Folder Status

↓

Repository Memory

↓

Conversation / Request Context

Conversation supplies intent and task information; it does not override repository authority.

# Context Loading Workflow

Repository Synchronization

↓

Repository Integrity Check

↓

Repository Tree / Index Loading

↓

Target Folder Selection

↓

Folder Context Loading

↓

Dependency / Authority Validation

↓

Execution

# Repository Context

Runtime SHOULD load the current evidence relevant to the operation, including:

- Repository revision / baseline
- Repository structure
- Canonical index and map
- Relevant folder states
- Current engineering target
- Applicable Governance and Architecture constraints

The runtime MUST NOT treat a historical `completed` claim as current state without validation.

# Folder Context

Before engineering a folder, load as applicable:

- `README.md`
- Canonical documents
- `_FOLDER_STATUS.md`
- Related documents
- Dependencies
- Architecture references
- Governance references

# Repository Reality Rule

Repository Reality overrides:

- Conversation
- AI memory
- Previous sessions
- Temporary notes
- Engineering assumptions

However, the current user request remains the source of requested intent and MUST be combined with repository evidence rather than ignored.

# Context Refresh

Refresh context whenever:

- repository synchronization occurs;
- repository revision changes;
- engineering switches to another folder;
- a canonical artifact changes;
- a relevant folder completion state changes;
- a validation failure requires re-evaluation.

# Context Validation

Before execution verify, as applicable:

- repository synchronized;
- required repository context loaded;
- folder context loaded;
- architecture references resolvable;
- governance references resolvable;
- repository baseline current;
- required dependencies available.

# Failure Conditions

Stop or enter `HOLD` / `FAULT` when:

- repository context is unavailable;
- repository corruption is detected;
- required authority cannot be resolved;
- material ambiguity prevents safe execution;
- required engineering context is missing.

Automatic continuation is permitted only after required validation gates pass.

# Related Documents

- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-002_INITIALIZATION.md`
- `Runtime/RUN-003_CONFIGURATION.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `PROJECT_BOOTSTRAP.md`
- applicable Engine / AI context-loading specifications

---

# Guiding Statement

Correct engineering begins with correct context; correct context begins with current repository evidence.

---

End of Document
