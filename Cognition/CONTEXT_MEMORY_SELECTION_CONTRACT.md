# Context Memory Selection Contract

## Purpose

Define when historical Memory evidence may enter the current Cognition Context.

## Selection Rule

Historical evidence may be selected when it is directly scoped to:

- the current task; or
- the current project.

Everything else remains historical and is excluded from the active selection.

## Important Distinction

Selection does **not** promote historical evidence into a current fact.

```text
Historical Memory
      ↓
Scope Check
   ↙       ↘
MATCH      NO MATCH
  ↓            ↓
Selected     Excluded
  ↓
HISTORICAL_EVIDENCE
  ↓
Context Loader
```

## Safety Rules

1. Historical evidence must retain provenance.
2. Historical evidence must remain labeled as historical evidence.
3. Unrelated history must not enter Context merely because it exists in Memory.
4. Selection does not equal truth promotion.
5. Selection does not grant decision or execution authority.
6. A future semantic/relevance scorer may refine selection, but must preserve these boundaries.
