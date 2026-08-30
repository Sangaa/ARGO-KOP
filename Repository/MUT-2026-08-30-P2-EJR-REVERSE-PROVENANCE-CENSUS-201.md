# MUT-2026-08-30 — P2 EJR REVERSE-DIRECTION PROVENANCE CENSUS — LEASE 201

Status: `PREWRITE / OPEN`
Lease: `R71-20260830-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
Baseline: `main@62b08f67af7f1f58e23236f8563d590b4d24cf04`

## Purpose
Add deterministic, evidence-only content/reference/consumer provenance observability for the four H1-only reverse namespace-direction ambiguity groups proven by Lease 199:

- `EJR-178`
- `EJR-189`
- `EJR-222`
- `EJR-338`

The known current lineage cardinalities are heterogeneous (`3 / 2 / 4 / 2`) and MUST NOT be normalized to the three-member assumption used for Lease 200.

## Authorized functional scope
1. ADD `Quality/Integration/ejr_reverse_provenance_census.py`.
2. ADD `Quality/Integration/test_ejr_reverse_provenance_census.py`.
3. MODIFY `.github/workflows/internal-id-audit.yml` only to test, emit, and upload the new deterministic evidence report.
4. MODIFY this lease's Mutation Matrix in the same functional change set.

## Required evidence behavior
The classifier MUST:
- fail closed if Git history is shallow/incomplete;
- require the four current target IDs to exist in the current ambiguity report;
- require every current member to remain `FIRST_H1_FALLBACK`;
- require current member cardinalities to remain exactly `EJR-178=3`, `EJR-189=2`, `EJR-222=4`, `EJR-338=2`; any drift produces incomplete classification rather than reinterpretation;
- emit exact current member paths, namespace surface, first H1, content SHA-256 and UTF-8 byte count;
- emit current external exact-ID references;
- emit current external exact-member-path references;
- expose whether member contents are all distinct;
- emit no owner, canonical, migration, rename, delete, reassignment, suppression, allocation, or authority decision.

## Forbidden scope
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- no modification to the Internal Document-ID scanner semantics;
- no REP-012, REP-016, or REP-020 mutation;
- no change to six MIXED explicit-ID ambiguity groups;
- no Priority-2, Phase-1, Connected-Baseline, provider-authentication, Memory-integrity, or global integrity closure claim.

## Verification contract
Before functional ref update:
- construct unattached commit;
- compare against live parent and prove exactly the four authorized paths;
- re-read live `main` and require exact parent equality;
- fast-forward with `force=false` only.

After functional update:
- read back modified files;
- observe exact-head Internal-ID, Full-Stack, Runtime, M2, and Real Matrix workflows;
- inspect the uploaded reverse-provenance artifact and classify only what it proves;
- close with a Room 071 resume-safe checkpoint and re-verify closure-head workflows.

## Preserved boundary
Chronology, namespace direction, content similarity/distinctness, ID-level references, or exact-path reference absence are provenance evidence only. None can independently select a canonical owner.
