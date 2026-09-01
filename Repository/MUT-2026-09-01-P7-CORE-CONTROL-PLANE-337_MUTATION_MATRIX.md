# MUT-2026-09-01-P7-CORE-CONTROL-PLANE-337 — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-CONTROL-PLANE-337
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: FIX-FORWARD-FUNCTIONAL / CI-PENDING
Date: 2026-09-01
Entry baseline before incident: `bbcf9845415ba68446da7f88405ae7ed68c2d19b`
Verified original pre-functional HEAD: `a0a1b0c6de9c208846a24e53d5019988849cfa80`
Functional HEAD under diagnosis: `1b525f184ab688608555e43043be1402543b6d39`
Fix-forward prewrite HEAD: `a7e9ab16b5faa9a6c712916786251ea74ccc3219`

## Entry-order incident
The initial P337 Matrix was written before live-main rediscovery completed. GitHub accepted that write, so it is a real repository mutation and is not represented as compliant execution. Two additional Matrix-only commits followed while the incident was being made explicit, including one unnecessary same-content commit. Compare from the prior resume-safe P336 head `bbcf9845...` to `a0a1b0c6...` proves the net repository change across those four commits is this Matrix only. No functional/control-plane target changed.

The incident is retained as negative execution evidence. Exact-head CI on `a0a1b0c6...` was green, so the functional transaction proceeded from that verified state without rewriting history or force-updating refs.

## Prior-learning retrieval
- P293 proved abbreviated replacement of REP-013 can destroy preserved inventory detail.
- GOV-014 therefore requires complete-source segmentation/candidate preservation and zero unexpected changes.
- P336 established exact local Core inventory: 18 top-level files, with `CORE-000_PLATFORM_IDENTITY.md` physical but legacy/noncanonical, and Core certification still open.
- P336 explicitly deferred REP-001/REP-002/REP-013 control-plane reconciliation.
- Earlier current-manifest incidents established that `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` must be refreshed when a listed control-plane artifact changes identity/version/status; the executable gate is intentionally fail-closed on drift.

## Scope refinement
The original intent was to reconcile REP-001, REP-002 and REP-013 in one P337 transaction. After current source inspection, the transaction was deliberately reduced to REP-013 only because all three are large/high-risk controlled documents and splitting them materially reduces preservation risk. REP-001 and REP-002 remain open for separate governed transactions.

## Observed REP-013 defect
The pre-P337 REP-013 Core content inventory began at CORE-003 and omitted current physical members including `ARGO_KERNEL.md`, `Core.md`, both physical CORE-000 paths, `CORE-000A`, `CORE-001`, `CORE-002`, and `CORE-012`. This contradicted the exact current Core enumeration and P336 local reconciliation.

## Functional mutation already applied
Functional commit `1b525f184ab688608555e43043be1402543b6d39` applied the bounded REP-013 repair and its direct regression/progress records. Read-back confirmed the intended 18-file Core physical inventory and preserved the legacy/noncanonical CORE-000 identity boundary.

Exact-head CI on `1b525f184ab688608555e43043be1402543b6d39` produced a HARD HOLD: Full-Stack, Real Mutation Matrix, M2, Runtime prototype and Runtime integrity passed, while Runtime `integration-tests` failed in `Run integration quality suite`.

## HARD-HOLD diagnosis
The new P337 regression is consistent with current REP-013 content. Independent inspection identified the failing cross-artifact condition instead: `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` still recorded REP-013 version `1.1.2`, while P337 advanced REP-013 to `1.1.3`.

`Quality/Integration/control_plane_reconciliation_gate.py` explicitly compares each current-manifest row to the live artifact and fails closed on version mismatch. `Quality/Integration/test_control_plane_current_manifest.py` requires zero mismatches and `boundary_pass=True`. Therefore the correct fix-forward is to synchronize the non-authoritative current manifest; weakening the gate or reverting the valid REP-013 inventory repair is prohibited.

## Authorized functional change set
| Change | Target | Action | Applied | Verified |
|---|---|---|---:|---:|
| 337-01 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE exact Core physical inventory, metadata audit/version, bounded integrity wording, and append P337 reconciliation section | Y | read-back Y / final CI pending |
| 337-02 | `Quality/Integration/test_core_rep013_control_plane_reconciliation.py` | CREATE exact physical-inventory regression | Y | source/read-back Y / final CI pending |
| 337-03 | `Repository/P7_CORE_REP013_CONTROL_PLANE_RECONCILIATION_337_2026-09-01.md` | CREATE bounded P7 progress record | Y | read-back Y / final CI pending |
| 337-04 | `Repository/REP-016_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P337.md` | CREATE operational progress addendum | Y | read-back Y / final CI pending |
| 337-05 | `Repository/REP-011_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P337.md` | CREATE traceability addendum | Y | read-back Y / final CI pending |
| 337-06 | this Matrix | UPDATE in functional change set and fix-forward change set | Y | final CI pending |
| 337-07 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | FIX-FORWARD current REP-013 row from version 1.1.2 to 1.1.3 and refresh current evidence checkpoint/baseline only; preserve all semantic boundaries | Y | final CI pending |

## Fix-forward pre-write validation
Authorized fix-forward paths are exactly:
1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`;
2. this Matrix in the same functional fix-forward change set.

KEEP unchanged during fix-forward: REP-013 content, the new P337 regression, REP-001, REP-002, REP-011/014/016 canonical bodies, all Core authority documents, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1/global status, and the executable control-plane gate itself.

The manifest is evidence-only and already declares that it must be refreshed after a listed identity/version/status mutation. The fix-forward changes only its date/current checkpoint/verified source baseline and REP-013 version row; no closure boundary is promoted.

## Candidate validation history
An unreferenced Git candidate commit `b702a7386c32faa6e416bd45e2f8b09aae5f4610` was built from the complete REP-013 source. Its compare showed only intended REP-013 semantic areas plus one unintended final-newline deletion. That candidate was REJECTED. The corrected functional candidate preserved the original trailing newline before main ref movement.

## Closure boundary
P337 may close only the REP-013 Core physical control-plane inventory subgate after the fix-forward reaches exact-head green CI. Priority 7 remains OPEN. REP-001/REP-002 Core representation, GOV-006 disposition, Core dependency/consumer validation, Core certification, Phase 1 and Global Connected Baseline remain open.
