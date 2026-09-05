# P12 Transaction B — Unit 16 Corrective Matrix A

Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Corrective scope: `UNIT16 / POST-REGISTRATION REL-012 GUARD TRANSITION`
State: `CORRECTIVE APPLIED / EXACT-HEAD CI PENDING`
Date: 2026-09-05

## Trigger

Unit-16 canonical registry head `1081d06d6852bcbfa32936ea689d862a57013e8f` produced:

- Real Mutation Matrix Regression — SUCCESS (`33977557344`)
- M2 Multi-Channel Proposal Training — SUCCESS (`33977557336`)
- Full-Stack Repository Audit — SUCCESS (`33977557318`)
- ARGO Runtime Prototype and Integration Tests — FAILURE (`33977557379`)

Runtime subjobs showed prototype and integration SUCCESS; the integrity suite was bounded to one failure with `254 passed, 1 failed`.

Failing guard:

`Quality/Integrity/test_models_p12_mod011_relationships.py::test_registry_is_not_silently_treated_as_already_corrected`

The guard asserted the pre-registration canonical representation:

`REL-012 = MOD-011 → KNW-004 / DEPENDS_ON`

and rejected the newly verified representation:

`REL-012 = MOD-011 → KNW-004 / REFERENCES`.

## Classification

`STALE PRE-REGISTRATION GUARD / CURRENT SOURCE AND CANONICAL REGISTRY AGREE`.

The evidence surface D is intentionally preserved as pre-registration provenance, including its then-pending registry action. The corrective change does not rewrite that historical evidence and does not modify REP-014.

## Corrective action

Only the executable guard is updated so that it now:

- preserves the evidence surface's historical action state;
- requires canonical `REL-012 = MOD-011 → KNW-004 / REFERENCES`;
- rejects the superseded `DEPENDS_ON` registry form;
- requires the registry's `STABLE-ID TYPE CORRECTION` marker.

No source model, endpoint, relationship type, registry row, manifest, allocation plan or authority status is changed by this corrective action.

## Invariant

`HISTORICAL EVIDENCE STATE != CURRENT CANONICAL REGISTRY STATE`.

A guard may preserve what was pending at an earlier checkpoint without requiring the canonical registry to remain stale after the governed mutation executes.

## Validation requirement

This corrective Matrix filename intentionally belongs to the `CORRECTIVE_MATRIX` trigger family so all four workflow families must run on the same corrective head. No Unit-17/status/queue mutation is authorized until exact-head 4/4 SUCCESS.
