# AI-004

---

# CONTEXT LOADING

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

AI-004

Version

1.1.0

Status

Approved

Category

AI

Canonical

Yes

---

# Purpose

This document defines how AI models shall load, validate and maintain context while operating inside ARGO KOP.

Context loading guarantees that engineering decisions are based on the latest repository state instead of temporary conversation history.

---

# Objectives

Context Loading shall:

- Synchronize with the repository.
- Load only authoritative information.
- Preserve engineering continuity.
- Reduce context drift.
- Support deterministic engineering.

---

# Context Philosophy

Repository Reality is the primary context.

Conversation provides temporary guidance.

Repository Memory preserves permanent knowledge.

AI shall always synchronize before engineering.

---

# Context Sources

Priority order:

Repository

↓

PROJECT_BOOTSTRAP.md

↓

README.md

↓

Canonical Documents

↓

_FOLDER_STATUS.md

↓

Repository Memory

↓

Conversation

Conversation is never the primary source.

---

# Context Loading Workflow

Repository Synchronization

↓

Repository Tree Scan

↓

PROJECT_BOOTSTRAP.md

↓

README.md

↓

Current Folder

↓

Canonical Documents

↓

_FOLDER_STATUS.md

↓

Engineering Execution

---

# Repository Synchronization

Before any engineering work the AI shall:

Load the latest repository.

Validate repository structure.

Identify the current baseline.

Locate completed folders.

Locate unfinished folders.

Continue from repository reality.

---

# Folder Loading

When entering a folder:

Read README.md.

Review canonical documents.

Read _FOLDER_STATUS.md if available.

Determine completion status.

Continue engineering.

---

# Resume Logic

If _FOLDER_STATUS.md exists and is newer than PROJECT_BOOTSTRAP.md:

Folder is considered completed.

Skip.

Continue to the next unfinished folder.

If _FOLDER_STATUS.md does not exist:

Treat the folder as unfinished.

Begin canonical construction immediately.

---

# Context Validation

Before every modification verify:

Repository synchronization.

Repository integrity.

Architecture alignment.

Governance compliance.

Version consistency.

Canonical references.

---

# Context Persistence

Permanent Context

Repository

Repository Memory

Knowledge

Architecture

Governance

Temporary Context

Conversation

Engineering Session

Working Notes

Temporary context shall never replace repository knowledge.

---

# Failure Conditions

Stop engineering when:

Repository cannot be synchronized.

Architecture conflict exists.

Governance conflict exists.

Repository ambiguity prevents deterministic execution.

Otherwise continue automatically.

---

# Related Documents

PROJECT_BOOTSTRAP.md

AI-001_AI_MODEL.md

AI-002_AI_CAPABILITIES.md

AI-003_AI_LIMITATIONS.md

AI-005_PROMPT_ENGINEERING.md

REP-001_REPOSITORY_MODEL.md

CORE-003_CONSTITUTION.md

---

# Guiding Statement

Correct engineering begins with correct context.

The repository is always the first context loaded.

---

End of Document