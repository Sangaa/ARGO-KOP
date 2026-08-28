# P383 — Reconcile REL-009 Negative Gate With Governed B07 Seam

Date: 2026-08-28
Status: `CLOSED / VERIFIED / ISOLATED / CI PENDING / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
P382 produced the first real observable Actions run for the isolated branch. The run was bound to the exact pre-fix head `83c26b6...` and exposed a deterministic integrity failure rather than an execution-channel absence.

## OBSERVED FAILURE
The integrity job executed `110` passing tests and `1` failing test. The failure was:
`test_no_srv009_literal_in_runtime_execution_python_scope`

The failure occurred because the newly introduced governed B07 consumer is intentionally located in `Runtime/Execution/run010_eng006_srv009_consumer.py` and necessarily names the target service `SRV-009`.

Therefore the old negative gate was stricter than the current B07 architecture: it prohibited the very governed consumer seam that P374 defined as the minimum callable boundary.

## RECONCILIATION DECISION
The correct repair is not to hide or obfuscate `SRV-009`, and not to move the consumer merely to satisfy a lexical test.

The gate was narrowed to prohibit **ad-hoc** SRV-009 literals outside the one governed B07 consumer, while adding a positive structural assertion that the permitted consumer uses `RepositoryConnector` and remains provider-neutral.

This preserves the original safety intent while reconciling it with the now-explicit architecture.

## MUTATION
Updated:
`Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py`

New rules:
- the governed B07 consumer is the single permitted runtime SRV-009 seam;
- other Runtime/Execution Python files remain prohibited from ad-hoc SRV-009 references;
- the B07 consumer must reference `RepositoryConnector` through `Services.REPOSITORY_CONNECTOR_INTERFACE`.

Commit:
`5893f77b79348abddbd9a9ff4c96eceffff03977`

## CURRENT CI OBSERVATION
The PR #64 head advanced to `5893f77...`. At the time of this close, the available commit-run observation channel returned no run for that new head yet.

Therefore the repair is **source-verified but execution-pending**.

No PASS is claimed for the repaired gate.

## EVIDENCE STATE
- Original failure: `PROVEN BY CI / EXACT HEAD 83c26b6...`
- Root architectural conflict: `PROVEN BY INSPECTION`
- Repair source: `PROVEN`
- Repair behavioral result: `PENDING`
- B07 integration execution after repair: `UNPROVEN`
- B08 real-provider dispatch: `UNPROVEN`
- Canonical mutation: `NONE`
- Promotion: `NOT JUSTIFIED`

## KNOWLEDGE DELTA
**KD-068 — A negative integrity rule must encode the architectural boundary it protects, not a historical lexical approximation that becomes incompatible with an intentionally governed seam.**

**KD-069 — When CI converts an earlier `UNPROVEN` execution question into a concrete failure, the failure becomes actionable evidence; repair should address the violated contract rather than suppress the observation.**

## CHECKPOINT
`P383 → observe CI for exact repaired HEAD 5893f77... → inspect integrity + integration jobs → if green, inspect B07 matrix behavior → bind evidence to exact HEAD → then address current-SHA/read-before-write gap → B07 closure → controlled B08 observation.`

## CLOSE
`CLOSED / VERIFIED / ISOLATED / CI PENDING / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
