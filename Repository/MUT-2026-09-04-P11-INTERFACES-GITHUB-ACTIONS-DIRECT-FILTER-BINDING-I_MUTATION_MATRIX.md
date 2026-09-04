# P11 GITHUB ACTIONS DIRECT FILTER BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-DIRECT-FILTER-BINDING-I`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `930afdaef48b1577eec5c06e6be6d9a503d29654`
Material HEAD: `3440d92d9a377584a9a2a755be4925cf43074484`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction H is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addressed only direct result binding for the existing `branch` and `event` filters in `list_workflow_runs(...)`.

The connector already sent these filters to GitHub. Live provider evidence exposes the corresponding stable fields as `head_branch` and `event`. Before this transaction a provider result could disagree with those requested direct filters and still be returned as a valid observation.

This transaction does not bind `status`, alter exact-head binding, validate request argument types, change dispatch behavior, authenticate GitHub, or claim production success.

## Required invariants now enforced

`IF branch FILTER IS PROVIDED -> EACH RETURNED workflow_run.head_branch == REQUESTED branch`.

`IF event FILTER IS PROVIDED -> EACH RETURNED workflow_run.event == REQUESTED event`.

`FILTER NOT PROVIDED -> NO NEW FIELD REQUIREMENT FOR THAT FILTER`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-I-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind returned `head_branch` and `event` to requested direct filters | Y | Y |
| P11-I-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and empty direct-filter results | Y | Y |
| P11-I-03 | this Matrix | CREATE/FINALIZE | bind direct-filter-only scope, provider observation, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated validation harness exercised seven cases: matching branch+event, empty filtered collection, missing branch, branch mismatch, missing event, event mismatch, and no direct filters.

Result: `7 / 7 expected outcomes`.

This remained bounded semantic evidence; repository truth came from immutable read-back and exact-head CI.

## Immutable material read-back

Material HEAD: `3440d92d9a377584a9a2a755be4925cf43074484`.

Observed material blobs:

- `Services/GITHUB_ACTIONS_CONNECTOR.py` → `571d9110cd70881105c887a1e0024cec72095c49`;
- `Quality/Integration/test_github_actions_connector.py` → `c22f0ed5b20bb77b4abced4a38564d0d165db4e2`;
- this Matrix → `7362af900e2610710dee6b036ee6f7b1ab3a5df9` before closure finalization.

Entry→material compare: one commit ahead, zero behind, exactly the three authorized paths above. No unexpected path changed.

## Exact material-head CI evidence

All required workflow families completed successfully on exact material HEAD `3440d92d9a377584a9a2a755be4925cf43074484`:

- Real Mutation Matrix Regression — run `33880012797` — `completed / success`;
- M2 Multi-Channel Proposal Training — run `33880013068` — `completed / success`;
- ARGO Runtime Prototype and Integration Tests — run `33880013040` — `completed / success`;
- Full-Stack Repository Audit — run `33880012933` — `completed / success`.

These runs validate repository material at the exact commit. They do not prove ARGO connector provider authentication, remote delivery initiated by that connector, or production success.

## Provider observation

A live GitHub Actions request constrained by exact `head_sha`, `branch=main`, and `event=push` returned workflow-run objects with matching `head_sha`, `head_branch=main`, and `event=push`. This proves the direct provider representation used by this bounded transaction only.

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

## Closure

Material validity, transaction validity and closure validity were evaluated separately. Material read-back matches intended blobs, entry→material scope is exact, and all required exact-material-head workflow families are green.

This finalization commit changes only this Matrix. Its own exact-head workflow runs must remain green before I is used as the next live predecessor.

Unexpected Changes: `NONE`.

Transaction I: `CLOSED / VERIFIED / RESUME-SAFE`, subject to exact closure-head CI confirmation before subsequent mutation.
