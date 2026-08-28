# Knowledge Reuse Policy

## Rule

Promoted knowledge may be reused only within the scope recorded by its knowledge record.

## Reuse Is Not Promotion

Using an existing knowledge record in a new task does not expand or rewrite the record.

New observations belong to the new task's evidence package.

`REUSE != PROMOTION != AUTHORITY`.

## Experience Spine Projection

The Experience Spine is an advisory semantic projection over existing promoted knowledge.

It may select, order, filter, and expose retrieval metadata for the current task. It must not:

- create a second persistence layer;
- change lifecycle, validation, evidence, or authority state;
- infer missing scope or consumer routing;
- convert repository presence or repeated reuse into authority;
- treat free-text similarity alone as governed relevance;
- load all historical records merely because they exist.

The packet is reasoning input only. Current evidence and applicable authority remain stronger than retrieved experience.

Recommended reasoning order:

`CURRENT EVIDENCE → APPLICABLE AUTHORITY → RELEVANT EXPERIENCE → CONFLICT/CORRELATION CHECK → ASSUMPTIONS → OPTIONS → TESTABLE DECISION`.

## Contradiction

If new evidence conflicts with promoted knowledge:

```text
Promoted Knowledge
      ↓
New Evidence
      ↓
Contradiction Detected
      ↓
Demotion Review
```

The original record remains intact until a governed decision changes its state.

If two retrieved experience projections contradict each other, retrieval must expose the conflict and require review; it must not silently choose one by rank, model identity, recency guess, or file order.

## Supersession

A projection explicitly marked with `superseded_by` is excluded from the active Experience Spine packet while the underlying historical record remains preserved.

Supersession changes current retrieval applicability; it does not erase provenance.

## Correlated Evidence

Multiple knowledge records may derive from the same material evidence or incident.

When they share an `evidence_group`, the Experience Spine must expose that correlation. Separate files, summaries, or model analyses derived from one source do not become independent confirmation merely because they have separate identities.

`MULTIPLE REPRESENTATIONS OF ONE SOURCE != MULTIPLE INDEPENDENT SOURCES`.

## Provenance

Every reuse event should retain the source knowledge record and the new task evidence so that later reasoning can distinguish inherited knowledge from newly observed facts.

Experience projection additionally preserves source identity, source type, evidence state, authority state, evidence group, applicability boundaries and counterindications when present.

## Cognitive-Benefit Boundary

A deterministic retrieval packet proves retrieval mechanics only.

It does not by itself prove improved reasoning, transfer, generalization, or durable learning. Cognitive benefit must be evaluated separately using the existing Invariant Generalization Test (IGT) or another governed validation path.

`RETRIEVAL VERIFIED != COGNITIVE IMPROVEMENT VERIFIED`.
