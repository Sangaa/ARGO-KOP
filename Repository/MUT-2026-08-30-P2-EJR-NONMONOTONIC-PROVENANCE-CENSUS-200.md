# P2 EJR NON-MONOTONIC PROVENANCE CENSUS — LEASE 200

Date: 2026-08-30
Execution role: HERMUZ / Room71
Transaction: `MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Baseline: `main@9762b1dbc0240dc9a8cfc4c409ed39982018d1d9`
Functional head: `2bce04b83567736415ac2fa91217da585922cb1e`
State: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`

## Trigger
Lease 199 proved four non-monotonic H1-only ambiguity groups: `EJR-195`, `EJR-196`, `EJR-197`, `EJR-198`, each with exact-path namespace chronology `ROOT_EJR → MEMORY_EJR → ROOT_EJR`.

Chronology and namespace direction do not establish ownership. Lease 200 therefore added independent content/reference/consumer observability before any identity migration is even considered.

## Functional change
Added deterministic companion analyzer:

`Quality/Integration/ejr_nonmonotonic_provenance_census.py`

with synthetic coverage in:

`Quality/Integration/test_ejr_nonmonotonic_provenance_census.py`.

The existing Internal Document-ID scanner semantics were not changed.

The analyzer is deliberately evidence-only. It emits current member paths, first-H1 titles, content SHA-256 values, current exact-ID references, current exact sibling-path references, and content distinctness. It contains no owner/canonical/migration/rename/suppression disposition.

## Exact-head verification
At functional head `2bce04b83567736415ac2fa91217da585922cb1e` all observed workflows succeeded:

- Internal Document-ID Audit `33319971746` — `SUCCESS`.
- Full-Stack Repository Audit `33319971759` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33319971731` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33319971699` — `SUCCESS`.
- Real Mutation Matrix Regression `33319971704` — `SUCCESS`.

Internal-ID job `99280108727` also proved:
- new provenance-census tests `SUCCESS`;
- deterministic current-repository census emission `SUCCESS`;
- artifact upload `SUCCESS`.

Artifact:
- ID `9734601892`
- name `ejr-nonmonotonic-provenance-census`
- digest `sha256:d5bdc6792235c9adc5ea0974bb33a05692866f280d9e9113562abffa3be5b948`
- `history_complete = true`
- `classification_complete = true`
- `decision = CENSUSED`
- `group_count = 4`

## Current census result
Each of `EJR-195..198` has exactly three current `FIRST_H1_FALLBACK` members and every one of the twelve member files has a distinct content SHA-256.

Therefore these ambiguity groups are not simple byte-identical duplicate-copy groups.

Observed first-H1 distinctions include:

- `EJR-195`: `Final Evidence Pointers` / `2026-08-14 CONTROL-PLANE RECONCILIATION CHECKPOINT` / `P4 Reverse-Evidence & Search-Learning Review`.
- `EJR-196`: `Closure Meta` / `2026-08-14 SESSION FINAL CLOSURE` / `P4 Current State Reconciliation`.
- `EJR-197`: `Safe Matrix Mutation Boundary` / `2026-08-14 SESSION FINAL CLOSURE` / `P1 Closure Review`.
- `EJR-198`: `Session Close` / `2026-08-14 SESSION FINAL CLOSURE` / `P2 Identity Scope Reconciliation`.

This supports a bounded classification:

`DISTINCT RECORDS / EJR-ID REUSE EVIDENCE / PATH-LEVEL OWNERSHIP UNRESOLVED`.

It does not identify a canonical owner and does not authorize migration.

## Consumer/reference evidence
For all twelve exact member paths:

`external_exact_sibling_path_references = []`.

No current tracked text consumer outside the groups and Lease-200 self-generated evidence names any of the twelve exact member paths.

ID-level references do exist:

- `EJR-195`: 3 external exact-ID reference paths;
- `EJR-196`: 2;
- `EJR-197`: 3;
- `EJR-198`: 2.

Most are Lease-199 / Room-199 analytical provenance records. Two materially useful sequential references also exist:

- `EJR-196_P4_CURRENT_STATE_RECONCILIATION_2026-08-17.md` refers to a previous `EJR-195` checkpoint by ID;
- `EJR-198_P2_IDENTITY_SCOPE_RECONCILIATION_2026-08-17.md` refers to previous session checkpoint `EJR-197` by ID.

Because those references are ID-only while each ID currently names three distinct records, they cannot safely be rebound to one exact member path without additional authoritative provenance evidence.

## Learned rules
1. `CONTENT DISTINCTNESS + ABSENCE OF EXACT-PATH CONSUMERS CAN PROVE THAT AN ID AMBIGUITY IS NOT A SIMPLE COPY DUPLICATE, BUT IT DOES NOT SELECT A CANONICAL OWNER.`
2. `ID-LEVEL REFERENCES MUST NOT BE REBOUND TO A SPECIFIC AMBIGUOUS MEMBER WITHOUT PATH-LEVEL OR OTHER AUTHORITATIVE PROVENANCE EVIDENCE.`
3. `A DISTINCT RECORD CAN SHARE A HISTORICAL ID WITHOUT BEING A DERIVATIVE COPY; CONTENT AND CONSUMER EVIDENCE MUST BE TESTED SEPARATELY.`
4. `PROVENANCE OBSERVABILITY MAY NARROW THE DISPOSITION CLASS WITHOUT AUTHORIZING IDENTITY MUTATION.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- no ownership assignment;
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

## Next legal action
The non-monotonic `EJR-195..198` groups are now bounded as distinct-record ID-reuse evidence, but ownership/migration remains unresolved and blocked.

Next bounded Priority-2 provenance work should apply the same independent content/reference/consumer census to the four reverse-direction groups `EJR-178`, `EJR-189`, `EJR-222`, and `EJR-338` before any cross-group migration theory is considered.
