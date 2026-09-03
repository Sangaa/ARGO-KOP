# P10 Runtime — Exact Physical Inventory and Allocation — Transaction N

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-EXACT-INVENTORY-ALLOCATION-N`
Priority: `10 — Runtime`
State: `PRE-WRITE / AUTHORIZED / MATERIAL CHANGE PENDING`
Entry HEAD: `d197a35c9ab7872235f57ceb80d710d699d51a3b`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-011 / REP-012 / REP-013 / REP-016 / Transaction M`

## Verified gap and method

Current Git tracks exactly `118` Runtime paths. Existing REP-013 Runtime content is explicitly non-exhaustive, while REP-012 allocates only an earlier candidate cohort. This violates REP-012's folder completion rule that physical inventory be reconciled and every known file have an allocation record.

The bounded repair will use one exact allocation manifest rather than duplicate 118 narrative rows across multiple control surfaces. Exactness is bound by the canonical sorted `git ls-files Runtime` digest `a5db51a6d6cbf7dbf22bdb971fc0d2238d2bdef6627caadc4ee2b1933dad4438`, per-directory counts and a deterministic drift test. Allocation records classify artifact role only; they do not grant semantic or executable authority.

## Authorized material set

| Change ID | Target | Action | Expected change | KEEP requirements | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-N-01 | `Repository/REP-012_PRIORITY10_RUNTIME_EXACT_ALLOCATION_MANIFEST_2026-09-03_N.tsv` | CREATE | one allocation record for every tracked Runtime path | no authority promotion; deterministic sorted order | PASS | PENDING |
| P10-N-02 | `Quality/Integrity/test_runtime_p10_exact_inventory_allocation.py` | CREATE | compare manifest paths/count/digest to current Git tree and validate allocation fields | fail on added, missing, duplicate or unclassified Runtime path | PASS | PENDING |
| P10-N-03 | `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` | UPDATE | bind exact manifest and role-count allocation | preserve historical sections, control-plane/global holds | PASS | PENDING |
| P10-N-04 | `Repository/REP-013_REPOSITORY_CONTENT_TREE.md` | UPDATE | supersede non-exhaustive Runtime inventory with exact digest/count/addendum pointer | preserve all non-Runtime inventory and authority boundaries | PASS | PENDING |
| P10-N-05 | `Runtime/_FOLDER_STATUS.md` | UPDATE | mark exact physical inventory/allocation reconciled; move to explicit P10 closure-readiness review | Gates 12–15 and all provider/production/global non-claims | PASS | PENDING |
| P10-N-06 | `Repository/REP-011_PRIORITY10_RUNTIME_EXACT_INVENTORY_ALLOCATION_ADDENDUM_2026-09-03_N.md` | CREATE | bounded review evidence and non-claims | no semantic review claim from role allocation | PASS | PENDING |
| P10-N-07 | this Matrix | UPDATE | bind material/read-back/tests/CI | exact authorized path set | PASS | PENDING |

## Expected exact allocation

Directory counts: top-level `17`, Context `4`, Decision `12`, Execution `41`, Integration `2`, Learning `17`, Prototype `25`.

Role counts: canonical Runtime contract `10`, candidate Runtime contract `5`, supporting contract `24`, implementation `36`, test `36`, navigation `2`, status evidence `1`, evidence report `1`, schema `1`, test fixture `1`, test configuration `1`.

## Non-claims

- Allocation records do not certify semantic correctness, canonical authority, executable promotion, provider authenticity or production readiness.
- This transaction does not close Priority 10; it removes one blocker and requires a separate closure-readiness decision.
- Phase 1, repository-wide graph, Global Connected Baseline and Global Integrity remain OPEN/HOLD.

Validation:
`pre-write → exact manifest/control-surface mutation → immutable read-back → deterministic inventory test → full local suites → exact-head four-family CI → close N or HOLD / RESUME-SAFE`.
