# GT-050 — Test Architecture: Shared Capability + P6 Domain Separation

Date: 2026-08-24
Status: PROPOSAL RECORDED / IMPLEMENTATION DEFERRED

## Decision

Adopt a layered test architecture rather than maintaining separate GitHub tool implementations for P6 and pre-P6 tests.

The preferred model is:

- **L0 — Shared Capability Tests:** GitHub/repository capabilities such as files, Blob/Tree/Commit objects, branches, PRs, reviews, patches, and Actions observation.
- **L1 — Repository Integrity Tests:** repository identity, SHA binding, structural relationships, canonical state, and state-transition integrity.
- **L2 — Evidence & Provenance Tests:** provenance, evidence independence, execution identity, semantic classification, and evidence-surface attribution.
- **L3 — P6 Integration Tests:** runtime lineage, P6 identity, execution evidence, downstream observation state, and final P6 decision/validation.

P6 should reuse the shared tooling layers rather than duplicate GitHub connector infrastructure.

## Rationale

Training established that GitHub capabilities are reusable across domains, while P6 adds a higher-order integration/evidence contract. Existing probes also demonstrate that capability, surface availability, execution evidence, and semantic authority must not be conflated.

GT-043 is a concrete example: the test-only runtime-lineage adapter proves compatibility across an explicit boundary but does not authorize production promotion. A verified upstream identity is not automatically downstream semantic authority.

## Post-Training Test Reassessment Plan

After the GitHub tool training phase reaches its intended completion point:

1. Freeze the current test state.
2. Inventory existing tests and probes; reuse existing evidence rather than recreating probes.
3. Classify each test into L0/L1/L2/L3.
4. Identify duplicate, obsolete, hypothetical, fixture-drift, and genuinely failing tests.
5. Remove or redesign tests that depend on unsupported capabilities or false assumptions.
6. Establish a clean baseline.
7. Reassess P6 using the layered model.
8. Only then authorize targeted mutations required to close real gaps.

## Capability Re-evaluation Trigger

During active P6 work, if a failure indicates that the current GitHub tool surface is insufficient or misunderstood:

`STOP → search connector capabilities → search existing repository probes → test the newly discovered capability → update the model → resume`

Absence of evidence on one surface must not be interpreted as proof that an event or capability does not exist.

## Non-Goals

This proposal does not:

- authorize production adapter changes;
- authorize immediate migration of existing tests;
- declare the current suite clean;
- replace existing canonical governance;
- introduce duplicate P6-specific GitHub tooling.

## Relationship to P6

P6 remains the active integration target. The test-only GT-043 bridge demonstrated a controlled path from verified runtime lineage to P6 evidence while explicitly retaining observation provenance and rejecting unverified lineage.

The next P6 work should therefore use the shared capability layers and add only the domain-specific contract needed for P6.

## Future Architecture Note

This layered test architecture should later be evaluated alongside the proposed Document/BLOB/EDI object model. The two efforts are related but must remain separate decisions until the test baseline is clean.

## Closure

GT-050 records the agreed architecture direction. No existing test was modified by this proposal.
