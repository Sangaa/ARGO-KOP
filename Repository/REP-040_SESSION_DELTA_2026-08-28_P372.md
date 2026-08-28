# P372 — PR #63 Divergence and Promotion Boundary

Date: 2026-08-28
Status: `CLOSED / VERIFIED / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P371. The required action was to compare PR #63 head against current `main` before deciding whether any prior isolated implementation could be reused.

## EXACT COMPARISON
Base: current `main` at `3a0bc21363b39cd3c8d4499b4e227a1fea8ddaa1`
Head: PR #63 at `a18bf9bae5fbdc29cde0fd237830f0c63b71556c`
Merge base: `2ce52292f4d8d8cfebd5c7b24fe84bc89036a934`

GitHub reports:
- `main` and PR head are `diverged`.
- PR head is `48` commits ahead of the current main comparison base.
- PR head is `64` commits behind the current main comparison base.
- The comparison contains 32 changed files, including runtime, services, tests, matrices, governance, and OpenHands qualification material.

## RECONCILIATION RESULT
The PR is not a small forward patch that can be safely replayed as-is. It is a historical isolated workstream with substantial divergence from current `main`.

The changed surface includes `Runtime/Execution/connected_spine_runner.py`, `Runtime/Execution/run010_eng006_consumer.py`, `Services/ENG006_REAL_PROVIDER_FACTORY.py`, multiple P4/REL-009 matrices, multiple session records, and `GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md`.

Therefore:

`PR #63 contents = historical evidence + candidate implementation material`

not:

`PR #63 contents = current-main-ready implementation`.

## CI / EXECUTION BOUNDARY
The combined commit-status query for PR head returned no statuses. This does not prove that no workflow ever ran; it proves only that no combined status records are currently exposed for that commit through this check.

Accordingly, PR-head execution status is classified as `UNPROVEN` in this reconciliation and must not be upgraded from the existence of files or prior reports.

## DECISION
Do not merge PR #63.
Do not cherry-pick or manually copy its broad surface into `main`.
Do not create a duplicate PR.
Do not declare REL-009 promoted.

If the current mainline still requires RUN-010 → ENG-006 evidence, create a fresh minimal implementation from the current main head, reusing only concepts that survive contract reconciliation. Preserve the old PR as historical provenance rather than treating it as the current implementation branch.

## KNOWLEDGE DELTA
**KD-048 — Divergence magnitude is itself a safety signal: the larger the temporal and structural divergence, the stronger the requirement for fresh reconciliation before reuse.**

**KD-049 — Historical implementation may be reusable as design evidence without being reusable as code.**

**KD-050 — Absence of exposed status records is `UNPROVEN`, not `FAIL` and not `PASS`.**

## EVIDENCE STATE
- Exact PR/main divergence: `PROVEN`
- Historical isolated implementation exists: `PROVEN`
- Current-main compatibility: `UNPROVEN`
- PR-head combined status currently exposed: `UNPROVEN`
- Production connectivity: `UNPROVEN`
- Merge safety: `NOT JUSTIFIED`
- Promotion: `NOT JUSTIFIED`

## CHECKPOINT
`P372 → identify the exact current-main REL-009 claim → reconcile only the minimum required concepts from PR #63 → implement on a fresh current-main branch if justified → run affected CI → bind exact-head evidence → reconcile → promotion gate.`

## CLOSE
`CLOSED / VERIFIED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
