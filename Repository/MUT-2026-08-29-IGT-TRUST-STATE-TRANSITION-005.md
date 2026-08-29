# MUT-2026-08-29-IGT-TRUST-STATE-TRANSITION-005

Transaction ID: `MUT-2026-08-29-IGT-TRUST-STATE-TRANSITION-005`
Lease: `R71-20260829-IGT-TRUST-TRANSITION-005`
Entry baseline: `main@60e5739a19ee673031ebfbffca40d9c9c852c288`
Lease-opening commit: `c7c769496399bba30bff6de5dd78fa17fd81561f`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + Room71 repository-first execution + current IGT trust boundaries`
Status: `ACTIVE / FAIL-CLOSED TRANSITION ORCHESTRATION`
Authority: `NONE`

## Objective

Add an executable orchestration boundary that prevents callers or later models from skipping legal IGT evidence stages.

Current implemented legal transition:

`UNTRUSTED_QUARANTINED → RESOLVED_UNAUTHENTICATED`

The guard must earn that transition by invoking the existing quarantine-resolution gate itself.

All later authenticity / execution / delivery / qualification / authority states remain unavailable until their own governed implementation and evidence exist.

## Pre-Write Evidence

Current repository searches found no independent executable trust-state transition guard. Trust boundaries currently exist inside individual gates and documentation, which leaves orchestration susceptible to callers inventing a later state outside those gates.

Provider-authentication readiness was separately assessed and closed as `NOT READY / HARD TRUST-ANCHOR HOLD`; therefore this transaction must not simulate, stub, or fake provider authentication.

## Guard Principles

1. Caller-supplied target state is a request, not evidence.
2. Caller-supplied booleans/labels such as `verified`, `authenticated`, or `authorized` grant no transition.
3. A legal transition must invoke the concrete implemented stage that earns it.
4. Stage failure preserves the prior trust state.
5. Same-state requests are no-op and invoke no stage.
6. Unknown states fail closed.
7. Known future states without an implemented stage return `TRANSITION_NOT_ENABLED` before invoking any unrelated dependency.
8. No generic upward transition is inferred from name ordering or semantic similarity.

## State Vocabulary Boundary

Implemented current states:

- `UNTRUSTED_QUARANTINED`
- `RESOLVED_UNAUTHENTICATED`

Known but **not enabled** upward targets include current repository vocabulary such as:

- `PROVIDER_AUTHENTICATED`
- `SOURCE_AUTHENTICATED`
- `EXTERNAL_AUTHENTICITY_VERIFIED`
- `EXECUTION_VERIFIED`
- `DELIVERY_VERIFIED`
- `QUALIFIED`
- `AUTHORIZED`
- `ADMITTED_BOUNDED`
- `PROMOTED`

Recognition of a name does not implement that state.

## Mutation Matrix

| Target | Action | Boundary |
|---|---|---|
| `Quality/Integration/experience_spine_igt_trust_state_transition_gate.py` | ADD | orchestrate only implemented transitions |
| `Quality/Integration/test_experience_spine_igt_trust_state_transition_gate.py` | ADD | prove no-op, legal transition and illegal-jump failure semantics |
| `Repository/IGT_TRUST_STATE_TRANSITION_CONTRACT_2026-08-29.md` | ADD | semantic state-machine contract |
| this transaction | UPDATE | execution evidence / learning / closure |
| `Repository/ROOM071_CURRENT_STATE.json` | UPDATE | close lease only after exact-head CI |

## Non-Claims

- The guard does not authenticate providers.
- It does not establish delivery or model execution.
- It does not implement qualification or authority.
- It does not make trust monotonic by numeric ordering; only explicit legal edges exist.
- It does not close the external-evidence lifecycle beyond currently implemented stages.
