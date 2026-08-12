# EJR-128 — Governed Repository Evidence Target Boundary

**Date:** 2026-08-12  
**Status:** Closed checkpoint  
**Role:** Evidence-boundary construction

## Context

EJR-126/EJR-127 established that the actual controlled runtime can produce a registry-ready evidence set and that runtime/outcome lineage must be explicitly verified before registry promotion. The remaining construction question was the smallest safe path for permanent repository-backed runtime evidence.

## Decision

Do not create a second persistence layer.

Add one thin repository-backed boundary to the existing `runtime_evidence_capture` adapter. Permanent runtime evidence may be captured only beneath:

`Quality/Integration/evidence/runtime/`

The caller supplies only a relative filename beneath that governed root. Absolute paths, traversal (`..`), and empty targets are rejected with `HOLD`.

## Reused Components

```text
connected_spine_runner
        ↓
actual execution trace
        ↓
runtime_evidence_capture
        ↓
existing runtime_result_persistence_adapter
        ↓
Quality/Integration/evidence/runtime/<explicit-name>.json
        ↓
loader / verifier / registry
```

The persistence adapter continues to require `record_type == EXECUTION_TRACE` and does not implicitly mutate canonical Memory.

## Tests Added

`Quality/Integration/test_repository_evidence_capture.py`

Coverage:

- traversal target is rejected;
- valid repository capture is constrained to the governed evidence root;
- exact runtime trace identity is preserved.

## Important Boundary

This checkpoint does **not** certify a permanent `CONNECTED` seam merely because the writer exists. A repository-backed artifact becomes certification evidence only after it is produced by the actual runtime path and passes:

1. canonical trace shape validation;
2. runtime/outcome lineage verification;
3. evidence loader checks;
4. verified registry requirements;
5. canonical spine audit.

The implementation deliberately does not auto-commit runtime output into the repository and does not mutate canonical Memory implicitly. A governed write target is now defined; the actual repository-backed evidence run remains the next proof step.

## Deferred / Not Done

- No new persistence architecture.
- No automatic canonical Memory mutation.
- No automatic Git commit of runtime artifacts.
- No `CONNECTED` claim from this checkpoint alone.
- Full Repository Connectivity / Construction Audit remains later, after the current seam set is mature.

## Resumption Point

Run the actual controlled runtime against the governed repository evidence boundary, verify the resulting artifact, then pass the same artifact through the loader, lineage verifier, registry and canonical audit. If successful, close the first repository-backed seam and expand to the next highest-value seam.
