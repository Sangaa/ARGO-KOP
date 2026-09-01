# Priority 7 — CORE-003 ↔ ARC-011 Registry Reconciliation — Transaction M

Date: 2026-09-01
State: `RECOVERY-CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`
Failed material candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Failure evidence commit: `6433e8c6246cbb547b66d54c967019e51f845640`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`

## Relationship result under recovery verification

Transaction L's direct-source validation is reconciled into REP-014 as exactly two controlled relationships:

`REL-068 | CORE-003 | ARC-011 | GOVERNS`

`REL-069 | ARC-011 | CORE-003 | REFERENCES`

The two directions deliberately carry different semantics. Constitutional authority establishes the governing direction; ARC-011's explicit subordinate/Related-Documents language establishes the reference direction. Neither direction is promoted to `DEPENDS_ON`.

## Failure retained

The first material candidate passed M2, Real Mutation Matrix and Full-Stack, while Runtime/Integration workflow `33519622061` failed only its `integrity-tests` job. Prototype and integration jobs succeeded. Failure Evidence 01 classifies the cause as a case-sensitive test-assertion drift introduced while rebinding the focused regression, not a source-authority contradiction.

Recovery R1 restores the already-proven exact source assertions from Transaction L while retaining M's exact REL-068/069 and anti-overpromotion assertions. The relationship registry, manifest, Core status, CORE-003 and ARC-011 are not changed by R1.

## Learning retained

Bidirectionality does not imply semantic symmetry. A valid graph pair can contain `GOVERNS` in one direction and `REFERENCES` in the other when each edge has independent source evidence.

Failure learning: during a registry-only conversion, preserve previously proven source assertions verbatim unless source evidence changed. Rephrasing assertions can manufacture test drift unrelated to the material semantics being reconciled.

## Non-claims

No dependency promotion; no source-authority mutation; no Core/Architecture certification; no Phase-1 closure; no Connected Baseline or repository-wide graph closure; no Global PASS.

## Closure gate

M remains open until R1 exact-head required workflows all succeed. The failed candidate remains permanent evidence and is not relabeled as success.
