# P11 GITHUB ACTIONS STATUS RESULT BINDING MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-STATUS-RESULT-BINDING-L`
Priority: `11 — Interfaces`
State: `MATERIAL PREPARED / EXACT-HEAD WRITE PENDING`
Entry HEAD: `cfee8422a819ec8e94f4ee7eba240568f1c5969e`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction K is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only semantic result binding for the existing `status` filter of `list_workflow_runs(...)`.

GitHub's authoritative REST contract states that the `status` query parameter returns workflow runs with the check-run `status` OR `conclusion` specified by the caller. Therefore equality against `run.status` alone would be a false transfer from branch/event binding.

This transaction does not introduce a hardcoded local enum, does not alter request-shape validation, does not change branch/event/head_sha guards, and does not claim provider authentication or production execution.

## Required invariants

`IF status FILTER IS PROVIDED -> REQUESTED VALUE MUST BE REPRESENTED BY returned run.status OR returned run.conclusion`.

`SIMILAR FILTER SHAPE != IDENTICAL FILTER SEMANTICS`.

`NO status FILTER -> NO NEW status/conclusion FIELD REQUIREMENT`.

`EMPTY workflow_runs COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-L-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | bind requested status to returned status-or-conclusion semantics | Y | exact-head CI pending |
| P11-L-02 | `Quality/Integration/test_github_actions_connector_status_binding.py` | CREATE | regress conclusion match, runtime-status match, mismatch, missing representation and unfiltered behavior | Y | exact-head CI pending |
| P11-L-03 | this Matrix | CREATE | bind status-only scope, provider semantics, KEEP constraints and closure | Y | Y |

## Evidence

Authoritative GitHub REST documentation for `List workflow runs for a repository` defines `status` as returning workflow runs with the check-run `status` or `conclusion` specified by the caller. Live provider observations also showed `status=success` returning runs with `status=completed` and `conclusion=success`.

The implementation therefore applies result/evidence binding at the actual provider semantics instead of copying the direct-equality implementation used for branch/event.

## HORUS transfer check

Abstract principle: bind requested semantic constraints to returned evidence.

Context-specific prior implementation: branch/event use direct equality against one returned field.

Current capability meaning: GitHub `status` query spans two returned semantic fields, status and conclusion.

False transfer avoided: no `requested_status == run.status` invariant and no convenience enum copied locally.

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

Apply connector + focused regression + this Matrix atomically against exact entry HEAD. Immutable read-back all three paths and compare entry→material HEAD; no path outside this authorized set may change.

All four required exact-material-head workflow families must complete successfully before closure. Closure evidence must be Matrix-only and closure-head CI must independently be green before L can be used as predecessor.

Unexpected Changes: `NONE AUTHORIZED`.
