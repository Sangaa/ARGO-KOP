# MUT-2026-09-04-P11-INTERFACES-GITHUB-EVIDENCE-BLOB-SHA-IDENTITY-P MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-EVIDENCE-BLOB-SHA-IDENTITY-P`

Priority: `11 — Interfaces`

Protocol: HERMUZ governed mutation; live-main reconstruction → bounded material change → immutable read-back → exact-head CI → Matrix-only closure.

Entry HEAD: `1259b1c9682d98ddf917f5ffc0eb0eb83d4885fb`

## Contract / evidence basis

`Interfaces/INTF-010_INTEGRATIONS.md` requires adapters to validate payload structure and preserve source identifiers/provenance. `Services/EVIDENCE_RESOLVER_ADAPTER_INTERFACE.py` defines this adapter as a governed acquisition boundary whose successful reacquisition does not itself establish authenticity.

At entry HEAD, `GitHubEvidenceResolverAdapter._decode_json_value()` used `str(payload.get("sha", ""))`. A boolean, integer, container, or other non-string provider value could therefore be converted into a new textual value and recorded as `github_artifact_blob_sha`, even though the provider never supplied that textual identity.

Bounded invariant:

`PROVIDER BLOB IDENTITY MUST REMAIN AN EXACT NON-BLANK STRING; TYPE COERCION MUST NOT CREATE AN IDENTITY.`

This transaction deliberately does NOT impose a 40-hex/full-Git-object format on returned blob SHA. The repair concerns representation/type integrity only; stronger syntax is not inferred without a governing contract.

## Authorized paths

1. `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py`
2. `Quality/Integration/test_github_evidence_resolver_blob_identity.py`
3. `Repository/MUT-2026-09-04-P11-INTERFACES-GITHUB-EVIDENCE-BLOB-SHA-IDENTITY-P_MUTATION_MATRIX.md`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P-001 | `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` | MODIFY | Validate returned blob identity as an exact non-blank string before provenance recording; remove coercive `str(...)` synthesis | YES | YES |
| P-002 | `Quality/Integration/test_github_evidence_resolver_blob_identity.py` | ADD | Focused tests for exact string preservation and rejection of missing, blank, boolean, numeric, and container identities | YES | YES |
| P-003 | This Matrix | ADD / KEEP | Record bounded contract, authorized paths, evidence, validation and closure state | YES | YES |

## Semantic boundaries

`IDENTIFIER TYPE VALIDITY != IDENTIFIER AUTHENTICITY.`

`REACQUISITION SUCCESS != PROVIDER AUTHENTICATION != MODEL EXECUTION VERIFICATION.`

`VALIDATE IDENTIFIER != NORMALIZE IDENTIFIER != SYNTHESIZE IDENTIFIER.`

No uniqueness, full-hex format, provider authenticity, workflow completion, or production-success claim is introduced.

## Learning capture

`A PROVIDER IDENTIFIER IS EVIDENCE, NOT A VALUE TO COERCE. TYPE COERCION CAN FABRICATE A REPRESENTATION THE PROVIDER NEVER RETURNED; VALIDATE IDENTIFIER SHAPE BEFORE RECORDING PROVENANCE.`

The learning remains transaction-scoped; no separate Governance/Learning file is created merely to prove process.

## POST-WRITE / READ-BACK

- Exact authorized-path compare: PASS — exactly 3 authorized paths; no unexpected path.
- Immutable source read-back at material HEAD: PASS.
- Immutable focused-test read-back at material HEAD: PASS.
- Immutable Matrix read-back at material HEAD: PASS.

## TESTS / EXACT-HEAD CI

Material HEAD: `be4bc79772e01fa4f4490ff46cdb44896c6860cf`

- Full-Stack Repository Audit: `33909218366` — SUCCESS
- ARGO Runtime Prototype and Integration Tests: `33909218316` — SUCCESS
- M2 Multi-Channel Proposal Training: `33909218299` — SUCCESS
- Real Mutation Matrix Regression: `33909218324` — SUCCESS

Closure HEAD: PENDING

- Full-Stack Repository Audit: PENDING
- ARGO Runtime Prototype and Integration Tests: PENDING
- M2 Multi-Channel Proposal Training: PENDING
- Real Mutation Matrix Regression: PENDING

## Unexpected Changes

NONE. Entry→material compare contained only the three authorized paths.

## State

`MATERIAL VERIFIED / CLOSURE COMMIT PENDING`
