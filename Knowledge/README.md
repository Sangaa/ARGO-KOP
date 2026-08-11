# ARGO KOP — KNOWLEDGE DOMAIN

Domain: Knowledge
Status: Integrity Hold
Role: Canonical semantic layer for validated, traceable and reusable knowledge.

## Purpose

Knowledge is where ARGO stores knowledge objects after they have been captured, classified, evidenced, related and validated for their declared scope.

Knowledge is not a raw document archive and not an automatic truth store.

## Core Boundary

```text
Source / Experience
        ↓
Evidence
        ↓
Knowledge Candidate
        ↓
Validation
        ↓
Scoped Knowledge
        ↓
Relationships
        ↓
Operational Use
        ↓
Review / Learning
        ↓
Promotion / Reclassification
```

A source claim remains distinguishable from ARGO's interpretation. A validated item does not automatically become canonical platform knowledge.

## Scope

Knowledge may belong to:

- `SESSION`
- `USER`
- `PROJECT`
- `DEPLOYMENT`
- `SHARED_CANDIDATE`
- `PLATFORM`

Subject classification is separate from scope. For example, Technical knowledge may be project-local without becoming platform knowledge.

## Knowledge Object Minimum

A governed knowledge object should preserve, as applicable:

- identity;
- subject classification;
- scope/domain;
- owner;
- source/provenance;
- evidence state;
- knowledge state;
- relationships;
- version;
- review history;
- repository location.

## Sources

Knowledge may originate from repository documents, human experience, operational events, project experience, validated external sources, AI model outputs, databases, APIs, tools, sensors and future ARGO-native runtime sources.

External availability does not grant authority. AI model outputs are evidence or candidates until independently validated and authorized.

## Relationship to Memory

Memory preserves contextual continuity and experience. Knowledge provides structured, reusable representations of information that have passed the applicable evidence and scope controls.

A project lesson may therefore move toward knowledge without automatically becoming platform truth:

```text
Project Observation
      ↓
Captured Experience
      ↓
Validated Lesson
      ↓
Reusable Knowledge Candidate
      ↓
Cross-Context Evidence
      ↓
Broader Knowledge Candidate
```

## Relationship to Learning

The Knowledge domain is a consumer and producer in the future learning pipeline. It should eventually support ingestion from books and other sources by preserving source claims, extracted concepts, evidence, relationships, validation results and reusable lessons.

That future capability must not bypass the existing authority and provenance boundaries.

## Canonical Artifacts

- `KNW-001_KNOWLEDGE_MODEL.md`
- `KNW-002_KNOWLEDGE_CLASSIFICATION.md`
- `KNW-003_KNOWLEDGE_RELATIONSHIPS.md`
- `KNW-004_KNOWLEDGE_LIFECYCLE.md`
- `KNW-005_KNOWLEDGE_GOVERNANCE.md`
- `KNW-006_KNOWLEDGE_QUALITY.md`
- `KNW-007_KNOWLEDGE_BASELINE.md`
- `KNW-008_KNOWLEDGE_TRACEABILITY.md`
- `KNW-009_KNOWLEDGE_EVOLUTION.md`
- `KNW-010_KNOWLEDGE_MAINTENANCE.md`

`Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md` defines the source/provenance boundary used by this domain.

## Authority Boundary

Knowledge remains subordinate to Constitution, Governance, Architecture and Repository authority. Knowledge relationships do not transfer authority, and storage location does not determine semantic authority.

## Integrity Hold

The domain is substantially modeled but remains on Integrity Hold pending consolidated cross-layer validation, reference synchronization and implementation validation.

## Guiding Principle

**ARGO may learn from every source, but it must preserve what was claimed, what was evidenced, what ARGO inferred, what was validated, where it applies and what authority it has.**

---

End of Document
