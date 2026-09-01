# MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: FUNCTIONAL-CLOSED / CI-VERIFIED / P7-OPEN
Date: 2026-09-01
Entry HEAD: `0fc456381e623fae971c5c025df4db6d0db33452`
Initial prewrite HEAD: `6baa803aa33334029e5c37ed6f5a90ded4328537`
Refined pre-functional HEAD: `26940126ad132030123888ce013f4b5651b24acf`
Initial functional HEAD: `fa7a85d538c0e111596f277dc82bb7569dcd3bf1`
CI recovery HEAD: `f19f7af8b86c8fdddaf9ff640eecdfacba0bb2f5`

## Problem / change definition
Priority 7 Core local inventory and REP-001/REP-002/REP-013 representation are reconciled. Current `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` still declared the CORE prefix canonical parent as `Architecture/` and used `Architecture/CORE-003_CONSTITUTION.md` as its example, while current repository reality, the exact P336 Core inventory, and current consumers consistently use `Core/CORE-003_CONSTITUTION.md`.

The stale Architecture parent originated in the historical GOV-006 canonicalization line and was not supported by current repository paths. This was factual naming/path drift, not evidence that the Core layer should move.

## Prior-learning retrieval
- P336 explicitly recorded the GOV-006 Core parent/example mismatch as a remaining Priority 7 gap.
- P337 and the subsequent REP-001 / REP-002 transactions established the actual current Core representation under `Core/`.
- Exact repository search for `Architecture/CORE-003_CONSTITUTION.md` recovered GOV-006 historical/current text, while independent search for `Core/CORE-003_CONSTITUTION.md` recovered multiple current consumers across Runtime, AI, Architecture and Core.
- Historical commit `1fa61fc58309122e14781a5fd391213b1cd74ecb` showed the stale Architecture example was preserved into GOV-006 during 2026-08-08 canonicalization rather than proven by current Core structure.
- After the initial CI failure, prior-learning retrieval recovered `Memory/Engineering_Journal/EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md` as DIRECTLY APPLICABLE. Its durable rule requires integrity assertions to target the semantic authority boundary rather than treating historical explanatory text as active metadata.
- GOV-014A required this Matrix before protected mutation.

## Authority boundary
This transaction repairs repository-fact alignment only. It MUST NOT promote GOV-006 from `Proposed / Audit-Derived Update` to Approved, expand its authority, or reinterpret references to GOV-006 as independent proof of active governance authority. Status/authority disposition remains a separate governance decision.

## Scope refinement before functional write
The initial Matrix included `Core/_FOLDER_STATUS.md` as a same-transaction synchronization target. Before any protected functional target was changed, the transaction was reduced further: the Core status record is a separate large evidence surface and is not required to repair the GOV-006 factual defect itself. It is therefore KEEP-unchanged here and may be reconciled in a later bounded transaction after this factual repair is execution-verified.

## Authorized functional change set
| Change | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| C-01 | `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` | UPDATE | Change active CORE canonical parent/example from `Architecture/` to `Core/`; advance bounded version/audit metadata; add explicit repository-reality reconciliation note; preserve status/authority | Y | Y |
| C-02 | `Quality/Integration/test_gov006_core_parent_reconciliation.py` | CREATE + REPAIR | Regression proving the active CORE authority row uses `Core/`, the stale Architecture authority row is absent, historical explanatory provenance remains permitted, and status remains Proposed | Y | Y |
| C-03 | `Repository/P7_GOV006_CORE_PARENT_RECONCILIATION_2026-09-01_C.md` | CREATE + CLOSEOUT UPDATE | Bounded progress/evidence and CI-recovery record | Y | Y |
| C-04 | this Matrix | UPDATE | Execution, failure-recovery and closure accounting | Y | Y |

## KEEP requirements
KEEP unchanged: `Core/_FOLDER_STATUS.md`, REP-001, REP-002, REP-013, REP-011/014/015/016 canonical bodies, REP-020 current manifest, all Core authority documents, Architecture authority files, Runtime/Engine/Services/Interfaces code and authority, relationship direction/type, Phase-1 status, Connected-Baseline status and global integrity claims.

Preserve GOV-006 `Document ID`, `Canonical: Yes`, `Priority`, legacy namespace boundary, canonical identity rules, canonicalization history, and current `Status: Proposed / Audit-Derived Update` unless a separate governed promotion transaction explicitly changes authority.

## Functional execution and CI failure boundary
Initial functional HEAD `fa7a85d538c0e111596f277dc82bb7569dcd3bf1` correctly repaired the GOV-006 active CORE row and added a direct integration regression, but exact-head Runtime run `33469880999` failed in job `integration-tests`, step `Run integration quality suite`.

The first meaningful failure was contained in `test_gov006_core_parent_matches_current_repository_reality`: the regression required the literal string `Architecture/CORE-003_CONSTITUTION.md` to be absent from the entire document while the same functional change intentionally preserved that literal inside the historical reconciliation narrative.

Classification: `TEST DEFECT / SEMANTIC AUTHORITY BOUNDARY TOO BROAD`.

The GOV-006 factual repair itself was not reverted. The test was narrowed to the active table row boundary and a separate assertion explicitly preserves historical explanatory provenance.

## CI recovery validation
Recovery commit: `f19f7af8b86c8fdddaf9ff640eecdfacba0bb2f5`.

Exact-head evidence:
- ARGO Runtime Prototype and Integration Tests `33475437864`: SUCCESS.
- Full-Stack Repository Audit `33475437728`: SUCCESS.
- M2 Multi-Channel Proposal Training `33475437912`: SUCCESS.
- Runtime workflow jobs include prototype, integrity and integration success after the semantic-boundary correction.

The changed regression was re-read after mutation and matches the directly applicable EJR-179 rule. No novel learning rule is promoted because the required durable control already exists.

## Closure result
The bounded GOV-006 Core parent/example factual mismatch is CLOSED and CI-VERIFIED.

Priority 7 remains OPEN. This closure does not certify Core globally and does not close material dependency/consumer validation, `Core/_FOLDER_STATUS.md` synchronization, REP-014 relationship reconciliation, GOV-006 authority/promotion disposition, explicit Core certification, Phase 1, repository-wide graph validation or Global Connected Baseline.

## Next legal boundary
Select the next Priority 7 action only from current live-main evidence after this closure commit is revalidated. The known deferred candidate `Core/_FOLDER_STATUS.md` synchronization must not be assumed to be next until current Priority 7 evidence confirms it is the highest-value legal gap.
