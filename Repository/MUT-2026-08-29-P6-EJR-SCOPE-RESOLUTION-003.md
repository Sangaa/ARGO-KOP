# P6 EJR Scope Resolution — Mutation Matrix

Transaction ID: `MUT-2026-08-29-P6-EJR-SCOPE-RESOLUTION-003`  
Parent transaction: `MUT-2026-08-29-CONTROL-PLANE-CONVERGENCE-001`  
Working branch: `argo/control-plane-convergence-20260829`  
Base transaction main: `28e3ec16f1b0e6decee6623f77f48cda74e229c7`  
Status: `OPEN / PRE-MUTATION MATRIX ESTABLISHED`  
Authority basis: `GOV-013 + GOV-014 + GOV-015 + GOV-016 + P6-SCOPE-001`

## Verified gap

Issue #15 and `EJR/EJR-284_2026-08-21_HERMUZ_P6_DOCUMENTATION_PATH_POLICY_GAP.md` record an unresolved governance question: whether documentation-only `EJR/**` changed paths are direct P6 impact-correlation scope.

Current P6 architecture already separates scope policy from correlation implementation:

`changed path → P6_SCOPE_ELIGIBILITY_REGISTRY → correlation → execution evidence → classification`.

The correlator does not need a code workaround; the canonical scope registry is the intended policy surface.

## Current evidence supporting a decision

1. `GOV-015` now classifies Engineering Journal as a learning/handoff transfer surface and explicitly separates evidence from authority/promotion.
2. `GOV-016` requires learning promotion through `Observation → Root Cause → Lesson → General Rule → Test → Validation → Promotion → Transfer`; an EJR record does not become governance/runtime/relationship authority merely by existing.
3. Existing Mutation Matrix preflight regression treats `EJR/**` as documentation/session evidence rather than a protected implementation mutation path.
4. P6 issue #15 itself forbids adding REP-020 relationships/mappings merely to make documentation paths pass.
5. P6 scope resolution can therefore be made at the policy layer without changing runtime semantics, relationship authority, or correlation code.

## Decision

`EJR/**` is `OUT_OF_SCOPE` for **direct P6 implementation/relationship impact correlation**.

Meaning:

- an EJR-only changed path returns `NOT_APPLICABLE`, not `UNMAPPED` and not `POLICY_UNRESOLVED`;
- the EJR remains valid provenance/learning/session evidence;
- EJR content can influence future work only through the applicable review/promotion/handoff mechanism;
- if the same transaction also changes an in-scope implementation/control/relationship path, those changed paths remain independently evaluated by P6;
- no EJR relationship or REP-020 mapping is created by this scope decision.

This is an impact-scope decision, not a declaration that EJR has no architectural value.

## Change matrix

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P6E-01 | `Repository/P6_SCOPE_ELIGIBILITY_REGISTRY.md` | UPDATE | resolve `EJR/**` from `UNRESOLVED` to bounded `OUT_OF_SCOPE` with explicit authority/evidence rationale | N | N |
| P6E-02 | `Quality/Integration/test_p6_canonical_repository.py` | UPDATE | canonical regression proves EJR-only path is `NOT_APPLICABLE` and mapping evidence cannot promote it | N | N |
| P6E-03 | P6 correlator implementation | KEEP | no code workaround; policy remains data-driven | N/A | N/A |
| P6E-04 | `REP-020` / `REP-014` | KEEP | no invented mapping or relationship promotion | N/A | N/A |
| P6E-05 | Issue #15 | CLOSE after verification | governance decision no longer unresolved | N | N |
| P6E-06 | Issue #16 | CLOSE after #15 disposition | historical session closure no longer active work | N | N |

## Abort / hold

Hold if:

- current P6 canonical test does not actually consume the scope registry;
- a higher canonical authority explicitly requires EJR to be IN_SCOPE;
- changing the registry would require correlation implementation changes to force the result;
- regression demonstrates EJR mapping evidence can still promote OUT_OF_SCOPE into MAPPED.

## Non-claims

This transaction does not:

- make EJR non-evidence;
- weaken journal provenance;
- promote or demote any relationship;
- prove P6 runtime/CI execution;
- close unrelated unknown repository path classes;
- resolve repository-wide P6 scope.
