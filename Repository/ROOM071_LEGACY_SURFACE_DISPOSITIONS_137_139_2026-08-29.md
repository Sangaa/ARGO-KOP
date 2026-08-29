# ROOM71 LEGACY SURFACE DISPOSITIONS — LEASES 137–139

Date: 2026-08-29
Role: HERMUZ via Room71
Baseline: `56c8c796c7116bb4f3d8c80610b65b58d8d7c157`
Authority: bounded current-repository evidence only

## Lease 137 — Projects identity and implemented-structure disposition

Current physical `Projects/` surface is a flat set of `PROJECT-001..010` documents plus `README.md`; the current listing does not implement the README's described `Active/`, `Planned/`, and `Completed/` project directories.

The first three project-model documents also demonstrate a stable identity mismatch:
- `PROJECT-001_PROJECT_FRAMEWORK.md` internally declares `PROJ-001`;
- `PROJECT-002_PROJECT_LIFECYCLE.md` internally declares `PROJ-002`;
- `PROJECT-003_PROJECT_METADATA.md` internally declares `PROJ-003`.

The documents are thin Foundation-era project-model material and do not establish a current project-control implementation merely from their filenames or README wording.

Bounded disposition:

`PROJECTS_CURRENT_SURFACE = LEGACY_THIN_PROJECT_MODEL_MATERIAL / FLAT_PHYSICAL_STRUCTURE`

`PROJECT_FILENAME_PREFIX PROJECT != INTERNAL_ID_PREFIX PROJ = IDENTITY_RECONCILIATION_REQUIRED`

`README_ACTIVE_PLANNED_COMPLETED_TOPOLOGY = INTENDED_DESIGN / NOT_CURRENT_PHYSICAL_IMPLEMENTATION`

No rename, archive, promotion, or project-domain certification is authorized by this classification.

Lease 137 close state:

`CLOSED / BOUNDED CURRENT-AUTHORITY-AND-STRUCTURE CLASSIFICATION`

## Lease 138 — Archive ARC namespace authority disposition

Current Archive tree contains thin Foundation-era files named `ARC-001_ARCHIVE_POLICY.md` through `ARC-005_HISTORY_INDEX.md`, plus later preserved historical material under `Governance-Legacy/`.

The inspected `Archive/ARC-001_ARCHIVE_POLICY.md` contains no internal Document ID, Version, Status, Canonical declaration, or authority metadata; it is a short historical rule surface.

Current active Architecture uses the `ARC-*` namespace for Architecture artifacts. `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md` explicitly declares:
- Document ID `ARC-001`;
- Version `1.3.0`;
- Status `Validated / Integrity Hold`;
- Category `Architecture`.

Therefore Archive filenames do not acquire Architecture authority from their `ARC-*` naming alone.

Bounded disposition:

`ARCHIVE_ARC001_005 = LEGACY_THIN_ARCHIVE_FILENAME_FAMILY / ARCHITECTURE_AUTHORITY_NOT_ESTABLISHED`

`ARCHITECTURE_ARC_NAMESPACE = OWNED_BY_CURRENT_ARCHITECTURE_ARTIFACTS_WITH_VERIFIED_INTERNAL_IDS`

No deletion or rename is authorized because Archive provenance must remain recoverable and a future archive-namespace migration requires explicit consumer/provenance analysis.

Lease 138 close state:

`CLOSED / BOUNDED NAMESPACE-AUTHORITY CLASSIFICATION / NO DELETE`

## Lease 139 — Release version-dimension authority disposition

Current `Release/VERSION.md` explicitly separates two version dimensions:
- Official Release Version: `1.0.0`;
- Current Development Baseline: `3.2.1`.

It states that Foundation 1.0.0 remains the latest official release and that the 3.2.1 post-foundation repository state MUST NOT be presented as an official release without a governed release decision.

The current Release directory contains six tracked release/reference files: `VERSION.md`, `RELEASE_MANIFEST.md`, `INSTALLATION.md`, `QUICK_START.md`, `KNOWN_LIMITATIONS.md`, and `COMPATIBILITY_MATRIX.md`.

Bounded disposition:

`RELEASE_VERSION_AUTHORITY = CLEAR / VERSION_MD`

`1.0.0 = LATEST_OFFICIAL_RELEASE`

`3.2.1 = CURRENT_DEVELOPMENT_BASELINE`

`OFFICIAL_RELEASE_VERSION != DEVELOPMENT_BASELINE`

This closes the version-dimension ambiguity only. It does not certify installation usability, compatibility completeness, or authorize a new release.

Lease 139 close state:

`CLOSED / BOUNDED RELEASE-VERSION AUTHORITY CLASSIFICATION`

## Learning

1. `FILENAME TAXONOMY != IMPLEMENTED DOMAIN TOPOLOGY`.
2. A legacy prefix in Archive does not inherit the authority of the active domain currently owning that namespace.
3. `OFFICIAL RELEASE != DEVELOPMENT BASELINE`; both may legitimately coexist.
4. Semantic ambiguity can be closed without mutating thin historical artifacts when current authority evidence is sufficient.

## Non-Claims

These closures do not close Projects, Archive, Release, Architecture, or Connected Baseline globally; do not authorize deletion; and do not alter provider-authentication or cognitive-benefit holds.
