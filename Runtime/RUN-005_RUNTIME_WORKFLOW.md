# RUN-005

---

# RUNTIME WORKFLOW

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

RUN-005

Version

1.1.0

Status

Approved

Category

Runtime

Canonical

Yes

Priority

Critical

---

# Purpose

This document defines the complete Runtime Workflow executed by ARGO KOP.

The workflow guarantees deterministic repository engineering from repository synchronization until engineering completion.

---

# Objectives

The Runtime Workflow shall:

Synchronize the repository.

Load runtime context.

Determine engineering priority.

Execute engineering.

Validate results.

Continue automatically.

Maintain repository consistency.

---

# Workflow Overview

Receive Repository

↓

Repository Synchronization

↓

Repository Scan

↓

Internal Knowledge Update

↓

Repository Validation

↓

Priority Analysis

↓

Engineering Queue

↓

Folder Execution

↓

Validation

↓

Folder Completion

↓

Next Folder

↓

Repository Complete

---

# Phase 1 — Repository Intake

Receive latest repository.

Replace previous repository baseline.

Discard obsolete engineering context.

Repository becomes the active execution source.

---

# Phase 2 — Repository Synchronization

Synchronize every repository file.

Synchronize repository structure.

Synchronize folder status.

Synchronize engineering baseline.

No engineering begins before synchronization completes.

---

# Phase 3 — Repository Scan

Read:

Every Folder

Every File

README.md

_FOLDER_STATUS.md

Canonical Documents

Store the repository tree internally.

---

# Phase 4 — Internal Knowledge Refresh

Update runtime knowledge from the synchronized repository.

Discard previous repository assumptions.

Repository Reality becomes the only engineering reference.

---

# Phase 5 — Engineering Priority

Determine folder status.

Priority order:

1. Runtime

2. Services

3. Models

4. Lifecycle

5. Blueprints

6. Remaining unfinished folders

Completed folders are skipped automatically.

---

# Phase 6 — Folder Execution

For each selected folder:

Load README.md

↓

Load Canonical Documents

↓

Load _FOLDER_STATUS.md

↓

Execute Engineering

↓

Validate

↓

Update Folder

↓

Generate _FOLDER_STATUS.md

↓

Continue Automatically

---

# Phase 7 — Validation

Validate:

Repository Integrity

Architecture

Governance

Cross References

Folder Completion

Repository Consistency

Version Alignment

---

# Phase 8 — Automatic Continuation

Immediately continue to the next unfinished folder.

No explanations.

No summaries.

No confirmation requests.

Engineering has execution priority.

---

# Stop Conditions

Stop only when:

Repository corruption exists.

Architecture conflict exists.

Governance conflict exists.

Repository dependency missing.

Repository ambiguity prevents deterministic execution.

Otherwise continue automatically.

---

# Runtime Rules

Repository Reality > Conversation

Repository Reality > AI Memory

Repository Reality > Assumptions

Complete Canonical File Replacement Only

No Partial Updates

Automatic Folder Continuation

---

# Related Documents

RUN-001_BOOT_SEQUENCE.md

RUN-002_INITIALIZATION.md

RUN-003_CONFIGURATION.md

RUN-004_CONTEXT_LOADING.md

RUN-006_AI_PROTOCOL.md

PROJECT_BOOTSTRAP.md

---

# Guiding Statement

The Runtime Workflow transforms repository reality into deterministic engineering through continuous, uninterrupted execution.

---

End of Document