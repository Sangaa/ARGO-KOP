# MUT-2026-08-29-IGT-QUARANTINE-RESOLUTION-003

Transaction ID: `MUT-2026-08-29-IGT-QUARANTINE-RESOLUTION-003`
Lease: `R71-20260829-EXT-EVIDENCE-RESOLUTION-003`
Entry baseline: `main@78342410e9cc6c59cf238a0dc7df3118c29bc18d`
Lease-opening commit: `922da8c545df253e9a0cb48f61894deeb83fe65a`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + Room71 repository-first lease control + existing IGT evidence boundaries`
Status: `ACTIVE / BOUNDED RESOLUTION ONLY`
Authority: `NONE`

## Objective

Implement the smallest legal downstream stage after verified untrusted external-evidence intake:

`UNTRUSTED_QUARANTINED → APPROVED TECHNICAL RE-ACQUISITION / EXACT CONTENT CORRELATION → RESOLVED_UNAUTHENTICATED`

This transaction SHALL NOT implement or claim provider authentication, model-execution authenticity, external delivery proof, independence, authority, or cognitive effect.

## Pre-Write Evidence

Current intake contract explicitly requires a later stage of independent resolution or provider-backed authentication and caps intake at `VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE` / `UNTRUSTED_QUARANTINED`.

Current external resolver infrastructure can correlate model-run participant and attestation evidence and can invoke an approved adapter, but its shared adapter protocol exposes only:

- `acquire_participant(evidence_ref)`;
- `acquire_attestation(evidence_ref)`.

A quarantine artifact may be a delivery receipt, model-execution receipt, provider attestation, participant response, or other external evidence. Reusing the participant channel for arbitrary quarantined evidence would create a semantic lie.

Repository search found no implemented `RESOLVED_UNAUTHENTICATED` state.

## Design Decision

Create a separate generic quarantine-resolution capability rather than weakening or overloading the established participant/attestation protocol.

The governed gate must invoke the resolver itself and must validate:

1. the quarantine intake envelope is still valid;
2. adapter identity is canonical and stable;
3. adapter identity matches an explicit approved registry record;
4. acquisition requested reference exactly equals intake `source_ref`;
5. acquisition has a non-empty identity/surface and ordered timestamps;
6. acquisition observation cannot inject resolver/trust/authority control fields;
7. `FOUND` must re-acquire the same source reference;
8. acquired raw JSON value must exactly equal intake `raw_evidence`;
9. canonical acquired-content digest must equal the sealed intake raw-evidence digest;
10. mismatch/unavailable/partial states remain fail-closed and do not advance trust;
11. adapter execution or registry approval never becomes provider authentication.

## Maximum State

Only a successful exact approved-path re-acquisition may return:

`RESOLVED_UNAUTHENTICATED`

with:

- `provider_authenticity = UNVERIFIED`;
- `external_delivery = NOT_PROVEN`;
- `model_execution_authenticity = NOT_PROVEN`;
- `independence = UNVERIFIED`;
- `authority = NONE`;
- `cognitive_effect = NOT_ESTABLISHED`.

## Failure States

At minimum:

- `INTAKE_NOT_ELIGIBLE`
- `ADAPTER_IDENTITY_REJECTED`
- `ADAPTER_NOT_APPROVED`
- `RESOLUTION_EXECUTION_FAILED`
- `RESOLUTION_UNAVAILABLE`
- `RESOLUTION_INCONCLUSIVE`
- `RESOLUTION_MISMATCH`

`UNAVAILABLE` proves only that this governed adapter path did not acquire the artifact at that attempt; it is not proof that the artifact does not exist elsewhere.

## Mutation Matrix

| Target | Action | Boundary |
|---|---|---|
| `Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py` | UPDATE | add separate generic external/quarantine resolver protocol only; do not alter participant/attestation semantics |
| `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | UPDATE | add read-only generic JSON acquisition while preserving existing channel behavior |
| `Quality/Integration/experience_spine_igt_quarantine_resolution_gate.py` | ADD | governed invocation + exact correlation + fail-closed state boundary |
| `Quality/Integration/test_experience_spine_igt_quarantine_resolution_gate.py` | ADD | adversarial resolution tests |
| `Quality/Integration/test_github_evidence_resolver_adapter.py` | UPDATE | prove generic acquisition preserves raw JSON and remains read-only |
| `Repository/IGT_QUARANTINE_RESOLUTION_CONTRACT_2026-08-29.md` | ADD | semantic contract / non-claims |
| this transaction | UPDATE | execution evidence / learning / closure |
| `Repository/ROOM071_CURRENT_STATE.json` | UPDATE | close lease only after current-head CI + read-back |

## Non-Claims

- Approved resolver identity is not provider identity.
- GitHub commit/path/blob identity is not provider/model authenticity.
- Exact content re-acquisition is not external-delivery proof.
- Resolution does not authorize the evidence.
- Resolution does not prove cognitive benefit.
