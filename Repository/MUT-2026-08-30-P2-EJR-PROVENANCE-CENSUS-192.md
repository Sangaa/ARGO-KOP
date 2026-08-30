# P2 EJR PROVENANCE CENSUS — LEASE 192

Transaction ID: `MUT-2026-08-30-P2-EJR-PROVENANCE-CENSUS-192`
Lease: `R71-20260830-P2-EJR-PROVENANCE-CENSUS-192`
Protocol: HERMUZ / GOV-014
Status: `CLOSED / ANALYTICAL CENSUS COMPLETE / NO EJR MUTATION / RESUME-SAFE`
Entry head: `ed4036c86a0e5c2e3900776106eedfbaf7a47793`
Prewrite head: `595ebd23e393bc7eb57de6930d60ce7211a66e9a`

## Scope

Classify the bounded Priority-2 EJR ambiguity groups containing at least one explicit `Document ID` claim. No EJR rename, delete, suppression or normalization was authorized.

## Exact source evidence

Lease-191 Internal-ID artifact: `9731526902`.
Digest: `sha256:92e07c6b47bf17d97f76e8a2557acd039101a5fddde366c18f452202c38ae67d`.

Exact census from that artifact:

- ambiguous groups: `144`;
- EJR ambiguous groups: `121`;
- EJR groups containing `DOCUMENT_ID_FIELD`: exactly `6`;
- bounded IDs: `EJR-003`, `EJR-026`, `EJR-180`, `EJR-181`, `EJR-182`, `EJR-183`.

## Bounded classifications

### EJR-003 — EARLY EXPLICIT CLAIM + LATER DISTINCT REUSE

- explicit metadata: `Memory/Engineering_Journal/EJR-003_2026-08-09_HERMUZ_SESSION_HANDOFF_FAILURE_ANALYSIS.md`;
- later H1 identity: `Memory/Engineering_Journal/EJR-003_P6_FALSE_POSITIVE_EXECUTION.md`;
- explicit record entered Git at `c720931674b2f2bdfe046efa84ad47199971dd36` on 2026-08-09;
- later distinct record is dated 2026-08-19.

This is real later reuse, not parser-only ambiguity.

### EJR-026 — CONFIRMED ALLOCATION / DISCOVERY DEFECT

- H1 record `EJR-026_2026-08-11_OPERATIONAL_MEMORY_BUILD_AND_REPOSITORY_REBALANCE.md` entered Git at `94fada3d5769a974241c8ade9593685100ff0624` on 2026-08-11;
- later repair committed `EJR-026_2026-08-10_RUNTIME_BASELINE_REVALIDATION.md` at `5ac96480be18e3fd2aa934795c72833161450de2` on 2026-08-17 with message `assign unique identity`.

Therefore the supposedly unique replacement ID was already occupied in repository history.

### EJR-180 — UNRESOLVED MULTI-CLAIM / HISTORICAL REUSE

Five distinct records share EJR-180: four H1-derived claims and one explicit metadata claim. Multiple H1 records date to 2026-08-14; the explicit metadata learning record entered Git at `6f5de15aff4375055382ab4413f156d1f154e983` on 2026-08-16.

No unique owner is promoted merely because one member has stronger metadata syntax.

### EJR-181 — CONFIRMED ALLOCATION / DISCOVERY DEFECT

The explicit reconciliation record states that it was migrated from conflicting `EJR-013` to `EJR-181`. Git records that migration at `c144f7e6113ec301e76290d34f4ae22f0cc796e0` on 2026-08-17. Distinct EJR-181 H1 journal records already existed from 2026-08-14/16.

The repair allocator therefore selected an occupied journal number.

### EJR-182 — UNRESOLVED MULTI-CLAIM / PRE-EXISTING REUSE

A representative H1 EJR-182 record entered Git at `74737bc06ac07e490238496036e62c253b58b0cc` on 2026-08-14. The explicit `CONTROLLED_DOCUMENT_MUTATION_LEARNING` record entered at `79cc006db596c99f1f7f815e29d43e3697899dc1` on 2026-08-17.

Chronology therefore prevents treating explicit metadata strength as ownership proof.

### EJR-183 — CONFIRMED ALLOCATION / DISCOVERY DEFECT

`EJR-183_2026-08-14_BASELINE_AUTHORITY_CONFLICT_REVIEW.md` entered Git at `097ad9b95eecee25e61eb4a79a45ae5d731d20f0` on 2026-08-14. A later P2 identity correction migrated another record from EJR-182 to EJR-183 at `48e87ad71b01ad89e9f48f81f990e85e52e503fb` on 2026-08-17.

This directly proves that historical repair allocation could miss pre-existing H1 identity claims.

## Root cause

The historical identity-repair process did not prove namespace vacancy across every identity-bearing surface before allocating a replacement EJR number.

Required future allocation precondition:

`CANDIDATE EJR ID → METADATA CLAIM SEARCH → H1 CLAIM SEARCH → FILENAME CLAIM SEARCH → GIT-HISTORY EXISTENCE CHECK → ONLY THEN ALLOCATE`

This refines REP-012's existing `ALLOCATE → READ → VERIFY IDENTITY...` rule with the missing occupancy/discovery gate.

## Tooling incident

A separate census artifact and updated Matrix were prepared as exact Git blobs, but `create_tree` was blocked twice by the tool-policy layer before any functional tree or repository mutation occurred. The live branch remained at the 192 prewrite head during both attempts.

No unsafe fallback, partial tree, EJR mutation or detector suppression was performed. The analytical evidence is persisted in this Lease instead.

Learning:

`AN ALLOCATION REPAIR IS NOT SAFE UNTIL VACANCY IS PROVEN ACROSS ALL IDENTITY-BEARING SURFACES AND HISTORY.`

## Closure / continuation

Lease 192 closes the six-group census and root-cause classification only.

Priority 2 remains OPEN.

Next bounded gate:

`P2 EJR COLLISION-SAFE ALLOCATION GATE` — enforce/verify candidate-ID vacancy across metadata, H1, filename and Git history before any identity migration.

Global Connected Baseline, Provider Authentication holds, Phase 1 overall and global BOOTED/INTEGRITY PASS remain unchanged.
