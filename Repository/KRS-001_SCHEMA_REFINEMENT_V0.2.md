# KRS-001 — Schema Refinement v0.2

Status: CONTROLLED / PRE-PILOT

## Basis
The v0.1 INTF-006 object proved useful for traceability, but its `CURRENTNESS` value was too coarse and its evidence/relationship semantics were not sufficiently machine-addressable.

## Required v0.2 fields

### IDENTITY
- OBJECT_ID
- OBJECT_TYPE
- SOURCE_PATH
- SOURCE_DOCUMENT_VERSION

### CONTROL
- OBJECT_STATUS
- MIGRATION_STATUS
- PRODUCTION_AUTHORITY
- CURRENTNESS_CLASS
- CURRENTNESS_AS_OF

### PROVENANCE
- SOURCE_REF
- SOURCE_BLOB_SHA
- CREATED_BY_MUTATION
- LAST_DIRECT_CHANGE
- LAST_RECONCILIATION

### RELATIONSHIPS
Each relation must identify:
- TARGET
- RELATION_TYPE
- TARGET_CURRENTNESS
- RELATION_EVIDENCE
- VALIDATED_AT

### EVIDENCE
Each evidence item must identify:
- EVIDENCE_ID
- EVIDENCE_TYPE
- CLAIM
- REF / SHA / RUN where applicable
- RESULT
- VALIDATED_AT
- SCOPE

### ASSERTIONS
Each assertion must identify:
- ASSERTION_ID
- CLAIM
- STATUS
- EVIDENCE_IDS
- VALID_FROM
- SUPERSEDED_BY (nullable)

### CONSTRAINTS
Each constraint must identify:
- CONSTRAINT_ID
- RULE
- AUTHORITY
- ENFORCEMENT_SURFACE

### HISTORY
Historical states are append-only and must retain the prior classification and the evidence that caused transition.

### PAYLOAD
Human-readable semantic content remains source-owned during migration. The object may reference or summarize it but must not silently replace it.

### INTEGRITY
- SOURCE_INTEGRITY
- OBJECT_INTEGRITY
- TRACEABILITY_STATUS
- MIGRATION_DECISION

## New invariant
`Canonical` identifies authority location; it does not establish current validity.

`Verified` is always scoped to a claim, evidence surface, and validity point.

## Second pilot candidate
Use one heterogeneous artifact that is not a canonical interface: a governance/control document or mutation matrix. The purpose is to test whether v0.2 handles policy assertions, temporal validity, and control authority without forcing interface-specific fields.

## Gate
Do not migrate the candidate yet. First perform currentness/relationship review and record a mutation matrix for the second pilot.
