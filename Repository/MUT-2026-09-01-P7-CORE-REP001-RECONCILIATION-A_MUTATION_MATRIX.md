# MUT-2026-09-01-P7-CORE-REP001-RECONCILIATION-A — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-REP001-RECONCILIATION-A
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: FUNCTIONAL-CANDIDATE / CI-PENDING / REDUNDANT-MATRIX-COMMIT-RECORDED
Date: 2026-09-01
Entry HEAD: `044c40c6b36fad9ab9c059322073ff7a2e03c98b`
Initial prewrite HEAD: `101cea66257d8911a9e977883b9dd9f12df0f0a9`
Refined pre-functional HEAD: `7734b1572b6aced27401bd46378d3b70cba5a487`
Current pre-functional HEAD: `d481491c9bb287c7d5f992082e101a89d0bc8610`

## Problem / change definition
Priority 7 Core local inventory is reconciled, and REP-013 Core physical inventory was reconciled in P337. Current evidence still records a bounded REP-001 drift: `Core/CORE-000A_PLATFORM_GLOSSARY.md` is a current official/revalidated Core reference and appears in exact current Core inventory, but the REP-001 active Core list does not visibly include it. REP-002 remains a separate follow-up because it has two mapped-path gaps (`CORE-000A` and `CORE-012`).

## Prior-learning retrieval
- P336 established the exact 18-file top-level Core inventory and explicitly recorded the REP-001/REP-002 drift.
- P337 proved that large control-plane documents should be reconciled in separate bounded transactions.
- P337 HARD HOLD proved that any version change to an artifact actually listed in `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` must synchronize that manifest.
- GOV-014A requires this Matrix to exist before protected mutation.

## Evidence correction before functional write
The initial prewrite incorrectly assumed REP-001 was listed in the executable current control-plane manifest. Direct manifest read disproved that assumption: the current manifest lists REP-011, REP-012, REP-013, REP-014, REP-015, REP-016 and REP-020 only. Therefore no REP-001 manifest synchronization is required or authorized in this transaction.

A candidate manifest blob that would have added REP-001 to the manifest was created off-ref during analysis and is explicitly REJECTED. It was never committed or referenced by `main`.

## Execution discipline incident
After the refined prewrite reached green exact-head CI, the Matrix was submitted once more with content identical to the existing Matrix. GitHub created commit `d481491c9bb287c7d5f992082e101a89d0bc8610` with the same tree as parent `7734b1572b6aced27401bd46378d3b70cba5a487`. This is an unnecessary Matrix-only commit and is retained as negative execution evidence. No protected functional target or repository content changed. The functional candidate is rebuilt from `d481491c...`; no force update, history rewrite or bypass is used.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| A-01 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | Add `Core/CORE-000A_PLATFORM_GLOSSARY.md` to Core Layer, advance REP-001 version/audit metadata, and append bounded reconciliation wording without promoting Core certification | Y | candidate/read-back pending main |
| A-02 | `Quality/Integration/test_core_rep001_control_plane_reconciliation.py` | CREATE | Direct regression proving CORE-000A is indexed while legacy `CORE-000_PLATFORM_IDENTITY.md` remains outside active REP-001 inventory | Y | CI pending |
| A-03 | `Repository/P7_CORE_REP001_CONTROL_PLANE_RECONCILIATION_2026-09-01_A.md` | CREATE | Bounded progress/evidence record | Y | read-back/CI pending |
| A-04 | this Matrix | UPDATE | Same-change-set execution state and exact target accounting | Y | CI pending |

## KEEP requirements
Preserve byte/content-equivalent state outside the explicitly authorized REP-001 metadata/Core-section/reconciliation wording. KEEP unchanged: `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`, REP-002, REP-013, REP-011/014/015/016 canonical bodies, all Core authority files, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

`Core/CORE-000_PLATFORM_IDENTITY.md` is a physical provenance artifact with `Canonical: No / Legacy / Superseded` and MUST NOT be promoted into the active REP-001 Core list.

## Candidate validation
Unreferenced REP-001 candidate commit `3d517c9a05eefb303d73ebd558324fe4a734b2d1` changes REP-001 only. Its exact REP-001 patch is bounded to version/audit metadata, CORE-000A list membership, bounded discoverability wording and the P7 reconciliation note. No other REP-001 section changed.

A full functional candidate assembled over the refined state changes exactly four authorized paths: REP-001, the direct regression, the bounded progress record and this Matrix. The rejected manifest blob is excluded.

## Pre-write validation state
- Refined pre-functional exact-head CI at `7734b157...` is green: Full-Stack `33468189447`, Runtime/Integration `33468189434`, Real Mutation Matrix `33468189462`, M2 `33468189440`.
- `d481491c...` is tree-identical to `7734b157...`; it adds no content delta.
- Direct current REP-001 read confirmed CORE-000A absent before mutation.
- Direct current Core status and CORE-000A content established the bounded gap and authority state.
- Direct current manifest read confirms REP-001 is not in manifest scope.

## Functional validation required
1. Rebuild functional candidate over `d481491c...` with exactly four authorized paths.
2. Compare exact candidate diff.
3. Re-read live main immediately before ref movement and require `d481491c...`.
4. Advance `main` fast-forward only (`force=false`).
5. Re-read changed artifacts.
6. Require exact-head Full-Stack, Runtime/Integration, Real Matrix and M2 success.
7. Only then close this Matrix.

## Closure boundary
This transaction may close only the REP-001 Core inventory drift for CORE-000A. Priority 7 remains OPEN. REP-002 Core mapping drift, GOV-006 disposition, Core dependency/consumer validation, relationship reconciliation, Core certification, Phase 1, repository-wide graph and Global Connected Baseline remain OPEN / not certified.
