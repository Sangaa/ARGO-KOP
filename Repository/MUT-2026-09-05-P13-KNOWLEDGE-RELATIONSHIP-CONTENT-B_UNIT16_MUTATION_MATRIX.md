# MUTATION MATRIX — P13 KNOWLEDGE RELATIONSHIP/CONTENT B — UNIT 16 LEARNING REGISTRY ADMISSIBILITY

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Verified predecessor head: `34da5d3125813a5a4a16361955430b12c434c10a`
State: `ADMISSIBILITY CLASSIFIED / EXACT-HEAD VALIDATION PENDING`

## Purpose

Determine whether the executable Learning seams observed in Unit 15 should create new canonical REP-014 relationships now, while preserving stable relationship ordering and avoiding duplicate or invalid edge admission.

## Findings

1. `Runtime/Context/runtime_context_pipeline.py → Knowledge/Learning/contextual_retrieval.py` is a direct executable consumption seam: import plus function call are current source evidence.
2. `Runtime/Context/runtime_context_pipeline.py → Knowledge/Learning/knowledge_correction.py` is also direct executable consumption, but Priority-10 already produced governed boundary evidence for the same runtime correction seam. Unit 16 therefore does not manufacture a duplicate relationship merely from re-observation.
3. The historical `Knowledge/Learning/promotion_gate_adapter.py → Runtime/Prototype/learning_promotion_gate.py` reverse dependency was removed in Unit 15 and is explicitly rejected from registry admission.
4. Canonical REP-014 currently ends at `REL-167`; the verified bridge reserves `REL-168..REL-206` for the earlier P13 cross-layer cohort and states canonical REP-014 synchronization remains open.

## Ordering rule

No new Learning executable relationship may allocate `REL-168`, collide with `REL-168..206`, or jump directly to `REL-207` while the prior cohort remains bridge-only.

`VERIFIED EXECUTABLE SEAM != PERMISSION TO BREAK STABLE RELATIONSHIP ORDERING`.

The contextual-retrieval seam is therefore classified:

`ADMISSIBLE AFTER REL-168..206 CANONICAL FOLD / NEXT-ID REVIEW REQUIRED`.

This is a controlled deferral, not rejection of the executable evidence.

## Material paths

Exactly three logical paths:

1. `Repository/P13_KNOWLEDGE_LEARNING_REGISTRY_ADMISSIBILITY_2026-09-05_J.tsv`
2. `Quality/Integrity/test_knowledge_p13_learning_registry_admissibility.py`
3. this Matrix

No REP-014 mutation, REL-ID allocation, Knowledge source change, or control-plane authority mutation occurs in Unit 16.

## Required gate

`COMPARE VERIFIED PREDECESSOR → UNIT-16 HEAD → EXACT 3 LOGICAL PATHS → ALL FOUR WORKFLOW FAMILIES EXPLICITLY COMPLETED/SUCCESS`.

After success, the next strongly connected work is to attempt a full-preservation canonical REP-014 fold of the verified `REL-168..206` cohort if the available Git-data path can preserve the entire long registry safely. If that cannot be proven safe, canonical fold remains an explicit closure blocker rather than being simulated by a new addendum.

Priority 13 remains OPEN.

---

End of Unit-16 Mutation Matrix
