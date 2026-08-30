# P2 EJR AMBIGUITY SOURCE-SIGNATURE CENSUS — LEASE 196

Transaction ID: `MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Protocol: HERMUZ / GOV-014
Status: `CLOSED / EXECUTION-VERIFIED / CENSUS EVIDENCE CAPTURED / RESUME-SAFE`
Entry head: `afe52f71cef0041e7f58218d6846f9182c868f83`
Prewrite heads: `9ee7028b868b896a86cf7784b51ec286a067fa5a`, `7ea957bddbe726d1dc29d2e517703b59c5e03509`
Functional head: `32021e605f5410de2a4833c73cbeca5350c1cbd6`

## Bounded purpose completed

Lease 196 added an evidence-only companion analyzer over the existing member-level `ambiguous_duplicate_records` emitted by the internal Document-ID audit. The identity scanner itself and its ambiguity membership/pass-fail semantics were not modified.

The final construction is:

`internal_document_id_audit.scan() → ejr_ambiguity_source_signature_census.summarize() → deterministic evidence JSON`

## Functional scope

Exactly four functional paths changed:

1. `Quality/Integration/ejr_ambiguity_source_signature_census.py`
2. `Quality/Integration/test_ejr_ambiguity_source_signature_census.py`
3. `.github/workflows/internal-id-audit.yml`
4. `Repository/MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196_MUTATION_MATRIX.md`

`Quality/Integration/internal_document_id_audit.py` remained unchanged at blob `50454dd20a2a5691f788c4580cce234dac13f0c1`.

## Exact-head execution evidence

At functional head `32021e605f5410de2a4833c73cbeca5350c1cbd6`:

- Internal Document-ID Audit `33315075640` — `SUCCESS`.
- Full-Stack Repository Audit `33315075636` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33315075614` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33315075651` — `SUCCESS`.
- Real Mutation Matrix Regression `33315075663` — `SUCCESS`.

Internal-ID job `99266877144` executed the existing audit tests, vacancy-gate tests, new ambiguity-census tests, emitted both deterministic reports, and uploaded both artifacts successfully.

Census artifact:

- artifact ID: `9733176940`;
- name: `ejr-ambiguity-source-signature-census`;
- digest: `sha256:1bd941ff549e22bc91a41adb836fc9ff770abdbdb0c9f30913a0ad61e2af047c`.

## Observed census

Whole ambiguous identity surface:

- ambiguous groups: `144`;
- `FIRST_H1_FALLBACK_ONLY`: `128`;
- `MIXED`: `16`;
- `DOCUMENT_ID_FIELD_ONLY`: `0`.

EJR subset:

- ambiguous EJR groups: `121`;
- `FIRST_H1_FALLBACK_ONLY`: `115`;
- `MIXED`: `6`;
- `DOCUMENT_ID_FIELD_ONLY`: `0`.

EJR cardinality distribution:

- cardinality 2: `103` groups;
- cardinality 3: `12` groups;
- cardinality 4: `3` groups;
- cardinality 5: `2` groups;
- cardinality 6: `1` group.

The six mixed EJR groups are exactly:

`EJR-003`, `EJR-026`, `EJR-180`, `EJR-181`, `EJR-182`, `EJR-183`.

This independently aligns with Lease 192's six-group explicit-metadata census. Therefore all other `115` current EJR ambiguity groups are first-H1-only under the current scanner evidence.

## Learned rule

**MEMBER-LEVEL OBSERVABILITY SHOULD BE AGGREGATED BY A COMPANION EVIDENCE ANALYZER WHEN THE SOURCE GATE ALREADY EXPOSES THE REQUIRED FACTS; DO NOT MUTATE A CORRECT GATE MERELY TO ADD ANALYTICAL POLICY.**

A second operational rule follows from the observed partition:

**A large ambiguity population should be partitioned by observable source signature and cardinality before chronology/ownership analysis; otherwise heterogeneous conflicts are treated as one undifferentiated migration problem.**

## Preserved boundaries

- no EJR rename, delete, reassignment, migration, normalization, suppression, or replacement allocation occurred;
- internal audit ambiguity membership and pass/fail semantics were not changed;
- REP-012, REP-016, REP-020 and authority indexes were not changed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where a real trust anchor is absent;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target

Next bounded Priority-2 task: historical/provenance chronology classification for the `115` H1-only EJR ambiguity groups, beginning with the dominant cardinality-2 population (`103` groups) as evidence permits. No migration is authorized by this lease.
