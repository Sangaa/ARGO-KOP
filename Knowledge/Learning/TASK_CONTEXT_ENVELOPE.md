# Task Context Envelope

## Purpose

Bound knowledge retrieval to the context of the task instead of treating the entire knowledge repository as equally relevant.

## Context Fields

- `task_id`
- `session_id`
- `execution_identity`
- `project_id`
- `domain`
- `active_state`
- `claim`
- `allowed_scope`

For the Experience Spine candidate, callers should also provide:

- `problem_types` — explicit task/problem classes;
- `allowed_scopes` — one or more permitted knowledge scopes;
- `artifact_ids` — exact affected artifacts when known;
- `failure_classes` — applicable governed failure classes when known;
- `max_records` — bounded packet size (default 5, maximum 10).
- `consumer_route` — current `ARGO`, `HORUS`, `HERMUZ`, or `SHARED` consumer path.
- `repository_ref` / `repository_head` — exact repository context when repository work is involved.
- `concurrent_work_refs` — known parallel branches/PRs relevant to collision review.

The legacy singular `allowed_scope` remains supported by existing retrieval code. The Experience Spine uses plural `allowed_scopes` so widening must be explicit. `execution_identity` and `consumer_route` are required by the Experience Spine candidate so outputs from parallel model instances remain attributable and correctly routed.

## Retrieval Principle

```text
Task Context
    ↓
Context Filters
    ↓
Promoted Knowledge
    ↓
Relevant Knowledge
```

## Safety

Missing context must reduce retrieval confidence rather than silently widening the search scope.

A record outside `allowed_scope` is not eligible for reuse merely because its text looks similar.

## Experience Spine Entry

Before material reasoning, a model may build the bounded packet defined by `EXPERIENCE_SPINE_CONTRACT.md`.

```text
Task Context Envelope
    ↓
Explicit Retrieval Keys + Allowed Scopes
    ↓
Bounded Experience Packet
    ↓
Evidence / Authority Separation
    ↓
Reasoning
```

If required context is missing, retrieval returns `HOLD`. It must not compensate by loading broad history or treating free-text similarity as governed relevance.

