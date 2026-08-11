# PROTOTYPE INTEGRATION CONTRACT

Platform: ARGO KOP
Status: Candidate / Integrity Hold
Version: 1.0.0
Date: 2026-08-11

## Purpose

Define how the safe cognitive-loop prototype may be used to validate canonical ARGO contracts without becoming an accidental replacement for Runtime, Engine, Memory or Governance.

## Contract

The prototype is a probe at the boundary:

```text
Canonical Contracts
        ↓
Prototype Adapter
        ↓
Deterministic Harness
        ↓
Trace
        ↓
Acceptance Tests
```

It may consume representative inputs derived from canonical contracts, but it must not silently redefine them.

## Promotion Rules

Prototype behavior may be promoted only when:

1. the behavior is supported by a canonical contract;
2. the trace satisfies the acceptance matrix;
3. failure behavior is explicit;
4. provenance is preserved;
5. authorization remains explicit;
6. the change does not introduce unreviewed external side effects.

## Non-Promotion Rules

Do not promote prototype code merely because:

- a demo produces a plausible answer;
- a model recommends the architecture;
- a single test passes;
- the code is convenient to reuse.

## External Model Boundary

External models may supply reasoning candidates or audit observations. They do not define canonical interfaces or authorize promotion.

## Related Artifacts

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md`
- `Runtime/Prototype/cognitive_loop_harness.py`
- `Runtime/Prototype/trace_schema.json`

## Integrity Hold

This contract governs prototype use until an implementation review authorizes integration into canonical runtime services.
