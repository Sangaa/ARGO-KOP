# EJR-300 — GT-039 Provenance Root/Parent Consistency

Date: 2026-08-24
Status: VERIFIED BY CONTROLLED REGRESSION / CI EXECUTION PENDING
Scope: `Quality/Integration/test_evidence_reasoning_classification.py`

## Problem

GT-039 tests a child observation that declares:

- `provenance_root = ROOT-B`
- `provenance_parent = ROOT-A`

while both `ROOT-A` and `ROOT-B` exist as provenance anchors.

The child therefore claims a direct parent under `ROOT-A` while simultaneously declaring a different provenance root, `ROOT-B`.

## Decision

This is **INVALID PROVENANCE**, not a claim-level **CONTRADICTION**.

Reason:

1. `CONTRADICTION` is reserved for conflicting observed values of the same validated claim identity.
2. `provenance_parent` and `provenance_root` describe lineage structure, not the observed value of the domain claim.
3. A child whose declared root disagrees with the root of its declared parent violates the provenance graph invariant.
4. Because provenance integrity is invalid, downstream evidence classification must not select a winner or promote corroboration. The classifier therefore returns **UNRESOLVED** for a comparison requiring that provenance graph.

## Implementation

`provenance_graph_state()` now validates not only missing links and cycles, but also parent/root consistency.

For a node with a declared parent:

`child.provenance_root == parent.provenance_root`

must hold when both roots are explicitly declared.

The existing valid-anchor case remains valid when:

`child.provenance_root == parent.provenance_root == parent.evidence_id`

## Regression Coverage

Added:

- `test_gt039_root_parent_mismatch_is_invalid_provenance_not_claim_contradiction`
- `test_gt039_matching_root_and_parent_remains_valid`

The first test contains explicit `ROOT-A`, `ROOT-B`, and `CHILD` observations and asserts:

- `provenance_graph_state(...) == "INVALID PROVENANCE"`
- classification is `UNRESOLVED` rather than `CONTRADICTION`

The second test proves the matched root/parent case remains `VALID PROVENANCE` and `CONSISTENT / CORRELATED`.

## Evidence Boundary

The mutation was committed as:

`8ba54980c0e8eb684d00c6be739b109d0deb5a58`

The repository's `runtime-prototype-tests.yml` workflow includes `Quality/Integration/**` in its push trigger and runs `python -m pytest -q Quality/Integration`. No workflow run was exposed for this commit at verification time, so CI/runtime execution is **not claimed**.

## Learning

Provenance root and parent are not competing claims to be resolved by authority. They are graph constraints. When the constraints disagree, the correct state is an invalid provenance graph, and dependent evidence reasoning remains unresolved until provenance is repaired.

This is a reusable boundary for future provenance tests: **graph-structural invalidity must be detected before claim-value contradiction logic is applied.**
