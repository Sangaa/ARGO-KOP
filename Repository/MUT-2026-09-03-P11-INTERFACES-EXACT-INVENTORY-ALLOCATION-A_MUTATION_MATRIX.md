# P11 Interfaces — Exact Inventory and Allocation Entry — Transaction A

Transaction ID: `MUT-2026-09-03-P11-INTERFACES-EXACT-INVENTORY-ALLOCATION-A`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `da948c89208878e47a095d51d9d018592ef49c27`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-016`

## Legal entry and material gap

Current evidence-bound addenda close Priorities 1–10. Priority 11 is not already closed; REP-016 names Interfaces as the next partition and its required entry artifacts INTF-001/004/006/010 are present. `Interfaces/_FOLDER_STATUS.md` explicitly records `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER AND EXTERNAL-TRUST VALIDATION OPEN`, so a bounded local inventory/control-plane reconciliation is a valid entry action and does not require provider evidence or Human Authority.

The exact Git-tracked Interfaces tree has `12` paths and SHA-256 `81e052fe0ae6cf61f6a70b15acafa4cd07e5372ef168a1228790db314c8eaae9`. The folder status lists all 12, but REP-001, REP-002 and REP-013 list only five, while REP-012 has no one-record-per-path Interfaces allocation. This is the highest-value smallest current P11 material gap.

## Authorized material set

| ID | Target | Action | Required result |
|---|---|---|---|
| P11-A-01 | `Repository/REP-012_PRIORITY11_INTERFACES_EXACT_ALLOCATION_MANIFEST_2026-09-03_A.tsv` | CREATE | exactly one sorted allocation row per tracked Interfaces path; no authority promotion |
| P11-A-02 | `Quality/Integrity/test_interfaces_p11_exact_inventory_allocation.py` | CREATE | fail on path/count/digest/allocation/control-surface drift |
| P11-A-03 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | preserve verified active subset; point to exact physical surfaces and exclude legacy/unverified inventory from active membership; `1.11.5 → 1.11.6` |
| P11-A-04 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | exact 12-path Interfaces map and bounded identity/authority notes; `1.7.6 → 1.7.7` |
| P11-A-05 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | bind exact Interfaces allocation manifest/count/digest; version increment |
| P11-A-06 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | replace five-path partial Interfaces view with exact 12-path inventory; version increment |
| P11-A-07 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | synchronize REP-012/013 versions and P11-A checkpoint metadata; preserve listed set/statuses |
| P11-A-08 | `Interfaces/_FOLDER_STATUS.md` | UPDATE | bind exact digest/control-plane reconciliation and P11 entry; retain all external-trust/cross-layer holds |
| P11-A-09 | `Repository/REP-011_PRIORITY11_INTERFACES_ENTRY_ADDENDUM_2026-09-03_A.md` | CREATE | bounded review/entry evidence and non-claims |
| P11-A-10 | `Repository/REP-016_PRIORITY11_INTERFACES_ENTRY_ADDENDUM_2026-09-03_A.md` | CREATE | current queue interpretation: P11 entered/in progress, not closed |
| P11-A-11 | `Quality/Integration/test_core_rep001_control_plane_reconciliation.py` | UPDATE | preserve Core/index invariants; accept only governed REP-001 version `1.11.6` |
| P11-A-12 | `Quality/Integration/test_core_rep002_control_plane_reconciliation.py` | UPDATE | preserve Core/map invariants; accept only governed REP-002 version `1.7.7` |
| P11-A-13 | this Matrix | UPDATE | exact read-back/path proof/local tests/exact-head CI |

## Non-claims

- Physical inventory and allocation do not certify interface semantics, connector implementation, provider authenticity, authentication capability, permission, external evidence or production side effects.
- INTF-006 active-versus-legacy identity classification remains unchanged; no rename/archive/delete/migration is authorized.
- P11 remains OPEN after this entry transaction; cross-layer relationship and external-trust validation remain governed next work.
- Priority 10 remains closed; Phase 1, repository-wide graph, Global Connected Baseline and Global Integrity PASS remain open/unclaimed.

Validation: `pre-write → exact manifest/control-surface material → immutable read-back → parent/path proof → deterministic local suites → four-family exact-head CI → close A or HOLD / RESUME-SAFE`.

## Material read-back

- Exact authorized path set: `13`; no path outside P11-A-01 through P11-A-13.
- Git-tracked Interfaces inventory: `12`; sorted-path SHA-256 `81e052fe0ae6cf61f6a70b15acafa4cd07e5372ef168a1228790db314c8eaae9`.
- Read-back preserves INTF-006 active-versus-legacy identity, all external-trust boundaries, Priority 10 closure and P11 OPEN state.
- Targeted entry/inventory/control-plane tests: `10 passed`.
- Integrity: `190 passed`.
- Integration: `588 passed / 11 subtests passed`, with one pre-existing internal document-ID audit RuntimeWarning.
- Runtime Prototype: `23 passed`; acceptance scenarios: `3 passed`.
- `git diff --check`: PASS.
- Material HEAD: `af209b732635544c12a8ee66cd512169b9c6bfff`.
- Full-Stack Repository Audit: PASS, run `33780614716`.
- Runtime Prototype and Integration Tests: PASS, run `33780614711`.
- M2 Multi-Channel Proposal Training: PASS, run `33780614621`.
- Real Mutation Matrix Regression: PASS, run `33780614638`.
- Transaction A is `CLOSED / VERIFIED / RESUME-SAFE`; Priority 11 remains IN_PROGRESS on its cross-layer/external-trust validation scope.

## Preserved pre-material control-plane failure

The first full Integration run produced `1 failed / 587 passed / 11 subtests passed`: active-index expansion in the candidate caused the current filename-alignment guard to report `INTF-007/008/009` filenames against internal `INT-007/008/009` identities. The assertion remains a valid identity invariant; physical presence is not active authority.

Primary classification: `CONTROL_PLANE / MANIFEST DRIFT`. The repair keeps exact physical inventory in REP-002/012/013/status, restores REP-001 to the directly verified active subset, explicitly excludes legacy/unverified physical members from active indexing, and updates the deterministic P11 test to enforce that separation. The identity guard is unchanged.
