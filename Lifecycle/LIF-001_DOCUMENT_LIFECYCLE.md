# LIF-001

---

# DOCUMENT LIFECYCLE STANDARD

Platform

ARGO KOP (Knowledge Operating Platform)

Document ID

LIF-001

Version

1.2.0

Status

Validated / Integrity Re-audit

Category

Lifecycle Standard

Canonical

Yes

Priority

Critical

Last Audit

2026-08-08

---

# Purpose

Defines the lifecycle of ARGO KOP document artifacts.

This lifecycle is **document-scoped**. It does not replace the platform lifecycle, knowledge lifecycle, repository lifecycle, project lifecycle, or decision lifecycle.

# Scope Boundary

`LIF-001` answers:

**What lifecycle state is this document artifact in?**

It does not by itself determine:

- whether the document is an authoritative governance instrument;
- whether a knowledge object is validated;
- whether a repository baseline is released;
- whether a project is complete;
- whether a platform change is accepted.

Those decisions remain governed by their applicable authorities.

# States

Draft

↓

Review

↓

Validated

↓

Approved

↓

Released

↓

Deprecated

↓

Archived

# State Definitions

## Draft

Initial document creation or controlled working revision.

No authoritative release claim may be inferred from Draft status.

## Review

The document is undergoing the applicable technical, architectural, repository and governance checks.

## Validated

The stated inspection scope has been checked against the applicable evidence and no blocking finding remains within that scope.

Validation does not create release or governance authority.

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

# Rules

1. Released documents cannot be deleted without an explicit governed archival policy that preserves traceability.
2. Archived documents cannot be modified as active artifacts.
3. A status label does not prove that the required approval or release evidence exists.
4. Lifecycle transitions require evidence appropriate to the transition.
5. A document lifecycle state must not be used as proof of the lifecycle state of the platform, repository, knowledge object, project or decision represented by that document.
6. If lifecycle evidence conflicts with repository or governance evidence, the conflict must be resolved before the state is treated as authoritative.
7. A lifecycle identifier must be unique among active canonical artifacts.
8. Similar lifecycle vocabulary across layers does not create shared identity or authority.

# Relationship to Other Lifecycles

`LIF-001` is the **document-state lifecycle**.

Other lifecycle authorities operate at different scopes:

- `Core/CORE-009_PLATFORM_LIFECYCLE.md` — platform evolution and operating lifecycle.
- `Repository/REP-006_REPOSITORY_LIFECYCLE.md` — repository artifact governance and repository evolution.
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md` — knowledge-object lifecycle.

These lifecycles may interact, but similar state names do not imply that they are the same lifecycle or that one automatically controls another.

# Validation Requirement

Before declaring a document `Approved` or `Released`, validate at minimum:

- current file identity;
- applicable authority;
- repository registration;
- required related-document references;
- version consistency;
- lifecycle evidence;
- applicable upstream/downstream impact.

# Migration Note

The former artifact `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` used the same active Document ID as the canonical Governance review standard `Governance/GOV-005_REVIEW_STANDARD.md`.

This was an identity collision caused by assigning a governance numeric identity to a document-lifecycle artifact. The lifecycle artifact is now `LIF-001`, while the canonical governance review standard retains `GOV-005`.

The historical path is retired after migration; Git history preserves provenance.

# Related Documents

- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Core/CORE-009_PLATFORM_LIFECYCLE.md`
- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`

# Guiding Statement

**A lifecycle is meaningful only within its defined scope. Shared vocabulary does not create shared authority.**

---

End of Document
