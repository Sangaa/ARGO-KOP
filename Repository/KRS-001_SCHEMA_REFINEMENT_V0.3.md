# KRS-001 — Schema Refinement v0.3

Status: CONTROLLED / VALIDATION-ONLY

## Basis
Derived from reconciliation of Pilot 1 (INTF-006) and Pilot 2 (GOV-013). v0.2 is retained as historical pilot schema; v0.3 resolves observed representation drift and evidence/currentness ambiguity before any third pilot.

## Canonical envelope
All Knowledge Objects MUST use the following ordered envelope:

`IDENTITY → CONTROL → PROVENANCE → RELATIONSHIPS → EVIDENCE → ASSERTIONS → CONSTRAINTS → HISTORY → PAYLOAD → INTEGRITY`

## IDENTITY
- OBJECT_ID: stable object identity
- OBJECT_TYPE: controlled type
- SOURCE_PATH: exact repository path
- SOURCE_DOCUMENT_VERSION: source-declared version, nullable

## CONTROL
- OBJECT_STATUS
- MIGRATION_STATUS
- PRODUCTION_AUTHORITY
- CURRENTNESS_CLASS: controlled value
- CURRENTNESS_AS_OF: exact commit SHA or explicit historical timestamp + SHA

Allowed currentness classes:
- CURRENT-VERIFIED
- CURRENT-BUT-STALE-DEPENDENCY
- HISTORICAL
- SUPERSEDED
- CONTRADICTED
- UNRECONCILED
- UNKNOWN

## PROVENANCE
- SOURCE_REF: immutable commit SHA
- SOURCE_BLOB_SHA: exact source blob SHA when source is a file
- CREATED_BY_MUTATION: exact mutation identifier
- LAST_DIRECT_CHANGE: exact commit SHA + date
- LAST_RECONCILIATION: exact commit SHA + date

No descriptive placeholder may substitute for an immutable SHA when the SHA is obtainable.

## RELATIONSHIPS
Each relationship MUST include:
- RELATION_ID
- TARGET_ID or exact TARGET_PATH
- TARGET_VERSION when available
- RELATION_TYPE
- TARGET_CURRENTNESS
- RELATION_EVIDENCE_ID(S)
- VALIDATED_AT: exact SHA/date

A relationship is not evidence merely because the target is linked or named.

## EVIDENCE
Evidence types are controlled:
- DIRECT-SOURCE
- HISTORY
- CI
- RUNTIME
- STRUCTURAL
- DERIVED
- RELATIONSHIP

Each evidence record MUST include:
- EVIDENCE_ID
- EVIDENCE_TYPE
- CLAIM
- REF/SHA/RUN as applicable
- RESULT
- VALIDATED_AT
- SCOPE

`RESULT=PASS` is insufficient without claim scope and identity correlation.

## ASSERTIONS
Each assertion MUST include:
- ASSERTION_ID
- CLAIM
- STATUS
- EVIDENCE_ID(S)
- VALID_FROM
- SUPERSEDED_BY (nullable)

Assertions MUST NOT be promoted solely from document status labels.

## CONSTRAINTS
Each constraint MUST include:
- CONSTRAINT_ID
- RULE
- AUTHORITY
- ENFORCEMENT_SURFACE

## HISTORY
Append-only state transitions. Every transition MUST identify the previous state, new state, cause, and supporting evidence.

## PAYLOAD
Source-owned semantic content remains authoritative during migration. A Knowledge Object may summarize/reference payload but may not silently replace or rewrite source meaning.

## INTEGRITY
- SOURCE_INTEGRITY
- OBJECT_INTEGRITY
- TRACEABILITY_STATUS
- MIGRATION_DECISION
- OBJECT_BLOB_SHA when independently materialized and available

Integrity is identity-aware; status text alone is not integrity proof.

## Required reconciliation rule
If a source, relationship, or evidence item is stale or unresolved, the object MUST represent that state explicitly. Missing retrieval evidence MUST NOT be interpreted as artifact absence until the appropriate retrieval surfaces have been exhausted.

## Pilot gate
v0.3 is validation-only. It is NOT authorized for source replacement or bulk migration. It must first be validated against Pilot 1 and Pilot 2, then against one heterogeneous runtime/provenance artifact. Any third pilot requires a pre-write mutation matrix and exact-SHA CI correlation.
