# Priority 7 — CORE-003 ↔ RUN-003 Authority Seam — Transaction P

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / VALIDATION-FIRST / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-AUTHORITY-P`
Work Lease: `HERMUZ-P7-P-CORE003-RUN003-20260901`
Entry HEAD: `1392b031a49c187453daa2f03cfa8250aa08e6db`
Pre-write Matrix HEAD: `86fe1d5d4ea905dd70104b8d3d9bb15753a659f8`

## Finding

Direct current source evidence supports the bounded candidate pair:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

Disposition:

`BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`

## Direct evidence

`Core/CORE-003_CONSTITUTION.md` states that the Constitution defines the highest governing rules of ARGO and that all repository components shall comply with it within applicable scope.

`Runtime/RUN-003_CONFIGURATION.md` is `Canonical: Yes`, `Priority: Critical`, controls runtime behavior, states that configuration does not modify repository architecture or authority, and explicitly states under its Authority Boundary that Runtime configuration does not override `Core/CORE-003_CONSTITUTION.md`. The same file directly lists CORE-003 under Related Documents and states that repository authority remains above runtime assumptions.

This is materially stronger than a bare Related Documents mention because RUN-003 can change execution behavior while explicitly declaring the constitutional non-override boundary.

## Registry boundary

Current REP-014 v1.2.13 is deliberately not a complete graph. Transaction P therefore does not register the pair merely because a reference exists.

Validation-first P requires the registry to remain without:

- `CORE-003 → RUN-003 = GOVERNS`;
- `RUN-003 → CORE-003 = REFERENCES`;

until exact-head validation succeeds and a separate current-state recomputation determines whether registry synchronization is the next legal obligation.

## Prior learning

- REL-037/038 `CORE-003 ↔ RUN-001` — `DIRECTLY APPLICABLE`: same Constitution→critical Runtime governing/reference pattern.
- Transactions L/M — `TRANSFERABLE`: authority subordination/non-override is distinct from dependency.
- Transactions N/O — `TRANSFERABLE`: validation-first proof is separated from registry synchronization.

No new governance rule is warranted by this finding.

## Forbidden promotion

Transaction P does not support or claim:

- `RUN-003 → CORE-003 = DEPENDS_ON`;
- reverse `RUN-003 → CORE-003 = GOVERNS`;
- `IMPLEMENTS` or `CONSUMES` in either direction;
- executable or runtime reachability proof;
- Runtime folder certification;
- Core folder certification;
- Priority-7 closure;
- Phase-1 closure;
- Connected Baseline closure;
- repository-wide graph completion;
- Global PASS.

## Verification contract

The focused regression binds exact direct source semantics, absence of premature REP-014 registration, forbidden stronger relationship types, and continued Core `CROSS-LAYER VALIDATION OPEN` / Folder Certification pending state.

Required closure path:

`EXACT-HEAD READ-BACK → ONE-COMMIT/THREE-PATH SCOPE CHECK → FOUR REQUIRED WORKFLOWS → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Work Lease remains `OPEN` until that sequence completes.
