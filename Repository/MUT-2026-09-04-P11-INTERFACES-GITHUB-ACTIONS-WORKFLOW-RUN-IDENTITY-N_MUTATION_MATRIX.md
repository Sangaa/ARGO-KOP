# P11 GITHUB ACTIONS WORKFLOW RUN IDENTITY MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-WORKFLOW-RUN-IDENTITY-N`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `8f09d9f3822337416d48de0570676d0d25bf4992`
Material HEAD: `d53b7d0971491e681472df03d0c6453456c52b07`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction M is `CLOSED / VERIFIED / RESUME-SAFE` and is the exact predecessor.

M binds returned `jobs[].id` before downstream job-log consumption. N addresses the parallel but distinct workflow-run identity seam: `list_workflow_runs(...)` returns workflow-run objects whose `id` is subsequently consumable by `get_workflow_run(run_id)` and `list_workflow_run_jobs(run_id)`, while the list boundary previously accepted missing, boolean, non-integer, zero, or negative run identities.

Live exact-head workflow observations on predecessor closure returned positive integer run IDs `33902072777`, `33902072797`, `33902072786`, and `33902072800`.

## Required invariants

`RETURNED workflow_runs[].id MUST BE AN EXACT POSITIVE INTEGER BEFORE IT MAY SERVE AS WORKFLOW-RUN EXECUTION IDENTITY`.

`BOOLEAN != EXECUTION IDENTITY`.

`WORKFLOW-RUN IDENTITY VALIDITY != FILTER SEMANTICS`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

No uniqueness claim is introduced.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-N-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | validate every returned nonempty `workflow_runs[].id` as exact positive int before existing filter guards | Y | Y |
| P11-N-02 | `Quality/Integration/test_github_actions_connector_run_identity.py` | CREATE | regress valid identity, invalid/missing/bool/zero/negative/non-int rejection, filter preservation, empty collection | Y | Y |
| P11-N-03 | `Quality/Integration/test_github_actions_connector_status_binding.py` | UPDATE | normalize legacy status fixtures with valid run identity while preserving status-specific assertions | Y | Y |
| P11-N-04 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | normalize legacy direct-filter fixtures with valid run identity while preserving branch/event-specific assertions | Y | Y |
| P11-N-05 | this Matrix | CREATE/UPDATE | bind N scope, evidence, KEEP constraints and closure | Y | Y |

## Fixture normalization rule

The stronger identity invariant makes historical synthetic fixtures incomplete where their intended seam is status/branch/event semantics rather than identity. Those fixtures were repaired at the stable contractual representation by adding only a valid positive integer `id`. Production identity semantics were not weakened to preserve obsolete synthetic data.

## Material evidence

Material commit `d53b7d0971491e681472df03d0c6453456c52b07` was created from exact entry HEAD and changed exactly five authorized paths: connector, focused identity regression, two historical fixture files, and this Matrix. Entry→material compare found no unexpected path. Immutable read-back confirmed the run-identity guard before existing filter guards.

## Exact material-head CI

All four required workflow families completed successfully on exact material HEAD `d53b7d0971491e681472df03d0c6453456c52b07`:

- ARGO Runtime Prototype and Integration Tests — run `33905427792` — SUCCESS;
- Full-Stack Repository Audit — run `33905427793` — SUCCESS;
- M2 Multi-Channel Proposal Training — run `33905427816` — SUCCESS;
- Real Mutation Matrix Regression — run `33905427800` — SUCCESS.

## KEEP Preservation

KEEP unchanged:

- Transaction H exact `head_sha` binding;
- Transaction I branch/event direct-result binding;
- Transaction L status/conclusion semantic binding;
- Transaction M job identity and Transaction G job→run lineage binding;
- request-shape guards, dispatch semantics, collection-shape validation, and empty-list acceptance;
- provider authentication/configuration and log transport behavior.

## Closure rule

This commit changes only this Matrix. N remains `CLOSED / VERIFIED / RESUME-SAFE` only if all four required workflow families independently complete successfully on the exact closure HEAD. If closure-head CI is not 4/4 successful, this state is automatically non-authoritative until contradictory evidence is resolved.

Unexpected Changes: `NONE AUTHORIZED`.
