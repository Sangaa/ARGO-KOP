# MUT-2026-08-29-IGT-QUARANTINE-RESOLUTION-003

Transaction ID: `MUT-2026-08-29-IGT-QUARANTINE-RESOLUTION-003`
Lease: `R71-20260829-EXT-EVIDENCE-RESOLUTION-003`
Entry baseline: `main@78342410e9cc6c59cf238a0dc7df3118c29bc18d`
Lease-opening commit: `922da8c545df253e9a0cb48f61894deeb83fe65a`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + Room71 repository-first lease control + existing IGT evidence boundaries`
Status: `CLOSED / RESOLUTION GATE EXECUTION-VERIFIED`
Authority: `NONE`

## Objective

Implement the smallest legal downstream stage after verified untrusted external-evidence intake:

`UNTRUSTED_QUARANTINED → APPROVED TECHNICAL RE-ACQUISITION / EXACT CONTENT CORRELATION → RESOLVED_UNAUTHENTICATED`

This transaction does NOT implement or claim provider authentication, model-execution authenticity, external delivery proof, independence, authority, or cognitive effect.

## Pre-Write Evidence

The existing intake contract required a later independent-resolution or provider-backed-authentication stage and capped intake at `VERIFIED_UNTRUSTED_EXTERNAL_EVIDENCE_INTAKE / UNTRUSTED_QUARANTINED`.

The pre-existing resolver protocol exposed only participant and independence-attestation channels. Arbitrary quarantined evidence may be a delivery receipt, model-execution receipt, provider attestation, participant response, or other external evidence; routing all such evidence through `acquire_participant()` merely to reuse an interface would create a semantic falsehood.

Repository search found no implemented `RESOLVED_UNAUTHENTICATED` state before this transaction.

## Implemented Boundary

A separate generic quarantine-resolution capability was added rather than weakening the participant/attestation semantics.

### Interface

`Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py`

Added `QuarantineEvidenceResolverAdapter.acquire_external(evidence_ref)` as a generic technical re-acquisition protocol. Protocol conformance grants no authenticity or authority.

### GitHub immutable resolver

`Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py`

Added read-only generic JSON re-acquisition from immutable `github+artifact://owner/repo@FULL_SHA/path` references.

Generic external content is nested under `evidence_content`; raw keys such as `authority` or `resolver_id` are never copied into resolver control state.

Existing participant/attestation behavior remains separate.

### Governed resolution gate

`Quality/Integration/experience_spine_igt_quarantine_resolution_gate.py`

The gate itself:

1. re-verifies the sealed intake;
2. validates immutable adapter identity;
3. requires exact approved-registry identity match;
4. invokes the generic resolver itself;
5. verifies exact requested-reference binding and acquisition timestamps/surface;
6. rejects resolver/trust/authority control-field injection;
7. separates `FOUND`, `UNAVAILABLE`, and `PARTIAL`;
8. for `FOUND`, requires exact source reference, exact raw JSON value and canonical SHA-256 digest equality;
9. keeps mismatch/unavailable/partial/failure paths in quarantine;
10. stops at `RESOLVED_UNAUTHENTICATED`.

## Maximum State

Only successful exact approved-path re-acquisition may return:

`RESOLVED_UNAUTHENTICATED`

with:

- `provider_authenticity = UNVERIFIED`;
- `external_authenticity = NOT_ESTABLISHED_BY_RESOLUTION`;
- `external_delivery = NOT_PROVEN`;
- `model_execution_authenticity = NOT_PROVEN`;
- `independence = UNVERIFIED`;
- `authority = NONE`;
- `cognitive_effect = NOT_ESTABLISHED`.

Next required stage:

`PROVIDER_BACKED_AUTHENTICATION_OR_OTHER_GOVERNED_AUTHENTICITY_EVIDENCE`.

## Failure States Verified

- `INTAKE_NOT_ELIGIBLE`
- `ADAPTER_IDENTITY_REJECTED`
- `ADAPTER_NOT_APPROVED`
- `RESOLUTION_EXECUTION_FAILED`
- `RESOLUTION_UNAVAILABLE`
- `RESOLUTION_INCONCLUSIVE`
- `RESOLUTION_MISMATCH`

`UNAVAILABLE` proves only that the artifact was unavailable through that approved adapter path at that attempt. It is not evidence of global nonexistence.

## Mutation Matrix Result

| Target | Planned | Executed | Result |
|---|---|---|---|
| `Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py` | UPDATE | UPDATE | generic quarantine resolver protocol added |
| `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | UPDATE | UPDATE | generic immutable JSON re-acquisition added |
| `Quality/Integration/experience_spine_igt_quarantine_resolution_gate.py` | ADD | ADD | fail-closed governed transition implemented |
| `Quality/Integration/test_experience_spine_igt_quarantine_resolution_gate.py` | ADD | ADD | adversarial state/reference/content tests implemented |
| existing GitHub resolver test file | UPDATE | KEEP | existing contract intentionally left untouched |
| `Quality/Integration/test_github_quarantine_evidence_resolution.py` | not originally separate | ADD | dedicated tests isolate new generic contract and minimize churn |
| `Repository/IGT_QUARANTINE_RESOLUTION_CONTRACT_2026-08-29.md` | ADD | ADD | semantic contract recorded |
| this transaction | UPDATE | UPDATE | execution evidence and learning captured |
| Room 71 | UPDATE | PENDING FINAL CLOSE WRITE | lease closes after this transaction evidence is committed |

The test-file deviation is intentional: adding a dedicated generic-quarantine test module avoided unnecessary edits to the established participant/attestation resolver test contract.

## Adversarial Coverage

The new tests cover at minimum:

- exact approved re-acquisition;
- unapproved adapter non-invocation;
- registry implementation mismatch;
- invalid/promoted intake rejection before invocation;
- acquisition requested-ref mismatch;
- observed-ref mismatch;
- raw content/digest mismatch;
- JSON type distinction (`true` versus `1`) through canonical digest;
- unavailable versus mismatch semantics;
- contradictory unavailable-with-content observation;
- partial/inconclusive resolution;
- reserved trust/authority control injection;
- adapter identity mutation during execution;
- adapter exception/failure;
- non-object JSON evidence;
- immutable GitHub generic re-acquisition;
- GitHub 404 unavailable behavior;
- external control-looking fields remaining nested inside raw evidence.

## Execution Evidence

Exact functional/documented head:

`bfdfd2ee9f59965d9a1a185f584bc03940ed7e93`

Observed GitHub Actions for that exact SHA:

- `ARGO Runtime Prototype and Integration Tests` — run `33236755213` — `SUCCESS`;
- `Full-Stack Repository Audit` — run `33236755205` — `SUCCESS`;
- `M2 Multi-Channel Proposal Training` — run `33236755330` — `SUCCESS`.

Runtime workflow job evidence:

- integrity-tests = `SUCCESS`;
- prototype-tests = `SUCCESS`;
- integration-tests = `SUCCESS`.

The integration job `99058963768` executed:

`python -m pytest -q Quality/Integration`

and completed with:

`483 passed, 1 warning, 11 subtests passed in 9.85s`.

Therefore the new quarantine-resolution tests were included in the actual integration suite; this is not merely workflow-level green status.

The warning is the explicit current-tree internal identity-audit report and preserves the separate known Governance identity HOLD.

## Learning Captured

1. **Semantic channel reuse can be structurally valid yet epistemically false.** A generic quarantined artifact requires a generic acquisition contract; participant/attestation channels must not be overloaded for convenience.
2. **Raw evidence and resolver control state require structural separation.** Nesting external content under `evidence_content` prevents arbitrary external fields from laundering themselves into resolver identity, trust, or authority state.
3. **Exact technical re-acquisition is weaker than authentication.** Even immutable GitHub commit/path/blob resolution advances only to `RESOLVED_UNAUTHENTICATED`.
4. **UNAVAILABLE is path-scoped evidence.** Failure to retrieve through one approved resolver is not global evidence of absence.
5. **Canonical digest is required in addition to language-level equality.** JSON `true` and `1` can compare loosely in Python; canonical serialized digest preserves JSON-type identity.
6. **Test-contract isolation reduces regression risk.** A new semantic channel should receive dedicated tests rather than forcing unrelated existing tests to absorb a new meaning.

## Closed Point

`EXT-EVIDENCE-RESOLUTION-SUBGATE = CLOSED / EXECUTION-VERIFIED`

The broader external-evidence lifecycle remains open because provider-backed authenticity and subsequent qualification/authority stages are not established by this transaction.

## Explicit Non-Claims

- Approved resolver identity is not provider identity.
- GitHub commit/path/blob identity is not provider/model authenticity.
- Exact content re-acquisition is not external-delivery proof.
- Resolution does not authorize evidence.
- Resolution does not establish independence.
- Resolution does not prove cognitive benefit.
- Governance identity/index HOLD is unaffected by this transaction.

## Final Disposition

This bounded transaction is closed for the resolution stage only.

The next legal external-evidence question is whether a real, independently verifiable provider/source trust anchor exists. If no such anchor exists, the correct next result is an explicit authentication-readiness HOLD, not fabricated authenticity.
