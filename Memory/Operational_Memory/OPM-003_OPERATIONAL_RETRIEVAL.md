# OPM-003 — OPERATIONAL RETRIEVAL

Document ID: OPM-003
Version: 1.0.0
Status: Build-01 / Integrity Hold
Category: Memory / Operational Memory
Canonical: Candidate — pending domain consolidation

---

## Purpose

Define how operational memories are selected for reuse during active work.

## Retrieval Principle

Operational Memory retrieval must prefer relevance plus evidence quality, not recency or textual similarity alone.

## Retrieval Inputs

- Current task / problem
- Context
- Required capability
- Known constraints
- Relevant project
- Relevant decision history
- Evidence requirements

## Retrieval Flow

```text
Current Need
   ↓
Candidate Memories
   ↓
Context Match
   ↓
Evidence / Validation Check
   ↓
Conflict Check
   ↓
Relevant Experience Set
   ↓
Reasoned Reuse
```

## Reuse Rules

1. A memory is a candidate input, not an unquestionable instruction.
2. Higher-confidence memories do not override current repository evidence automatically.
3. Conflicting memories must remain visible until resolved or explicitly bounded.
4. Reuse conditions must be checked before transferring an experience to a new context.
5. Failed experiences may be more relevant than successful ones when the current risk resembles the failure conditions.
6. Retrieval should preserve links back to the originating memory items and evidence.

## Future Representation

Vector or matrix representations may later accelerate similarity and relationship retrieval. They must remain derived representations; canonical source content and provenance remain authoritative.

---

End of Document
