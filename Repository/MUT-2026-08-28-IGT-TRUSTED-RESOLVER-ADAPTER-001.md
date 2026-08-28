# IGT Trusted Resolver Adapter Boundary — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-TRUSTED-RESOLVER-ADAPTER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@0664fb5451d2dacc7175009549ef9972d4efb0e6`
Working branch: `hermuz/igt-trusted-resolver-adapter-boundary-20260828`
Status: `SOURCE + READ-BACK + PRE-DOC-HEAD CI VERIFIED / FINAL DOC-HEAD CI REQUIRED`
Authority: `NONE`

## Entry State

External evidence correlation gate is merged and post-merge verified:
- main `0664fb5451d2dacc7175009549ef9972d4efb0e6`;
- Runtime/Integration `33207699164` — SUCCESS;
- Full-Stack `33207699158` — SUCCESS;
- M2 `33207699101` — SUCCESS.

Current bounded state:

`EXTERNAL EVIDENCE CORRELATION GATE = EXECUTION-VERIFIED`.

`PRODUCTION TRUSTED RESOLVER ADAPTER = NOT IMPLEMENTED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

## Problem

The pure correlation layer can compare package content with resolver observations but deliberately cannot prove how those observations were acquired.

The next architectural gap is an execution boundary that:
1. invokes an adapter itself rather than accepting caller-supplied observations as trusted evidence;
2. records adapter identity and acquisition context;
3. binds adapter outputs to the correlation result;
4. refuses trust-by-flag, trust-by-class-name, or trust-by-self-declared receipt;
5. still avoids overclaiming external authenticity before a real provider-backed adapter is independently validated.

Core separation:

`ADAPTER INTERFACE != APPROVED ADAPTER IDENTITY != ADAPTER EXECUTION != PROVIDER-BACKED AUTHENTICITY`.

## Design Decision

This transaction establishes a **Trusted Resolver Adapter Execution Boundary**, not a provider connector.

Maximum positive state:

`APPROVED_ADAPTER_PATH_CORRELATED`.

Explicitly forbidden state:

`EXTERNAL_AUTHENTICITY_VERIFIED`.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py` | provider-neutral protocol, immutable adapter/acquisition records, explicit failure state, no authority inference | Y | Y |
| C02 | `Quality/Integration/experience_spine_igt_trusted_adapter_gate.py` | package precondition, registry identity checks, governed adapter invocation, acquisition normalization, identity-stability checks, correlation delegation | Y | Y |
| C03 | `Quality/Integration/test_experience_spine_igt_trusted_adapter_gate.py` | 15 positive/adversarial regressions | Y | Y on pre-documentation head |
| C04 | `Repository/IGT_TRUSTED_RESOLVER_ADAPTER_CONTRACT_2026-08-28.md` | governed adapter-path contract and no-authenticity-overclaim boundary | Y | Y |
| C05 | current integration suite | exact-head discovery/execution | Y | Y on pre-documentation head; final doc-head CI required |

## D13 — Package Eligibility Must Precede External Acquisition

Pre-test review found an ordering defect in the first gate draft: adapter identity/acquisition could be reached before full local package qualification.

That would permit external side effects for invalid/quarantined evidence.

Correction:

`validate_package -> require STRUCTURALLY_QUALIFIED -> inspect adapter -> registry check -> acquire`.

Required law:

`INVALID OR QUARANTINED PACKAGE = ZERO EXTERNAL ACQUISITION CALLS`.

Regression verifies both participant and attestation call counts remain zero.

## Additional Hardened Boundaries

- Adapter identity is snapshotted before, between, and after acquisition channels; identity mutation fails closed.
- Participant and attestation acquisition IDs must be distinct.
- Acquisition start/end timestamps are parsed and ordered.
- Observation payload cannot self-inject `resolver_id`, `resolution_id`, or `requested_ref`; those are derived by the gate.
- Registry identity match checks adapter ID, kind, and implementation ID.
- Registry match proves path eligibility only.
- Adapter output mismatch remains mismatch after approved-path execution.
- Caller data flags such as `trusted=true` or `approved=true` have no authorizing effect.

## Existing Pattern Reused

`Services/REPOSITORY_CONNECTOR_INTERFACE.py` already defines explicit connector failure states and:

`NO AUTHORITY INFERENCE FROM TECHNICAL ACCESS`.

This transaction transfers the same principle to evidence acquisition:

`NO AUTHENTICITY INFERENCE FROM ADAPTER INVOCATION ALONE`.

## Read-Back / Diff Reconciliation

Compare against exact base `0664fb5451d2dacc7175009549ef9972d4efb0e6` showed:
- `behind_by = 0`;
- exactly 5 changed paths;
- all 5 paths declared in this transaction;
- no Runtime, provider-specific connector, workflow, cognition, memory, or production dispatch mutation.

## Pre-Documentation-Head CI Evidence

PR #80 was opened as Draft from exact base with head:

`b1f3dbb4fa367126b5d1cd3543ee225df0667a55`.

Required CI completed successfully:
- Runtime/Prototype/Integration workflow `33208120628` — SUCCESS;
- Full-Stack Repository Audit `33208120643` — SUCCESS.

Integration job:
- job `98974315209` — SUCCESS;
- checkout merge ref `34ee96a38b7dd3e64b7874e2358d14f81a5b38a6`;
- checkout identity logged as `Merge b1f3dbb4fa367126b5d1cd3543ee225df0667a55 into 0664fb5451d2dacc7175009549ef9972d4efb0e6`;
- command: `python -m pytest -q Quality/Integration`;
- result: `365 passed, 1 warning, 11 subtests passed`.

Current main baseline before this transaction was 350 integration tests. Therefore this transaction added and executed exactly 15 regressions:

`365 - 350 = 15`.

The existing P2 identity-scope warning remains unchanged and is not classified as an adapter-boundary defect.

Interpretation boundary:

`CI SUCCESS = ADAPTER EXECUTION BOUNDARY MECHANICS VERIFIED ON THIS HEAD`.

It does **not** mean:
- a real provider-backed resolver exists;
- registry membership authenticates an upstream provider;
- external model-run authenticity is established;
- B0/L1/L2 cognitive benefit is established.

## Exact-Head Closure Rule

This documentation update changes the branch head. Therefore `b1f3dbb4...` CI remains valid pre-documentation execution evidence but is not the final merge gate.

Required next gate:
1. exact new-head Full-Stack + Runtime/Integration CI;
2. freeze branch after success;
3. reconcile current main, PR #80, open-PR surface and exact five-path diff;
4. expected-head-SHA squash merge only;
5. post-merge exact-main verification.

## Explicit Non-Claims

- Registry membership is not cryptographic provider authentication.
- Adapter identity metadata is not upstream source authenticity by itself.
- Deterministic fake adapters verify orchestration mechanics only.
- Correlated adapter output does not populate IGT participant evidence as externally verified.
- No broad cognitive-effect or learning claim follows from this layer.

## Verification Plan

1. Implement interface + governed execution gate — PASS.
2. Add adversarial tests before provider-specific work — PASS.
3. Read back all paths and reconcile exact diff — PASS.
4. Open Draft PR from exact current main — PASS (#80).
5. Require exact-head Full-Stack + Runtime/Integration CI and inspect test count — PASS on pre-documentation head.
6. Document any discovered defect/repair — PASS; D13 recorded; no CI failure occurred after hardening.
7. Final documentation-head CI → freeze → expected-SHA squash merge → post-merge exact-main verification — PENDING.

## Closure Boundary

Current verified result:

`TRUSTED RESOLVER ADAPTER EXECUTION BOUNDARY = SOURCE + READ-BACK + PRE-DOC-HEAD EXECUTION-VERIFIED`.

while:

`REAL PROVIDER-BACKED RESOLVER ADAPTER = NOT IMPLEMENTED / NOT VERIFIED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
