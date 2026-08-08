# CONSTITUTION

---

Document ID
CORE-003
Version
1.3
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

All repository components shall comply with this Constitution within the scope applicable to them.

---

# Constitutional Laws

## Law 1 — Reality Before Theory

Reality has priority over assumptions.

Analysis shall begin with verified evidence appropriate to the decision or change being made.

---

## Law 2 — Authoritative Source

Each logical object shall have one clearly identified authoritative source within its defined scope.

Non-authoritative copies, derived views, caches, exports, archives and examples may exist when their status is explicit and they do not compete with the authoritative source.

References should replace unnecessary authoritative duplication.

---

## Law 3 — Architecture Before Implementation

Architecture defines implementation within the applicable architectural scope.

Implementation shall not silently redefine architecture.

When implementation evidence exposes an architectural defect, the architecture itself may be reviewed through the applicable change process.

---

## Law 4 — Repository Before Memory

The current repository is the authoritative source for repository state.

Conversation memory shall never override current repository content.

---

## Law 5 — Evidence Before Conclusion

Every material conclusion shall be supported by verifiable evidence appropriate to its scope.

Unsupported conclusions shall be explicitly identified as assumptions or hypotheses.

---

## Law 6 — Inspection Before Assessment

A repository assessment shall not claim evidence that has not been inspected.

Historical knowledge may guide inspection but shall never substitute for direct verification when current evidence is required.

---

## Law 7 — Scope Declaration

Every material review shall explicitly declare, as applicable:

- Inspection Scope
- Repository Coverage
- Confidence Level
- Assessment Type

The level of evidence shall be proportional to the impact of the claim or change.

---

## Law 8 — Decision Traceability

Every material architectural decision shall be traceable.

The repository should preserve, as applicable:

- decision
- reason
- owner
- version
- evidence

---

## Law 9 — Controlled Evolution

Removal, replacement and archival shall preserve required traceability.

Nothing shall be treated as permanently untouchable merely because it is old or previously approved.

A governed archival or removal path shall be used when preservation, recovery or auditability is required.

---

## Law 10 — Ownership and Scope

Every authoritative artifact shall have a defined owner or owning authority within its applicable scope.

An artifact may legitimately serve multiple components or domains when its cross-cutting role is explicit and its authority boundaries are clear.

Ownership shall not be inferred solely from physical folder location.

---

## Law 11 — Operational Conservatism

Communicate verified facts only when presenting them as facts.

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

The complete approved document shall be the canonical target state when practical and safe. Partial updates are permitted when the current content, target state, scope and resulting integrity have been verified and the update does not bypass Governance or Architecture.

No write is permitted after a failed required validation gate.

---

## Law 13 — Proportional Folder Governance

A folder shall maintain a dedicated `_FOLDER_STATUS.md` when the repository architecture or governance designates folder-level status as necessary.

Folder status is a coordination and evidence summary; it does not create authority and does not certify uninspected content.

A folder shall not receive additional status machinery merely because another folder has it.

---

## Law 14 — Continuous Improvement

The platform shall continuously improve while preserving required architectural consistency and repository integrity.

---

# Constitutional Reviewability

Constitutional laws are the highest current governing rules, but they are not beyond review.

A constitutional rule may be proposed for revision when evidence shows that it is:

- incorrect or internally inconsistent;
- unnecessarily complex;
- too broad for its intended scope;
- counterproductive to repository integrity;
- incompatible with validated architecture; or
- replaceable by a simpler control with equal or better protection.

Revision requires explicit evidence, impact assessment, traceability and governed acceptance. Until accepted, the current Constitution remains authoritative.

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

This precedence applies within the defined scope of each authority and does not prevent a higher-level rule from being formally reviewed and revised.

---

# Constitutional Interpretation Rule

Where a lower-level runtime or implementation rule conflicts with this Constitution, the lower-level rule must be corrected or execution must enter `HOLD` until the conflict is resolved.

Where the Constitution itself appears defective, the conflict shall be recorded and escalated through Constitutional Review rather than silently bypassed.

---

End