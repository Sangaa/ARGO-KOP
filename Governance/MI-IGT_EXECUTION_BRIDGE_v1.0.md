# MI-IGT EXECUTION BRIDGE v1.0

Status: `GOVERNED / EXECUTION-READY / NOT-AUTHORITY`

## Purpose
Bridge the repository-first multi-instance learning candidate into independently executable validation without promoting the candidate by repetition.

## Rule
An IGT result is evidence only when the test context is materially independent from the source observation and the expected invariant is evaluated without leaking the source answer.

## Execution Surfaces
- Instance/window/platform identity
- Baseline repository ref before test
- Task scope and mutation boundary
- Invariant under test
- Novel state transformation
- Expected invariant behavior (not expected answer text)
- Observed behavior
- Leakage check
- Relationship revalidation
- CI/runtime evidence where applicable
- Failure/revision record

## Required Sequence
`CAPTURE BASELINE → ISOLATE CONTEXT → TRANSFORM STATE → TEST INVARIANT → CHECK LEAKAGE → REVALIDATE RELATIONSHIPS → RECORD OUTCOME → COMPARE WITH BASELINE`

## Independence Conditions
A run is not independent merely because it has a new session ID, a rewritten prompt, or a different report. Independence requires a materially distinct execution context and a novel state/configuration that was not supplied with the source conclusion.

## Promotion Boundary
Passing IGT demonstrates invariant transfer for the tested case only. It does not by itself prove persistence, broad generalization, meta-learning, weight change, or governance authority.

## Multi-Instance Safety
Each run must use an explicit scope and mutation boundary. Read-only IGT is preferred. Any mutation requires pre-check, current-state comparison, minimal change, re-read, relationship validation, and affected tests/CI.

## Required Record
Every completed run must produce an LPE-compatible record:
`SOURCE → OBSERVATION → INVARIANT → TRANSFORMED CASE → PREDICTION → OBSERVED OUTCOME → LEAKAGE RESULT → RELATIONSHIP RESULT → FAILURE/REVISION → PROMOTION STATUS`

`AUTHORITY = NONE`
