# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 REL-071/072 RECONCILIATION — Q

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-REL071-072-Q`
Work Lease: `HERMUZ-P7-Q-REL071-072-20260901`
Priority: `7 — Core cross-layer relationship reconciliation`
State: `PRE-WRITE / LEASE OPEN / SYNCHRONIZATION`
Entry HEAD: `194b23856a5f5b45c00bdb27a9c28c43288acf11`
Pre-write Matrix HEAD: `PENDING THIS COMMIT`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Problem / legal action

Transaction P independently validated a material constitutional Runtime-configuration seam:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

with disposition `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY` and exact-head 4/4 workflow success on both material candidate and closure HEAD.

Fresh post-P recomputation at live `main@194b23856a5f5b45c00bdb27a9c28c43288acf11` confirms Priority 7 remains open, current REP-014 is v1.2.13 and ends at REL-070, the validated P pair remains absent, Core status still directs `validate → reconcile REP-014 where evidence requires → certification review`, and the current manifest still binds REP-014 v1.2.13.

Therefore the highest-value legal local obligation is synchronization of P's already-validated seam before unrelated exploration. This transaction does not discover new semantics.

## Prior-learning classification

| Evidence | Classification | Use in Q |
|---|---|---|
| Transaction P | DIRECTLY APPLICABLE | Exact source semantics and validation evidence for the pair. |
| REL-037/038 CORE-003↔RUN-001 | DIRECTLY APPLICABLE | Existing Constitution→critical Runtime GOVERNS/REFERENCES pattern. |
| Transactions M and O | DIRECTLY APPLICABLE | Validation-first seam followed by separate bounded registry synchronization. |
| L/N authority/non-dependency discipline | TRANSFERABLE | Prevents dependency or symmetry inflation. |

No new governance rule is required.

## Authorized material change set — exactly 6 paths

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| Q-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | v1.2.13→v1.2.14; add exactly REL-071 CORE-003→RUN-003 GOVERNS and REL-072 RUN-003→CORE-003 REFERENCES with bounded evidence; preserve all prior content. | N | N |
| Q-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | Bind REP-014 v1.2.14 and Q refresh while preserving Phase-1 OPEN / Integrity HOLD / Global PASS NOT CLAIMED. | N | N |
| Q-03 | `Core/_FOLDER_STATUS.md` | UPDATE | v1.3.10→v1.3.11; add the P-validated/Q-registered seam as an eighth bounded seam; preserve certification pending and broader P7 gaps. | N | N |
| Q-04 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | UPDATE | Replace validation-first absence assertions with exact unique REL-071/072 registration assertions; preserve direct-source and forbidden stronger-semantics checks. | N | N |
| Q-05 | `Repository/P7_CORE003_RUN003_REL071_072_RECONCILIATION_2026-09-01_Q.md` | CREATE | Bounded synchronization evidence and non-authority record. | N | N |
| Q-06 | this Matrix | UPDATE IN SAME MATERIAL CHANGE SET | Bind candidate and verification state. | N | N |

Unexpected path expansion authorized: `0`.

## KEEP / forbidden promotion

- `Core/CORE-003_CONSTITUTION.md` — KEEP unchanged.
- `Runtime/RUN-003_CONFIGURATION.md` — KEEP unchanged.
- REL-001..REL-070 — KEEP unchanged.
- Add no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, reverse RUN-003→CORE-003 GOVERNS, executable-reachability or runtime-coupling claim.
- Do not certify Runtime or Core.
- Do not close Priority 7, Phase 1, Connected Baseline, repository-wide graph, or Global PASS.

## Pre-write evidence

- live main independently rediscovered as `194b23856a5f5b45c00bdb27a9c28c43288acf11` after P closure 4/4;
- REP-014 direct read: Version 1.2.13, relationship list explicitly incomplete, last current row REL-070, no RUN-003 pair;
- REP-020 current manifest binds REP-014 v1.2.13 and preserves open/hold boundaries;
- Core status v1.3.10 lists seven bounded seams and keeps cross-layer validation open / certification pending;
- P focused test still intentionally asserts pair absence and must change atomically with registration;
- P direct source semantics are closed/CI-verified; no new semantic inference is authorized.

Pre-write decision: `AUTHORIZED FOR EXACT SIX-PATH SYNCHRONIZATION UNIT ONLY`.

Work Lease remains `OPEN` until candidate exact-head CI, closure commit, and closure-head 4/4 verification complete.
