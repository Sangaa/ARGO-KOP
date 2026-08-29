# IGT Trust-State Transition Contract — 2026-08-29

Status: `IMPLEMENTED BOUNDED CONTRACT / CI REQUIRED`
Authority: `NONE`

## Purpose

Prevent trust-state promotion by caller label, conversational assumption, ordinal naming, or unimplemented semantic shortcut.

Trust transition is an executable edge, not a string rewrite.

## Current Enabled Graph

Only one upward edge is currently enabled:

`UNTRUSTED_QUARANTINED → RESOLVED_UNAUTHENTICATED`

That edge is earned only by invoking `execute_quarantine_resolution(...)` and receiving its exact success state.

## Known But Disabled States

The guard recognizes later vocabulary only so it can reject premature jumps explicitly:

- `PROVIDER_AUTHENTICATED`
- `SOURCE_AUTHENTICATED`
- `EXTERNAL_AUTHENTICITY_VERIFIED`
- `EXECUTION_VERIFIED`
- `DELIVERY_VERIFIED`
- `QUALIFIED`
- `AUTHORIZED`
- `ADMITTED_BOUNDED`
- `PROMOTED`

Recognition is not implementation.

## Laws

1. `CALLER CLAIM != TRANSITION EVIDENCE`.
2. A legal upward edge must name a concrete governed earning stage.
3. The guard invokes the earning stage itself; it does not accept a caller-supplied successful stage result as proof.
4. Stage failure preserves the prior trust state.
5. Same-state requests are `NO_OP` and invoke nothing.
6. Unknown current or target state fails closed.
7. Known but unimplemented edges return `TRANSITION_NOT_ENABLED` and invoke nothing.
8. No state ordering, lexical ordering, or naming similarity grants an edge.
9. `RESOLVED_UNAUTHENTICATED` remains provider-authenticity `UNVERIFIED` and authority `NONE`.
10. Provider authentication remains blocked by the separately documented trust-anchor HOLD.

## Current Executable Boundary

Implementation:
`Quality/Integration/experience_spine_igt_trust_state_transition_gate.py`

Regression suite:
`Quality/Integration/test_experience_spine_igt_trust_state_transition_gate.py`

The regression suite proves at minimum:

- exact legal transition invokes the governed resolution stage;
- caller `verified/authenticated/authorized` flags have no effect;
- direct authentication, execution, authority, admission and promotion jumps are rejected;
- disabled transitions invoke no resolver;
- same-state no-op invokes no stage;
- unknown states fail closed;
- missing stage dependencies do not advance trust;
- resolution failure preserves quarantine.

## Extension Rule

A future state may be added to `ENABLED_EDGES` only in the same governed transaction that introduces and verifies the concrete stage that earns that state.

A future provider-authentication edge therefore requires a real independently anchored provider/source verification mechanism. A fake/stub verifier or evidence-self-supplied trust key is insufficient.

## Non-Claims

- This contract does not authenticate any provider.
- It does not establish delivery or model execution.
- It does not establish independence.
- It does not qualify claims for authority.
- It does not prove cognitive benefit.
- It does not close the full external-evidence lifecycle.
