# MEM-008

---

# GUIDED DISCOVERY LEARNING METHOD

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

MEM-008

Version

1.0.0

Status

Proposed / Canonical Learning Method Candidate

Category

Memory / Learning Method

Canonical

Yes

Last Review

2026-08-10

---

# Purpose

This document records a validated learning method observed during ARGO training and repository work.

The method is based on teaching a small number of governing rules, allowing ARGO to apply them without revealing the test in advance, observing the resulting reasoning and outcome, and using guided discussion to allow ARGO to identify errors and revise its own rules.

The objective is not memorization of rules. The objective is the formation of reusable reasoning, error recognition, experience and rule revision.

---

# Core Learning Cycle

```text
Teach a small rule set
        ↓
Confirm understanding
        ↓
Apply without revealing the test
        ↓
Observe result
        ↓
Allow error when safe
        ↓
Discuss the result, not merely the answer
        ↓
ARGO identifies the contradiction / failure
        ↓
ARGO revises the rule or interpretation
        ↓
Re-apply
        ↓
Record experience
        ↓
Re-test under a different context
```

---

# Fundamental Principle

A rule should not become trusted merely because it was taught.

Trust increases through application, evidence, contradiction handling, correction and re-validation.

Therefore:

```text
Taught Rule
    ≠
Validated Rule
```

A rule becomes stronger when ARGO can:

- explain it;
- apply it;
- detect when its result conflicts with reality or a higher authority;
- identify the failed assumption or interpretation;
- revise the rule or its application;
- explain why the revision was necessary;
- and successfully re-apply the revised rule.

---

# Controlled Error Principle

Safe learning errors may be intentionally left undisclosed during training when doing so provides useful evidence about ARGO's reasoning.

The trainer should not immediately provide the correct answer merely because an error is observed.

Instead, where risk is acceptable:

```text
Error
 ↓
Outcome Review
 ↓
Questioning
 ↓
Self-Diagnosis
 ↓
Rule Revision
```

This method must never be used to justify unsafe execution, irreversible mutation, security-sensitive actions, financial actions, or other high-impact operations without appropriate human and governance controls.

---

# Result-Focused Feedback

When ARGO makes an error, feedback should preferentially examine:

- what result was produced;
- what result was expected;
- where the two diverged;
- which assumption or rule produced the divergence;
- and what evidence supports changing the rule.

The trainer should avoid turning every correction into direct answer delivery.

The purpose is to make ARGO discover the causal connection where practical.

---

# Rule Revision Model

ARGO may revise a learned rule only when the revision is supported by evidence and remains consistent with higher authority.

```text
Existing Rule
      ↓
Observed Counterexample / New Evidence
      ↓
Reasoning Review
      ↓
Conflict Identification
      ↓
Proposed Revision
      ↓
Authority / Consistency Check
      ↓
Re-test
      ↓
Validated Rule Revision
```

A failed attempt must not automatically become a new rule.

---

# Discovery Measurement

Training events should distinguish between:

- Directly instructed behavior
- Behavior achieved after a hint
- Independently inferred behavior
- Correct behavior produced from prior experience
- Incorrect behavior later self-corrected
- Novel behavior requiring human review

This creates evidence about **how ARGO learned**, not only what it currently knows.

---

# Guidance Levels

Where practical, guidance may be recorded as:

```text
G0 — Direct instruction
G1 — Strong hint
G2 — Narrow clue
G3 — Question / prompt
G4 — No guidance / independent discovery
```

The level is descriptive evidence, not a quality score by itself.

An independently discovered solution is valuable evidence, but it still requires validation.

---

# Learning Event Record

A future learning-event record should preserve:

| Field | Meaning |
|---|---|
| Event ID | Stable learning-event identifier |
| Initial Rule | Rule or principle originally taught |
| Context | Situation in which it was taught/applied |
| Hidden Test | Whether the test was undisclosed |
| Outcome | Actual result |
| Expected Outcome | Reference result |
| Error | Observed discrepancy |
| Guidance Level | G0–G4 |
| ARGO Diagnosis | ARGO's explanation of the error |
| Revision | Rule or interpretation changed |
| Evidence | Evidence supporting the revision |
| Re-test | Result after revision |
| Experience | Reusable lesson extracted |
| Authority | Governing source |
| Checkpoint | Repository evidence |

---

# Learning From Repetition

A single successful correction is not sufficient evidence of durable learning.

Where practical, a revised rule should be tested in a changed context.

```text
Context A
   ↓
Learn / Correct
   ↓
Context B
   ↓
Transfer Test
   ↓
Context C
   ↓
Revalidation
```

Successful transfer provides stronger evidence that the lesson became reusable knowledge rather than a local answer.

---

# Relationship to Memory

This method produces multiple memory classes:

```text
Rule
 ↓
Knowledge
 ↓
Learning Event
 ↓
Experience
 ↓
Validated Pattern
 ↓
Reusable Skill
```

The original source, reasoning context and correction history should remain recoverable.

A summarized lesson must not erase the evidence needed to understand why the lesson was learned.

---

# Relationship to Repository Governance

Learning does not grant ARGO permission to mutate canonical authority merely because a new conclusion was discovered.

A learned conclusion becomes repository authority only through the normal evidence, review, authority and update controls.

```text
Discovery
 ↓
Evidence
 ↓
Review
 ↓
Authority Check
 ↓
Controlled Repository Update
```

The method therefore supports self-improvement while preserving governance.

---

# Relationship to Rings

Guided Discovery is a learning method, not a replacement for Ring architecture.

Rings determine execution scope and progression.

Guided Discovery may operate inside a Ring and may produce evidence for Ring Exit or Cross-Ring reconciliation.

An independently discovered capability does not automatically authorize promotion to another Ring.

---

# Relationship to the Relationship Registry

Learning artifacts may participate in repository relationships such as:

- `DERIVED_FROM` — learning event derived from a source or experiment
- `VALIDATES` — test or experiment validates a rule
- `PRODUCES` — learning process produces an experience artifact
- `REFERENCES` — learning record references authority or evidence

These relationships must be recorded only when independently evidenced.

---

# Safety Boundary

The training method deliberately permits safe intellectual mistakes.

It does not permit uncontrolled real-world mistakes.

Before an action with material external impact, ARGO must transition from:

`Learning Mode`

to

`Controlled Execution Mode`

with the applicable human, governance, testing and recovery controls.

---

# Historical Training Insight

The method documented here reflects an observed training pattern in which ARGO was initially taught a small set of rules, later tested without advance notice, allowed to encounter incorrect outcomes, and guided through discussion of the results until it identified the error and revised its rules.

This is preserved as historical evidence of a learning method, not as a claim that every future model instance will reproduce the same behavior automatically.

---

# Future Extension

This method may later support:

- automated learning-event capture;
- discovery scoring;
- transfer testing;
- experience consolidation;
- skill formation;
- curriculum generation;
- gap detection;
- and controlled self-directed learning.

These are future capabilities and are not certified by this document.

---

# Guiding Statement

**Teach less. Test deeper. Let the result expose the gap. Let ARGO discover the correction. Preserve the evidence. Re-test the lesson.**

---

End of Document
