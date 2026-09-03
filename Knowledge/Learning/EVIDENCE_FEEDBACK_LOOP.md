# Evidence Feedback Loop

## Purpose

Define how promoted knowledge is used, challenged and corrected without silent mutation.

## Loop

```text
Promoted Knowledge
      ↓
Retrieval
      ↓
Use in New Task
      ↓
New Evidence
      ↓
Consistency Check
      ↓
┌───────────────┐
│ No Conflict   │ → Keep / reinforce evidence
└───────────────┘

┌──────────────────────┐
│ Conflict Detected    │ → Demotion Review
└──────────────────────┘
                         ↓
                 Correct / Scope / Demote
```

## Governance Rule

New evidence must never silently overwrite a promoted record.

A contradiction may create `DEMOTION_REVIEW_REQUIRED` only after the correction boundary proves all of the following: the source record has a stable non-empty task identity, the source is currently `PROMOTED`, evidence is a non-empty list of non-empty text items, and the contradiction signal is an actual boolean.

Invalid evidence, identity, source state or contradiction signal must fail closed as `HOLD` with no record mutation and must not open a demotion review. `DEMOTION_REVIEW_REQUIRED` remains a review proposal only; the promoted record remains immutable until governed authority acts.

## Learning Consequence

This creates the foundation for knowledge to become revisable rather than permanently frozen.
