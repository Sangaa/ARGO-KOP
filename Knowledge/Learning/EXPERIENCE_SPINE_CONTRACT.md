# Experience Spine Contract

Status: `CANDIDATE / TESTABLE / NON-CANONICAL`
Checkpoint: `P375`

## Purpose

Provide every task with a small, traceable packet of relevant prior experience before reasoning begins. The spine organizes existing governed knowledge; it does not create another memory store, promote learning, or replace repository authority.

## Position in the Reasoning Flow

```text
Task Definition
      ↓
Task Context Envelope
      ↓
Experience Spine Retrieval
      ↓
Bounded Experience Packet
      ↓
Evidence / Authority Separation
      ↓
Reasoning → Decision → Execution → Outcome
      ↓
Learning Assessment → Existing Promotion Gate
```

The packet is advisory input. Current task evidence and applicable authority remain stronger than retrieved experience.

## Required Task Context

- `task_id`
- `execution_identity`
- `domain`
- `problem_types`
- `allowed_scopes`
- `consumer_route`

Optional precision fields:

- `project_id`
- `artifact_ids`
- `failure_classes`
- `max_records`
- `repository_ref`
- `repository_head`
- `concurrent_work_refs`

Missing required context returns `HOLD`; it must never widen retrieval.

## Experience Record Compatibility

The spine consumes existing promoted/reusable records. A record remains eligible only when it preserves:

- stable identity (`knowledge_id`, or the legacy `task_id` + `session_id` pair);
- lifecycle state: `PROMOTED`, `REUSABLE`, `VERIFIED`, or `CANONICAL`;
- `knowledge_scope` within the task's `allowed_scopes`;
- evidence/provenance reference;
- explicit source identity and source type;
- explicit authority state;
- an eligible consumer route;
- at least one exact retrieval key matching the task.

Recommended retrieval keys are `domains`, `problem_types`, `artifact_ids`, and `failure_classes`. Legacy records without retrieval keys are not guessed into relevance; they remain available to existing retrieval paths and can be enriched through governed review.

Recommended lineage/routing fields are `source_identity`, `source_type`, `consumer_routes`, `applicability_boundaries`, `counterindications`, and `contradicts`. Records missing source identity or routing remain excluded from this candidate packet until governed enrichment; repository presence does not erase their origin.

## Selection Rules

1. Match only explicit keys; free-text similarity alone is insufficient.
2. Require scope compatibility.
3. Exclude `INVALIDATED`, `REJECTED`, `HOLD`, and `UNPROVEN` records.
4. Enforce consumer routing: `SHARED` may serve any route; otherwise the current route must be explicit.
5. Rank exact matches deterministically: artifact, failure class, problem type, domain.
6. If two selected records claim the same knowledge identity, return `HOLD`; never choose one silently.
7. Cap the packet at `max_records` (default `5`, maximum `10`).
8. Preserve source, evidence state, authority state, boundaries, and counterindications.
9. Return exclusions by reason so absence and filtering remain auditable.
10. Never change a record's state or authority during retrieval.

## Packet Contract

The output contains:

- task identity and retrieval status;
- execution identity and repository/concurrent-work snapshot;
- ordered `experience_items` with match reasons;
- `conflicts` when selected records contradict one another;
- `excluded_summary` by reason;
- `reasoning_start` instructions;
- an explicit `authority_boundary`.

The reasoning start is:

```text
CURRENT EVIDENCE → APPLICABLE AUTHORITY → RELEVANT EXPERIENCE
→ CONFLICT CHECK → ASSUMPTIONS → OPTIONS → TESTABLE DECISION
```

Experience may suggest a path, but it cannot turn a candidate into proof or authorize mutation.

When several repository instances are active, `repository_ref`, `repository_head`, and `concurrent_work_refs` make the packet attributable to the exact work context. They do not prove that another branch is inactive or conflict-free; branch/PR reconciliation remains a repository operation before mutation.

## Non-Goals

- No new persistence layer.
- No automatic canonical promotion.
- No ingestion of all EJR or REP-020 history into every prompt.
- No semantic-vector or keyword-only retrieval claim.
- No replacement of `GOV-013`, `GOV-015`, `GOV-016`, Memory, Knowledge, or the existing Promotion Gate.

## Verification Boundary

The accompanying tests establish deterministic filtering, scope control, authority preservation, conflict reporting, and packet size bounds. They do not establish repository-wide integration, model-behavior compliance, or canonical authority.

