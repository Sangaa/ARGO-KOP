# P4 — REL-009 Consumer Boundary Matrix

Date: 2026-08-17
Status: `EXECUTION-VERIFIED / REGISTRY-SYNCHRONIZED / CLOSURE-CANDIDATE / FINAL CI PENDING`
Authority: `GOV-013 / GOV-014 / GOV-015`

## Purpose
Protect `REL-009: RUN-010 → SRV-009` from speculative or over-broad promotion while preserving the bounded executable evidence now established and canonically synchronized.

This is a safety/evidence gate. It does not manufacture runtime evidence and does not authorize a bidirectional or universal runtime relationship claim.

## Required Reconsideration Evidence

A relationship-state reconsideration requires independent callable-consumer evidence from RUN-010 execution context to SRV-009 plus execution evidence reaching that governed dispatch boundary.

Architectural prose, shared workflow descriptions, repository-wide audit completeness, or ENG-006 → SRV-009 proof alone are insufficient.

## Gate

| Gate | Condition | Current State |
|---|---|---|
| B01 | REL-009 exists in canonical registry | VERIFIED |
| B02 | Canonical registry state matches the bounded directional disposition | VERIFIED — `REP-014` blob `d75f460d...` |
| B03 | RUN-010 distinguishes relationship description from universal runtime-path proof | VERIFIED |
| B04 | Automated safety test prevents accidental universal/executable overclaim | EXECUTION-VERIFIED |
| B05 | Boundary gate integrated into proven Full-Stack CI | VERIFIED |
| B06 | CI execution on merged P3/P4 main checkpoints | VERIFIED — `a538325b...` / `94a9bbb...` |
| B07 | Independent callable consumer source evidence | SOURCE-VERIFIED ON MAIN — pure handoff + integration-only observation seam |
| B08 | Independent execution trace proving attributable RUN-010 → SRV-009 dispatch | EXECUTION-OBSERVED / ISOLATED INTEGRATION / EXACT-MAIN CI VERIFIED |
| B09 | Negative runtime evidence gate proves inspected connected spine is simulation/trace-only at current boundary | EXECUTION-VERIFIED |
| B10 | Negative runtime evidence gate integrated into Full-Stack CI | VERIFIED |

## Historical Execution Evidence

### Boundary Gate

- Full-Stack workflow: `333498182`
- Successful run: `32046636097`
- Successful job: `95435955639`
- Verified stages:
  - P4 REL-009 consumer boundary safety gate: `SUCCESS`
  - Repository-wide audit: `SUCCESS`
  - Real runtime evidence emission: `SUCCESS`
  - Audit evidence upload: `SUCCESS`
  - Runtime evidence upload: `SUCCESS`

### Negative Runtime Evidence Gate

- Full-Stack workflow: `333498182`
- Successful run: `32047077359`
- Successful job: repository-audit
- Verified stages:
  - P4 REL-009 consumer boundary safety gate: `SUCCESS`
  - P4 negative runtime evidence gate: `SUCCESS`
  - Repository-wide audit: `SUCCESS`
  - Real runtime evidence emission: `SUCCESS`
  - Audit evidence upload: `SUCCESS`
  - Runtime evidence upload: `SUCCESS`

The inspected normal runtime seam is represented by `Runtime/Execution/connected_spine_runner.py` and `Runtime/Execution/execution_entrypoint.py`. That normal connected spine remains simulation/trace oriented and is not converted into a direct `SRV-009` dispatch path.

## Merged Current-Main Evidence — 2026-08-28

P3 clean extraction was squash-merged to main as:

`a538325bcde36d3a45f19583ca20d72d8f591e0a`

Current main contains:

1. `Runtime/Execution/run010_handoff_contract.py`
   - validates RUN-010 execution identity and trace;
   - requires successful authorization and explicit `authorization_id`;
   - builds the minimum governed production candidate;
   - performs no repository I/O and no SRV-009 dispatch itself.

2. `Quality/Integration/rel009_run010_srv009_observation.py`
   - integration-only observation harness outside protected normal Runtime/Execution consumer scope;
   - reuses the existing governed `ENG006_SRV009_PRODUCTION_ADAPTER.execute_update` path;
   - records explicit `runtime_reference=RUN-010`, `target=SRV-009`, callable boundary, execution/task/session/source-trace identity, authorization identity, downstream execution trace, dispatch status and post-read verification.

3. `Quality/Integration/test_rel009_run010_srv009_observation.py`
   - constructs an attributable RUN-010 execution record through the runtime execution entrypoint;
   - uses a controlled in-memory connector;
   - verifies successful governed dispatch and post-read;
   - verifies fail-closed behavior for missing authorization identity and blocked authorization.

Exact-main push workflows on `a538325b...`:

- Full-Stack Repository Audit `33196013636` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33196013609` — SUCCESS;
- Real Mutation Matrix Regression `33196013638` — SUCCESS;
- M2 Multi-Channel Proposal Training `33196013623` — SUCCESS.

P4 semantic reconciliation was then squash-merged to main as:

`94a9bbb43432f3e098854571130778a498f76299`

Exact-main push verification:

- Full-Stack Repository Audit `33196750118` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33196750113` — SUCCESS;
- M2 Multi-Channel Proposal Training `33196750126` — SUCCESS.

A separate provider-backed P3 E2E proved the reused ENG-006/SRV-009 adapter + GitHub connector create/update/read-back/cleanup boundary. That provider proof remains distinct from the RUN-010 integration observation and is not used to claim universal RUN-010 routing.

## Registry Synchronization — 2026-08-28

Controlled transaction:

`MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`

Workflow run `33197498585` completed successfully on the isolated transaction branch.

Verified evidence:

- mutation-builder tests: `3 passed`;
- source `REP-014` blob: `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- registry mutation commit: `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob: `d75f460d152898709044a31433e8ae4c705d9191`;
- request state: `APPLIED`;
- `verified_readback = true`.

The canonical REL-009 identity and type remain:

`RUN-010 → SRV-009 = CONSUMES`.

The synchronized state is:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

## Reconsideration Rule

B06, B07 and B08 are satisfied within the declared isolated integration scope, and B02 is now satisfied by canonical registry synchronization. Therefore the prior `REVALIDATION REQUIRED because executable evidence is absent` rationale is superseded for current operational interpretation.

The bounded disposition is now canonically synchronized. Final closure of this matrix still requires exact-head CI on the complete closure transaction so registry state, dependent guards, impact matrix and closure surfaces are proven together.

## Current Evidence Boundary

- RUN-010 explicitly treats the execution chain as a relationship description, not proof that every runtime operation follows it.
- ENG-006 → SRV-009 executable evidence does not propagate automatically into universal RUN-010 routing.
- The RUN-010 observation is deliberately isolated under `Quality/Integration`; it does not weaken the protected normal Runtime/Execution boundary.
- Provider-backed E2E and isolated RUN-010 observation are separate evidence classes.
- A directional `CONSUMES` relationship does not require a synthetic reverse dependency from SRV-009 to RUN-010 merely to satisfy symmetry.
- Canonical synchronization does not claim repository-wide graph closure or Connected-Baseline completion.

## Test Hardening Learning

The first historical CI implementation failed because the assertion searched for wording that differed from the canonical RUN-010 sentence even though the underlying evidence boundary was correct.

The final gate matches stable canonical evidence and keeps the assertion set minimal. This avoids turning harmless document-layout/wording drift into a false infrastructure failure while preserving the actual evidence boundary.

This learning remains reusable for future repository safety gates: assert stable canonical evidence, not approximate paraphrases.

## Negative Evidence Learning

A runtime trace producer is not equivalent to a downstream service invocation. Conversely, an isolated observed downstream invocation does not imply every normal runtime path invokes the service.

Both negative and positive evidence must retain their exact inspected boundary.

## Model-Independence

The gate is repository-controlled and does not depend on conversational memory or model identity.

## Next Safe Gate

`OPEN PR ON COMPLETE CLOSURE PAYLOAD → EXACT-HEAD FULL-STACK + RUNTIME/INTEGRATION CI → IF PASS, RECORD BOUNDED CLOSURE → FINAL-HEAD CI → MERGE REVIEW`.

---

End of Matrix
