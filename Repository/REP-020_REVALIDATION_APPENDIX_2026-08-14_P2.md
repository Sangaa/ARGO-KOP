# REP-020 Revalidation Appendix — 2026-08-14 P2

## P0/P1/P2 continuation checkpoint

This appendix extends REP-020 evidence without replacing the canonical matrix.

### TEST-INT-FAIL-003 — PR #4 CI

**Source:** GitHub Actions run `31773186691` for PR #4 head `8f7594de...`.

**Result:** `FAIL / PARTIAL`

- `prototype-tests`: PASS
- `Run prototype acceptance suite`: PASS
- `Run canonical acceptance scenarios`: PASS
- `integration-tests`: FAIL
- failure step: `Run integration quality suite`

The integration suite was previously captured as `78 passed / 2 failed` on the same CI generation. The two failures were classified as:

1. `test_core000_canonical_reference.py` — **STALE_CONTRACT / FORMAT_MISMATCH**. The canonical `CORE-000_PLATFORM_ARCHITECTURE.md` currently declares metadata as separate lines (`Document ID` / `CORE-000`, `Canonical` / `Yes`), while the test required colon-formatted metadata.
2. `test_repository_content_tree_canonicalization.py` — **STALE_MERGE_SNAPSHOT**. The PR merge snapshot used an older `REP-013` state; current `main` contains the required `Specifications/01-Knowledge-Organization.md` path.

### Corrective action

A controlled test-contract correction was applied to PR #4 branch only:

- Commit: `3046cae15a82bedd9d6d252a11000a80989d8bee`
- File: `Quality/Integration/test_core000_canonical_reference.py`
- Change: assert the canonical metadata representation actually present in authoritative `CORE-000`.
- Runtime behavior: unchanged by this correction.
- Integration test intent: unchanged; only stale formatting expectation corrected.

**Required revalidation:** PR #4 CI must rerun after this commit. The second integration failure is not patched in the test; it must be re-evaluated against the current `main` merge snapshot.

### Tests performed

| TEST-ID | Result | Evidence |
|---|---|---|
| PR4-CI-001 | PASS prototype / FAIL integration | run `31773186691` |
| PR4-CORE000-001 | PASS diagnosis | authoritative CORE-000 read on `main` |
| PR4-REP013-001 | PASS diagnosis | current-main REP-013 contains required Specifications path |
| PR4-CONTRACT-001 | PASS mutation | commit `3046cae...` |

### Tests not performed / pending

| TEST-ID | State |
|---|---|
| PR4-CI-002 | PENDING — CI after contract correction |
| PR4-INTEGRATION-002 | PENDING — full integration suite after current-main revalidation |
| REL-EXEC-001 | NOT_PERFORMED — executable RUN-010 → ENG-006 → SRV-009 proof |
| AUTH-BASELINE-001 | CONFLICT — 3.2.1 vs 3.3.0 unresolved |
| DUP-001 | PARTIAL — exhaustive internal-ID closure not complete |
| BOOT-VERIFY-002 | NOT_PERFORMED — wait for blocker closure |

### Integrity decision

**INTEGRITY HOLD.** No PASS promotion and no merge authorized by this checkpoint.

### Matrix impact

Affected nodes/edges:

- `CORE-000` ↔ `test_core000_canonical_reference.py`
- `REP-013` ↔ `test_repository_content_tree_canonicalization.py`
- `RUN-010` / Runtime Prototype authorization state
- Integration Quality verification boundary

Required revalidation chain:

`PR4-CI-002 → Integration revalidation → REP-020 update → baseline reconciliation → executable relationship proof → duplicate closure → Boot re-verification`.
