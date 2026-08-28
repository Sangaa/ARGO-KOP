# IGT External Evidence Resolver — Mutation Matrix

Transaction ID: `MUT-2026-08-28-IGT-EXTERNAL-EVIDENCE-RESOLVER-001`
Protocol: `GOV-013 / GOV-014 / GOV-015 + IGT + MI-IGT`
Base: `main@069c7c0b4103c745e40c6b2aa54f47816b560418`
Working branch: `hermuz/igt-external-evidence-resolver-20260828`
Status: `SOURCE IMPLEMENTED / READ-BACK + EXACT-HEAD CI PENDING / PRODUCTION TRUSTED ADAPTER NOT IMPLEMENTED`
Authority: `NONE`

## Entry State

Portable model-run evidence package gate is merged and post-merge verified:
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

A structurally qualified package carries external evidence references, but the repository lacked a governed surface for comparing those references with independently retrieved participant-execution and independence-attestation observations.

A caller-supplied dictionary or receipt must never become trusted external verification merely because its values match.

Core separation:

`PACKAGE QUALIFICATION != RESOLVER CORRELATION != RESOLVER TRUST != EXTERNAL AUTHENTICITY`.

## Critical Design Decision — No Pure-Function External Verification

This transaction deliberately provides **no code path** from deterministic correlation to `EXTERNAL_AUTHENTICITY_VERIFIED`.

Even when:
- participant observation correlates;
- attestation observation correlates;
- both resolver receipts bind exactly;

maximum positive pure-correlation state is:

`CORRELATED_AWAITING_TRUSTED_ADAPTER`.

Reason: a caller-provided receipt cannot authenticate the provenance of the resolver that allegedly produced it.

`RECEIPT BINDING != RESOLVER TRUST`.

A future connector/adapter transaction must establish trusted acquisition provenance outside package-supplied/self-declared content.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Quality/Integration/experience_spine_igt_external_resolver.py` | package eligibility; participant/attestation correlation; unavailable/partial/mismatch distinction; receipt binding; duplicate resolution/evidence fingerprint checks; no pure verification path | Y | source pending read-back |
| C02 | `Quality/Integration/test_experience_spine_igt_external_resolver.py` | adversarial + positive regressions for identity, digests, execution surface/time, attestation content, unavailable/partial, trust receipts, package eligibility and duplicate evidence | Y | source pending read-back |
| C03 | `Repository/IGT_EXTERNAL_EVIDENCE_RESOLVER_CONTRACT_2026-08-28.md` | correlation/trust contract, observation digest vs evidence fingerprint, explicit no-pure-verification boundary | Y | source pending read-back |
| C04 | current integration suite | exact-head discovery/execution | Y | CI pending |

## Correlation Surfaces

### Participant observation binds
- requested/observed evidence reference;
- run/case/condition;
- execution context;
- repository baseline;
- source model + instance;
- execution surface;
- execution start/end timestamps;
- participant payload digest;
- participant response digest.

### Attestation observation binds
- requested/observed attestation reference;
- run/context/baseline;
- attestation digest;
- exact attestation content.

The channels remain separately observable and separately classifiable.

## Resolver Event States

- `FOUND` — evidence retrieved and comparable;
- `UNAVAILABLE` — identified resolver could not retrieve the target;
- `PARTIAL` — some evidence exists but comparison is incomplete.

All states, including `UNAVAILABLE`/`PARTIAL`, require resolver ID, resolution ID and exact requested reference.

`UNAVAILABLE != MISMATCH`.

An identified negative retrieval is unresolved evidence, not direct contradiction.

## Correlation Results

- `CORRELATED` — applicable bindings match.
- `MISMATCH` — direct incompatible reference/identity/digest/content/time evidence.
- `UNAVAILABLE` — target could not be retrieved.
- `INCONCLUSIVE` — partial/ambiguous evidence.

Combined pure-correlation state can be:
- `PACKAGE_NOT_ELIGIBLE`;
- `EXTERNAL_EVIDENCE_MISMATCH`;
- `EXTERNAL_EVIDENCE_UNAVAILABLE`;
- `EXTERNAL_EVIDENCE_INCONCLUSIVE`;
- `CORRELATED_UNTRUSTED`;
- `CORRELATED_AWAITING_TRUSTED_ADAPTER`.

It cannot be `EXTERNAL_AUTHENTICITY_VERIFIED`.

## Resolver Receipt Boundary

Receipt binding checks:
- resolver ID;
- resolution ID;
- source reference;
- exact observation digest.

Result may be `RECEIPT_BOUND` or `RECEIPT_MISMATCH`, but pure code always records:

`resolver_trust = UNAUTHENTICATED_BY_PURE_CORRELATION`.

## D09 — Resolution Event Identity Is Not Evidence Identity

Pre-CI review exposed a potential evidence-laundering loophole: if duplicate detection hashed the complete observation including `resolver_id` / `resolution_id`, copying the same underlying evidence and changing only resolution metadata would generate a different digest and could look independent.

Correction introduces two separate hashes:

1. `observation_digest` — complete resolver record, used to bind a receipt to one exact resolution event;
2. `evidence_fingerprint` — same observation with `resolver_id` and `resolution_id` excluded, used to detect repeated underlying evidence.

Reusable laws:

`RESOLUTION EVENT IDENTITY != UNDERLYING EVIDENCE IDENTITY`.

`NEW RESOLUTION_ID != NEW EVIDENCE`.

`NEW RESOLVER_ID != NEW EVIDENCE` when the evidence fingerprint is unchanged.

## Additional Pre-CI Hardening

### D10 — Execution identity includes surface and time
External participant observation now binds `execution_surface`, `execution_started_at`, and `execution_completed_at`; matching run ID alone is insufficient.

### D11 — Unavailable evidence still needs resolver provenance
`UNAVAILABLE` / `PARTIAL` without resolver/resolution identity is invalid as a resolver event. Absence claims cannot arrive from an unidentified observation surface.

### D12 — Attestation content naming must reflect semantics
The observation field is `attestation_content`, not the misleading `independence_dimensions`, because the compared object includes run/context/baseline plus independence dimensions.

## Duplicate Evidence Boundary

Duplicate detection separately exposes:
- duplicate `(resolver_id, resolution_id)` events;
- duplicate complete observation digests;
- duplicate underlying evidence fingerprints.

Multiplicity never establishes independent corroboration.

## Explicit Non-Claims

- Resolver mechanics do not prove an external model run occurred.
- Matching deterministic fixtures are not external authenticity evidence.
- Matching receipts are not trusted-adapter provenance.
- External authenticity remains unverified/inconclusive until a real approved resolver adapter supplies provenance through a boundary not controlled by package content.
- No B0/L1/L2 participant row is populated by this transaction.
- Even later external authenticity does not by itself establish IGT transfer PASS, broad generalization, model-weight change, learning promotion, or governance authority.

## Verification Gates

1. Read back module, tests, contract, and matrix.
2. Compare branch to exact base; require declared-only paths.
3. Reconcile current main/open PR surface.
4. Open draft PR.
5. Require exact-head Full-Stack + Runtime/Integration CI.
6. Inspect actual checkout merge ref and integration test count.
7. Record failures/repairs rather than suppressing them.
8. Final documentation-head CI → freeze → expected-SHA squash merge → post-merge exact-main verification.

## Closure Boundary

Potential result:

`EXTERNAL EVIDENCE RESOLVER CORRELATION GATE = EXECUTION-VERIFIED`.

while:

`PRODUCTION TRUSTED RESOLVER ADAPTER = NOT IMPLEMENTED`.

`EXTERNAL MODEL-RUN AUTHENTICITY = UNVERIFIED / INCONCLUSIVE`.

`IGT PARTICIPANT EVIDENCE = UNSEEN`.

`EXPERIENCE SPINE COGNITIVE EFFECT = INCONCLUSIVE`.
