# IGT Provider Authentication Trust-Anchor Readiness

Date: `2026-08-29`
Assessment State: `NOT READY / HARD TRUST-ANCHOR HOLD`
Authority: `NONE`

## Question

After `RESOLVED_UNAUTHENTICATED`, does the current repository contain a real independently verifiable trust anchor that can legally support provider/source authentication?

Current answer:

`NO VERIFIED TRUST ANCHOR FOUND IN CURRENT REPOSITORY EVIDENCE`.

This is a readiness assessment, not proof that no external provider could ever offer such an anchor.

## Evidence Surfaces Checked

Independent current-repository searches were performed for:

- provider signatures;
- JWKS / provider key-discovery material;
- explicit signature-verification implementation;
- public-key material;
- HMAC authentication;
- webhook signature verification;
- cryptographic verification libraries/patterns;
- provider-backed authentication references.

Observed results:

- `JWKS`: no repository result;
- `signature verification`: no repository result;
- `public key`: no repository result;
- `HMAC`: no repository result;
- webhook + signature: no repository result;
- `cryptography`: no repository result;
- provider-signature search returned only intake/test material preserving the fact that provider identity/signature remains unverified;
- provider-backed references describe the required future boundary rather than an implemented trust anchor.

## Historical Boundary Evidence

The earlier trusted-resolver transaction explicitly separated:

`ADAPTER INTERFACE != APPROVED ADAPTER IDENTITY != ADAPTER EXECUTION != PROVIDER-BACKED AUTHENTICITY`.

It also recorded:

- registry membership is not cryptographic provider authentication;
- adapter identity metadata is not upstream source authenticity;
- real provider-backed resolver adapter was not implemented/verified;
- external model-run authenticity remained unverified/inconclusive.

The new quarantine-resolution gate intentionally preserves the same boundary and stops at:

`RESOLVED_UNAUTHENTICATED`.

## Why Resolution Is Insufficient

A repository can prove that:

1. a specific immutable location was queried;
2. an approved local adapter executed;
3. an exact JSON value was re-acquired;
4. the acquired value matches the sealed quarantine digest/content.

Those facts still do not prove that:

- a claimed external provider created the artifact;
- the provider attested to the exact request/response;
- a model actually executed;
- a receipt was not copied/replayed from another context;
- the claimed provider identity controls the evidence-signing key or authenticated API response.

## Minimum Unblock Criteria

Provider/source authentication MUST remain blocked until one concrete provider/source path supplies all required evidence for its chosen mechanism.

At minimum the path needs:

1. **Trust-anchor identity** — a provider-controlled verification anchor whose provenance can be independently established.
2. **Verification mechanism** — e.g. provider-documented signature verification, authenticated provider API lookup, signed receipt, attestation chain, or another independently verifiable equivalent.
3. **Key/endpoint provenance** — the verifier must know why the key, JWKS endpoint, certificate, authenticated API endpoint, or equivalent belongs to the provider rather than merely being supplied inside the evidence being verified.
4. **Exact claim binding** — verification must bind provider identity to the exact request/evidence/response identifiers and relevant digest(s), not merely prove that some provider-controlled token/signature exists.
5. **Freshness/replay controls** — timestamps, nonces, request IDs, receipt IDs, sequence or provider lookup semantics sufficient for the selected mechanism.
6. **Failure semantics** — unavailable, invalid, expired, revoked, mismatched, replayed and unsupported states must remain distinct and fail closed.
7. **No self-authentication** — evidence cannot authenticate its own provider simply by containing `provider`, `trusted`, `verified`, a public key, or a claimed signature.
8. **Independent verifier execution** — ARGO must execute or observe the verification path itself rather than trust a caller-supplied `verified=true` flag.
9. **Bounded claim scope** — successful provider authentication must specify exactly what was authenticated and must not automatically establish delivery, model execution, independence, authority or cognitive benefit unless those claims have their own evidence.
10. **Adversarial tests** — wrong provider, wrong request, wrong response, stale/replayed receipt, key substitution, valid signature on wrong content, revoked/rotated key, unavailable provider endpoint and malformed evidence.

## Allowed Current State Machine

Current implemented maximum:

`UNTRUSTED_QUARANTINED → RESOLVED_UNAUTHENTICATED`

Current forbidden jump:

`RESOLVED_UNAUTHENTICATED → PROVIDER_AUTHENTICATED`

until a trust-anchor transaction satisfies the unblock criteria above.

## Readiness Decision

`PROVIDER-AUTHENTICATION-TRUST-ANCHOR-READINESS = ASSESSED / NOT READY / HARD HOLD`

This closes the ambiguity about whether the next stage may be implemented generically from current evidence: it may not.

The hold may be reopened only when a concrete provider/source mechanism and independently verifiable trust anchor are available for inspection.

## Non-Claims

- This assessment does not prove that external providers lack authentication mechanisms.
- It does not prohibit future provider-specific adapters.
- It does not treat GitHub immutable artifact identity as provider identity.
- It does not treat ARGO resolver approval as provider approval.
- It does not authenticate any current evidence.
