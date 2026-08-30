# MUT-2026-08-30-P2-EJR-IDENTITY-STRATIFICATION-184

Date: 2026-08-30
Lease: `R71-20260830-P2-EJR-IDENTITY-STRATIFICATION-184`
Execution role: HERMUZ
Entry baseline: `main@310be157fa0dd9ede39f7c874c68a30741eafe94`
Status: `PREWRITE / LEASE ACTIVE / EJR CURRENT-STATE RECONSTRUCTION`

## Trigger

Lease 183 classified all 23 non-EJR ambiguity keys without identity mutation. The remaining raw audit population is dominated by 122 `EJR-*` keys.

Current Journal authority/evidence boundaries establish:

- `Memory/Engineering_Journal/_FOLDER_STATUS.md` remains `INTEGRITY WARNING / CONNECTED-BASELINE AUDIT` and explicitly states active canonical identity uniqueness is not globally certified.
- `Memory/Engineering_Journal/SESSION_INDEX.md` distinguishes Journal document identity from session identity and states that index/navigation evidence does not prove artifact truth.
- historical Journal records must be preserved; current repository reality controls current state.

## First proved stale-ambiguity case — EJR-013

The current Internal-ID artifact reports EJR-013 as ambiguous between:

1. `Memory/Engineering_Journal/EJR-013_2026-08-10_RUNTIME_EXECUTION_GRAPH_REVALIDATION.md`
2. `Repository/REP-020_SESSION_DELTA_2026-08-17_EJR013_CONFLICT.md`

The second path is a conflict-evidence record, not an EJR owner.

A historical conflict note states that a second Memory EJR-013 once existed at:

`Memory/Engineering_Journal/EJR-013_2026-08-10_RUNTIME_GRAPH_STATUS_RECONCILIATION.md`

Current-main absence was verified through three materially different surfaces:

- direct current-path fetch: 404;
- repository code search for `RUNTIME_GRAPH_STATUS_RECONCILIATION`: no result;
- direct current `Memory/Engineering_Journal` directory listing: path absent.

Git history then resolves the disappearance authoritatively: commit `226be7f9027bf90300a0c0888bc6d4878eece3c9` is explicitly named:

`P2: remove superseded EJR-013 duplicate after EJR-181 preservation`

The deleted artifact was originally created in commit `da23da7229739ff181e3bd79208416aef85a8fbc` with `Document ID: EJR-013`, `Canonical: No`, and `Status: Active Session Evidence / Integrity Hold`.

Therefore the historical true duplicate was explicitly dispositioned, but the retained conflict evidence still uses a structural first-H1 beginning with `EJR-013`, causing the current detector to interpret the evidence note itself as a peer EJR identity owner.

Classification:

`HISTORICAL_TRUE_DUPLICATE_RESOLVED / STALE_CONFLICT_EVIDENCE_TITLE_SHADOW`.

## Bounded objective

Reconstruct current EJR ambiguity by separating current owner conflicts from stale/historical/evidence title shadows.

At minimum classify:

1. `CURRENT_TRUE_DUPLICATE`
2. `HISTORICAL_TRUE_DUPLICATE_RESOLVED`
3. `EVIDENCE_TITLE_SHADOW`
4. `PARALLEL_JOURNAL_PATH / NAMESPACE_MIGRATION`
5. `MULTI-SESSION_ID_REUSE / CURRENT_CONFLICT`
6. `EXPLICITLY_NONCANONICAL_LINEAGE`
7. `UNRESOLVED`

## Initial population shape from exact-head artifact 9728177701

- EJR ambiguous keys: `122`
- group size distribution:
  - 104 keys have 2 paths
  - 12 keys have 3 paths
  - 3 keys have 4 paths
  - 2 keys have 5 paths
  - 1 key has 6 paths
- identity-source pattern:
  - 116 keys are entirely first-H1 fallback groups
  - 6 keys include exactly one explicit `Document ID` source plus first-H1 peers

This shape is evidence for triage only; it does not prove those 116 groups are false or true duplicates.

## Allowed paths

- `Repository/MUT-2026-08-30-P2-EJR-IDENTITY-STRATIFICATION-184.md`
- new bounded Repository EJR classification/closure evidence
- `Repository/REP-020_SESSION_DELTA_2026-08-17_EJR013_CONFLICT.md` only if a current-state evidence-title correction is proved necessary and no historical claim is erased
- `Quality/Integration/internal_document_id_audit.py` only if a generic, tested artifact-class classification improvement is proved safe
- `Quality/Integration/test_internal_document_id_audit.py` only for regressions tied to proved semantics

## Forbidden paths

- `Memory/Engineering_Journal/**` mutation
- `EJR/**` mutation
- deletion, rename, reassignment, archive move, or synthetic ID creation for any EJR record
- canonical owner mutation outside the single explicitly allowed historical conflict-evidence record
- `Repository/REP-001_*`
- `Repository/REP-002_*`
- `Repository/REP-014_*`
- `Repository/REP-016_*`
- `Governance/**`
- `Core/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- `Release/**`
- `PROJECT_STATUS.md`
- branch deletion
- force ref mutation

## C1-C6

- C1 PASS — unique Lease 184 record.
- C2 PASS — current-state reconstruction precedes any identity-owner change; EJR owners are read-only.
- C3 PASS — no canonical authority is created or promoted.
- C4 PASS — reducing a false ambiguity cannot auto-close P2 or Memory.
- C5 PASS — EJR-013 is backed by current triple-retrieval evidence plus Git history proving prior creation and explicit later removal.
- C6 PASS — Lease 183 is closed and hands off only the 122 EJR population.

## Stop conditions

HOLD if:

- two or more current EJR records still plausibly own the same identity;
- history does not prove disposition;
- a top-level `EJR/` vs `Memory/Engineering_Journal/` relationship cannot be established;
- a proposed detector rule could hide a real H1-only duplicate;
- a correction would rewrite historical content rather than clarify current evidence role.

## Learning candidates

`STATUS DRIFT MUST NOT REOPEN CLOSED REALITY.`

`A CONFLICT RECORD CAN BECOME A FALSE CONFLICT IF ITS TITLE IS PARSED AS THE IDENTITY IT DESCRIBES.`

`HISTORICAL DUPLICATE != CURRENT DUPLICATE AFTER EXPLICIT DISPOSITION.`

Initial state:

`P2_EJR_IDENTITY_STRATIFICATION_184 = IN_PROGRESS / EJR OWNERS READ-ONLY`.