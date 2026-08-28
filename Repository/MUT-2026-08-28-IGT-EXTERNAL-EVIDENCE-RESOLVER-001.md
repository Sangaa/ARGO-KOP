# IGT External Evidence Resolver — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-EXTERNAL-EVIDENCE-RESOLVER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@069c7c0b4103c745e40c6b2aa54f47816b560418`
Working branch: `hermuz/igt-external-evidence-resolver-20260828`
Status: `PRE-WRITE / EXTERNAL AUTHENTICITY CORRELATION DESIGN`
Authority: `NONE`

## Entry State

The portable model-run evidence package gate is merged and post-merge verified:
- main `069c7c0b4103c745e40c6b2aa54f47816b560418`;
- Runtime/Integration `33205273818` — SUCCESS;
- Full-Stack `33205273838` — SUCCESS;
- M2 `33205273807` — SUCCESS.

Current bounded state:

`PACKAGE GATE = EXECUTION-VERIFIED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.

## Problem

A structurally qualified package now carries external evidence references, but the repository has no governed correlation surface that can compare those references with independently retrieved execution/attestation observations.

A caller-provided dictionary must not become external verification merely because its fields match.

Required separation:

`PACKAGE QUALIFICATION != RESOLVER CORRELATION != RESOLVER TRUST != EXTERNAL AUTHENTICITY`.

## Design Boundary

This transaction builds the correlation/trust gate only. It does not add a provider API connector and therefore cannot manufacture `EXTERNALLY_VERIFIED` evidence from deterministic fixtures.

A resolver observation has two independent dimensions:

1. **Correlation** — does the retrieved observation bind to the package identity, evidence reference and digests?
2. **Resolver trust** — is the observation accompanied by a trusted resolver receipt produced by an approved external adapter rather than embedded/self-declared package content?

Without both, final authenticity remains unresolved.

## Target Invariants

1. The resolver must first require a locally `STRUCTURALLY_QUALIFIED` package.
2. Participant evidence and independence-attestation evidence are resolved separately.
3. Requested reference and observed reference must match exactly.
4. Run/case/condition/context/baseline/source identity must correlate where the observation claims them.
5. Participant payload/response digests must bind the external execution observation to the package content.
6. Attestation observation must bind run/context/baseline and independence dimensions.
7. `NOT_FOUND`, `UNAVAILABLE`, or partial evidence is not `MISMATCH`; it is unresolved/inconclusive.
8. Explicit incompatible identity/digest values are `MISMATCH`.
9. Correlated observations from an untrusted/self-declared resolver remain `CORRELATED_UNTRUSTED`, not externally verified.
10. A trusted resolver receipt must bind resolver identity, resolution ID, source reference and observation digest.
11. Trust receipt mismatch invalidates the resolver event rather than the underlying package.
12. Duplicate resolver receipts or duplicate resolution identity do not create independent corroboration.
13. External verification remains bounded to the exact package/run/condition; it does not establish cognitive benefit.
14. Deterministic CI fixtures verify resolver mechanics only.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_external_resolver.py` | ADD | correlate package with participant/attestation resolver observations; preserve unavailable vs mismatch; require trusted receipt before external verification | N | N |
| C02 | `Quality/Integration/test_experience_spine_igt_external_resolver.py` | ADD | positive/adversarial regressions for correlation, mismatch, unavailable, trust receipt, digest binding, duplicate resolver identity and non-claims | N | N |
| C03 | `Repository/IGT_EXTERNAL_EVIDENCE_RESOLVER_CONTRACT_2026-08-28.md` | ADD | resolver observation/receipt contract and authenticity state transitions | N | N |
| C04 | current integration suite | VERIFY | exact-head discovery and execution | N | N |

## Resolver States

### Participant / attestation resolution
- `CORRELATED` — observation is complete and matches the package.
- `MISMATCH` — direct incompatible identity/digest evidence exists.
- `UNAVAILABLE` — resolver could not retrieve target evidence.
- `INCONCLUSIVE` — evidence is partial/ambiguous.

### Trust
- `TRUSTED_RECEIPT_VALID` — receipt is structurally bound to the observation and supplied through the trusted adapter boundary.
- `UNTRUSTED` — observation may correlate but no trusted-adapter receipt exists.
- `RECEIPT_MISMATCH` — receipt does not bind the observation/resolution event.

### Final authenticity
- `EXTERNAL_AUTHENTICITY_VERIFIED` requires both participant and attestation correlation plus valid trusted receipts for both.
- `EXTERNAL_AUTHENTICITY_MISMATCH` if direct external evidence contradicts package identity/digests.
- `EXTERNAL_AUTHENTICITY_INCONCLUSIVE` for unavailable, partial, or untrusted evidence.

## Anti-Laundering Rule

A fixture may demonstrate that correlation logic works. It may not set the trusted-adapter boundary by embedding `trusted=true` inside the package or observation.

The correlation function accepts trust as a separate adapter receipt argument and labels deterministic receipts as test evidence only. Production `EXTERNAL_AUTHENTICITY_VERIFIED` remains unavailable until a real approved resolver adapter exists.

## Explicit Non-Claims

- Resolver mechanics do not prove any external model run occurred.
- A matching fixture is not external authenticity evidence.
- A matching observation without trusted resolver provenance is not externally verified.
- External authenticity, even when later verified, is not IGT transfer PASS by itself.
- No B0/L1/L2 participant row is populated by this transaction.

## Verification Plan

1. Implement correlation/trust state machine.
2. Implement adversarial tests including exact mismatches and unavailable distinctions.
3. Read back and reconcile exact diff.
4. Open draft PR.
5. Require exact-head Full-Stack + Runtime/Integration CI and inspect test count/log evidence.
6. Record any failure/repair.
7. Final doc-head CI → freeze → expected-SHA squash merge → post-merge exact-main verification.

## Closure Boundary

Potential result:

`EXTERNAL EVIDENCE RESOLVER CORRELATION GATE = EXECUTION-VERIFIED`.

while:

`PRODUCTION TRUSTED RESOLVER ADAPTER = NOT IMPLEMENTED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
