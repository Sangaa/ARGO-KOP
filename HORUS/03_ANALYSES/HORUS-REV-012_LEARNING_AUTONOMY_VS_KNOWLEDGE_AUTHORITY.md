# HORUS-REV-012 — Learning Autonomy vs Knowledge Authority

Date: 2026-08-23
Status: ANALYTICAL / CANDIDATE
Owner: HORUS
Scope: ARGO learning analysis only
Engineering boundary: HORUS does not perform repository construction; this record is analytical evidence for later consumption by ARGO/HERMUZ.

## 1. Purpose

Separate two dimensions that can otherwise be conflated:

1. how autonomously ARGO can generate or modify learning;
2. how much authority that learning has after generation.

## 2. Evidence

MEM-001 explicitly states that learning may be autonomous while canonical authority acquisition is not. It also separates session, project/deployment, shared-candidate, and platform memory, requiring evidence, validation, scope review, provenance, and authority checks before promotion.

Therefore, autonomous learning and canonical authority are orthogonal dimensions.

## 3. Analytical model

Learning autonomy axis:

`Guided → Adapted → Selected → Improved → Meta-level` 

Knowledge authority axis:

`Working → Local Experience → Shared Candidate → Validated Knowledge → Canonical Platform Knowledge`

A system can move upward on one axis without moving upward on the other.

Examples:

- Autonomous local learning + non-canonical scope is possible.
- Canonical knowledge may exist without being autonomously discovered by the current runtime.
- A system may discover a useful rule autonomously while still requiring external validation before canonical promotion.

## 4. Consequence for ARGO assessment

A future observation of autonomous strategy selection would provide evidence about learning autonomy, but would not by itself justify platform-level authority.

Conversely, a highly governed canonical rule does not prove that ARGO autonomously discovered it.

Therefore:

`Autonomous Discovery ≠ Canonical Truth`

and

`Canonical Truth ≠ Autonomous Discovery`

## 5. New measurement requirement

Every future learning claim should record two independent labels:

- `AUTONOMY_LEVEL`
- `AUTHORITY_LEVEL`

and preserve provenance for both.

## 6. Current assessment

ARGO has strong evidence of structured learning and governed knowledge handling. Autonomous learning is explicitly permitted by the architecture, but the observed record still does not establish autonomous meta-learning or autonomous discovery of the cross-domain abstraction.

The separation itself is now considered a reusable analytical principle.

## 7. Truth status

`LEARNING-AUTHORITY SEPARATION: STRONGLY SUPPORTED`

`AUTONOMOUS META-LEARNING: UNPROVEN`

`AUTONOMOUS DISCOVERY OF CROSS-DOMAIN ABSTRACTION: UNPROVEN`

`WORLD-FACING KNOWLEDGE: NOT PROMOTED`

## 8. Governing principle

Do not use the authority of a knowledge artifact as evidence for the autonomy of its discovery, and do not use autonomous discovery as a substitute for validation and scope authority.

## 9. Routing

Consumer: ARGO learning knowledge layer.
Engineering consumer: HERMUZ only when validated learning changes an engineering decision.
HORUS role: attribution, synthesis, boundary checking, and refinement of learning claims.

End of document.
