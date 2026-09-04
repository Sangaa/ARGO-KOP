# P11 GITHUB ACTIONS EXACT-HEAD FILTER BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-EXACT-HEAD-FILTER-H`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / BOUNDED LOCAL SEMANTIC VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `525d1b720ea57ba9bdd739c541557220d8c3928d`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction G is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only result binding for the existing `head_sha` filter in `list_workflow_runs(...)`.

The connector already sends `head_sha` to GitHub and validates the top-level `workflow_runs` collection, but it does not prove that returned run objects actually carry the requested exact head identity. This matters because exact-head evidence is used by the repository closure discipline.

This transaction does not bind branch, event or status filters, does not change workflow dispatch, does not authenticate GitHub, and does not convert provider observation into production success.

## Material Gap

The provider-neutral Actions interface promises:

`list_workflow_runs(... head_sha=...) -> List workflow runs using explicit execution filters.`

Live GitHub observation for exact-head queries returns each run with `head_sha` equal to the requested SHA. Passing the query parameter without checking the returned stable identity leaves a fail-open seam between requested exact-head evidence and observed result identity.

Required invariant:

`IF head_sha FILTER IS PROVIDED -> EACH RETURNED workflow_run.head_sha == REQUESTED head_sha`.

`NO head_sha FILTER -> NO NEW head_sha FIELD REQUIREMENT`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-H-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind each returned run to the requested exact `head_sha` when that filter is supplied | Y | bounded semantic |
| P11-H-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and unfiltered response behavior | Y | exact-head CI pending |
| P11-H-03 | this Matrix | CREATE | bind exact-head-only scope, evidence, KEEP constraints and closure rules | Y | Y |

## Bounded local semantic evidence

A local isolated validation harness exercised the exact candidate invariant across five cases:

- matching `head_sha` -> accepted;
- empty collection under a filter -> accepted;
- missing returned `head_sha` under a filter -> explicit structure failure;
- mismatched returned `head_sha` -> explicit filter mismatch;
- no requested `head_sha` -> no additional returned-field requirement.

Result: `5 / 5 expected outcomes`.

This is not full repository execution. Full targeted/regression truth remains exact-head CI after mutation.

## Provider observation

Live GitHub Actions query using exact `head_sha=525d1b720ea57ba9bdd739c541557220d8c3928d` returned workflow-run objects whose `head_sha` equals that exact requested value. This establishes the provider representation used by this bounded check only.

## KEEP Preservation

KEEP unchanged:

- Transaction G job-to-run lineage checks;
- Transaction F collection-shape validation;
- Transaction E exact run-id lookup validation;
- Transaction D response decoding;
- branch, event and status result-binding semantics;
- `per_page` input semantics;
- dispatch behavior and `204 accepted != completed` distinction;
- job-log behavior;
- provider credentials/configuration/authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, workflow-completion or production-success claim is introduced.

## Post-write and closure rules

After atomic mutation, immutable read-back all three paths and compare entry→material HEAD; no path outside this authorized set may change.

Exact material-head required workflow families must all complete successfully before closure. Closure evidence must be captured separately and closure-head CI must itself be green before the transaction is used as a predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
