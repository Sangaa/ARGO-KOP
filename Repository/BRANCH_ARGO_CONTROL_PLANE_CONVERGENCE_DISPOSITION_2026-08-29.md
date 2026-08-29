# BRANCH DISPOSITION — argo/control-plane-convergence-20260829

Date: 2026-08-29  
Room: 71  
Lease: `R71-20260829-BRANCH-HYGIENE-022`  
Role: HERMUZ / evidence-backed branch classification  
Baseline observed: `main@52f721bead18fa449ac95bae9c5cc98c2873455f`  
Branch tip observed: `564f7924c431afbd6271054d9e1d214e58c3a5fd`  
Merge base: `28e3ec16f1b0e6decee6623f77f48cda74e229c7`

## Classification

`HISTORICAL_CONTROL_PLANE_CONVERGENCE_EVIDENCE / FUNCTIONAL_RESULTS_SUBSEQUENTLY_RECONCILED_ON_MAIN / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Evidence

The branch diverges from current main and contains a 21-commit convergence transaction rooted at the earlier IGT intake baseline. Its changed surfaces include Governance identity migration, control-plane reconciliation, P6 scope handling, REP-001/REP-002 synchronization, REP-016, and the current REP-020 control-plane manifest.

Current main independently contains the later reconciled outcomes for those workstreams, including:

- Governance identity migration and REP-001/REP-002 synchronization closure;
- GOV-004 legacy placement retirement;
- P6 EJR scope closure;
- current control-plane manifest freshness closure;
- REP-016 status freshness closure;
- subsequent P6 control-surface correlation repairs.

A direct semantic spot-check of the branch tip's final REP-016 change shows it restores the Purpose boundary to `REP-011 through REP-015`; current main already contains that same corrected boundary. The branch manifest also records an older REP-016 version `1.4.0` and an earlier working transaction, while current main deliberately retains the later verified `REP-016 v1.3.0` content-preserving state and a refreshed current manifest. Therefore the branch must not overwrite current main merely because it contains an earlier convergence history.

## Decision

- Merge: `NO` — no unresolved functional delta has been established that justifies replaying the stale branch transaction onto current main.
- Promotion: `NO` — historical branch state is not current authority.
- Evidence preservation: `YES` — retain branch/history as reconstruction evidence.
- Delete branch: `NOT AUTHORIZED` — classification does not imply deletion safety.

## Learning

A branch can contain valid historical convergence work while its final files are no longer the correct current authority. Branch hygiene must compare semantic outcomes and chronology, not commit count or apparent completeness. A later mainline can absorb, refine, or intentionally reverse version/status choices while preserving the useful functional result.

## Non-claims

This classification does not prove that every branch-only commit is byte-for-byte present on main. It proves only that no current merge requirement was established for the inspected control-plane convergence transaction and that replaying it would risk reintroducing stale control-plane state.

## Result

`ARGO_CONTROL_PLANE_CONVERGENCE_BRANCH = CLOSED_CLASSIFIED_HISTORICAL_EVIDENCE_FUNCTIONALLY_RECONCILED_NO_MERGE_NO_DELETE`
