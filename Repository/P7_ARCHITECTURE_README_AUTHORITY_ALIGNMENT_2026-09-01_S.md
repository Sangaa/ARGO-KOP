# Priority 7 — Architecture README Authority Alignment — Transaction S

Date: 2026-09-01
State: `MATERIAL-CANDIDATE FAILED / CORRECTIVE S-C1 ACTIVE / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-ARCHITECTURE-README-20260901`
Entry HEAD: `cb45d5fd9b6dbba1727e52060b9e181a54db3239`
Pre-write Matrix HEAD: `cbba871330e9cb82486b7cbda73a20edd65f114e`
Rejected unpublished object candidate: `c81500caacbd385b9706a09de57b0fce55c2dae3`
Published failed material candidate: `c51ffc4efec9eaded777eeb4f97311386cc0a289`
Corrective subtransaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-S-C1`

## Why S was selected

Post-R Priority-7 recomputation did not treat `RUN-002 → CORE-003 = REFERENCES` as an automatic REP-014 registration obligation. A broader Core-consumer search exposed a higher-value semantic drift in canonical `Architecture/README.md` after Transaction I reconciled CORE-000.

At S entry the README still described CORE-000 as the `ultimate guiding text`, omitted ARC-011 from its old partial canonical-component list, treated that partial list as exhaustive, and retained stale `globally locked` / `Anti-Patch Policy` wording. Current CORE-000 and ARC-011 instead establish Constitution/Governance → ARC-011 → other Architecture → repository/implementation for structural-boundary and dependency-direction interpretation.

## Intended S repair preserved

S candidate `c51ffc4e...` corrected the bounded authority/inventory drift:

- README v3.2.0 → v3.2.1;
- status clarified to `Approved / Integrity Hold`;
- ARC-011 restored as current authoritative architectural reference for structural boundaries/dependency direction;
- CORE-000 retained as Core-level platform architecture intent aligned to ARC-011, not a competing Architecture model;
- ARC-001..ARC-011 represented as the current primary ARC review set;
- ARC_MAP / README / `_FOLDER_STATUS.md` separated as navigation/control surfaces;
- `01-System-Overview.md` retained as foundation/legacy material without authority promotion;
- stale lock/anti-patch wording replaced with current controlled-mutation governance;
- Architecture remains under Integrity Hold and broader gates remain open;
- no REP-014 relationship was manufactured.

## Pre-publish validation-design defect

Unpublished object candidate `c81500ca...` was rejected before `main` moved because the first focused test used whole-document first occurrence for ARC-001..ARC-011 ordering. ARC-011 is validly mentioned earlier in the authority section, so the test was corrected to scope ordering to Section 2. Classification: `PRE-PUBLISH VALIDATION_DESIGN_DEFECT / NO MAIN MUTATION / NO CI FAILURE`.

## Published candidate verification failure

Exact-head Runtime workflow `33530617715` on `c51ffc4e...` failed while prototype tests passed. Integrity and integration suites exposed two compatibility regressions.

First meaningful integrity log evidence:

1. `test_architecture_folder_inventory_reconciliation.py::test_architecture_status_closes_only_exact_physical_inventory` expected the established literal marker `Architecture ↔ Runtime / Interface boundary — OPEN`; S had changed it to `Architecture ↔ Runtime / Interface / AI boundary — OPEN`.
2. `test_canonical_reference_regressions.py::test_architecture_core_000_reference_targets_authoritative_core_path` expected `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` in `Architecture/README.md`; S preserved the Core path semantically but rendered it as code text rather than the established relative Markdown link.

Runtime integrity result: `136 passed / 2 failed` in the reported suite. Prototype job succeeded. Full-Stack candidate workflow `33530617711` succeeded, proving that green Full-Stack did not override the failed Runtime verification contract.

Classification: `MATERIAL_CANDIDATE_CI_FAILURE / BACKWARD-COMPATIBILITY REGRESSION / AUTHORITY-SEMANTICS NOT INVALIDATED`.

No rerun was used to bypass the failure. The failed candidate remains evidence.

## Corrective decision — S-C1

S-C1 restores exactly the two existing compatibility contracts while preserving S semantics:

- restore the exact Runtime / Interface open-gate marker;
- restore the canonical relative Markdown link to `../Core/CORE-000_PLATFORM_ARCHITECTURE.md`;
- do not modify the pre-existing tests that detected the regressions;
- do not modify the S focused authority regression;
- keep CORE-000/CORE-003/ARC-011/ARC-006/REP-014/Core status unchanged.

## Relationship and certification boundary

S/S-C1 does not add a REP-014 relationship and does not establish Architecture certification, Core certification, Priority-7 closure, Phase-1 closure, Connected Baseline closure, repository-wide graph completion or Global PASS.

## Learning retained

`SECTION-SCOPED SEMANTIC ASSERTION → TEST WITHIN THAT SECTION.`

`SEMANTIC REPAIR MUST PRESERVE ESTABLISHED INTERFACE/TEST CONTRACTS UNLESS THOSE CONTRACTS ARE THEMSELVES PROVEN STALE OR WRONG.`

Neither incident justifies a new Governance rule; existing validation and controlled-mutation discipline already covers the failure class.

## Continuation boundary

S remains open until S-C1 exact-head verification is green, parent-S closure documentation is committed, and the exact closure HEAD passes its applicable workflow verification. Only then may Priority 7 be freshly recomputed.
