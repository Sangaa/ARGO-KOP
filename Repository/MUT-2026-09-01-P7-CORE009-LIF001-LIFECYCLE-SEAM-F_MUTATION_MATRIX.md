# MUT-2026-09-01-P7-CORE009-LIF001-LIFECYCLE-SEAM-F — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE009-LIF001-LIFECYCLE-SEAM-F`
Protocol: `GOV-013 / GOV-014A`
Status: `PREWRITE / AUTHORIZED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `3e67f960e90f5f2c3ea56fcb73fc487de16c51e7`

## Problem definition

Current `Core/CORE-009_PLATFORM_LIFECYCLE.md` correctly describes a distinct document lifecycle, but its Relationship Model and Related Documents still identify that lifecycle as `GOV-005` / `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md`. Current repository authority establishes `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md` as the active canonical document-lifecycle artifact and explicitly records the former Lifecycle GOV-005 identity/path as retired after an identity collision with `Governance/GOV-005_REVIEW_STANDARD.md`.

This is a current Core semantic/authority-path drift and a material Priority-7 cross-layer seam.

## Prior-learning retrieval

- `GOV-013`: current repository evidence outranks historical wording; negative/identity findings require independent verification — DIRECTLY APPLICABLE.
- `GOV-014A`: Mutation Matrix must exist before protected mutation — DIRECTLY APPLICABLE.
- `LIF-001` migration note and `Lifecycle/_FOLDER_STATUS.md`: former Lifecycle GOV-005 path retired; LIF-001 is current document lifecycle — DIRECTLY APPLICABLE.
- Transaction E / EJR-179: protect semantic boundaries rather than incidental prose and do not manufacture stronger relationship types than evidence supports — TRANSFERABLE.

## Three-path verification

1. Current `CORE-009` directly names `GOV-005` and `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` for the document lifecycle.
2. Current `LIF-001` declares Document ID `LIF-001`, Canonical `Yes`, and records the former Lifecycle GOV-005 path as retired migration provenance.
3. Current `Lifecycle/_FOLDER_STATUS.md` enumerates only `LIF-001_DOCUMENT_LIFECYCLE.md` plus status, and states the retired GOV-005 active path is closed/test-enforced.

## Authorized change set

| ID | Target | Action | Expected change | Prewrite |
|---|---|---|---|---|
| F-01 | `Core/CORE-009_PLATFORM_LIFECYCLE.md` | UPDATE | replace stale document-lifecycle identity/path with current `LIF-001`; increment version minimally; preserve platform-lifecycle authority boundary | AUTHORIZED |
| F-02 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only evidence-backed bidirectional documentary references `CORE-009 → LIF-001` and `LIF-001 → CORE-009`; no dependency promotion | AUTHORIZED |
| F-03 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | refresh REP-014 version after F-02; preserve Phase-1/global holds | AUTHORIZED |
| F-04 | `Core/_FOLDER_STATUS.md` | UPDATE | record second bounded P7 seam while preserving broader cross-layer/certification hold | AUTHORIZED |
| F-05 | `Lifecycle/_FOLDER_STATUS.md` | UPDATE | record CORE-009 ↔ LIF-001 seam validation only; keep remaining consumer/cross-domain certification gaps open | AUTHORIZED |
| F-06 | `Quality/Integrity/test_core009_lif001_lifecycle_boundary.py` | CREATE | enforce current LIF-001 identity/path and non-dependency relationship boundary | AUTHORIZED |
| F-07 | `Repository/P7_CORE009_LIF001_LIFECYCLE_SEAM_2026-09-01_F.md` | CREATE | bounded evidence/progress/closure record | AUTHORIZED |
| F-08 | this Matrix | UPDATE | bind exact same-change-set mutation and later CI/closure evidence | AUTHORIZED |

## KEEP requirements

- `CORE-009` remains platform lifecycle authority only; it does not absorb document lifecycle authority.
- `LIF-001` remains document-state lifecycle authority only.
- `Governance/GOV-005_REVIEW_STANDARD.md` remains the active GOV-005 governance artifact; no identity reassignment.
- Former `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` remains retired historical provenance and is not recreated.
- Relationship type is `REFERENCES` in both directly evidenced directions, not `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, or `CONSUMES`.
- No Core certification, Phase-1 closure, repository-wide graph closure, Connected Baseline PASS, or Global integrity promotion.
- Protected changes will be committed atomically with this Matrix in the exact same Git change set.

## Pre-write decision

`PASS / AUTHORIZED FOR BOUNDED ATOMIC MUTATION`.
