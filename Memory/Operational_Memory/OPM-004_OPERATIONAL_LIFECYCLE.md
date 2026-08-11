# OPM-004 — OPERATIONAL MEMORY LIFECYCLE

Document ID: OPM-004
Version: 1.0.0
Status: Build-01 / Integrity Hold
Category: Memory / Operational Memory
Canonical: Candidate — pending domain consolidation

---

## Purpose

Define the lifecycle of an operational memory item from capture through reuse, revision, supersession, or archival.

## Lifecycle

```text
Captured
  ↓
Classified
  ↓
Under Review
  ├── Rejected
  ├── Deferred
  └── Validated
          ↓
      Reusable
          ↓
   Revalidated on Reuse
          ↓
   Revised / Superseded / Archived
```

## State Rules

### Captured
The event exists but has not yet been sufficiently evaluated.

### Under Review
Evidence, context, and interpretation are being examined.

### Validated
The memory has sufficient evidence for its declared scope.

### Reusable
The memory may be considered during retrieval, subject to current-context validation.

### Revised
New evidence changes the interpretation or reusable conditions.

### Superseded
A newer validated memory replaces the older memory for a defined scope while the historical record remains recoverable.

### Archived
The memory is retained for provenance but should not normally drive active retrieval.

## Revalidation Rule

Operational memory is never exempt from current evidence. Material context changes require revalidation before reuse.

## Learning Rule

The lifecycle must preserve changes in reasoning, especially cases where an initial rule or inference failed and was revised after examining the outcome.

## Authority Boundary

Lifecycle state controls memory usability. It does not create governance authority over other repository domains.

---

End of Document
