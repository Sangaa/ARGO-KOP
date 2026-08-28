# Task Context Envelope

## Purpose

Bound knowledge retrieval to the context of the task instead of treating the entire knowledge repository as equally relevant.

## Existing Context Fields

- `task_id`
- `session_id`
- `project_id`
- `domain`
- `active_state`
- `claim`
- `allowed_scope`

These fields remain valid for existing contextual retrieval.

## Experience Spine Context

The Experience Spine is a stricter optional retrieval projection. It requires enough context to avoid broad history loading or relevance guessing.

Required fields:

- `task_id` — current task identity;
- `execution_identity` — current model/session/execution identity;
- `domain` — explicit task domain;
- `problem_types` — one or more explicit problem classes;
- `allowed_scopes` — one or more knowledge scopes that may be reused;
- `consumer_route` — current `ARGO`, `HERMUZ`, `HORUS`, or other governed consumer route.

Optional precision/attribution fields:

- `project_id`;
- `artifact_ids` — exact affected artifacts when known;
- `failure_classes` — applicable failure classes when known;
- `max_records` — bounded packet size, default 5 and maximum 10;
- `repository_ref`;
- `repository_head`;
- `concurrent_work_refs` — known parallel PRs/branches/workstreams relevant to collision review.

The existing singular `allowed_scope` remains unchanged for legacy retrieval. The Experience Spine uses plural `allowed_scopes` because every additional allowed scope must be explicit.

`execution_identity`, `repository_head`, and `concurrent_work_refs` preserve attribution in a multi-writer environment. They do not prove that the repository or another branch remained unchanged after the snapshot.

## Retrieval Principle

Existing retrieval:

```text
Task Context
    ↓
Context Filters
    ↓
Promoted Knowledge
    ↓
Relevant Knowledge
```

Experience Spine projection:

```text
Current Task / Execution Identity
    ↓
Allowed Scope + Explicit Structural Keys
    ↓
Promoted + Validated Knowledge
    ↓
Optional Experience Projection Profile
    ↓
Conflict / Supersession / Correlation Check
    ↓
Bounded Advisory Experience Packet
    ↓
Current Evidence → Applicable Authority → Reasoning
```

## Safety

Missing context must reduce retrieval confidence rather than silently widening the search scope.

A record outside the allowed scope is not eligible for reuse merely because its text looks similar.

For Experience Spine retrieval, incomplete required context returns `HOLD`; the retrieval mechanism must not compensate by loading broader history or inferring missing scopes/routes.

The Experience Spine uses explicit structural keys rather than free-text similarity as governed relevance. Legacy records without explicit projection metadata remain available through existing retrieval paths but are not guessed into the stricter packet.

## Multi-Writer Boundary

Repository context is a snapshot, not a lock.

Before any repository mutation or merge, re-read live repository state independently of the packet:

`MAIN HEAD → ACTIVE WORKSTREAM HEADS → CHANGED PATHS → SEMANTIC OVERLAP → CURRENT CI → ACTION`.

Retrieved experience may remind a model to perform this check; it cannot substitute for the check itself.
