# P11 GITHUB ACTIONS LIST REQUEST SHAPE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-LIST-REQUEST-SHAPE-J`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / BOUNDED LOCAL SEMANTIC VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `e3096afca868baca8bcd90e6fd59e64eac2ff82e`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction I is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only typed caller-input validation for `list_workflow_runs(...)` before provider transport.

The provider-neutral interface declares optional `branch`, `event`, `head_sha`, and `status` filters as strings and `per_page` as an integer. Before this transaction, non-string filter values were URL-encoded and sent to the provider, while `per_page=True` and floating-point values could pass Python's numeric comparison and string values could escape as a raw `TypeError` rather than an explicit connector failure.

This transaction does not assign new semantics to empty strings, does not bind `status` results, does not change branch/event/exact-head response checks, does not alter dispatch behavior, and does not authenticate GitHub.

## Required invariants

`OPTIONAL FILTER PROVIDED -> VALUE IS str BEFORE TRANSPORT`.

`per_page -> type(value) is int AND 1 <= value <= 100`.

`BOOLEAN != per_page INTEGER IDENTITY`.

`INVALID CALLER SHAPE -> ConnectorError BEFORE PROVIDER TRANSPORT`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-J-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | reject non-string optional filters and non-real-int/out-of-range `per_page` before transport | Y | bounded semantic |
| P11-J-02 | `Quality/Integration/test_github_actions_connector_request_shape.py` | CREATE | regress invalid filter types and invalid `per_page` values with zero transport calls | Y | exact-head CI pending |
| P11-J-03 | this Matrix | CREATE | bind typed-list-input-only scope, evidence, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated validation harness exercised eleven cases: two valid calls; four non-string filter types; boolean, float and string `per_page`; and lower/upper bound violations.

Result: `11 / 11 expected outcomes`.

This validates the bounded guard semantics only. Full repository regression truth remains immutable read-back and exact-head CI.

## KEEP Preservation

KEEP unchanged:

- Transaction I branch/event result binding;
- Transaction H exact-head result binding;
- Transactions G/F/E/D lineage/shape/identity/response guards;
- empty-string filter semantics;
- `status` provider-result semantics;
- dispatch request semantics;
- job-log behavior;
- provider credentials/configuration/authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, workflow-completion or production-success claim is introduced.

## Post-write and closure rules

Apply connector + focused regression file + this Matrix atomically against exact entry HEAD. Immutable read-back all three paths and compare entry→material HEAD; no path outside this authorized set may change.

All required exact-material-head workflow families must complete successfully before closure. Closure evidence must be captured separately; closure-head CI must itself be green before J can be used as a predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
