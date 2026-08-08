# COG-009

---

# COGNITIVE SESSION

A cognitive session is not complete when reasoning stops. It is complete only after the session's validated experience has been handed back to the ARGO source and the responsible reviewing engineer.

---

# Session Lifecycle

Start

↓

Load Current Repository Context

↓

Reason / Analyze

↓

Generate Decisions and Findings

↓

Capture Experience, Errors, Lessons and Feedback

↓

Validate Learning Candidates

↓

Prepare Session Learning Handoff

↓

Transmit to ARGO Source / Parent Context + Responsible Review Engineer

↓

Store or Queue for Repository Ingestion

↓

Apply Authorized Repository Updates

↓

Post-Change Validation

↓

Close Session

---

# Session Closure Gate

A session shall not be considered fully closed until its learning handoff is completed or an explicit handoff failure is recorded.

The handoff shall identify, when applicable:

- session identity;
- model / instance identity;
- repository baseline used;
- verified findings;
- errors encountered;
- lessons learned;
- rejected or deferred hypotheses;
- proposed improvements;
- evidence supporting each material lesson;
- affected ARGO components;
- unresolved questions;
- changes already applied;
- changes requiring review;
- recommended repository destinations.

---

# Authority Boundary

The session may generate and transmit learning without granting itself authority to publish that learning as canonical truth.

The source parent and responsible review engineer receive the learning for review and repository integration according to applicable authority.

Session feedback is therefore:

**Learning Input → Review → Repository Knowledge**

not:

**Learning Input → Automatic Canonical Truth**

---

# Feedback Handoff Principle

Every participating model instance should return useful experience to the parent ARGO system before session termination whenever the session produced material learning.

A session that consumes ARGO knowledge but returns no record of material learning creates a one-way training channel and loses part of the value of the interaction.

---

# Failure Handling

If the source parent, responsible engineer, or repository destination is unavailable, the session shall preserve the handoff packet locally or in the designated session record and mark the handoff as **PENDING**, **FAILED**, or **BLOCKED**.

The session must not falsely report successful knowledge transfer.

---

# Guiding Statement

**Every session should leave ARGO wiser than it found it, without silently changing what ARGO is.**

---

End