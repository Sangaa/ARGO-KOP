# P11 GITHUB ACTIONS JOB IDENTITY MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-IDENTITY-M`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `bbd228d9f8dfc06e985521955ff529a98a49eb90`
Material HEAD: `193ac1e9e385931ca7cc0dbe4f8b7283961e1316`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction L is `CLOSED / VERIFIED / RESUME-SAFE` and is the exact predecessor.

Transaction G already binds returned `jobs[].run_id` to the requested workflow run. M does not reopen or broaden G. M addresses the adjacent execution-identity seam: `list_workflow_run_jobs(...)` returns job objects whose `id` is subsequently consumed by `get_workflow_job_logs(job_id)`, but the list boundary did not previously fail closed when that provider identity was absent, boolean, non-integer, zero, or negative.

Live provider observation on exact predecessor run `33901643565` returned three jobs with positive integer `id` values and `run_id=33901643565` for each job.

## Required invariants

`RETURNED jobs[].id MUST BE AN EXACT POSITIVE INTEGER BEFORE IT MAY SERVE AS JOB EXECUTION IDENTITY`.

`BOOLEAN != EXECUTION IDENTITY`.

`JOB IDENTITY VALIDITY != RUN LINEAGE VALIDITY`.

`EMPTY jobs COLLECTION REMAINS VALID`.

No uniqueness claim is introduced. No provider-authenticity or log-integrity claim is introduced.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-M-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | validate every returned nonempty `jobs[].id` as exact positive int before preserving existing run-lineage validation | Y | Y |
| P11-M-02 | `Quality/Integration/test_github_actions_connector_job_identity.py` | CREATE | regress positive identity, missing/bool/zero/negative/non-int rejection, lineage preservation and empty collection | Y | Y |
| P11-M-03 | this Matrix | CREATE/UPDATE | bind M scope, provider evidence, KEEP constraints, material evidence and closure | Y | Y |

## Provider and consumer evidence

Exact predecessor source already requires the caller-supplied `job_id` consumed by `get_workflow_job_logs(job_id)` to be an exact positive integer and constructs the provider endpoint `jobs/{job_id}/logs` from that identity.

The same source's `list_workflow_run_jobs(run_id)` previously validated only `jobs[].run_id`. Thus a malformed returned job could carry valid run lineage while exposing an unusable or ambiguous `id` to the downstream log-observation boundary.

Live GitHub observation from Runtime closure run `33901643565` returned positive integer job identities `101116874243`, `101116874419`, and `101116874809`, each bound to that run.

## Material rule

For each returned job object, validate `type(job.get("id")) is int` and `id > 0` before the existing `run_id` lineage checks. Invalid provider identity raises the existing response-structure failure class for `GET runs/{run_id}/jobs.jobs[].id`.

This is shape/identity validation only. It does not assert uniqueness, ownership beyond the already separately checked `run_id`, authenticity of GitHub as provider, or successful log retrieval.

## Material evidence

Material commit `193ac1e9e385931ca7cc0dbe4f8b7283961e1316` was created from exact entry HEAD `bbd228d9f8dfc06e985521955ff529a98a49eb90` and changed exactly three authorized paths:

- `Services/GITHUB_ACTIONS_CONNECTOR.py` — five-line positive exact-int job identity guard;
- `Quality/Integration/test_github_actions_connector_job_identity.py` — focused regression;
- this Matrix.

Entry→material compare showed no unexpected path. Immutable read-back confirmed the connector guard, focused regression, and Matrix.

## Exact material-head CI

All four required workflow families completed successfully on exact material HEAD `193ac1e9e385931ca7cc0dbe4f8b7283961e1316`:

- ARGO Runtime Prototype and Integration Tests — run `33901946846` — SUCCESS;
- Full-Stack Repository Audit — run `33901946811` — SUCCESS;
- M2 Multi-Channel Proposal Training — run `33901946920` — SUCCESS;
- Real Mutation Matrix Regression — run `33901946860` — SUCCESS.

Material validity remains distinct from closure validity; this commit therefore records Matrix-only closure evidence and requires independent exact-closure-head validation.

## KEEP Preservation

KEEP unchanged:

- Transaction G exact `jobs[].run_id` lineage binding;
- Transaction L status filter result binding;
- run identity and workflow-run filter guards;
- dispatch request-shape protections and `204 accepted != completed`;
- collection-shape validation and empty-job-list acceptance;
- log transport and UTF-8 decoding behavior;
- provider credentials/configuration/authentication;
- Runtime consumers and Interface documentary contracts.

## Closure rule

This commit must change only this Matrix. M may remain `CLOSED / VERIFIED / RESUME-SAFE` only if all four required workflow families independently complete successfully on the exact closure HEAD.

If closure-head CI is not 4/4 successful, this state is automatically non-authoritative until contradictory evidence is resolved.

Unexpected Changes: `NONE AUTHORIZED`.
