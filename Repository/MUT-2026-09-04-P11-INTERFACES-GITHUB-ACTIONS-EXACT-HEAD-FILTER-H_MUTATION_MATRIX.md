# P11 GITHUB ACTIONS EXACT-HEAD FILTER BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-EXACT-HEAD-FILTER-H`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `525d1b720ea57ba9bdd739c541557220d8c3928d`
Material HEAD: `4f4dc7cdb6d0136c87116e08c2d52a045bbd5afb`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction G is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addressed only result binding for the existing `head_sha` filter in `list_workflow_runs(...)`.

The connector already sent `head_sha` to GitHub and validated the top-level `workflow_runs` collection, but it did not prove that returned run objects actually carried the requested exact head identity. Exact-head identity is part of repository closure evidence and must fail closed when provider observation disagrees.

This transaction does not bind branch, event or status filters, does not change workflow dispatch, does not authenticate GitHub, and does not convert provider observation into production success.

## Invariants now enforced

`IF head_sha FILTER IS PROVIDED -> EACH RETURNED workflow_run.head_sha == REQUESTED head_sha`.

`NO head_sha FILTER -> NO NEW head_sha FIELD REQUIREMENT`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-H-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind each returned run to the requested exact `head_sha` when supplied | Y | Y |
| P11-H-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and unfiltered behavior | Y | Y |
| P11-H-03 | this Matrix | CREATE/FINALIZE | bind exact-head-only scope, evidence, KEEP constraints and closure | Y | Y |

## Bounded local semantic evidence

An isolated local validation harness exercised five cases: matching SHA, empty collection, missing returned SHA, mismatched returned SHA, and unfiltered behavior.

Result: `5 / 5 expected outcomes`.

This remained bounded semantic evidence; repository truth came from immutable read-back and exact-head CI.

## Immutable material read-back

Material HEAD: `4f4dc7cdb6d0136c87116e08c2d52a045bbd5afb`.

Observed material blobs:

- `Services/GITHUB_ACTIONS_CONNECTOR.py` → `b27e9ec893b3bc0519bdc338345963f85c5551e1`;
- `Quality/Integration/test_github_actions_connector.py` → `cd1a8cc6545be1d02d2709e4ef19325df13bb544`;
- this Matrix → `9f03565301078cea9c4a86289bda5a807b47b03d` before closure finalization.

Entry→material compare: one commit ahead, zero behind, exactly the three authorized paths. No unexpected path changed.

## Exact material-head CI evidence

All required workflow families completed successfully on exact material HEAD `4f4dc7cdb6d0136c87116e08c2d52a045bbd5afb`:

- Real Mutation Matrix Regression — run `33879562935` — `completed / success`;
- M2 Multi-Channel Proposal Training — run `33879563067` — `completed / success`;
- ARGO Runtime Prototype and Integration Tests — run `33879562990` — `completed / success`;
- Full-Stack Repository Audit — run `33879562858` — `completed / success`.

These CI results verify the repository material at the exact commit. They do not prove ARGO connector provider authentication, remote delivery initiated by the connector, or production success.

## Provider observation

Live GitHub Actions queries using exact `head_sha=4f4dc7cdb6d0136c87116e08c2d52a045bbd5afb` returned workflow-run objects whose `head_sha` equals that requested value. A combined live query also showed direct provider fields `head_branch=main` and `event=push`; those fields remain outside H and are candidates for a later bounded transaction.

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

## Closure

Material validity, transaction validity and closure validity were evaluated separately. Material is boundedly locally checked, immutable read-back matches intended blobs, entry→material scope is exact, and all required exact-material-head workflow families are green.

This finalization commit changes only this Matrix. Its own exact-head workflow runs must remain green before H is used as the next live predecessor.

Unexpected Changes: `NONE`.

Transaction H: `CLOSED / VERIFIED / RESUME-SAFE`, subject to exact closure-head CI confirmation before subsequent mutation.
