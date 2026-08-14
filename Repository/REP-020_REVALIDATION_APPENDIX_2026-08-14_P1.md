# REP-020 Revalidation Appendix — 2026-08-14

This appendix extends the evidence ledger of REP-020 without replacing its canonical matrix content.

## Latest integration evidence

| TEST-ID | Source | Result | Evidence | Impact |
|---|---|---|---|---|
| INT-FAIL-002 | GitHub Actions run 31772269633 / job 94681554508 | CONFLICT | `python -m pytest -q`: 78 passed, 2 failed | Integration contract revalidation required |
| INT-FAIL-002-A | `test_core000_canonical_reference.py` | STALE_CONTRACT / FORMAT_MISMATCH | Expected `Document ID: CORE-000`; CORE-000 uses separate metadata lines | CORE-000 ↔ integration contract |
| INT-FAIL-002-B | `test_repository_content_tree_canonicalization.py` | STALE_MERGE_SNAPSHOT | PR #3 merge commit tested an older REP-013 state; current main contains the required Specifications path | REP-013 ↔ integration suite |

## Runtime candidate

| TEST-ID | Source | Result | Evidence | Impact |
|---|---|---|---|---|
| PR4-CAND-001 | PR #4, head `8f7594decc80a45bdc22fab3afdcefd6a4a2b7dd` | QUEUED | Candidate created from current main; one Runtime Prototype file changed | RUN-010 / prototype state semantics |

PR #4 changes only the unreachable `REJECTED` state/branch in `Runtime/Prototype/cognitive_loop_harness.py`. No integration tests were modified.

## Tests performed

- PR #3 integration workflow inspection — PASS for environment/setup, FAIL semantic suite.
- Full integration log extraction — PASS (exact failures captured).
- Current-main CORE-000 comparison — PASS.
- Current-main REP-013 comparison — PASS.
- PR #4 candidate creation from latest main — PASS.

## Tests not yet performed

- PR #4 CI final result — QUEUED.
- Post-PR4 integration rerun — NOT PERFORMED.
- Full prototype regression after PR4 — NOT PERFORMED.
- Executable RUN-010 → ENG-006 → SRV-009 proof — NOT PERFORMED / documentation only.
- Baseline 3.2.1 vs 3.3.0 authority reconciliation — NOT RESOLVED.
- Exhaustive internal-ID duplicate closure — PARTIAL.

## Integrity

Current decision remains **INTEGRITY HOLD**. This appendix does not promote REP-020 or ARGO to PASS.

## Required revalidation

1. Run PR #4 CI.
2. If integration still fails, distinguish CORE-000 format contract from test defect before mutation.
3. Revalidate REP-013 against current main state.
4. Update the main REP-020 matrix content in the next controlled documentation mutation.
5. Continue baseline and executable relationship proof.
