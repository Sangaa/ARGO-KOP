# P11 GITHUB ACTIONS JOB RUN LINEAGE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-RUN-LINEAGE-G`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / LOCAL VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `c33e36e98c8d063b9c094b1003873174c7c4a57a`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction F is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only the lineage identity inside `list_workflow_run_jobs(run_id)`. The collection is already required to be a list of objects, but the concrete connector can still return a job object whose provider-reported `run_id` is missing, non-integer, boolean, or belongs to a different workflow run.

This is provider-response lineage validation inside the existing Actions observation boundary. It does not validate job identity itself, job-log content, dispatch behavior, provider authentication, or workflow completion.

## Material Gap

The provider-neutral Actions interface states:

`list_workflow_run_jobs(run_id) -> List jobs for an already identified workflow run.`

Live GitHub observation for the same endpoint includes `run_id` on each job object. Therefore accepting a job whose provider-reported run lineage does not equal the requested authoritative run identity would weaken the existing interface contract.

Required invariants:

`REQUESTED RUN IDENTITY == EACH RETURNED JOB.run_id`.

`BOOLEAN != PROVIDER RUN IDENTITY`.

`EMPTY JOB COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-G-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require each returned job to carry the exact requested integer `run_id` | Y | Y |
| P11-G-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and boolean provider run lineage | Y | Y |
| P11-G-03 | this Matrix | CREATE | bind lineage-only scope, local evidence, KEEP constraints and exact-head hold | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `18 passed`.

This proves only local connector behavior against controlled responses.

## Provider observation

Live GitHub Actions jobs response for an exact run exposes a numeric `run_id` on each returned job and showed it equal to the requested run identity. This is structural/lineage evidence for this check only; it is not proof that ARGO's runtime connector credentials are authenticated, production-authorized, or that a remote workflow succeeded because of this connector.

## KEEP Preservation

KEEP unchanged:

- Transaction F collection-shape validation and valid empty collections;
- Transaction E exact workflow-run identity validation;
- Transaction D response-decoding and empty-response semantics;
- workflow-run filter semantics;
- workflow-job identity beyond its parent run lineage;
- job-log response semantics;
- dispatch 204 acceptance and `accepted != completed` distinction;
- provider configuration, credentials and authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, execution-completion or production-success claim is introduced.

## Post-write read-back and exact-head verification

After atomic mutation, read back all three changed paths and compare entry→material HEAD. No path outside the authorized set may change. Exact-head required workflow families must be green before closure.

`Verified=Y` means bounded source/test/local verification until exact-head CI succeeds.

## Unexpected Changes

Unexpected Changes: `NONE AUTHORIZED`.

Any workflow-run filter-result binding, job identity validation, log-content validation, Runtime change, provider configuration change, Interface contract edit, relationship edit or Governance mutation is outside this transaction.

## Closure Rule

Close only after immutable read-back and exact-head CI. Correct job-to-run lineage remains distinct from provider authentication, remote delivery, and proof that a remote workflow completed successfully.
