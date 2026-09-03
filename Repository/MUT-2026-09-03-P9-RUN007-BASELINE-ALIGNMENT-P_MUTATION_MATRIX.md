# P9 Architecture — RUN-007 Runtime Security Baseline Alignment — Transaction P

Transaction ID: `MUT-2026-09-03-P9-RUN007-BASELINE-ALIGNMENT-P`
Priority: `9 — Architecture`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `9ffcf81bad193f964b92f484769a62bb14882380`
Pre-write HEAD: `535b5524ef29fcd892377b9e36e6ce5ea868404e`
First material HEAD: `4b0b9c4ef4195fd53149d80266e50dda930a1467`
Recovery material HEAD: `deadc418010283a83fbbe7f076214a2df1f40e34`
Target: `Runtime/RUN-007_RUNTIME_SECURITY.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|
| `RUN-007` | factual metadata repair: Version `1.2.1 → 1.2.2`; Development Baseline `3.3.0 → 3.2.1`; Last Audit `2026-08-09 → 2026-09-03`; add `Release/VERSION.md` as explicit related baseline authority during recovery | Status remains `Validated / Integrity Hold`; Canonical remains Yes; Runtime Security semantics, least-authority boundary, interface/auth/provenance ordering, UNKNOWN handling, recovery and learning boundary preserved | PASS | PASS |

## Evidence

- Authoritative `Release/VERSION.md` declares `Current Development Baseline: 3.2.1` and latest official release `1.0.0`.
- Direct exact-head reads of `RUN-001`, `RUN-002`, `RUN-003`, `RUN-004`, `RUN-005`, `RUN-006`, `RUN-008`, `RUN-009`, and `RUN-010` align to development baseline `3.2.1` where the field is present.
- Entry-state direct read of `RUN-007_RUNTIME_SECURITY.md` alone declared `Development Baseline: 3.3.0` with blob `4b46f47d6cb5f83cfac195ffb3c238b4c5903fc1`.
- Runtime folder status declares development baseline `3.2.1`; no current Runtime baseline authority supports `3.3.0`.
- Repository code search failed to return the directly observed `3.3.0` string; direct authoritative-path evidence therefore controls.
- Gate-13 semantic review finds RUN-007 content aligned with Architecture: least authority, no Architecture/Governance bypass, interface contract before external execution, authentication distinct from authorization, provenance preservation, `UNKNOWN != SUCCESS`, governed recovery and no automatic learning promotion.

## First material attempt and failure preservation

First material HEAD `4b0b9c4ef4195fd53149d80266e50dda930a1467` correctly changed exactly three metadata facts in `RUN-007`; immutable read-back produced blob `42a4d8c250d07d601b0cfa2ab01229a1bbc2805c`, and exact parent compare showed only `Runtime/RUN-007_RUNTIME_SECURITY.md` with `3 additions / 3 deletions`.

Material CI disposition:
- M2 run `33721644582` — SUCCESS.
- Full-Stack run `33721644628` — FAILURE at `Enforce Mutation Matrix on current change set`.
- Failure evidence: `changed_files=1`, `protected_changes=1`, `mutation_matrices=0`, protected path `Runtime/RUN-007_RUNTIME_SECURITY.md`.

The failure was a transaction-packaging failure, not a RUN-007 semantic/test failure. The pre-write matrix existed in the parent commit, but protected-change enforcement requires the mutation matrix in the same current change set. The gate was preserved; no test was weakened or bypassed.

## Atomic recovery

Git Data atomic tree/commit capability was used to update both the protected RUN-007 target and this mutation matrix in one fast-forward commit. The protected target received one evidence-hardening change justified by the detected drift: `Release/VERSION.md` was added to Related Documents as the explicit authoritative source for baseline metadata.

Recovery verification:
- Recovery HEAD: `deadc418010283a83fbbe7f076214a2df1f40e34`.
- Final RUN-007 blob: `26c353a727b768bf716f5f6f1eed2c6ef5b9fce2`.
- Exact compare `4b0b9c4ef4195fd53149d80266e50dda930a1467 → deadc418010283a83fbbe7f076214a2df1f40e34` changes exactly two files: this matrix (`31 additions / 8 deletions`) and `Runtime/RUN-007_RUNTIME_SECURITY.md` (`1 addition / 0 deletions`).
- RUN-007 read-back confirms Version `1.2.2`, Development Baseline `3.2.1`, Last Audit `2026-09-03`, Status `Validated / Integrity Hold`, all security semantics preserved, and `Release/VERSION.md` added as baseline authority reference.

Recovery exact-head CI:
- Full-Stack Repository Audit `33721850926` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests `33721850938` — SUCCESS.
- Real Mutation Matrix Regression `33721850928` — SUCCESS.
- M2 Multi-Channel Proposal Training `33721850927` — SUCCESS.

## Learning captured

For protected-file transactions under the current Full-Stack enforcement, a mutation matrix created only in the parent commit is not sufficient when the protected target is changed by a later one-file contents-API commit. The protected target and the mutation matrix must be present in the same current change set. The available Git Data `blob → tree → commit → fast-forward ref` path provides a bounded atomic packaging mechanism without weakening tests or rewriting unrelated files.

## Non-claims

- This transaction does not close Gate 13.
- It does not certify Runtime or Interfaces.
- It does not change Runtime Security authority or operational semantics.
- It does not resolve Runtime folder cross-layer holds, interface implementation proof or repository control-plane gaps.
- Transaction B / REL-073 remains separate local Registry hold.

Closure:
`CLOSED / VERIFIED / RESUME-SAFE` after exact recovery-head 4/4 CI; closure-head workflow verification remains required before advancing the next protected mutation.
