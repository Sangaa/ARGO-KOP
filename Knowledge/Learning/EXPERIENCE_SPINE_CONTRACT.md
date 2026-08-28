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
- `domain`
- `problem_types`
- `allowed_scopes`

Optional precision fields:

- `project_id`
- `artifact_ids`
- `failure_classes`
- `max_records`

Missing required context returns `HOLD`; it must never widen retrieval.

## Experience Record Compatibility

The spine consumes existing promoted/reusable records. A record remains eligible only when it preserves:

- stable identity (`knowledge_id`, or the legacy `task_id` + `session_id` pair);
- lifecycle state: `PROMOTED`, `REUSABLE`, `VERIFIED`, or `CANONICAL`;
- `knowledge_scope` within the task's `allowed_scopes`;
- evidence/provenance reference;
- explicit authority state;
- at least one exact retrieval key matching the task.

Recommended retrieval keys are `domains`, `problem_types`, `artifact_ids`, and `failure_classes`. Legacy records without retrieval keys are not guessed into relevance; they remain available to existing retrieval paths and can be enriched through governed review.

## Selection Rules

1. Match only explicit keys; free-text similarity alone is insufficient.
2. Require scope compatibility.
3. Exclude `INVALIDATED`, `REJECTED`, `HOLD`, and `UNPROVEN` records.
4. Rank exact matches deterministically: artifact, failure class, problem type, domain.
5. Cap the packet at `max_records` (default `5`, maximum `10`).
6. Preserve evidence state and authority state separately.
7. Return exclusions by reason so absence and filtering remain auditable.
8. Never change a record's state or authority during retrieval.

## Packet Contract

The output contains:

- task identity and retrieval status;
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

## Non-Goals

- No new persistence layer.
- No automatic canonical promotion.
- No ingestion of all EJR or REP-020 history into every prompt.
- No semantic-vector or keyword-only retrieval claim.
- No replacement of `GOV-013`, `GOV-015`, `GOV-016`, Memory, Knowledge, or the existing Promotion Gate.

## Verification Boundary

The accompanying tests establish deterministic filtering, scope control, authority preservation, conflict reporting, and packet size bounds. They do not establish repository-wide integration, model-behavior compliance, or canonical authority.


