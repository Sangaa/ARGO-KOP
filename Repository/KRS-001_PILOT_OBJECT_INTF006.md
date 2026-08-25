# KRS-001 Pilot Knowledge Object — INTF-006

OBJECT_FORMAT: KRS-KO/0.1
OBJECT_ID: INTF-006
OBJECT_TYPE: CANONICAL_INTERFACE
SOURCE_PATH: Interfaces/INTF-006_ENVIRONMENT_SENSING.md
SOURCE_DOCUMENT_VERSION: 1.1.1
SOURCE_STATUS: Proposed / Integrity Hold
SOURCE_CANONICAL: Yes
SOURCE_AUDIT: 2026-08-10

## CONTROL
CURRENTNESS: CURRENT-BUT-STALE-DEPENDENCY
AUTHORITY: Interface contract authority remains the source artifact.
MIGRATION_STATUS: PILOT-ONLY
PRODUCTION_AUTHORITY: NONE

## PROVENANCE
SOURCE_REF: cf4b2edd482120ebae4c17180b41e74b1df0f3d7
LATEST_DIRECT_CHANGE_EVIDENCE: P223/P224 lineage
P224_EVIDENCE: commit 8b43512e6b98af65172f98786ea0f57a3e7a3381; CI run 32887640103

## RELATIONSHIPS
ARCHITECTURE: Architecture/ARC-007_INTEGRATION_MODEL.md
INTEGRATION: Interfaces/INTF-010_INTEGRATIONS.md
RUNTIME: Runtime/RUN-005_RUNTIME_WORKFLOW.md
TEST: Quality/Integrity/test_environment_sensing_boundary.py
SESSION_EVIDENCE: Repository/REP-020_SESSION_DELTA_2026-08-25_P224_INTF006_SAFE_SEAM_VERIFICATION.md

## EVIDENCE
STRUCTURAL: VERIFIED
CONTRACT: VERIFIED
IMPLEMENTED: UNPROVEN
INTEGRATION_TESTED: BOUNDED-NON-PRODUCTION
RUNTIME_VERIFIED: UNPROVEN

## ASSERTIONS
A001: Canonicality defines the contract/evidence boundary, not implementation readiness.
A002: Production provider/consumer is not established.
A003: Synthetic seam evidence must not be promoted to production evidence.
A004: Raw observation remains distinct from interpretation and verified fact.

## CONSTRAINTS
C001: No fabricated sensing source/provider/permission/runtime call.
C002: Authorization and provenance remain explicit.
C003: Unknown sensing state remains distinct from successful acquisition.
C004: Original Markdown remains authoritative during the pilot.

## HISTORY
H001: P223 established implementation/consumer frontier as unproven.
H002: P224 established a bounded synthetic seam and verified it through CI without production promotion.

## PAYLOAD
This object is a traceability representation only. It intentionally does not copy the full semantic payload of INTF-006. The source artifact remains the authoritative human-readable contract.

## INTEGRITY
PILOT_ASSERTION: The structured representation is supplemental and must not replace the source until the pilot proves improved traceability and validation.
