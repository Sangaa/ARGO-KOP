# PM-001 — PROJECT RECORD MODEL

Version: 1.0.0
Status: Build-01 / Integrity Hold

## Purpose

Define the minimum structure for preserving project context in a reusable and traceable form.

## Required Project Context

A project record should identify:

- Project ID
- Project name
- Objective
- Scope
- Current state
- Constraints
- Assumptions
- Evidence
- Decisions
- Dependencies
- Milestones
- Outcomes
- Lessons
- Open questions
- Related repository artifacts
- Provenance

## Separation Rules

Project Memory must distinguish:

- fact from assumption;
- project-local rule from platform rule;
- planned state from observed state;
- decision from outcome;
- historical context from current state.

## Relationships

A project record may reference:

```text
Project
 ├── Decisions
 ├── Evidence
 ├── Operational Events
 ├── Engineering Journal
 ├── Architecture
 ├── Knowledge
 └── Outcomes / Lessons
```

References are relationships, not authority transfers.

## Boundary

This model defines project-memory structure only. It does not define project management workflow or platform-wide governance.

---

End of PM-001
