# P8 — GOVERNANCE EXACT INVENTORY / ALLOCATION RECONCILIATION G — MUTATION MATRIX

Transaction ID: `MUT-2026-09-03-P8-GOVERNANCE-EXACT-INVENTORY-ALLOCATION-G`
Priority: `8 — Governance`
State: `PRE-WRITE / NOT YET APPLIED`
Entry HEAD: `68d1b497f37810a2373c73b777643d436dad633a`
Protocol: GOV-014 / `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-013B / GOV-014A / GOV-015 / GOV-016 / REP-011 / REP-012 / REP-013 / REP-016`

## Legal-entry proof

- Live `main` was rediscovered at the entry HEAD and matched the last bounded REL-004 closure checkpoint.
- Priority 7 remains boundedly closed and no reopen evidence was found.
- Priority 8 remains the first open queue partition.
- Current Governance identity migration, current identified candidate review, MOD-011 semantic revalidation, REL-001/003/004/010..014 work and exact-head CI evidence remain closed within their recorded bounds.
- Room #71 has no active lease and remains coordination-only.

## Closure-blocker finding

Fresh physical enumeration found exactly 52 files under `Governance/`, including one nested support artifact. Current control-plane surfaces do not yet provide a 52/52 allocation record. They also omit:

- active canonical addendum `Governance/GOV-014A_HERMUZ_PREWRITE_MUTATION_MATRIX_GATE.md` from the active REP-001/REP-002/REP-013 Governance representation; and
- `Governance/GOV-013B_HERMUZ_TOOL_SURFACE_DECISION_BOUNDARY.md` from the explicit non-active candidate representation even though its own state is `Approved Candidate / Canonical Promotion Pending CI`.

This is a Priority-8 closure blocker because REP-013 requires reconciled physical inventory and an allocation record for every known file before bounded folder closure.

## Classification boundary

`GOV-014A` is already `Approved / Canonical Addendum`; mapping it is synchronization, not promotion.

`GOV-013B` remains a non-active candidate. Mapping it does not satisfy its promotion rule or authorize canonical promotion. Any later promotion decision is separate and may require governance/Human Authority.

`REL-011 | MOD-011 → KNW-003 | REFERENCES | Revalidation Required` is a local non-blocking hold for this transaction: it is documentary, cross-domain, non-dependency, and does not control Governance inventory/allocation closure. No endpoint or row mutation is authorized here.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P8-G-01 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | add GOV-014A to active Governance and GOV-013B to explicit non-active candidates | N | N |
| P8-G-02 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | mirror the same authority-bounded Governance mapping | N | N |
| P8-G-03 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | include GOV-013B/GOV-014A in known current-identity inventory without claiming exhaustive body completion | N | N |
| P8-G-04 | `Repository/REP-012_PRIORITY8_GOVERNANCE_ALLOCATION_ADDENDUM_2026-09-03_G.md` | CREATE | allocate and classify all 52 current Governance files | N | N |
| P8-G-05 | `Repository/REP-013_PRIORITY8_GOVERNANCE_INVENTORY_ADDENDUM_2026-09-03_G.md` | CREATE | bind exact 52-file physical inventory and bounded review dispositions to REP-013 | N | N |
| P8-G-06 | `Governance/_FOLDER_STATUS.md` | UPDATE | record exact inventory/allocation readiness while retaining content/relationship/global non-claims | N | N |
| P8-G-07 | `Quality/Integrity/test_governance_p8_inventory_allocation.py` | CREATE | enforce exact physical/allocation/classification coverage and authority boundaries | N | N |
| P8-G-08 | this Matrix | UPDATE | bind applied scope, immutable read-back and verification outcome | N | N |

## KEEP requirements

All Governance source/candidate/compatibility/support artifact bodies other than `_FOLDER_STATUS.md` are `KEEP`.

REL-011, KNW-003, MOD-011, REP-014, all P1-P7 closure claims, all P9+ states, Room #71, release/version, runtime behavior, provider-authentication state and global integrity state are `KEEP`.

No candidate promotion, archival move, deletion, relationship invention, repository-wide graph claim, Phase-1 global closure, Connected Baseline closure or Global PASS is authorized.

## Pre-write validation

- Action type: one bounded P8 inventory/allocation cohort.
- Current parent: entry HEAD above; live-main guard must be rechecked immediately before each ref move.
- Expected pre-write path count: 1 (this Matrix only).
- Expected material path count: 8 (seven targets plus finalized Matrix).
- Atomicity: GOV-014A active mapping, GOV-013B non-active classification, exact allocation/inventory evidence, folder-status readiness and regression must land together.
- Main movement: yes, fast-forward only after exact parent comparison.
- Post-write read-back must compare all eight authorized paths against this Matrix before acceptance.
- Unexpected Changes must equal `0`; any addition, deletion or modification outside the authorized set is a transaction failure.

## Closure condition

This transaction closes only when immutable read-back proves every authorized path and all required exact-head workflows pass. It establishes closure readiness prerequisites; a separate explicit Priority-8 closure review is still required.
