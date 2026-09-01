# Priority 7 — RUN-002 → CORE-003 Initialization Authority Reference — Transaction R

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / VALIDATION-FIRST / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-RUN002-CORE003-REFERENCE-R`
Work Lease: `HERMUZ-P7-R-RUN002-CORE003-20260901`
Entry HEAD: `abfa867f2fa5d34ac1430f39e2c40143327f1018`
Pre-write Matrix HEAD: `33ce1e490b07fa1a123930b3c7dd958c471924c3`

## Finding

Direct current source evidence supports only the bounded one-way candidate:

`RUN-002 → CORE-003 = REFERENCES`

Disposition:

`INTENTIONAL ONE-WAY / INITIALIZATION-AUTHORITY-RESOLUTION-ALIGNED / NON-DEPENDENCY`.

## Why this reference is material

`Runtime/RUN-002_INITIALIZATION.md` is canonical and critical. It defines the Runtime initialization gate executed after boot, requires validation before execution, requires each component to verify declared dependencies, prohibits `READY` while required integrity is failed/held, and enters governed `FAULT` / `HOLD` when required authority cannot be resolved.

RUN-002 directly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents.

That makes the direct documentary reference relevant to material initialization/authority resolution rather than mere navigation.

## Why no reverse or stronger edge

`CORE-003` generally governs repository components within applicable scope, but RUN-002 does not contain a source-specific constitutional non-override statement comparable to RUN-003. Transaction R therefore does not create or validate a separately enumerated `CORE-003 → RUN-002 = GOVERNS` row.

No source evidence establishes `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, executable coupling or reverse documentary semantics between these exact artifacts.

## Registry boundary

REP-014 v1.2.14 is deliberately not a complete graph and currently contains no RUN-002/CORE-003 pair. R is validation-first and requires the registry to remain unchanged during proof.

Any later registry synchronization must be separately justified after exact-head validation and fresh Priority-7 recomputation.

## Prior learning

- Transactions P/Q — `DIRECTLY APPLICABLE`: distinguish source-specific authority proof from broad constitutional applicability.
- Transactions N/O — `DIRECTLY APPLICABLE`: one-way documentary validation-first then separate synchronization.
- REL-037/038 — `TRANSFERABLE`: Runtime authority precedent, not copied mechanically because current evidence differs.
- ARC_MAP boundary — `TRANSFERABLE NEGATIVE`: navigation/listing alone does not create a registry relationship.

No new governance rule is warranted.

## Forbidden promotion

R does not support or claim:

- `RUN-002 → CORE-003 = DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES`;
- any `CORE-003 → RUN-002` registry row;
- executable/runtime reachability proof;
- Runtime folder certification;
- Core folder certification;
- Priority-7 closure;
- Phase-1 closure;
- Connected Baseline closure;
- repository-wide graph completion;
- Global PASS.

## Verification contract

The focused regression binds exact RUN-002 initialization/authority-resolution evidence, direct CORE-003 reference, validation-first registry absence, forbidden stronger/reverse semantics, and continued Core hold/certification-pending state.

Required path:

`EXACT-HEAD READ-BACK → ONE-COMMIT/THREE-PATH SCOPE CHECK → FOUR REQUIRED WORKFLOWS → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

Work Lease remains `OPEN` until that sequence completes.
