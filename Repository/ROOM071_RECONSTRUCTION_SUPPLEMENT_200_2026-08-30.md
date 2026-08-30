# ROOM 071 — RECONSTRUCTION SUPPLEMENT 200 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Functional head: `2bce04b83567736415ac2fa91217da585922cb1e`

## What was resolved
The four non-monotonic H1-only ambiguity groups `EJR-195..198` now have independent current content/reference/consumer provenance evidence in addition to the chronology and namespace-lineage evidence from Leases 197-199.

The bounded result is:

`DISTINCT RECORDS / EJR-ID REUSE EVIDENCE / PATH-LEVEL OWNERSHIP UNRESOLVED`.

This is not a canonical-owner decision and authorizes no migration.

## Exact-head evidence
At `2bce04b83567736415ac2fa91217da585922cb1e`:
- Internal Document-ID Audit `33319971746` — `SUCCESS`.
- Full-Stack Repository Audit `33319971759` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33319971731` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33319971699` — `SUCCESS`.
- Real Mutation Matrix Regression `33319971704` — `SUCCESS`.

Artifact:
- ID `9734601892`
- digest `sha256:d5bdc6792235c9adc5ea0974bb33a05692866f280d9e9113562abffa3be5b948`
- `history_complete = true`
- `classification_complete = true`
- `decision = CENSUSED`
- `group_count = 4`

## Provenance result
For each of `EJR-195`, `EJR-196`, `EJR-197`, `EJR-198`:
- current ambiguity membership is exactly three `FIRST_H1_FALLBACK` records;
- all three current member contents are SHA-256 distinct;
- no current external tracked-text consumer names any exact member path.

Across all twelve exact member paths:

`external_exact_sibling_path_references = []`.

Therefore none of the four groups is safely reducible to a simple duplicate-copy disposition.

Current exact-ID reference counts are:
- EJR-195 = 3;
- EJR-196 = 2;
- EJR-197 = 3;
- EJR-198 = 2.

Most are Lease-199 / Room-199 provenance observations. The useful sequential cases are ID-level only: the later EJR-196 record refers to previous `EJR-195`, and the later EJR-198 record refers to previous `EJR-197`. Because each referenced ID currently maps to three distinct records, the reference cannot be rebound to one exact path without stronger provenance evidence.

## Learned rules
1. `CONTENT DISTINCTNESS + ABSENCE OF EXACT-PATH CONSUMERS CAN PROVE THAT AN ID AMBIGUITY IS NOT A SIMPLE COPY DUPLICATE, BUT IT DOES NOT SELECT A CANONICAL OWNER.`
2. `ID-LEVEL REFERENCES MUST NOT BE REBOUND TO A SPECIFIC AMBIGUOUS MEMBER WITHOUT PATH-LEVEL OR OTHER AUTHORITATIVE PROVENANCE EVIDENCE.`
3. `A DISTINCT RECORD CAN SHARE A HISTORICAL ID WITHOUT BEING A DERIVATIVE COPY; CONTENT AND CONSUMER EVIDENCE MUST BE TESTED SEPARATELY.`
4. `PROVENANCE OBSERVABILITY MAY NARROW THE DISPOSITION CLASS WITHOUT AUTHORIZING IDENTITY MUTATION.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, or replacement allocation;
- no canonical promotion or ownership assignment;
- Internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- six MIXED explicit-ID ambiguity groups remain separate and unsuppressed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target
Rediscover live `main`, re-enter from this checkpoint, then open the next bounded Priority-2 evidence lease for content/reference/consumer provenance on the four reverse-direction groups `EJR-178`, `EJR-189`, `EJR-222`, and `EJR-338`.

Do not infer ownership from namespace direction, chronology, content distinctness, or ID-only references. Do not mutate EJR identity without a later governed disposition lease.
