# EJR-130 — Governed Evidence Boundary Regression

Date: 2026-08-12
Status: Implemented / Awaiting CI Evidence

## Objective

Harden the governed repository evidence boundary before attempting permanent seam promotion.

## Change

Extended the runtime-to-registry integration regression to prove that the governed evidence capture boundary rejects:

- absolute evidence targets;
- parent-directory traversal targets.

The existing end-to-end proof continues to require an actual controlled runtime trace, verified runtime/outcome lineage, explicit governed capture, and registry promotion in the test sandbox.

## Important Boundary

The test sandbox is not canonical repository evidence. It proves the boundary behavior and promotion mechanics only. No permanent evidence artifact is being manufactured merely to obtain a CONNECTED status.

## Evidence

Changed artifact:
`Quality/Integration/test_runtime_trace_to_verified_registry.py`

Implementation under test:
`Quality/Integration/runtime_evidence_capture.py`

## Decision

Do not add another persistence layer. Do not promote a production repository seam until the governed target path is exercised with actual runtime-produced evidence and the resulting evidence set passes the loader, lineage verification, registry and canonical audit gates.

## Unresolved

- CI execution/result for this checkpoint is not yet observed.
- First permanent repository-backed CONNECTED seam remains unclaimed.

## Next Target

Run/inspect CI for this checkpoint, then inspect the actual repository-backed evidence path and promote only if all evidence gates pass.
