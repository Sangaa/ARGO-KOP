# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP/CONTENT B — UNIT 15 LEARNING EXECUTABLE DEPENDENCY DIRECTION

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Verified predecessor head: `50caba7cb497a5f530368ac7a40a61451d1d31e9`
State: `MATERIAL APPLIED / EXACT-HEAD VALIDATION PENDING`

## Trigger

Priority-13 Learning executable consumer review found two valid Runtime→Knowledge direct executable seams and one opposite-direction dependency:

- `Runtime/Context/runtime_context_pipeline.py` imports and calls `Knowledge/Learning/contextual_retrieval.py`;
- the same Runtime pipeline imports and calls `Knowledge/Learning/knowledge_correction.py`;
- `Knowledge/Learning/promotion_gate_adapter.py` imported `Runtime.Prototype.learning_promotion_gate.evaluate`.

Current `ARC-006` permits Knowledge to depend on Repository, Architecture and applicable Governance and states that dependencies must not reverse the canonical direction without an explicitly authorized governed architectural decision. Repository search found historical implementation/checkpoint evidence for the adapter but no governed architectural exception. `ARC-009` also states that implementation alone does not become architectural authority.

## Caller-graph finding

Repository-wide search confirmed that `promotion_gate_adapter.evaluate_evidence()` had no production caller. Current executable callers were limited to:

1. its Knowledge unit test;
2. the Quality integration boundary test.

Historical P131 evidence independently recorded the same no-production-caller result. Therefore removing Knowledge-owned Runtime evaluation does not remove an established production seam.

## Material disposition

The repair preserves the physical 50-leaf Knowledge inventory and avoids moving files:

1. `Repository/P13_KNOWLEDGE_LEARNING_EXECUTABLE_SEAM_AUDIT_2026-09-05_I.tsv` — executable seam classification evidence;
2. `Knowledge/Learning/test_promotion_gate_adapter.py` — validates Knowledge-owned candidate mapping only;
3. `Quality/Integration/test_readiness_to_promotion_gate_boundary.py` — explicitly composes Knowledge `build_candidate` with Runtime `evaluate` and validates authority separation;
4. `Knowledge/Learning/promotion_gate_adapter.py` — removes the upward Runtime import and `evaluate_evidence`; retains `build_candidate` only;
5. `Quality/Integrity/test_knowledge_p13_learning_dependency_direction.py` — guards all non-test Learning modules against direct Runtime imports and binds the discovered downward consumer seams + ARC-006 rule;
6. this Matrix.

Execution used bounded sequential Contents API commits. No force update, history rewrite, REP-014 mutation, canonical control-plane fold or REL-ID allocation is included.

## Semantic boundaries

`DIRECT IMPORT/CALL = EXECUTABLE DEPENDENCY EVIDENCE`

`EXECUTABLE DEPENDENCY != AUTHORITY TRANSFER`

`TEST CONSUMER != PRODUCTION CONSUMER`

`HISTORICAL IMPLEMENTATION CHECKPOINT != GOVERNED ARCHITECTURAL EXCEPTION`

`REVERSE DEPENDENCY DEFECT != RELATIONSHIP TO CANONICALIZE`

The P10 knowledge-correction boundary remains valid and must not be duplicated merely because Unit 15 re-observed its executable call. The contextual-retrieval Runtime seam remains a candidate for relationship/control-plane disposition only after stable identity and duplicate review.

`promotion_gate_adapter` now constructs the candidate; Runtime owns promotion-gate evaluation. `PROMOTION_ELIGIBLE` remains an eligibility result, not automatic knowledge persistence or canonical promotion.

## Required validation

Before Unit 16 or any new registry allocation:

1. compare predecessor → Unit-15 head and confirm only the six declared logical paths;
2. re-read repaired adapter and integration boundary;
3. all four workflow families must be explicitly `status=completed` and `conclusion=success` on the same exact head.

Priority 13 remains OPEN. REP-014 `REL-168..206` canonical fold, REP-002/012/013 canonical folds, REP-001 admission review and remaining consumer/status reconciliation remain OPEN.

---

End of Unit-15 Mutation Matrix
