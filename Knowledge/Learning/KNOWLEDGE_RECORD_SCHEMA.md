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

Lifecycle state is not evidence state, validation state, or authority state. Retrieval must not reinterpret values from one axis as values on another axis.

## Optional Experience Projection Profile

A promoted record may carry an optional nested `experience_profile` used only to project the record into a bounded Experience Spine packet.

The profile does not change the record's promotion state or authority.

Recommended fields:

- `source_identity` — attributable originating model, engineer, task, system, or governed source;
- `source_type` — source class such as `HERMUZ-ENGINEERING`, `HORUS-ANALYSIS`, `ARGO-EXPERIENCE`, or `EXTERNAL-EVIDENCE`;
- `evidence_state` — evidence classification kept separate from lifecycle/validation;
- `authority_state` — explicit authority classification of the reusable experience;
- `consumer_routes` — allowed consumers such as `ARGO`, `HERMUZ`, `HORUS`, or `SHARED`;
- `evidence_group` — stable lineage grouping for records derived from the same material evidence;
- `domains` — explicit applicable domains;
- `problem_types` — explicit applicable problem classes;
- `artifact_ids` — exact affected artifacts when applicable;
- `failure_classes` — governed failure classes when applicable;
- `applicability_boundaries` — scope limits that reasoning must preserve;
- `counterindications` — conditions under which reuse should be avoided or re-reviewed;
- `contradicts` — known conflicting knowledge identities;
- `superseded_by` — newer knowledge identities that supersede this projection for current retrieval.

This profile is retrieval metadata, not a second knowledge record.

Legacy promoted records remain valid without it. They continue to participate in existing retrieval paths. They are not guessed into Experience Spine relevance until governed enrichment provides explicit structural keys, source/authority evidence and lineage grouping.

`ABSENT EXPERIENCE PROFILE != INVALID KNOWLEDGE`.

## Scope Rule

A promoted record must state what was actually established. It must not silently expand a tested example into a universal rule.

Experience projection inherits this scope. Retrieval may narrow applicability but must never widen `knowledge_scope`.

## Provenance Rule

Promotion must never sever the relationship between the knowledge record and its evidence.

Experience projection must also preserve source identity, evidence state, authority state and evidence lineage. Multiple records sharing one `evidence_group` must not be represented as independent confirmation merely because they are stored separately.
