# P11 GITHUB ACTIONS DISPATCH REQUEST SHAPE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-DISPATCH-REQUEST-SHAPE-K`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / BOUNDED LOCAL SEMANTIC VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `917151f2bda3384fde0e4341906c019b57d8f9c2`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction J is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only typed caller-input validation for `dispatch_workflow(...)` before provider transport.

The provider-neutral interface declares `workflow_id: str | int`, `ref: str`, and `inputs: dict[str, str] | None`. Before this transaction, boolean/unsupported workflow identities could be interpolated into the URL, non-string refs could escape as raw attribute errors, and malformed inputs could be serialized and sent to the provider.

This transaction does not introduce a numeric range rule for integer workflow IDs, does not change workflow-name semantics, and does not alter the meaning of GitHub's empty 204 dispatch response.

## Required invariants

`workflow_id -> str OR exact int; BOOLEAN != workflow identity`.

`workflow_id AS str -> nonblank`.

`ref -> nonblank str BEFORE TRANSPORT`.

`inputs -> None OR dict[str, str] BEFORE TRANSPORT`.

`INVALID CALLER SHAPE -> ConnectorError BEFORE PROVIDER TRANSPORT`.

`204 ACCEPTED != WORKFLOW COMPLETED` remains unchanged.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-K-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | fail closed on invalid dispatch argument shapes before POST | Y | bounded semantic |
| P11-K-02 | `Quality/Integration/test_github_actions_connector_dispatch_shape.py` | CREATE | regress invalid workflow identity, ref and inputs with zero transport | Y | exact-head CI pending |
| P11-K-03 | this Matrix | CREATE | bind dispatch-input-only scope, evidence, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated validation harness exercised thirteen cases covering valid string/int identities, boolean/unsupported/blank identities, invalid refs, and malformed input containers/members.

Result: `13 / 13 expected outcomes`.

Integer workflow-ID range semantics were deliberately kept outside this transaction because the interface establishes the type but does not establish a local numeric-range contract.

## KEEP Preservation

KEEP unchanged:

- Transaction J list-request caller-shape guards;
- Transactions I/H/G/F/E/D response filter/lineage/shape/identity/decoding guards;
- workflow integer-ID range semantics;
- valid string workflow-name semantics;
- dispatch response behavior and `204 accepted != completed` distinction;
- `status` result semantics;
- job-log behavior;
- provider credentials/configuration/authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, workflow-completion or production-success claim is introduced.

## Post-write and closure rules

Apply connector + focused dispatch regression file + this Matrix atomically against exact entry HEAD. Immutable read-back all three paths and compare entry→material HEAD; no path outside this authorized set may change.

All required exact-material-head workflow families must complete successfully before closure. Closure evidence must be captured separately; closure-head CI must itself be green before K can be used as a predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
