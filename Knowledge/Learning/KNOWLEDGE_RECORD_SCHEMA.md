# Knowledge Record Schema

## Purpose

Define the minimum governed structure created when a promotion candidate is actually promoted.

## Required Properties

- `task_id` — originating learning task;
- `session_id` — originating session;
- `evidence` — traceable evidence references;
- `pattern` — the tested claim/pattern;
- `confidence` — confidence at promotion time;
- `validation` — validation state;
- `promoted_at` — promotion timestamp;
- `knowledge_scope` — explicit scope of what was established;
- `provenance_preserved` — confirmation that source/evidence lineage remains available.

## State Model

```text
CANDIDATE
   ↓
PROMOTION_ELIGIBLE
   ↓
PROMOTED
```

`PROMOTION_ELIGIBLE` is a decision state. `PROMOTED` is a persisted knowledge state.

## Scope Rule

A promoted record must state what was actually established. It must not silently expand a tested example into a universal rule.

## Provenance Rule

Promotion must never sever the relationship between the knowledge record and its evidence.
