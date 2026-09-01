# MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: PREWRITE / OPEN
Date: 2026-09-01
Entry HEAD: `0fc456381e623fae971c5c025df4db6d0db33452`

## Problem / change definition
Priority 7 Core local inventory and REP-001/REP-002/REP-013 representation are reconciled. Current `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` still declares the CORE prefix canonical parent as `Architecture/` and uses `Architecture/CORE-003_CONSTITUTION.md` as its example, while current repository reality, the exact P336 Core inventory, and current consumers consistently use `Core/CORE-003_CONSTITUTION.md`.

The stale Architecture parent originates in the historical GOV-006 canonicalization line and is not supported by current repository paths. This is a factual naming/path drift, not evidence that the Core layer should move.

## Prior-learning retrieval
- P336 explicitly recorded the GOV-006 Core parent/example mismatch as a remaining Priority 7 gap.
- P337 and the subsequent REP-001 / REP-002 transactions established the actual current Core representation under `Core/`.
- Exact repository search for `Architecture/CORE-003_CONSTITUTION.md` recovers only GOV-006 itself, while independent search for `Core/CORE-003_CONSTITUTION.md` recovers multiple current consumers across Runtime, AI, Architecture and Core.
- Historical commit `1fa61fc58309122e14781a5fd391213b1cd74ecb` shows the stale Architecture example was preserved into GOV-006 during 2026-08-08 canonicalization rather than proven by current Core structure.
- GOV-014A requires this Matrix before protected mutation.

## Authority boundary
This transaction repairs repository-fact alignment only. It MUST NOT promote GOV-006 from `Proposed / Audit-Derived Update` to Approved, expand its authority, or reinterpret references to GOV-006 as independent proof of active governance authority. Status/authority disposition remains a separate governance decision.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| C-01 | `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` | UPDATE | Change CORE canonical parent/example from `Architecture/` to `Core/`; advance bounded version/audit metadata; add explicit repository-reality reconciliation note; preserve status/authority | N | N |
| C-02 | `Quality/Integration/test_gov006_core_parent_reconciliation.py` | CREATE | Regression proving CORE parent/example use `Core/` and the stale Architecture CORE-003 example is absent; verify status remains Proposed | N | N |
| C-03 | `Repository/P7_GOV006_CORE_PARENT_RECONCILIATION_2026-09-01_C.md` | CREATE | Bounded progress/evidence record | N | N |
| C-04 | `Core/_FOLDER_STATUS.md` | UPDATE | Record GOV-006 path-disposition closure while keeping dependency/consumer, relationship and certification gates open | N | N |
| C-05 | this Matrix | UPDATE | Same-change-set execution state and exact target accounting | N | N |

## KEEP requirements
KEEP unchanged: REP-001, REP-002, REP-013, REP-011/014/015/016 canonical bodies, REP-020 current manifest, all Core authority documents, Architecture authority files, Runtime/Engine/Services/Interfaces code and authority, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

Preserve GOV-006 `Document ID`, `Canonical: Yes`, `Priority`, legacy namespace boundary, canonical identity rules, canonicalization history, and current `Status: Proposed / Audit-Derived Update` unless a separate governed promotion transaction explicitly changes authority.

## Pre-write validation
- Live main rediscovered at `0fc456381e623fae971c5c025df4db6d0db33452` immediately before this Matrix.
- Closure-head Runtime run `33469303593` completed SUCCESS with integration, integrity and prototype jobs all successful.
- Direct GOV-006 read confirms current stale CORE parent/example.
- Independent exact-path searches establish `Architecture/CORE-003_CONSTITUTION.md` only in GOV-006 and widespread current use of `Core/CORE-003_CONSTITUTION.md`.
- P336 Core status explicitly lists GOV-006 disposition as an open Priority 7 gate.
- `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` directly lists REP-011/012/013/014/015/016/020 only; GOV-006 and Core status are not manifest rows, so no manifest expansion or version synchronization is authorized.

## Functional validation required
1. Build full-content candidates from the exact current GOV-006 and Core status sources.
2. Compare exact candidate diff before ref movement.
3. Require exactly five authorized functional paths.
4. Re-read live main immediately before ref movement.
5. Fast-forward only (`force=false`).
6. Re-read changed artifacts.
7. Require relevant exact-head CI including Full-Stack, Runtime/Integration, Real Matrix, M2, GOV-014 and any triggered identity/quality gates.
8. Close this Matrix only after green CI.

## Closure boundary
This transaction may close only the GOV-006 factual Core parent/example mismatch and synchronize the Core status record for that bounded fact. Priority 7 remains OPEN. Core material dependency/consumer validation, relationship-registry reconciliation, GOV-006 authority/promotion disposition, explicit Core certification, Phase 1, repository-wide graph and Global Connected Baseline remain OPEN / not certified.
