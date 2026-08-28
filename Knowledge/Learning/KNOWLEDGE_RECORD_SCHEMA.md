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

## Experience Spine Retrieval Profile

Promoted records remain valid under the properties above. For deterministic Experience Spine retrieval, a record should additionally carry:

- `knowledge_id` — stable identity that must not silently collide;
- `source_identity` — model, engineer, system, task, or governed source that produced the record;
- `source_type` — for example `ARGO-EXPERIENCE`, `HORUS-ANALYSIS`, `HERMUZ-ENGINEERING`, or `EXTERNAL-EVIDENCE`;
- `authority_state` — separate from evidence/validation state;
- `consumer_routes` — one or more of `ARGO`, `HORUS`, `HERMUZ`, or `SHARED`;
- `domains`;
- `problem_types`;
- `artifact_ids` when applicable;
- `failure_classes` when applicable;
- `applicability_boundaries`;
- `counterindications`;
- `contradicts` — known conflicting knowledge identities.

This profile is backward-compatible storage guidance. It does not retroactively invent missing values for legacy records or change their promotion state. A legacy record may remain promoted while being ineligible for the stricter Experience Spine packet until governed enrichment supplies explicit lineage, route, and retrieval keys.

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

Retrieval must also preserve source identity and authority state. Repository location or repeated reuse must not erase who produced a record or promote its authority.

