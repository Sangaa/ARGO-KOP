# P266 — Mutation Matrix

Status: `APPLIED / HETEROGENEOUS PILOT ONLY`
Parent: `afc85d60829e677723838b31dac7a2b1c6195489`

| Change | Risk | Control | Validation |
|---|---|---|---|
| Add EJR-328 KRS object pilot | semantic loss / false promotion | preserve source authority; KRS-KO/0.2 only | read-back + exact-SHA CI |
| Add this matrix | governance drift | same atomic changeset | read-back + exact-SHA CI |

## Measurements
- Source class: Engineering/Integration Seam Audit.
- Candidate class: KRS Knowledge Object.
- Size comparison: record exact byte counts at verification; do not infer compression from file count.
- Operational comparison: authority, provenance, typed relationships, evidence classification, assertions, constraints, history, and human reviewability.

## Explicit Non-Changes
- No source artifact modified or deleted.
- No canonical authority changed.
- No runtime behavior changed.
- No new schema created.
- No migration or retirement performed.

## Gate
Pilot result must separately establish semantic preservation and any size/operational advantage. Migration remains blocked until equivalence, integrity, relationship validation, runtime compatibility where applicable, regression evidence, and a production-safe migration path are demonstrated.

## Session Closure
`Execute → Read-back → Exact-SHA CI → classify evidence → close; no promotion on absent proof.`