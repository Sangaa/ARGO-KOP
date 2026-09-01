# Priority 7 — CORE-000 Canonical Architecture Drift — I

Date: 2026-09-01
State: `ATOMIC CANDIDATE / CI PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I`
Entry HEAD: `f8fc6d4e26518ed09e0227ff458337bbbd68712d`

## Finding

Direct live-main review confirmed that `Core/CORE-000_PLATFORM_ARCHITECTURE.md` still carried a superseded structural model: eight primary architectural components and `Archive` as active Layer 8.

Current canonical Architecture authority independently converges on the nine-boundary model:

`Identity/Core → Governance → Architecture → Repository → Knowledge/Specifications/Standards → Memory → Cognition/Engine → Runtime/Services/AI → Projects/Applied Artifacts`.

`Archive` is a repository preservation domain and is not an active dependency layer.

## Candidate Repair

Transaction I performs one bounded material correction:

- reconcile CORE-000 structural-boundary content to the current ARC-011-aligned model;
- preserve Core-level platform architecture intent without creating a competing structural authority;
- advance CORE-000 review metadata because CORE-000 itself is materially revalidated;
- synchronize `Core/_FOLDER_STATUS.md` without promoting Core certification;
- add a semantic regression that checks the nine-boundary order and Archive boundary without freezing incidental prose;
- preserve REP-014 and the current control-plane manifest unchanged.

## Atomicity

The candidate is constructed through Git objects and must contain exactly these I surfaces in one commit:

1. `Core/CORE-000_PLATFORM_ARCHITECTURE.md`
2. `Core/_FOLDER_STATUS.md`
3. `Quality/Integrity/test_core000_canonical_architecture_boundary.py`
4. `Repository/P7_CORE000_CANONICAL_ARCHITECTURE_DRIFT_2026-09-01_I.md`
5. `Repository/MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I_MUTATION_MATRIX.md`

## Validation Boundary

Candidate closure requires exact-head success for:

- Runtime/Integration;
- Full-Stack;
- M2;
- Real Mutation Matrix Regression.

Any required failure reopens GOV-013 §9B HARD HOLD and blocks closure.

## Explicit Non-Claims

- Priority 7 remains OPEN.
- Core certification is not claimed.
- Architecture certification is not claimed.
- No REP-014 relationship is registered by I.
- Phase 1 and Global Connected Baseline remain OPEN.

## Resume-Safe Rule

After exact-head CI succeeds, this record and the mutation matrix must be closed against the verified candidate lineage before any new Priority-7 transaction is opened.
