# P9 Architecture — RUN-007 Runtime Security Baseline Alignment — Transaction P

Transaction ID: `MUT-2026-09-03-P9-RUN007-BASELINE-ALIGNMENT-P`
Priority: `9 — Architecture`
State: `RECOVERY / ATOMIC PACKAGING REPAIR IN PROGRESS`
Entry HEAD: `9ffcf81bad193f964b92f484769a62bb14882380`
Pre-write HEAD: `535b5524ef29fcd892377b9e36e6ce5ea868404e`
First material HEAD: `4b0b9c4ef4195fd53149d80266e50dda930a1467`
Target: `Runtime/RUN-007_RUNTIME_SECURITY.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|
| `RUN-007` | factual metadata repair: Version `1.2.1 → 1.2.2`; Development Baseline `3.3.0 → 3.2.1`; Last Audit `2026-08-09 → 2026-09-03`; add `Release/VERSION.md` as explicit related baseline authority during recovery | Status remains `Validated / Integrity Hold`; Canonical remains Yes; Runtime Security semantics, least-authority boundary, interface/auth/provenance ordering, UNKNOWN handling, recovery and learning boundary preserved | PASS | RECOVERY PENDING |

## Evidence

- Authoritative `Release/VERSION.md` declares `Current Development Baseline: 3.2.1` and latest official release `1.0.0`.
- Direct exact-head reads of `RUN-001`, `RUN-002`, `RUN-003`, `RUN-004`, `RUN-005`, `RUN-006`, `RUN-008`, `RUN-009`, and `RUN-010` align to development baseline `3.2.1` where the field is present.
- Entry-state direct read of `RUN-007_RUNTIME_SECURITY.md` alone declared `Development Baseline: 3.3.0` with blob `4b46f47d6cb5f83cfac195ffb3c238b4c5903fc1`.
- Runtime folder status declares development baseline `3.2.1`; no current Runtime baseline authority supports `3.3.0`.
- Repository code search failed to return the directly observed `3.3.0` string; direct authoritative-path evidence therefore controls.
- Gate-13 semantic review finds RUN-007 content aligned with Architecture: least authority, no Architecture/Governance bypass, interface contract before external execution, authentication distinct from authorization, provenance preservation, `UNKNOWN != SUCCESS`, governed recovery and no automatic learning promotion.

## First material attempt

First material HEAD `4b0b9c4ef4195fd53149d80266e50dda930a1467` correctly changed exactly three metadata facts in `RUN-007`; immutable read-back produced blob `42a4d8c250d07d601b0cfa2ab01229a1bbc2805c`, and exact parent compare showed only `Runtime/RUN-007_RUNTIME_SECURITY.md` with `3 additions / 3 deletions`.

Material CI disposition:
- M2 run `33721644582` — SUCCESS.
- Full-Stack run `33721644628` — FAILURE at `Enforce Mutation Matrix on current change set`.
- Failure evidence: `changed_files=1`, `protected_changes=1`, `mutation_matrices=0`, protected path `Runtime/RUN-007_RUNTIME_SECURITY.md`.

The failure is a transaction-packaging failure, not a RUN-007 semantic/test failure. The pre-write matrix existed in the parent commit, but protected-change enforcement requires the mutation matrix in the same current change set. The gate is preserved; no test is weakened or bypassed.

## Recovery design

Use Git Data atomic tree/commit capability to update both the protected RUN-007 target and this mutation matrix in one commit. The protected target receives one evidence-hardening change justified by the detected drift: `Release/VERSION.md` is added to Related Documents as the explicit authoritative source for baseline metadata. This prevents the recovery from manufacturing an unrelated semantic change and makes the provenance of the corrected baseline explicit.

Recovery acceptance:
- one atomic commit contains both `Runtime/RUN-007_RUNTIME_SECURITY.md` and this matrix;
- RUN-007 retains corrected baseline `3.2.1`, version `1.2.2`, audit `2026-09-03`, and all security semantics;
- exact compare from failed material HEAD to recovery HEAD contains exactly the target and matrix;
- protected-change enforcement, Full-Stack and applicable Runtime/M2 checks must pass before closure.

## Non-claims

- This transaction does not close Gate 13.
- It does not certify Runtime or Interfaces.
- It does not change Runtime Security authority or operational semantics.
- It does not resolve Runtime folder cross-layer holds, interface implementation proof or repository control-plane gaps.
- Transaction B / REL-073 remains separate local Registry hold.

Validation plan:
`atomic target+matrix recovery → immutable read-back → exact parent compare → exact-head CI → finalize matrix → closure-head CI`.
