# MUT-2026-08-29 — GOV-004 LEGACY ACTIVE-PLACEMENT RETIREMENT — 012

State: CLOSED / EXECUTION-VERIFIED
Lease: R71-20260829-GOV-CONTENT-012
Baseline: 13c1fbcde94c71cb8ac9d787a2c5f4ef7d375514
Functional SHA: 1ba17f1fddae4ca7107ddbee7f1350b56f61ee42
Scope: Governance active-namespace semantic/placement repair

## Finding

Two physical GOV-004-looking surfaces existed under active Governance:

- canonical `Governance/GOV-004_DOCUMENT_METADATA.md` — internal `Document ID: GOV-004`, `Canonical: Yes`;
- legacy `Governance/GOV-004_TRACEABILITY_STANDARD.md` — no internal Document ID/version/canonical declaration, but a filename that could falsely imply active GOV-004 authority.

The document-ID audit correctly did not treat the legacy text as a second internal Document ID, but that did not eliminate the placement/semantic-authority risk created by its active filename and folder.

## Consumer search

Three materially different current repository searches were used: exact path, filename identity, and distinctive source phrase. No consumer/reference result was returned. Direct current-path retrieval independently confirmed the file existed before retirement. The bounded claim remains: no discoverable current consumer was established by those searches.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| GCS-012-01 | `Governance/GOV-004_TRACEABILITY_STANDARD.md` | RETIRE FROM ACTIVE NAMESPACE | path absent from active Governance | Y | Y |
| GCS-012-02 | `Archive/Governance-Legacy/GOV-004_TRACEABILITY_STANDARD_LEGACY_2026-08-29.md` | CREATE | preserved source + historical/non-canonical disposition | Y | Y |
| GCS-012-03 | this transaction | CREATE | evidence, bounds, verification and learning | Y | Y |

## Exact-head verification

At `1ba17f1fddae4ca7107ddbee7f1350b56f61ee42`:
- M2 Multi-Channel Proposal Training run `33240071820` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests run `33240071802` — SUCCESS.
- Full-Stack Repository Audit run `33240071837` — SUCCESS.

## KEEP REQUIREMENT

- Canonical `Governance/GOV-004_DOCUMENT_METADATA.md` remained unchanged.
- Legacy source content remains recoverable in Archive and Git history.
- No new traceability authority was created.
- Governance content-semantic review remains open beyond this bounded repair.

## Continuous-improvement learning

Identity audits that rely on internal Document IDs can miss authority ambiguity created by filenames and active-folder placement. A robust content/authority review therefore needs both **declared identity** and **implied active identity/placement** checks.

## Non-claims

- No repository-wide identity closure is inferred.
- No archived legacy text is promoted.
- No claim is made that every possible non-search-indexed consumer is absent.

## Closure

`GOV004_LEGACY_ACTIVE_PLACEMENT = CLOSED / ARCHIVED / EXECUTION-VERIFIED`.
