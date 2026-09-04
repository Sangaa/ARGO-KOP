# P11 GITHUB ACTIONS DIRECT FILTER BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-DIRECT-FILTER-BINDING-I`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / BOUNDED LOCAL SEMANTIC VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `930afdaef48b1577eec5c06e6be6d9a503d29654`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction H is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only direct result binding for the existing `branch` and `event` filters in `list_workflow_runs(...)`.

The connector already sends these filters to GitHub. Live provider evidence exposes the corresponding stable fields as `head_branch` and `event`. Before this transaction a provider result could disagree with those requested direct filters and still be returned as a valid observation.

This transaction does not bind `status`, alter exact-head binding, validate request argument types, change dispatch behavior, authenticate GitHub, or claim production success.

## Required invariants

`IF branch FILTER IS PROVIDED -> EACH RETURNED workflow_run.head_branch == REQUESTED branch`.

`IF event FILTER IS PROVIDED -> EACH RETURNED workflow_run.event == REQUESTED event`.

`FILTER NOT PROVIDED -> NO NEW FIELD REQUIREMENT FOR THAT FILTER`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-I-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind returned `head_branch` and `event` to requested direct filters | Y | bounded semantic |
| P11-I-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and empty direct-filter results | Y | exact-head CI pending |
| P11-I-03 | this Matrix | CREATE | bind direct-filter-only scope, provider observation, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated validation harness exercised seven cases:

- matching branch+event -> accepted;
- empty filtered collection -> accepted;
- missing branch -> structure failure;
- mismatched branch -> filter mismatch;
- missing event -> structure failure;
- mismatched event -> filter mismatch;
- no branch/event filters -> no new returned-field requirement.

Result: `7 / 7 expected outcomes`.

This is not full repository execution; immutable read-back and exact-head CI remain authoritative for material and closure validity.

## Provider observation

A live GitHub Actions request constrained by exact `head_sha`, `branch=main`, and `event=push` returned workflow-run objects with:

- `head_sha` equal to the requested exact head;
- `head_branch = main`;
- `event = push`.

This proves the direct provider representation used by this bounded transaction only. It does not prove authentication by ARGO's connector or remote execution initiated through that connector.

## KEEP Preservation

KEEP unchanged:

- Transaction H exact-head filter binding;
- Transactions G/F/E/D response lineage/shape/identity/decoding protections;
- `status` filter semantics;
- request argument type/emptiness validation;
- `per_page` semantics;
- dispatch behavior and `204 accepted != completed` distinction;
- job-log behavior;
- provider credentials/configuration/authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, workflow-completion or production-success claim is introduced.

## Post-write and closure rules

Apply connector + regression tests + this Matrix atomically against exact entry HEAD. Immutable read-back all three paths and compare entry→material HEAD; no path outside this authorized set may change.

All required exact-material-head workflow families must complete successfully before closure. Closure evidence must be captured separately; closure-head CI must itself be green before I can be used as a predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
