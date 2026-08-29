# GOV-004 Legacy Placement — Mutation Matrix

Transaction ID: `MUT-2026-08-29-GOV004-LEGACY-PLACEMENT-002`
Parent transaction: `MUT-2026-08-29-CONTROL-PLANE-CONVERGENCE-001`
Base transaction branch: `argo/control-plane-convergence-20260829`
Status: `OPEN / PRE-MUTATION MATRIX ESTABLISHED`

## Verified finding

`Governance/GOV-004_TRACEABILITY_STANDARD.md` physically exists in the active Governance directory while `Governance/GOV-004_DOCUMENT_METADATA.md` is the indexed/canonical `GOV-004` owner.

The traceability file contains no explicit internal Document ID, version, canonical declaration, or ownership metadata; its filename nevertheless competes with the active `GOV-004` namespace and violates current naming/path uniqueness expectations.

Three materially different consumer/reference searches found no current repository reference to the exact legacy filename/title. This is bounded negative evidence; it does not prove the concepts in the file are unused, only that the file is not established as an active referenced authority.

## Decision

Preserve the traceability text under `Archive/Governance-Legacy/` with explicit historical/non-canonical status, then remove the misleading active Governance path. Do not merge its prose into the canonical `GOV-004` document because no evidence establishes semantic equivalence or required content transfer.

## Matrix

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| G4-01 | `Archive/Governance-Legacy/GOV-004_TRACEABILITY_STANDARD_LEGACY_2026-08-29.md` | ADD | preserve original text/provenance | N | N |
| G4-02 | `Governance/GOV-004_TRACEABILITY_STANDARD.md` | REMOVE ACTIVE PATH | eliminate misleading duplicate namespace placement | N | N |
| G4-03 | Governance status/index evidence | RECONCILE | record sole active canonical GOV-004 ownership | N | N |

## Non-claims

This mutation does not certify the entire Governance folder or repository-wide duplicate-ID audit. It resolves only the directly observed legacy active-path defect.
