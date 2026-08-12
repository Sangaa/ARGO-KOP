# EJR-142 — Learning and Reasoning Seam Repair

Date: 2026-08-12

## Trigger

CI Run 87 reduced the integration failures to 10. The remaining failures exposed two real contract mismatches rather than independent test noise.

## Repairs

### Reasoning packet

`Cognition/reasoning_packet_classifier.py` previously iterated `knowledge` as a list of records, while the live integration fixture supplied a single knowledge mapping. The classifier now normalizes a mapping to one knowledge item and accepts a list only when every item is a mapping. Invalid context/knowledge shapes are held explicitly instead of failing with an attribute error.

### Outcome evaluation

`Runtime/Learning/outcome_evaluator.py` validated outcome confidence indirectly through the downstream quality gate, but discarded the confidence field when constructing the evaluated outcome. This caused valid HIGH-confidence outcomes to become `QUALITY_REJECTED`. The evaluator now preserves `confidence` in the evaluated contract, allowing the existing quality gate to assess it without changing promotion authority.

## Boundary preserved

No automatic learning promotion was introduced. Readiness remains separate from promotion, and the existing promotion gate remains authoritative.

## Remaining CI evidence

The current CI run must be rerun against these repairs. Repository evidence registry failures and the explicit `Execution -> Outcome` seam question remain separate issues and will be handled only after fresh test evidence confirms the effect of these repairs.

## Session closure

Do not claim CI success until a new workflow run certifies the commits.
