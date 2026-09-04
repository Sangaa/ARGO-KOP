# MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-LOG-EVIDENCE-O MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-LOG-EVIDENCE-O`

Priority: `11 — Interfaces`

Protocol: HERMUZ governed mutation; live-main reconstruction → bounded material change → immutable read-back → exact-head CI → Matrix-only closure.

Entry HEAD: `ec5c961be59def1d55357b9de5570b70aefe1107`

## Contract / evidence basis

`Interfaces/INTF-010_INTEGRATIONS.md` requires adapters to preserve provenance and enough original context for later verification, states that normalization MUST NOT destroy material source distinctions, and requires the original representation or sufficient provenance to remain available when normalization is lossy.

At entry HEAD, `Services/GITHUB_ACTIONS_CONNECTOR.py::get_workflow_job_logs()` decoded provider bytes with `decode("utf-8", errors="replace")`. Invalid UTF-8 could therefore be silently rewritten into Unicode replacement characters and returned as if it were provider log text.

Bounded invariant:

`JOB-LOG BYTES MUST NOT BE SILENTLY REWRITTEN INTO LOSSY TEXT.`

For this existing `str`-returning interface:
- valid UTF-8 is decoded exactly;
- invalid UTF-8 fails explicitly with `GITHUB_ACTIONS_RESPONSE_ENCODING_INVALID: GET jobs/{job_id}/logs`;
- no bytes-returning API is introduced;
- HTTP error-body diagnostics are outside this transaction because they are failure diagnostics, not successful job-log evidence;
- encoding validity does not establish provider authenticity, workflow completion, remote delivery, or production success.

## Authorized paths

1. `Services/GITHUB_ACTIONS_CONNECTOR.py`
2. `Quality/Integration/test_github_actions_connector_job_log_evidence.py`
3. `Repository/MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-JOB-LOG-EVIDENCE-O_MUTATION_MATRIX.md`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| O-001 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | MODIFY | Replace lossy successful job-log UTF-8 decoding with strict decoding and explicit encoding failure | YES | YES |
| O-002 | `Quality/Integration/test_github_actions_connector_job_log_evidence.py` | ADD | Focused tests for exact valid UTF-8 preservation, invalid UTF-8 fail-closed behavior, and failure classification | YES | YES |
| O-003 | This Matrix | ADD / KEEP | Record bounded contract, authorized paths, evidence, validation and closure state | YES | YES |

## Semantic boundaries

`TEXT DECODING SUCCESS != PROVIDER AUTHENTICITY.`

`ENCODING FAILURE != TRANSPORT FAILURE != WORKFLOW FAILURE.`

`PROVIDER LOG EVIDENCE != WORKFLOW COMPLETION != PRODUCTION SUCCESS.`

The transaction does not alter job identity, run lineage, workflow filters, dispatch semantics, authentication, pagination, or HTTP error-body decoding.

## Learning capture

`WHEN AN INTERFACE MUST MAP PROVIDER BYTES INTO TEXT, SILENT REPLACEMENT IS AN EVIDENCE MUTATION. PRESERVE THE REPRESENTATION EXACTLY OR FAIL EXPLICITLY; DO NOT SUBSTITUTE LOSSY TEXT AND CALL IT PROVIDER EVIDENCE.`

This is captured here as transaction-scoped reusable learning; no separate Governance/Learning artifact is created merely to prove process.

## POST-WRITE / READ-BACK

- Exact authorized-path compare: PASS — exactly 3 authorized paths; no unexpected path.
- Immutable source read-back at material HEAD: PASS.
- Immutable focused-test read-back at material HEAD: PASS.
- Immutable Matrix read-back at material HEAD: PASS.

## TESTS / EXACT-HEAD CI

Material HEAD: `0608c4babf2251df201a36a506421bec336b41e6`

- Full-Stack Repository Audit: `33908367149` — SUCCESS
- ARGO Runtime Prototype and Integration Tests: `33908367111` — SUCCESS
- M2 Multi-Channel Proposal Training: `33908367071` — SUCCESS
- Real Mutation Matrix Regression: `33908367100` — SUCCESS

Closure HEAD: PENDING

- Full-Stack Repository Audit: PENDING
- ARGO Runtime Prototype and Integration Tests: PENDING
- M2 Multi-Channel Proposal Training: PENDING
- Real Mutation Matrix Regression: PENDING

## Unexpected Changes

NONE. Entry→material compare contained only the three authorized paths.

## State

`MATERIAL VERIFIED / CLOSURE COMMIT PENDING`
