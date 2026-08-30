# P2 CANONICAL-UNINDEXED CLASSIFICATION — LEASE 185

Date: 2026-08-30
Execution role: HERMUZ / Room71
Source audit: `internal-document-id-audit-report` artifact `9728177701`
State: `CLASSIFIED / NO INDEX MUTATION / PRIORITY-2 OPEN`

## Population

The source artifact reports 15 non-deferred paths whose own metadata says `Canonical: Yes` while their exact path is absent from REP-001 active inventory:

- `Architecture/README.md`
- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md`
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `Knowledge/KNW-003_KNOWLEDGE_RELATIONSHIPS.md`
- `Knowledge/KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `Knowledge/KNW-005_KNOWLEDGE_GOVERNANCE.md`
- `Knowledge/KNW-006_KNOWLEDGE_QUALITY.md`
- `Knowledge/KNW-007_KNOWLEDGE_BASELINE.md`
- `Knowledge/KNW-008_KNOWLEDGE_TRACEABILITY.md`
- `Knowledge/KNW-009_KNOWLEDGE_EVOLUTION.md`
- `Knowledge/KNW-010_KNOWLEDGE_MAINTENANCE.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`
- `Templates/README.md`

## Governing interpretation

Self-declared `Canonical: Yes` is evidence about the artifact, not unilateral permission to enter REP-001 active inventory.

Classification must reconcile:

`SELF DECLARATION → DOMAIN STATUS → CURRENT REVIEW → INDEX/MAP ROLE → PROMOTION BOUNDARY`.

## Classification

### 1. SHOULD-BE-INDEXED — 3 paths

#### `Core/ARGO_KERNEL.md`

Current evidence:

- Document ID `CORE-KERNEL`;
- `Status: Revalidated / Integrity Hold`;
- `Canonical: Yes`;
- `Core/Core.md` includes `ARGO_KERNEL.md` in the current repository inventory;
- `Core/_FOLDER_STATUS.md` says inventory is completed for known canonical Core artifacts and the Core Index review is completed/synchronized within its bounded scope;
- REP-001/REP-002 Core lists currently omit this path.

Disposition:

`SHOULD-BE-INDEXED / DISCOVERABILITY GAP / NO CORE CERTIFICATION PROMOTION`.

#### `Core/Core.md`

Current evidence:

- Document ID `CORE-INDEX`;
- `Status: Validated for inventory / Integrity Hold`;
- `Category: Core Registry`;
- `Canonical: Yes`;
- it is explicitly the inventory index for `Core/` and was re-audited against current repository inventory;
- REP-001/REP-002 Core lists omit it.

Disposition:

`SHOULD-BE-INDEXED / CORE NAVIGATION-REGISTRY DISCOVERABILITY GAP / NO CORE CERTIFICATION PROMOTION`.

#### `Quality/QLT-001_QUALITY_ASSURANCE.md`

Current evidence:

- Document ID `QLT-001`;
- `Status: Approved`;
- `Canonical: Yes`;
- `Quality/_FOLDER_STATUS.md` explicitly identifies QLT-001 as the canonical Quality specification and the only inspected canonical QLT specification in the current status;
- semantic repair 155 is execution-verified;
- REP-001/REP-002 do not currently register a Quality active path set containing QLT-001.

Disposition:

`SHOULD-BE-INDEXED / QUALITY SPEC DISCOVERABILITY GAP / NO QUALITY GLOBAL CERTIFICATION PROMOTION`.

### 2. DECLARED-CANONICAL-BUT-DOMAIN-HOLD — 10 paths

`Knowledge/KNW-001` through `Knowledge/KNW-010`.

Current evidence:

- individual KNW files self-declare canonicality (representative KNW-001 is `Integrity Hold / Revalidated`, `Canonical: Yes`);
- `Knowledge/_FOLDER_STATUS.md` explicitly says `Canonical Validation = Pending consolidated repository-wide validation`;
- folder approval remains HOLD until synchronization and relationship validation are complete;
- current repository policy says a validated knowledge item does not automatically become platform canonical knowledge;
- existing ARGO bounded state explicitly does not promote KNW-001..010.

Disposition for all ten:

`DECLARED-CANONICAL-BUT-DOMAIN-HOLD / DO NOT INDEX AS ACTIVE CANONICAL YET`.

This is not a claim that the KNW documents are invalid. It preserves the difference between file-local canonical declaration and domain-level active canonical admission.

### 3. NAVIGATION-SURFACE / DOMAIN RE-AUDIT — 1 path

#### `Architecture/README.md`

Current evidence:

- self-declares `Document ID: ARCHITECTURE_README`, `Status: Approved`, `Canonical: Yes`;
- function is explicitly `ARCHITECTURE LAYER SPECIFICATION & DIRECTORY HANDBOOK`;
- `Architecture/_FOLDER_STATUS.md` lists README in the exact physical inventory but says REP-001 Architecture inventory is synchronized for the currently promoted set and Architecture remains under re-audit;
- REP-001/REP-002 currently list ARC_MAP, ARC-001..011 and `_FOLDER_STATUS.md`, but not README.

Disposition:

`NAVIGATION-SURFACE / CURRENTLY NOT IN PROMOTED ARCHITECTURE SET / DO NOT AUTO-INDEX`.

The self-declared canonical marker requires later content/authority review; this classification does not erase it.

### 4. NAVIGATION-SURFACE / RECONSTRUCTION-HOLD — 1 path

#### `Templates/README.md`

Current evidence:

- Document ID `TPL-README`;
- `Status: Validated / Reconstruction In Progress`;
- `Canonical: Yes`;
- purpose is directory navigation and template policy guidance;
- Templates remain an inventorying/reconstruction partition, and template presence explicitly does not create authority.

Disposition:

`NAVIGATION-SURFACE / RECONSTRUCTION-HOLD / DO NOT AUTO-INDEX`.

## Counts

- `SHOULD-BE-INDEXED = 3`
- `DECLARED-CANONICAL-BUT-DOMAIN-HOLD = 10`
- `NAVIGATION-SURFACE / DOMAIN RE-AUDIT = 1`
- `NAVIGATION-SURFACE / RECONSTRUCTION-HOLD = 1`
- `UNRESOLVED = 0` within this classification pass

## Critical finding

The source audit currently treats all 15 as one `canonical_unindexed` failure class, but repository semantics prove two different problems:

1. **true discoverability gaps** — three current reviewed/canonical paths should be represented in active index/map without promoting their whole domains;
2. **promotion-boundary mismatches** — twelve paths should not be auto-indexed merely because their local metadata says canonical.

Therefore:

`CANONICAL FIELD != ACTIVE INDEX ADMISSION`.

`CANONICAL_UNINDEXED REQUIRES AUTHORITY-AWARE CLASSIFICATION BEFORE REPAIR`.

## Protected mutation requirement

Only the three `SHOULD-BE-INDEXED` paths are candidates for REP-001/REP-002 synchronization:

- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`

Any such mutation must be a fresh protected transaction with:

- prewrite lease + Mutation Matrix;
- fresh live parent/tree;
- exact intended path changes only;
- no Knowledge/Architecture/Templates promotion;
- atomic fast-forward ref update with `force=false`;
- changed-file compare and read-back;
- exact-head CI;
- no inference of Core/Quality global closure.

## Learning

- `CANONICAL FIELD != ACTIVE INDEX ADMISSION`.
- `DOMAIN HOLD CAN OVERRIDE LOCAL PROMOTION ELIGIBILITY WITHOUT INVALIDATING THE DOCUMENT`.
- `INDEXING A CURRENT CANONICAL ARTIFACT != CERTIFYING ITS DOMAIN`.
- `NAVIGATION SURFACE CAN BE CANONICAL WITHOUT BELONGING TO THE CURRENT PROMOTED AUTHORITY SET`.

## Next legal action

Close Lease 185 as a classification subgate.

Open a protected index/map synchronization lease for exactly the three `SHOULD-BE-INDEXED` paths. Do not include the ten KNW files, Architecture README, or Templates README in that transaction.