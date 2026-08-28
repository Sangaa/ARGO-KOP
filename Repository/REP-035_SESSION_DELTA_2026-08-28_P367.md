# P367 — Executable Seam Recovery and Test-Validity Reassessment

Date: 2026-08-28
Status: `CLOSED / VERIFIED / EXECUTION STILL PENDING`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P366. The previous checkpoint required recovery of the actual executable/test surface before any production mutation.

## RECOVERY
Repository inspection recovered:
- `Quality/Integration/test_evidence_reasoning_classification.py`
- `Runtime/Prototype/cognitive_loop_harness.py`
- `Quality/Integration/test_engine_runtime_cognitive_loop_boundary.py`
- `EJR-330` documenting the original test-first fixture build.

The test fixture is not merely a placeholder: static inspection shows a frozen `EvidenceObservation` contract plus classification, provenance, execution-occurrence, authority-resolution, correlation, and independence assertions. The fixture therefore provides a materially useful semantic test surface.

## VALIDITY REASSESSMENT
The correct question is no longer whether an executable test surface exists. That gap is closed structurally and statically.

The remaining evidence gap is narrower:

`TEST FILE EXISTS` → `STATIC CONTRACT VERIFIED` → `TEST EXECUTION ARTIFACT` → `RUNTIME RESULT` → `INDEPENDENT RECONCILIATION`

The current GitHub read surface can recover the committed fixture, but this checkpoint did not obtain a verified execution result for that new fixture. Therefore the fixture must remain `EXECUTION-PENDING`, not `PASS`.

## TEST-SCOPE REVIEW
The fixture currently covers more than the original four vectors, including:
- contradiction and authority resolution;
- different evidence layers;
- incomplete evidence as unresolved;
- preservation of original observations;
- missing execution identity;
- capability versus occurrence binding;
- target/identity mismatch protection;
- correlated versus independent corroboration;
- transitive provenance behavior.

This is useful coverage, but breadth must not be confused with validity. The next execution must establish that these assertions actually run in the governed test surface and that failures are observable and attributable.

## DECISION
No production runtime mutation and no new governance gate are justified by this checkpoint.

The next mutation, if any, should be limited to the existing test/CI surface needed to obtain independently attributable execution evidence. If the existing CI already executes this path, reuse it; do not add a second runner merely to manufacture observability.

## EVIDENCE CLASSIFICATION
`EXECUTABLE TEST SURFACE EXISTS: PROVEN`
`TEST CONTRACT STATICALLY READABLE: PROVEN`
`TEST COVERAGE BROADER THAN FOUR ORIGINAL VECTORS: PROVEN`
`RUNTIME EXECUTION OF NEW FIXTURE: UNPROVEN`
`TEST PASS: UNPROVEN`
`PRODUCTION INTEGRATION: UNPROVEN`
`PROMOTION: NOT JUSTIFIED`

## KNOWLEDGE DELTA

**KD-037 — Recovering the executable seam changes the Gap; it does not close the runtime proof automatically.**

**KD-038 — Test breadth is not test validity.** A larger assertion set can improve discrimination only after execution, attribution, and reconciliation are established.

**KD-039 — The smallest useful next mutation is determined by the remaining evidence gap, not by the size of the discovered test surface.**

## CHECKPOINT
`P367 → determine whether existing CI executes test_evidence_reasoning_classification.py → if yes, bind exact run/job/result → if no, add the smallest existing-surface CI invocation → execute → inspect failures/results → reconcile evidence → only then consider production integration.`

## CLOSE
`CLOSED / VERIFIED / NO PRODUCTION MUTATION / NO AUTHORITY PROMOTION`
