# P301 — RUN-010 → ENG-006 EXECUTABLE CONSUMER CONTRACT BOUNDARY

Date: 2026-08-27
Status: CLOSED / CONTRACT-DEFINED / NO-RUNTIME-MUTATION
Protocol: GOV-013 + PROJECT_BOOTSTRAP
Baseline: main
Predecessor: P300

## Objective

Convert the unresolved `RUN-010 → ENG-006` evidence gap into an explicit, bounded construction contract without implementing runtime dispatch prematurely.

## Evidence Boundary

P300 established:

- `RUN-010 → ENG-006` is documented but not executable-verified.
- The current runtime path remains simulated and does not dispatch to ENG-006.
- `ENG-006 → SRV-009` is independently executable-verified in isolated E2E.
- Promoting REL-009 by inference is prohibited.

## Construction Contract

A future executable consumer may be admitted only if all of the following are demonstrated together:

1. **Caller identity:** the invocation originates from the governed RUN-010 execution boundary.
2. **Contract identity:** the call targets the declared ENG-006 execution contract, not a test-only surrogate.
3. **Validation preservation:** the pre-execution validation state is carried into the consumer boundary.
4. **Authorization preservation:** execution is rejected unless the governed authorization condition is satisfied.
5. **Trace continuity:** the RUN-010 execution identity remains correlated through ENG-006 and downstream SRV-009 execution.
6. **Side-effect gate:** the test can prove dry-run/non-mutating behavior separately from an explicitly authorized mutation path.
7. **Outcome evidence:** success, rejection, and failure outcomes are observable and attributable to the same execution identity.
8. **Regression scope:** existing Runtime, Engine, Service, Integrity, and Integration tests remain green after implementation.

## Required Test Matrix

| Case | Required evidence | Expected disposition |
|---|---|---|
| C1 | RUN-010 reaches ENG-006 with valid authorization | PASS / callable consumer |
| C2 | RUN-010 lacks authorization | REJECT / no downstream mutation |
| C3 | validation state invalid | REJECT / no downstream mutation |
| C4 | trace identity continuity | PASS / correlated trace |
| C5 | dry-run | PASS / no mutation |
| C6 | authorized isolated mutation | PASS / ENG-006 → SRV-009 evidence |
| C7 | downstream failure | FAIL-CLOSED / attributable outcome |

## Mutation Boundary

This checkpoint deliberately does **not** modify `Runtime/Execution`, `ENG-006`, `SRV-009`, or the relationship registry. It defines the minimum admissibility contract for the next implementation step.

## Decision

`GAP = CONFIRMED`
`CONTRACT = DEFINED`
`RUNTIME MUTATION = DEFERRED`
`REGISTRY PROMOTION = DEFERRED`

The next safe step is targeted implementation on an isolated branch, followed by the C1–C7 executable test matrix and full regression before any canonical promotion.

## Closure

- Evidence from P300 retained.
- Construction scope bounded.
- No runtime authority changed.
- No relationship promotion performed.
- This session is closed before reporting.

`P301 = CLOSED`
`REL-009 = REVALIDATION REQUIRED`
`RUN-010 → ENG-006 = CONTRACT-DEFINED / NOT YET EXECUTABLE-VERIFIED`
`GLOBAL INTEGRITY = HOLD`
