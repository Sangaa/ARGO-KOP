# IGT Trusted Resolver Adapter Boundary — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-TRUSTED-RESOLVER-ADAPTER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@0664fb5451d2dacc7175009549ef9972d4efb0e6`
Working branch: `hermuz/igt-trusted-resolver-adapter-boundary-20260828`
Status: `PRE-WRITE / TRUSTED ACQUISITION BOUNDARY DESIGN`
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

This transaction will establish a **Trusted Resolver Adapter Execution Boundary**, not a provider connector.

The boundary may prove that a registered adapter object was invoked through the governed path and that its outputs correlate with the package. It must not claim that the adapter's upstream provider is authentic merely because the adapter returned matching data.

Maximum positive state in this transaction:

`APPROVED_ADAPTER_PATH_CORRELATED`.

Explicitly forbidden state:

`EXTERNAL_AUTHENTICITY_VERIFIED`.

## Target Invariants

1. Caller cannot supply participant/attestation observations directly to the trusted-adapter gate.
2. Caller cannot create trust by passing `trusted=true`, `approved=true`, or equivalent data flags.
3. Adapter exposes immutable identity metadata separately from observation payloads.
4. Adapter ID and adapter kind must be checked against an explicit registry supplied by governance/runtime configuration.
5. Registry membership proves only approved-path eligibility, not upstream provider authenticity.
6. Adapter invocation returns participant and attestation acquisition records separately.
7. Acquisition records bind requested reference, adapter ID, acquisition ID, acquisition surface, start/end timestamps and observation payload.
8. The gate invokes the pure correlation layer after acquisition; it does not duplicate correlation semantics.
9. Adapter output mismatch remains `MISMATCH`, not trusted success.
10. Adapter exception/timeout/unavailable states remain explicit and fail closed.
11. A fake object with an approved-looking adapter ID is insufficient if it does not satisfy the governed adapter execution contract.
12. Even a contract-compliant fake used in deterministic tests proves mechanics only.
13. No deterministic test may yield `EXTERNAL_AUTHENTICITY_VERIFIED`.
14. Provider-backed verification remains a later transaction requiring real external acquisition evidence.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py` | ADD | provider-neutral adapter protocol + immutable adapter/acquisition records; no authority inference from technical access | N | N |
| C02 | `Quality/Integration/experience_spine_igt_trusted_adapter_gate.py` | ADD | registry/adapter execution gate that invokes adapter and delegates semantic comparison to existing pure correlation layer | N | N |
| C03 | `Quality/Integration/test_experience_spine_igt_trusted_adapter_gate.py` | ADD | positive/adversarial regressions for direct injection refusal, unregistered adapter, identity mismatch, acquisition failure, matching correlation and no authenticity overclaim | N | N |
| C04 | `Repository/IGT_TRUSTED_RESOLVER_ADAPTER_CONTRACT_2026-08-28.md` | ADD | governed adapter-path contract and trust boundaries | N | N |
| C05 | current integration suite | VERIFY | exact-head discovery/execution | N | N |

## Existing Pattern Reused

`Services/REPOSITORY_CONNECTOR_INTERFACE.py` already defines a provider-neutral connector contract with explicit failure states and the law:

`NO AUTHORITY INFERENCE FROM TECHNICAL ACCESS`.

`Services/GITHUB_REPOSITORY_CONNECTOR.py` also loads credentials/repository identity from runtime environment while explicitly refusing authority inference from access.

This transaction reuses that architectural principle for evidence acquisition.

## Explicit Non-Claims

- Registry membership is not cryptographic provider authentication.
- Adapter identity metadata is not upstream source authenticity by itself.
- Deterministic fake adapters verify orchestration mechanics only.
- Correlated adapter output does not populate IGT participant evidence as externally verified.
- No broad cognitive-effect or learning claim follows from this layer.

## Verification Plan

1. Implement interface + governed execution gate.
2. Add adversarial tests before provider-specific work.
3. Read back all paths and reconcile exact diff.
4. Open Draft PR from exact current main.
5. Require exact-head Full-Stack + Runtime/Integration CI and inspect test count.
6. Document any discovered defect/repair.
7. Final documentation-head CI → freeze → expected-SHA squash merge → post-merge exact-main verification.

## Closure Boundary

Potential result:

`TRUSTED RESOLVER ADAPTER EXECUTION BOUNDARY = EXECUTION-VERIFIED`.

while:

`REAL PROVIDER-BACKED RESOLVER ADAPTER = NOT IMPLEMENTED / NOT VERIFIED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
