# EJR-125 — Canonical Trace Shape at Audit Boundary

**Date:** 2026-08-12
**Status:** CHECKPOINT CLOSED

## Trigger
Before promoting any seam to `CONNECTED`, the integration audit must prove that its trace evidence is not merely an existing file. It must be a materialized execution trace compatible with the canonical runtime trace producer.

## Change
`Quality/Integration/canonical_spine_integration_audit.py` now requires the trace reference to resolve to a repository-relative JSON file containing:

- `record_type = EXECUTION_TRACE`
- non-empty `trace_id`
- non-empty `task_id`
- non-empty `session_id`
- non-empty `final_status`

The regression suite was aligned with this boundary and now explicitly rejects a non-canonical trace shape.

## Why this is the simpler safe path
No new persistence, registry, or evidence architecture was introduced. The audit reuses the canonical trace shape already emitted by `Runtime/Execution/execution_trace_producer.py` and applies that minimum validation at the promotion boundary.

## Safety Decision
Candidate provenance remains navigation-only. A candidate file, an arbitrary markdown file, or a file merely containing words such as `verified`/`connected` cannot become `CONNECTED`.

## Current Evidence Chain
Runtime execution → canonical execution trace → outcome/lineage verification → evidence capture → verified registry → canonical audit.

## Not Done Yet
- No new seam was promoted solely because of this change.
- Full repository connectivity/construction audit remains deferred until the current seam proof set reaches the planned maturity point.
- Missing folders/files, orphan/duplicate structures, documentation/version reconciliation remain part of that later full audit.
- `START_HERE.md` synchronization must be performed from its latest SHA; a prior 409 conflict prevented unsafe overwrite.

## Closure
This checkpoint strengthens the proof boundary without expanding architecture. Next work should attempt the smallest real evidence set and only then evaluate registry promotion.
