# ARGO KOP — PROJECT MEMORY

Domain: Memory
Subdomain: Project_Memory
Status: Build-01 / Integrity Hold

## Purpose

Project Memory preserves project-specific context needed to continue work across sessions without confusing temporary project state with platform-wide truth.

## Scope

Project Memory may preserve:

- project objectives and scope;
- project decisions and constraints;
- milestones and current state;
- project-specific evidence;
- implementation outcomes;
- project lessons and reusable experience;
- unresolved project questions;
- links to repository artifacts, decisions, operational events and engineering journal entries.

## Authority Boundary

Project Memory is subordinate to Constitution, Governance, Architecture and Repository authority. A project-specific rule does not automatically become a platform-wide rule.

Project Memory also does not replace Decision Memory. Decisions remain recorded through the applicable decision-memory path and may be referenced here.

## Core Flow

```text
Project Context
      ↓
Captured
      ↓
Classified
      ↓
Linked to Evidence / Decisions
      ↓
Executed / Observed
      ↓
Validated
      ↓
Reusable Project Experience
```

## Project State

Project state should distinguish at minimum:

- planned;
- active;
- blocked;
- completed;
- validated;
- superseded;
- archived.

State is contextual and must not be inferred solely from the existence of files.

## Continuity Rule

A new session should be able to recover the relevant project context from Project Memory without relying on conversational memory alone.

## Integrity Rule

Project Memory must preserve provenance, scope and temporal context. Historical or project-local information must not silently become current platform-wide truth.

## Build-01 Boundary

This README establishes the Project Memory domain contract. Detailed project-record models, lifecycle rules, retrieval rules and traceability artifacts are part of the next construction increments.

---

End of Document
