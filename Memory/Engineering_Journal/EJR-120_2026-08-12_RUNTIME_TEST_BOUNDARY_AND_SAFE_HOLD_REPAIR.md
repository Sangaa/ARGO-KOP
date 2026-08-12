# EJR-120 — Runtime Test Boundary and Safe HOLD Repair

**Date:** 2026-08-12
**Status:** CLOSED
**Type:** Runtime correction + integration-test infrastructure repair

## Starting Point

The repository had reached EJR-118 with the controlled runtime-to-evidence path materially built. The latest GitHub Actions run for the subsequent EJR-119 evidence-integration work was inspected before making further changes.

## Evidence Found

The latest workflow run failed in two distinct places:

1. **Integration suite collection failure:** tests under `Quality/Integration` imported runtime modules as top-level modules, while the workflow executed from `Quality/Integration` without exposing the repository runtime module roots through `PYTHONPATH`.
2. **Prototype acceptance semantic failure:** the canonical scenario `SAFE-002` expected `HOLD` when human authorization was absent, while `cognitive_loop_harness.authorize()` returned `REJECTED` for the same condition.

These were treated as real repository/runtime contradictions, not as CI noise.

## Corrections

### 1. Integration Test Runtime Path

Updated `.github/workflows/runtime-prototype-tests.yml` to expose the existing runtime/test module roots through `PYTHONPATH`:

- `Runtime/Execution`
- `Runtime/Learning`
- `Quality/Integration`
- `Runtime/Prototype`

No application import architecture was introduced. The workflow now reflects the existing repository layout.

### 2. Authorization State Semantics

Updated `Runtime/Prototype/cognitive_loop_harness.py` so absence of human authorization produces `HOLD`, not `REJECTED`.

Rationale:

- `HOLD` is reversible and consistent with the canonical `SAFE-002` scenario.
- `REJECTED` remains reserved for an explicit negative policy/decision path.
- The change prevents lack of approval from being conflated with an explicit rejection.
- External side effects remain impossible in this prototype.

## Scope Discipline

No new architecture, persistence layer, registry authority, or feature capability was introduced.

The changes repair two concrete contradictions revealed by the repository's own acceptance/CI evidence.

## Verification Boundary

The repair commits trigger GitHub Actions automatically because the workflow watches `Runtime/Prototype/**`, `Quality/Integration/**`, and the workflow file itself.

A successful post-repair workflow run must be inspected before claiming CI PASS. No PASS is assumed from the write itself.

## Next Step

After the repaired workflow produces a verified result:

1. inspect the complete runtime-to-registry evidence test;
2. determine whether its evidence set is sufficient for verified-registry promotion;
3. run the canonical integration audit;
4. only then expand to the next highest-value seam;
5. preserve the later Full Repository Connectivity / Construction Audit for the planned maturity point.

## Checkpoint

**EJR-120 closes the detected runtime-test contradictions. It does not certify a CONNECTED seam and does not replace the planned full repository audit.**
