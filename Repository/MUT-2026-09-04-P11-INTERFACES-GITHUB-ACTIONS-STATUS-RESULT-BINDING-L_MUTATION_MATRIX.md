# P11 GITHUB ACTIONS STATUS RESULT BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-STATUS-RESULT-BINDING-L`
Priority: `11 — Interfaces`
State: `CORRECTIVE MATERIAL PREPARED / EXACT-HEAD CI PENDING`
Entry HEAD: `cfee8422a819ec8e94f4ee7eba240568f1c5969e`
Initial Material HEAD: `8a942c1c6cfcc4674d289a2e3125e9f0565da05a`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction K is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only semantic result binding for the existing `status` filter of `list_workflow_runs(...)` and the bounded repair of one historical integration fixture exposed by that stronger invariant.

GitHub's authoritative REST contract states that the `status` query parameter returns workflow runs with the check-run `status` OR `conclusion` specified by the caller. Therefore equality against `run.status` alone would be a false transfer from branch/event binding.

This transaction does not introduce a hardcoded local enum, does not alter request-shape validation, does not change branch/event/head_sha guards, and does not claim provider authentication or production execution.

## Required invariants

`IF status FILTER IS PROVIDED -> REQUESTED VALUE MUST BE REPRESENTED BY returned run.status OR returned run.conclusion`.

`SIMILAR FILTER SHAPE != IDENTICAL FILTER SEMANTICS`.

`NO status FILTER -> NO NEW status/conclusion FIELD REQUIREMENT`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

`TEST FIXTURE MUST REPRESENT EVERY SEMANTIC FIELD REQUIRED BY THE FILTER IT CLAIMS TO EXERCISE`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-L-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind requested status to returned status-or-conclusion semantics | Y | initial material read-back verified; exact-head CI revalidation pending |
| P11-L-02 | `Quality/Integration/test_github_actions_connector_status_binding.py` | CREATE | regress conclusion match, runtime-status match, mismatch, missing representation and unfiltered behavior | Y | initial material read-back verified; exact-head CI revalidation pending |
| P11-L-03 | this Matrix | CREATE/UPDATE | bind status-only scope, provider semantics, corrective evidence, KEEP constraints and closure | Y | Y |
| P11-L-04 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | repair historical execution-filter fixture so its nonempty provider result represents requested `status=completed` | Y | exact-head CI pending |

## Initial material evidence

Initial material commit `8a942c1c6cfcc4674d289a2e3125e9f0565da05a` was applied against exact entry HEAD with only connector + focused regression + this Matrix changed. Immutable read-back and scope comparison passed.

Exact-initial-material-head CI produced three successful required workflow families and one failed family:

- Full-Stack Repository Audit: SUCCESS;
- M2 Multi-Channel Proposal Training: SUCCESS;
- Real Mutation Matrix Regression: SUCCESS;
- ARGO Runtime Prototype and Integration Tests: FAILURE, run `33884086071`, job `101059520087`, step `Run integration quality suite`.

L therefore remained OPEN and no closure commit was allowed.

## Corrective diagnosis

Exact-head inspection of `Quality/Integration/test_github_actions_connector.py` established a bounded stale-fixture collision. `test_list_workflow_runs_preserves_execution_filters` calls:

`list_workflow_runs(branch="main", event="push", head_sha="abc", status="completed")`

while its nonempty fake provider run represented `head_sha`, `head_branch`, and `event` but represented neither `status` nor `conclusion`.

Under the newly explicit and provider-correct L invariant, that fixture must fail closed. The failure is therefore evidence that the strengthened invariant exposed historical test data which was no longer semantically sufficient; it is not evidence that the invariant should be weakened.

Corrective action is bounded to the fixture: add returned `status="completed"`. No connector implementation change is authorized by this repair.

## Evidence

Authoritative GitHub REST documentation for `List workflow runs for a repository` defines `status` as returning workflow runs with the check-run `status` or `conclusion` specified by the caller. Live provider observations also showed `status=success` returning runs with `status=completed` and `conclusion=success`.

The implementation therefore applies result/evidence binding at the actual provider semantics instead of copying the direct-equality implementation used for branch/event.

## HORUS transfer check

Abstract principle: bind requested semantic constraints to returned evidence.

Context-specific prior implementation: branch/event use direct equality against one returned field.

Current capability meaning: GitHub `status` query spans two returned semantic fields, status and conclusion.

False transfer avoided: no `requested_status == run.status` invariant and no convenience enum copied locally.

Corrective learning: a stronger semantic invariant may invalidate an old synthetic fixture without invalidating the invariant. Repair the fixture at the stable contractual representation; do not weaken production semantics to preserve obsolete synthetic data.

## KEEP Preservation

KEEP unchanged:

- Transaction K dispatch caller-shape protections and `204 accepted != completed`;
- Transaction J list request-shape validation;
- branch/event/head_sha result binding;
- run/job identity and lineage guards;
- response decoding/collection-shape guards;
- provider credentials/configuration/authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, workflow-completion or production-success claim is introduced.

## Post-write and closure rules

Corrective material must be applied atomically against exact initial material HEAD `8a942c1c6cfcc4674d289a2e3125e9f0565da05a` with only the historical integration fixture and this Matrix changed. Immutable read-back both paths and compare initial-material→corrective-material HEAD; no path outside this corrective set may change.

All four required exact-corrective-material-head workflow families must complete successfully before closure. Closure evidence must be Matrix-only and closure-head CI must independently be green before L can be used as predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
