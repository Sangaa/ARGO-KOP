# EJR-173 — REP-020 Matrix Expansion / Control-Plane Reconciliation

**Date:** 2026-08-13
**Status:** Active / Audit-derived checkpoint
**Baseline:** 3.2.1

## Work completed

Re-read the current `REP-020`, `REP-013`, and `REP-014` before extending the relationship matrix.

Confirmed that `REP-020` is already a provisional Phase-1 seed, not an authority, and that it contains 21 initial control-plane/provenance edges. `REP-013` confirms the physical control-plane inventory; `REP-014` supplies the relationship contract and inspected relationship evidence.

## Matrix expansion rule

The matrix will be populated during review, not after review. Each inspected artifact must contribute:

- node metadata;
- authoritative source;
- baseline/version;
- freshness;
- verified checkpoint;
- outgoing relationships;
- incoming/reverse relationships where independently evidenced;
- consumer/dependency impact;
- revalidation trigger.

No relationship is promoted to `VERIFIED` solely because it appears in either registry.

## Current high-value review target

The next expansion scope is the control-plane-to-domain boundary. The control plane is structurally represented, while domain semantic relationships remain incomplete. This is the point where the matrix should prevent repeated rediscovery and expose missing reverse edges.

## Findings

1. `REP-020` is correctly aligned to baseline `3.2.1`.
2. `REP-013` explicitly warns that its inventory is progressive and not exhaustive; therefore wildcard entries such as `Services/SRV-001_*.md` cannot be treated as exact artifact identities.
3. `REP-014` explicitly states that a reference is not automatically a relationship and requires evidence, authority, impact, consumer scope and checkpoint.
4. The control-plane graph can be reused as the initial impact surface, but it must not be mistaken for the complete repository graph.
5. The next useful optimization is exact enumeration of currently wildcarded high-value folders, beginning with Services, followed by relationship evidence for their consumers/dependencies.

## New engineering knowledge

The matrix is most valuable when populated at the same moment an artifact is inspected. Delaying matrix updates creates a second discovery pass and recreates the very cost the matrix is intended to remove.

Therefore the working rule is:

> **Inspect once → capture node → capture edges → capture impact → continue.**

## Integrity

`INTEGRITY HOLD` remains unchanged. No certification or closure is inferred from matrix completeness.

## Next recovery point

Enumerate exact Service artifact filenames from current repository evidence and add verified/provisional nodes and edges to REP-020 while reviewing them. Preserve wildcard entries until exact physical evidence replaces them.
