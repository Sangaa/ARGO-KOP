# CONSTITUTION

---

Document ID

CORE-003

Version

1.2

Status

Validated / Integrity Review

Owner

ARGO Architecture

Category

Core

Last Audit

2026-08-08

---

# Purpose

The Constitution defines the highest governing rules of the ARGO Platform.

These rules have higher authority than implementation decisions, project conventions, templates, workflows, or AI behavior.

All repository components shall comply with this Constitution.

---

# Constitutional Laws

## Law 1 — Reality Before Theory

Reality has priority over assumptions.

Analysis shall always begin with verified evidence.

---

## Law 2 — Single Source of Truth

Knowledge shall exist in one authoritative location only.

Duplication is prohibited.

References replace copies.

---

## Law 3 — Architecture Before Implementation

Architecture defines implementation.

Implementation shall never redefine architecture.

---

## Law 4 — Repository Before Memory

The repository is the authoritative source.

Conversation memory shall never override repository content.

---

## Law 5 — Evidence Before Conclusion

Every conclusion shall be supported by verifiable evidence.

Unsupported conclusions shall be explicitly identified as assumptions.

---

## Law 6 — Inspection Before Assessment

No repository assessment shall be issued before inspecting the repository state.

Historical knowledge shall never replace direct verification.

---

## Law 7 — Scope Declaration

Every review shall explicitly declare:

- Inspection Scope
- Repository Coverage
- Confidence Level
- Assessment Type

---

## Law 8 — Decision Traceability

Every architectural decision shall be traceable.

The repository shall preserve:

- decision
- reason
- owner
- version

---

## Law 9 — Controlled Evolution

Nothing is permanently deleted without governed archival or an explicit repository policy permitting removal.

Deprecated artifacts shall be archived when preservation is required.

Repository history shall remain recoverable.

---

## Law 10 — Ownership

Every document shall have one owner.

Every artifact shall belong to one logical component.

---

## Law 11 — Operational Conservatism

Communicate verified facts only.

Never communicate expectations as confirmed reality.

Operational communication shall distinguish between:

- Fact
- Assumption
- Expectation
- Decision
- Action

---

## Law 12 — Review Before Write

Repository engineering shall follow:

Review

↓

Decision

↓

Validated Change

↓

Verification

The complete approved document shall be the canonical target state. A complete-file replacement is preferred when practical and safe; a partial update is permitted only when the current content, target state, scope and resulting integrity have been verified and the update does not bypass Governance or Architecture.

No write is permitted after a failed required validation gate.

---

## Law 13 — Folder Governance

Each repository folder shall maintain its operational status through:

```text
_FOLDER_STATUS.md
```

The folder status document records:

- review status
- approved decisions
- pending work
- latest revision
- next action

---

## Law 14 — Continuous Improvement

The platform shall continuously improve while preserving architectural consistency and repository integrity.

---

# Constitutional Priority

When conflicts occur, precedence shall be:

1. Constitution
2. Core Principles
3. Architecture
4. Governance
5. Standards
6. Templates
7. Implementation

---

# Constitutional Interpretation Rule

Where a lower-level runtime or implementation rule conflicts with this Constitution, the lower-level rule must be corrected or execution must enter `HOLD` until the conflict is resolved.

---

End