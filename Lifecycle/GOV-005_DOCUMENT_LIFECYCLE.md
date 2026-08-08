# DOCUMENT LIFECYCLE STANDARD

---

Document ID

GOV-005

Version

1.1.0

Status

Validated / Integrity Hold

Category

Governance / Lifecycle

Canonical

Yes

Last Audit

2026-08-08

---

# Purpose

Defines the lifecycle of ARGO KOP document artifacts.

This lifecycle is **document-scoped**. It does not replace the platform lifecycle, knowledge lifecycle, repository lifecycle, project lifecycle, or decision lifecycle.

---

# Scope Boundary

`GOV-005` answers:

**What lifecycle state is this document artifact in?**

It does not by itself determine:

- whether the document is an authoritative governance instrument;
- whether a knowledge object is validated;
- whether a repository baseline is released;
- whether a project is complete;
- whether a platform change is accepted.

Those decisions remain governed by their applicable authorities.

---

# States

Draft

↓

Review

↓

Approved

↓

Released

↓

Deprecated

↓

Archived

---

# State Definitions

## Draft

Initial document creation or controlled working revision.

No authoritative release claim may be inferred from Draft status.

## Review

The document is undergoing the applicable technical, architectural, repository and governance checks.

## Approved

The applicable authority has accepted the document within its defined scope.

Approval does not automatically mean the document is included in an official platform release.

## Released

The document is part of an approved repository/platform release according to the applicable release authority.

## Deprecated

The document is no longer recommended as the preferred active artifact but may remain necessary for traceability.

Deprecation does not mean deletion.

## Archived

The document is retained as historical reference and is not an active authority unless a governed process explicitly says otherwise.

---

# Rules

1. Released documents cannot be deleted without an explicit governed archival policy that preserves traceability.
2. Archived documents cannot be modified as active artifacts.
3. A status label does not prove that the required approval or release evidence exists.
4. Lifecycle transitions require evidence appropriate to the transition.
5. A document lifecycle state must not be used as proof of the lifecycle state of the platform, repository, knowledge object, project or decision represented by that document.
6. If lifecycle evidence conflicts with repository or governance evidence, the conflict must be resolved before the state is treated as authoritative.

---

# Relationship to Other Lifecycles

`GOV-005` is the **document-state lifecycle**.

Other lifecycle authorities operate at different scopes:

- `CORE-009_PLATFORM_LIFECYCLE` — platform evolution and operating lifecycle.
- `REP-006_REPOSITORY_LIFECYCLE` — repository artifact governance and repository evolution.
- `KNW-004_KNOWLEDGE_LIFECYCLE` — knowledge-object lifecycle.

These lifecycles may interact, but similar state names do not imply that they are the same lifecycle or that one automatically controls another.

---

# Validation Requirement

Before declaring a document `Approved` or `Released`, validate at minimum:

- current file identity;
- applicable authority;
- repository registration;
- required related-document references;
- version consistency;
- lifecycle evidence;
- applicable upstream/downstream impact.

---

# Related Documents

- `Core/CORE-009_PLATFORM_LIFECYCLE.md`
- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `PROJECT_BOOTSTRAP.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`

---

# Guiding Statement

**A lifecycle is meaningful only within its defined scope. Shared vocabulary does not create shared authority.**

---

End of Document
