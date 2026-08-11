# OPM-002 — OPERATIONAL EVENT CAPTURE

Document ID: OPM-002
Version: 1.0.0
Status: Build-01 / Integrity Hold
Category: Memory / Operational Memory
Canonical: Candidate — pending domain consolidation

---

## Purpose

Define how operational events become traceable memory without prematurely becoming rules.

## Capture Sequence

```text
Event
 ↓
Context
 ↓
Evidence
 ↓
Observation
 ↓
Action / Response
 ↓
Outcome
 ↓
Classification
 ↓
Validation State
```

## Required Discipline

1. Capture what happened before explaining why it happened.
2. Preserve source evidence whenever available.
3. Separate observation from interpretation.
4. Record failed outcomes as first-class learning material.
5. Record successful outcomes with the conditions that made them successful.
6. Do not convert praise, repetition, or confidence into evidence.
7. Link the event to related decisions, projects, and engineering records where applicable.

## Learning Boundary

An event can produce a lesson or experience candidate. It becomes reusable experience only after the applicable re-examination and validation path.

## Guided Discovery Compatibility

This capture model supports learning events in which the system is allowed to make a safe mistake, examine the resulting contradiction, revise its reasoning, and re-test. The capture must preserve both the original inference and the revised inference.

## Integrity Rule

If an event cannot be adequately reconstructed, preserve it as incomplete rather than filling missing facts by inference.

---

End of Document
