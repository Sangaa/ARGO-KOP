# MUT-2026-08-30 — P2 EJR H1 NAMESPACE LINEAGE SIGNAL CENSUS — LEASE 199

Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-H1-NAMESPACE-LINEAGE-199`
Baseline: `main@6b011215286aae70d78d0ad86d6d8acc75ee7fa2`
Functional head: `7599d7e1ded350ae72665e737e0033c9a5a3316d`

## Purpose and result
Lease 199 added an evidence-only companion classifier for the `115` current H1-only EJR ambiguity groups already covered by Leases 197-198 chronology. It combines exact-current-path first-seen Git ancestry with journal namespace surface (`EJR/` vs `Memory/Engineering_Journal/`) to expose provenance-direction signals without assigning ownership.

## Functional scope executed
1. `Quality/Integration/ejr_h1_namespace_lineage.py` — ADD.
2. `Quality/Integration/test_ejr_h1_namespace_lineage.py` — ADD.
3. `.github/workflows/internal-id-audit.yml` — MODIFY only to execute/test/emit/upload this evidence report.
4. `Repository/MUT-2026-08-30-P2-EJR-H1-NAMESPACE-LINEAGE-199_MUTATION_MATRIX.md` — synchronized same-change evidence.

Pre-ref compare proved exactly these four paths and no extras.

## Exact-head verification
At functional head `7599d7e1ded350ae72665e737e0033c9a5a3316d`:
- Internal Document-ID Audit `33318991190` — `SUCCESS`.
- Full-Stack Repository Audit `33318991036` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33318990918` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33318990948` — `SUCCESS`.
- Real Mutation Matrix Regression `33318990950` — `SUCCESS`.

Namespace-lineage artifact:
- ID `9734326330`.
- digest `sha256:a199bb24f415c0c5f4d843c4660a92d85114c470236c1aad4bd7313d103d0f36`.
- history complete = `true`.
- classification complete = `true`.
- group count = `115`.

## Observed namespace-lineage classes
- `SAME_SURFACE_ROOT_EJR` = `42`.
- `SAME_SURFACE_MEMORY_EJR` = `29`.
- `MEMORY_TO_ROOT_EJR` = `36`.
- `ROOT_TO_MEMORY_EJR` = `4`.
- `MULTI_NAMESPACE_TRANSITION` = `4`.

Member observations by namespace:
- `ROOT_EJR` = `138`.
- `MEMORY_EJR` = `108`.

The four reverse-direction groups are `EJR-178`, `EJR-189`, `EJR-222`, and `EJR-338`.

The four non-monotonic multi-transition groups are `EJR-195`, `EJR-196`, `EJR-197`, and `EJR-198`; each has the collapsed namespace sequence `ROOT_EJR → MEMORY_EJR → ROOT_EJR` under exact-path first-seen ancestry.

## Interpretation boundary
This result proves current exact-path namespace chronology only. It does not prove canonical owner, original semantic author, rename lineage, intended migration direction, or authority promotion.

The majority direction (`MEMORY_TO_ROOT_EJR` among cross-surface one-transition groups) cannot be promoted into a global migration or ownership rule because reverse and non-monotonic lineages are proven to exist.

## Learned rules
1. `NAMESPACE LINEAGE IS PROVENANCE EVIDENCE, NOT CANONICAL OWNERSHIP AUTHORITY.`
2. `A MAJORITY PROVENANCE DIRECTION MUST NOT BE PROMOTED INTO OWNERSHIP POLICY WHEN REVERSE AND NON-MONOTONIC LINEAGES EXIST.`
3. `NON-MONOTONIC NAMESPACE TRANSITIONS REQUIRE GROUP-SPECIFIC PROVENANCE REVIEW BEFORE ANY MIGRATION.`
4. `A DOMINANT DIRECTIONAL PATTERN MUST NOT ERASE MINORITY REVERSE OR MULTI-TRANSITION LINEAGES.`
5. Same-surface repeated IDs remain traceability conflicts; namespace stability does not resolve record ownership.

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, or allocation;
- internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- the six MIXED explicit-ID groups remain separate and unsuppressed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume direction
Next bounded Priority-2 work should inspect independent content/reference/consumer provenance signals for the exceptional cross-surface groups, prioritizing the four non-monotonic `EJR-195..198` (and then the four reverse-direction groups) before any migration or ownership action. Chronology and namespace direction alone remain insufficient to assign identity ownership.
