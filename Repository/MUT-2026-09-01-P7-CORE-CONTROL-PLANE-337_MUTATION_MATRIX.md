# MUT-2026-09-01-P7-CORE-CONTROL-PLANE-337 — Mutation Matrix

Transaction ID: MUT-2026-09-01-P7-CORE-CONTROL-PLANE-337
Protocol: GOV-013 / GOV-014 / GOV-014A
Status: OPEN / PREWRITE-VALIDATED / FUNCTIONAL-PENDING
Date: 2026-09-01
Entry baseline before incident: `bbcf9845415ba68446da7f88405ae7ed68c2d19b`
Current verified pre-functional HEAD: `a0a1b0c6de9c208846a24e53d5019988849cfa80`

## Entry-order incident
The initial P337 Matrix was written before live-main rediscovery completed. GitHub accepted that write, so it is a real repository mutation and is not represented as compliant execution. Two additional Matrix-only commits followed while the incident was being made explicit, including one unnecessary same-content commit. Compare from the prior resume-safe P336 head `bbcf9845...` to `a0a1b0c6...` proves the net repository change across those four commits is this Matrix only. No functional/control-plane target changed.

The incident is retained as negative execution evidence. Current exact-head CI on `a0a1b0c6...` is green, so the transaction may proceed from that verified state without rewriting history or force-updating refs.

## Prior-learning retrieval
- P293 proved abbreviated replacement of REP-013 can destroy preserved inventory detail.
- GOV-014 therefore requires complete-source segmentation/candidate preservation and zero unexpected changes.
- P336 established exact local Core inventory: 18 top-level files, with `CORE-000_PLATFORM_IDENTITY.md` physical but legacy/noncanonical, and Core certification still open.
- P336 explicitly deferred REP-001/REP-002/REP-013 control-plane reconciliation.

## Scope refinement
The original intent was to reconcile REP-001, REP-002 and REP-013 in one P337 transaction. After current source inspection, the transaction is deliberately reduced to REP-013 only because all three are large/high-risk controlled documents and splitting them materially reduces preservation risk. REP-001 and REP-002 remain open for separate governed transactions.

## Observed REP-013 defect
Current REP-013 Core content inventory begins at CORE-003 and omits current physical members including `ARGO_KERNEL.md`, `Core.md`, both physical CORE-000 paths, `CORE-000A`, `CORE-001`, `CORE-002`, and `CORE-012`. This contradicts the exact current Core enumeration and P336 local reconciliation.

## Authorized functional change set
| Change | Target | Action | Applied | Verified |
|---|---|---|---:|---:|
| 337-01 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE exact Core physical inventory, metadata audit/version, bounded integrity wording, and append P337 reconciliation section | N | N |
| 337-02 | `Quality/Integration/test_core_rep013_control_plane_reconciliation.py` | CREATE exact physical-inventory regression | N | N |
| 337-03 | `Repository/P7_CORE_REP013_CONTROL_PLANE_RECONCILIATION_337_2026-09-01.md` | CREATE bounded P7 progress record | N | N |
| 337-04 | `Repository/REP-016_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P337.md` | CREATE operational progress addendum | N | N |
| 337-05 | `Repository/REP-011_PRIORITY7_PROGRESS_ADDENDUM_2026-09-01_P337.md` | CREATE traceability addendum | N | N |
| 337-06 | this Matrix | UPDATE in same functional change set | N | N |

## KEEP requirement
Byte/content-equivalent preservation is required for every REP-013 section outside the explicitly changed metadata fields, Core section, bounded Integrity State sentence, and appended P337 reconciliation section. KEEP unchanged: REP-001, REP-002, REP-014, all Core authority documents, Governance, Architecture, Runtime, Engine, Services, Interfaces, relationship direction/type, Phase-1/global status.

## Candidate validation
An unreferenced Git candidate commit `b702a7386c32faa6e416bd45e2f8b09aae5f4610` was built from the complete REP-013 source. Its compare showed only intended REP-013 semantic areas plus one unintended final-newline deletion. That candidate is REJECTED. The final candidate must preserve the original trailing newline before any main ref movement.

Required before functional write:
1. build corrected REP-013 candidate with original final newline preserved;
2. compare corrected candidate against `a0a1b0c6...` and confirm only intended changes;
3. re-read live main and require it still equals `a0a1b0c6...`;
4. assemble all six authorized paths atomically in one commit;
5. move `main` only with `force=false`.

## Closure boundary
P337 may close only the REP-013 Core physical control-plane inventory subgate. Priority 7 remains OPEN. REP-001/REP-002 Core representation, GOV-006 disposition, Core dependency/consumer validation, Core certification, Phase 1 and Global Connected Baseline remain open.
