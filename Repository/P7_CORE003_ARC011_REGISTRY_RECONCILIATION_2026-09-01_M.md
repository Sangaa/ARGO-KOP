# Priority 7 — CORE-003 ↔ ARC-011 Registry Reconciliation — Transaction M

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`

## Result under verification

Transaction L's direct-source validation is reconciled into REP-014 as exactly two controlled relationships:

`REL-068 | CORE-003 | ARC-011 | GOVERNS`

`REL-069 | ARC-011 | CORE-003 | REFERENCES`

The two directions deliberately carry different semantics. Constitutional authority establishes the governing direction; ARC-011's explicit subordinate/Related-Documents language establishes the reference direction. Neither direction is promoted to `DEPENDS_ON`.

## Material unit

Authorized candidate paths are limited to REP-014, current control-plane manifest, Core folder status, focused integrity regression, this record and the rebound pre-write Matrix. CORE-003 and ARC-011 source content remain unchanged.

## Learning candidate

Bidirectionality does not imply semantic symmetry. A valid graph pair can contain `GOVERNS` in one direction and `REFERENCES` in the other when each edge has independent source evidence. Relationship reconciliation must preserve edge-specific semantics rather than normalize a pair to one type.

## Non-claims

No dependency promotion; no source-authority mutation; no Core/Architecture certification; no Phase-1 closure; no Connected Baseline or repository-wide graph closure; no Global PASS.

## Closure gate

This record remains candidate-only until exact-head read-back, diff-scope verification and all required CI/runtime/integrity workflows succeed. On failure, evidence is retained and the Work Lease remains open/held rather than rewritten as success.
