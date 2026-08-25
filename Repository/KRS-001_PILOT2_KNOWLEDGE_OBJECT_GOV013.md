# KRS-001 Pilot 2 — Knowledge Object — GOV-013

OBJECT
  OBJECT_ID: KRS-KO-GOV013-001
  OBJECT_TYPE: GOVERNANCE_CONTROL
  SOURCE_PATH: Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md
  SOURCE_DOCUMENT_VERSION: 1.1.2

CONTROL
  OBJECT_STATUS: PILOT-VERIFIED
  MIGRATION_STATUS: SUPPLEMENTAL_ONLY
  PRODUCTION_AUTHORITY: GOVERNANCE/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md
  CURRENTNESS_CLASS: CURRENT-VERIFIED
  CURRENTNESS_AS_OF: current repository HEAD at creation

PROVENANCE
  SOURCE_REF: main
  SOURCE_BLOB_SHA: source blob verified before objectization
  CREATED_BY_MUTATION: KRS-001-PILOT-002
  LAST_DIRECT_CHANGE: 2026-08-25 CI failure/root-cause and no-transition gate change
  LAST_RECONCILIATION: 2026-08-25

RELATIONSHIPS
  - TARGET: Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md
    RELATION_TYPE: SUPPLEMENTS
    TARGET_CURRENTNESS: CURRENT-VERIFIED
    RELATION_EVIDENCE: GOV-013A declares that it supplements GOV-013 and does not replace higher authority.
    VALIDATED_AT: 2026-08-25
  - TARGET: Repository/KRS-001_SCHEMA_REFINEMENT_V0.2.md
    RELATION_TYPE: OPERATIONALIZED_BY
    TARGET_CURRENTNESS: CURRENT-VERIFIED
    RELATION_EVIDENCE: v0.2 defines the pilot schema and explicitly requires the governance/control heterogeneous pilot.
    VALIDATED_AT: 2026-08-25
  - TARGET: Repository/KRS-001_PILOT2_GOV013_CURRENTNESS_RELATIONSHIP_MATRIX.md
    RELATION_TYPE: VERIFIED_BY
    TARGET_CURRENTNESS: CURRENT-VERIFIED
    RELATION_EVIDENCE: pilot matrix records the pre-write currentness and relationship review boundary.
    VALIDATED_AT: 2026-08-25

EVIDENCE
  - EVIDENCE_ID: E-GOV013-001
    EVIDENCE_TYPE: CANONICAL_SOURCE
    CLAIM: GOV-013 is the approved canonical HERMUZ session operating contract.
    REF: Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md
    RESULT: PASS
    VALIDATED_AT: 2026-08-25
    SCOPE: governance authority
  - EVIDENCE_ID: E-GOV013-002
    EVIDENCE_TYPE: DIRECT_CHANGE_HISTORY
    CLAIM: GOV-013 has current direct policy evolution including the CI failure/root-cause and no-transition gate.
    REF: commit history
    RESULT: PASS
    VALIDATED_AT: 2026-08-25
    SCOPE: temporal provenance
  - EVIDENCE_ID: E-GOV013-003
    EVIDENCE_TYPE: GOVERNANCE_RELATION
    CLAIM: GOV-013A supplements GOV-013 rather than replacing it.
    REF: Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md
    RESULT: PASS
    VALIDATED_AT: 2026-08-25
    SCOPE: authority relationship

ASSERTIONS
  - ASSERTION_ID: A-GOV013-001
    CLAIM: Canonical authority location does not by itself establish current validity.
    STATUS: ACTIVE
    EVIDENCE_IDS: E-GOV013-001,E-GOV013-002
    VALID_FROM: 2026-08-25
    SUPERSEDED_BY: null
  - ASSERTION_ID: A-GOV013-002
    CLAIM: Current repository evidence outranks historical handoff or conversation memory for continuation decisions.
    STATUS: ACTIVE
    EVIDENCE_IDS: E-GOV013-001,E-GOV013-002
    VALID_FROM: 2026-08-25
    SUPERSEDED_BY: null

CONSTRAINTS
  - CONSTRAINT_ID: C-GOV013-001
    RULE: Do not treat this supplemental object as replacement governance authority.
    AUTHORITY: GOV-013
    ENFORCEMENT_SURFACE: KRS-001 migration gate
  - CONSTRAINT_ID: C-GOV013-002
    RULE: Relationship claims must not be promoted beyond the evidence-supported state.
    AUTHORITY: GOV-013
    ENFORCEMENT_SURFACE: relationship/currentness validation

HISTORY
  - STATE: PRE-WRITE / CONTROLLED
    SOURCE: KRS-001_PILOT2_GOV013_CURRENTNESS_RELATIONSHIP_MATRIX
    TRANSITION: objectization authorized after relationship review
  - STATE: PILOT-VERIFIED
    SOURCE: this object
    TRANSITION: currentness and authority relationships reconciled

PAYLOAD
  Human-readable policy remains source-owned. This object is supplemental structured representation only.

INTEGRITY
  SOURCE_INTEGRITY: VERIFIED
  OBJECT_INTEGRITY: STRUCTURAL-VERIFIED
  TRACEABILITY_STATUS: VERIFIED
  MIGRATION_DECISION: PILOT-ONLY / NO-SOURCE-REPLACEMENT
