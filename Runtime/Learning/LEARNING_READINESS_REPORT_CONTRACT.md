# Learning Readiness Report Contract

## Purpose

Produce an auditable handoff from evaluated outcome feedback to the existing learning promotion authority.

## Report Must Preserve

- outcome identity;
- decision identity;
- evaluated result;
- confidence classification;
- evidence trace IDs;
- quality state;
- explicit promotion authority;
- explicit `knowledge_promoted=false` at this stage.

## States

`READY_FOR_PROMOTION_REVIEW` means only that the evidence/evaluation passed the upstream readiness gates.

`NOT_READY` means the material must not enter promotion review yet.

## Boundary

The report is a handoff artifact, not a promotion action.

```text
Readiness Report
      ↓
Existing Learning Promotion Gate
      ↓
Possible Knowledge Promotion
```
