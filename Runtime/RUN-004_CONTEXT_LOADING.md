# RUN-004

---

# CONTEXT LOADING

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

RUN-004

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

This document defines the Runtime Context Loading mechanism.

Context Loading ensures that every engineering decision is based on the latest synchronized repository rather than temporary conversation history.

Context Loading is mandatory before every engineering task.

---

# Objectives

Context Loading shall:

Load Repository Reality.

Load Repository Structure.

Load Engineering Context.

Load Folder Context.

Load Repository Memory.

Discard obsolete session context.

Guarantee deterministic execution.

---

# Context Priority

Repository Reality

↓

PROJECT_BOOTSTRAP.md

↓

Repository Tree

↓

Current Folder

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

Conversation is always the lowest priority.

---

# Context Loading Workflow

Repository Synchronization

↓

Repository Scan

↓

Repository Validation

↓

Repository Tree Loading

↓

Folder Selection

↓

Folder Context Loading

↓

Engineering Context

↓

Execution

---

# Repository Context

Runtime shall load:

Repository Version

Repository Structure

Repository Tree

Folder States

Completed Folders

Unfinished Folders

Repository Baseline

Current Engineering Target

---

# Folder Context

Before engineering a folder Runtime shall load:

README.md

Canonical Documents

_FOLDER_STATUS.md

Related Documents

Dependencies

Architecture References

Governance References

---

# Repository Reality Rule

Repository Reality always overrides:

Conversation

AI Memory

Previous Sessions

Temporary Notes

Engineering Assumptions

---

# Context Refresh

Runtime shall refresh context whenever:

A new repository is received.

Repository synchronization occurs.

Engineering switches to another folder.

Repository version changes.

Folder completion is detected.

---

# Context Validation

Before execution verify:

Repository synchronized.

Repository context loaded.

Folder context loaded.

Architecture references valid.

Governance references valid.

Repository version current.

---

# Failure Conditions

Stop Runtime when:

Repository context unavailable.

Repository corruption detected.

Repository ambiguity exists.

Required engineering context missing.

Otherwise continue automatically.

---

# Related Documents

RUN-001_BOOT_SEQUENCE.md

RUN-002_INITIALIZATION.md

RUN-003_CONFIGURATION.md

RUN-005_RUNTIME_WORKFLOW.md

PROJECT_BOOTSTRAP.md

AI-004_CONTEXT_LOADING.md

---

# Guiding Statement

Correct engineering begins with correct context.

Correct context always begins with the repository.

---

End of Document