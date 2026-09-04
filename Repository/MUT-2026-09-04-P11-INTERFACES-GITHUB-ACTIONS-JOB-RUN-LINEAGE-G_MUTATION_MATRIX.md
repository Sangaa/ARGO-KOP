# P11 GITHUB ACTIONS JOB RUN LINEAGE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-RUN-LINEAGE-G`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `c33e36e98c8d063b9c094b1003873174c7c4a57a`
Material HEAD: `187526d185ca43482e9077c08cfff138c47728a3`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction F is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addressed only the lineage identity inside `list_workflow_run_jobs(run_id)`. The collection was already required to be a list of objects, but the concrete connector could still return a job object whose provider-reported `run_id` was missing, non-integer, boolean, or belonged to a different workflow run.

This is provider-response lineage validation inside the existing Actions observation boundary. It does not validate job identity itself, job-log content, dispatch behavior, provider authentication, or workflow completion.

## Material Gap

The provider-neutral Actions interface states:

`list_workflow_run_jobs(run_id) -> List jobs for an already identified workflow run.`

Live GitHub observation for the same endpoint includes `run_id` on each job object. Accepting a job whose provider-reported run lineage does not equal the requested authoritative run identity would weaken the existing interface contract.

Required invariants now enforced:

`REQUESTED RUN IDENTITY == EACH RETURNED JOB.run_id`.

`BOOLEAN != PROVIDER RUN IDENTITY`.

`EMPTY JOB COLLECTION REMAINS VALID`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-G-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require each returned job to carry the exact requested integer `run_id` | Y | Y |
| P11-G-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and boolean provider run lineage | Y | Y |
| P11-G-03 | this Matrix | CREATE/FINALIZE | bind lineage-only scope, evidence, KEEP constraints and closure | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `18 passed`.

This proves only local connector behavior against controlled responses.

## Immutable material read-back

Material HEAD: `187526d185ca43482e9077c08cfff138c47728a3`.

Expected and observed material blobs:

- `Services/GITHUB_ACTIONS_CONNECTOR.py` → `976e2df000fe45e2f9b30389d0ed7201d7aea83a`;
- `Quality/Integration/test_github_actions_connector.py` → `03a14d854c73b666e3b4443acf6b8874590e9b59`;
- this Matrix → `edc8ed8f9db59a3a379df3733d0504165f81a14a` before closure finalization.

Entry→material compare: one commit ahead, zero behind, exactly the three authorized paths above. No unexpected path changed.

## Exact material-head CI evidence

All required workflow families completed successfully on exact material HEAD `187526d185ca43482e9077c08cfff138c47728a3`:

- Real Mutation Matrix Regression — run `33878944198` — `completed / success`;
- M2 Multi-Channel Proposal Training — run `33878944076` — `completed / success`;
- ARGO Runtime Prototype and Integration Tests — run `33878944069` — `completed / success`;
- Full-Stack Repository Audit — run `33878944301` — `completed / success`.

These runs validate repository material/closure discipline at the exact material commit. They do not prove provider authentication by the ARGO connector, remote delivery initiated by that connector, or production success.

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

## Closure

Material validity, transaction validity and closure validity were evaluated separately. Material is locally verified, immutable read-back matches intended blobs, entry→material scope is exact, and all required exact-material-head workflow families are green.

This finalization commit changes only this Matrix. Its own exact-head workflow runs must also remain green before using this transaction as the next live predecessor.

Unexpected Changes: `NONE`.

Transaction G: `CLOSED / VERIFIED / RESUME-SAFE`, subject to exact closure-head CI confirmation before subsequent mutation.
