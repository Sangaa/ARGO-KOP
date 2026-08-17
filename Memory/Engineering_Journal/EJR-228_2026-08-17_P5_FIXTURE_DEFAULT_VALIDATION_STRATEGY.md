# EJR-228 — P5 Fixture Default Validation Strategy

Date: 2026-08-17
Status: `CLOSED / LEARNING-PROMOTED / CI-VERIFIED`

## Decision

The reusable non-canonical fixture path is now the **default routine validation path** for P5 controlled-mutation testing.

The traditional repository-document path remains the **integration / compatibility / periodic regression path**.

This is a testing-strategy change only. It does not grant fixture execution authority to mutate canonical artifacts.

## Rationale

The fixture path is faster, isolated, deterministic and execution-verified for preservation, repeated updates, stale-state races, create races and dispatcher behavior.

The traditional path remains necessary because fixture-only success can miss differences between the fixture and real repository-document semantics.

Therefore:

`FIXTURE DEFAULT → REQUIRED GATES → TRADITIONAL/INTEGRATION WHEN APPLICABLE → GOVERNED CANONICAL WRITE ONLY`

## Repository Changes

- `Repository/P5_CONTROLLED_MUTATION_RECONCILIATION_HARNESS_MATRIX_2026-08-17.md` now defines the default-validation policy, fixture-fidelity rule and traditional integration boundary.
- `Quality/P5_CONTROLLED_MUTATION_RECONCILIATION_HARNESS_TEST_MATRIX_2026-08-17.md` now records `P5-T17` and `P5-T18` for default-path and fixture-fidelity behavior.
- `.github/workflows/p5-controlled-mutation-harness.yml` now executes the fixture validation path first, followed by the full compatibility/regression suite and canonical-artifact immutability guard.

## Verification Evidence

P5 workflow: `336293577`

Latest successful default-path run: `32042659900`

Head: `7c1d27092f399a40f8f00ec72e6b039588b305a5`

Job: `p5-harness` (`95424633249`)

Verified:

- Default fixture validation path: `SUCCESS`
- Compatibility/regression suite: `SUCCESS`
- Canonical-artifact immutability guard: `SUCCESS`

## Learning Boundary

This learning is repository-level and model-independent. Future models should inherit the strategy from the P5 matrix and workflow rather than conversation memory.

Fixture drift must be checked periodically against the traditional path. A fixture may never silently become the only evidence source for a canonical relationship or mutation.

## Current State

`P5 = EXECUTION-VERIFIED`

The fixture-default strategy is now `IMPLEMENTED / CI-VERIFIED`.

---

End of EJR-228
