# P11 GITHUB ACTIONS LIST REQUEST SHAPE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-LIST-REQUEST-SHAPE-J`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `e3096afca868baca8bcd90e6fd59e64eac2ff82e`
Material HEAD: `1debf9fd362b72a814e8a8970c9bfff726acd5d7`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction I is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addressed only typed caller-input validation for `list_workflow_runs(...)` before provider transport.

The provider-neutral interface declares optional `branch`, `event`, `head_sha`, and `status` filters as strings and `per_page` as an integer. Before this transaction, non-string filter values could be URL-encoded and sent to the provider, while boolean/floating `per_page` values could pass numeric comparison and string values could escape as raw `TypeError`.

No new semantics were assigned to empty strings or to provider `status` results.

## Required invariants now enforced

`OPTIONAL FILTER PROVIDED -> VALUE IS str BEFORE TRANSPORT`.

`per_page -> type(value) is int AND 1 <= value <= 100`.

`BOOLEAN != per_page INTEGER IDENTITY`.

`INVALID CALLER SHAPE -> ConnectorError BEFORE PROVIDER TRANSPORT`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-J-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | reject invalid filter types and invalid `per_page` before transport | Y | Y |
| P11-J-02 | `Quality/Integration/test_github_actions_connector_request_shape.py` | CREATE | regress caller-shape failures with zero transport calls | Y | Y |
| P11-J-03 | this Matrix | CREATE/FINALIZE | bind typed-list-input-only scope, evidence, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated validation harness exercised eleven cases: two valid calls; four non-string filter types; boolean, float and string `per_page`; and lower/upper bound violations.

Result: `11 / 11 expected outcomes`.

## Immutable material read-back

Material HEAD: `1debf9fd362b72a814e8a8970c9bfff726acd5d7`.

Observed material blobs:

- `Services/GITHUB_ACTIONS_CONNECTOR.py` → `b96ede24b13e0be7416c324b780d95a8904148cd`;
- `Quality/Integration/test_github_actions_connector_request_shape.py` → `e16734cf55c82f53410ec287f587bb2cd137d3e4`;
- this Matrix → `8e4f1188f91b6405a602ebad9dcaadc3defc2d20` before closure finalization.

Entry→material compare: one commit ahead, zero behind, exactly the three authorized paths. No unexpected path changed.

## Exact material-head CI evidence

All required workflow families completed successfully on exact material HEAD `1debf9fd362b72a814e8a8970c9bfff726acd5d7`:

- Real Mutation Matrix Regression — run `33880567127` — `completed / success`;
- M2 Multi-Channel Proposal Training — run `33880567117` — `completed / success`;
- ARGO Runtime Prototype and Integration Tests — run `33880567106` — `completed / success`;
- Full-Stack Repository Audit — run `33880567174` — `completed / success`.

These CI results verify repository material at the exact commit. They do not prove ARGO connector provider authentication, remote delivery initiated by that connector, or production success.

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

## Closure

Material validity, transaction validity and closure validity were evaluated separately. Material read-back matches intended blobs, entry→material scope is exact, and all required exact-material-head workflow families are green.

This finalization commit changes only this Matrix. Its exact closure-head workflow runs must remain green before J is used as the next live predecessor.

Unexpected Changes: `NONE`.

Transaction J: `CLOSED / VERIFIED / RESUME-SAFE`, subject to exact closure-head CI confirmation before subsequent mutation.
