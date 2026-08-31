# ROOM071 RECONSTRUCTION SUPPLEMENT 234 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 recomputation, EJR-173 disposition, EJR-406 vacancy proof, bounded root repair, cohort successor, and tool-sequencing learning

## Re-entry and target recomputation
The session independently rediscovered `main@36765d62599232b495f6ccaa64d14002041cca08` from Checkpoint229 and reconstructed REP-016, Plan204, Stratification184, and exact Internal-ID/census evidence. The previous completed-repair list was not treated as exhaustive.

The deterministic MEMORY_TO_ROOT census had 31 groups. EJR-173 was selected as a bounded pair: one Memory record plus one root record, with zero external exact-ID references and zero exact-member-path references.

Chronology proved:
- Memory `EJR-173_2026-08-13_REP020_MATRIX_EXPANSION.md` first appeared at `f3c93ad327d79b7fd18061f313ea536e13796ad5` on 2026-08-13;
- root `EJR-173_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md` first appeared at `448822fdda4e630309811d4354fc2192c3e8ff14` on 2026-08-14.

Because Plan204 was bounded to its original five groups, Lease230 explicitly extended disposition authority to EJR-173 only after provenance review. The earlier valid Memory allocation was retained and the later root record classified displaced.

## Preserved sequencing incident
During Lease230 prewrite, a same-content Contents API update was accidentally issued to `Quality/Integration/ejr_memory_to_root_provenance_census.py` with message `noop`. GitHub created commit `fac71011336b11ae782b241b96867fae012f336b`, but its tree was unchanged at `4cb5ef93276ccb820e1dd235e53a1e0831de6599`, identical to Checkpoint229. This was an unintended empty commit, not a content mutation.

History was not rewritten. Lease230 was recreated on top of the live empty commit and continued by non-force fast-forward. Learning captured: same-content Contents API writes are not valid state probes because they may create empty commits; use reads/rechecks and explicit git-object/ref sequencing instead.

## Lease231 — EJR-406 vacancy
Code and commit search found no EJR-406 claim, but this was discovery only. Dedicated complete-history workflow `33360919776` succeeded. Artifact `9746648292`, digest `sha256:0089cb5ab86d542efd59b56029a2ddf0c65346e3781501c6afe6539eb7854388`, proved current_claims=[], historical_claims=[], history_complete=true, occupied=false, vacant=true, decision=VACANT.

## Lease232 — EJR-173 → EJR-406
Functional head `20099314eb434d2e730864c53c027e024768341d`:
- retained Memory EJR-173 unchanged;
- replaced only the later root path with `EJR/EJR-406_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md`;
- preserved semantic body/chronology; changed only H1 identity;
- no consumers were rewritten because deterministic evidence showed zero exact consumers;
- baseline stayed 31 inside repair.

Repair-head verification: Runtime `33361053404`, Full-Stack `33361053409`, M2 `33361053372`, Real Matrix `33361053363` SUCCESS. Internal-ID `33361053387` failed solely at the MEMORY_TO_ROOT census after all preceding steps passed. Artifact `9746702793`, digest `sha256:841c5fa6b705703e3c095014d3a26db9b4611476d2f116577894cb0304eae857`, proved legitimate expected=31/observed=30 cohort drift, history complete, and neither EJR-173 nor EJR-406 remaining in the cohort.

## Lease233 — separate cohort successor
Prewrite `c13fe3b898863e113e1a082531e6b4984aa65053`; functional head `b29d29379598f1554c518461503bbe998d8037b1` changed only `EXPECTED_GROUP_COUNT = 31`→`30`. Compare proved one file / one addition / one deletion.

Exact functional-head verification:
- Internal-ID `33361269760`: SUCCESS;
- Full-Stack `33361269731`: SUCCESS;
- Runtime `33361269737`: SUCCESS;
- M2 `33361269738`: SUCCESS;
- Real Matrix: NOT APPLICABLE to census-only diff.

Artifact `9746770011`, digest `sha256:52705bdb43b64ae11760d9bacf22c832aa7f19aefebe68287ac2e52d3f89eb8a`, proved expected=30, observed=30, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].

## Current controlled boundary
Successor-verified repairs now include prior Checkpoint229 chains plus `EJR-173 → EJR-406`. The retained Memory EJR-173 remains the surviving EJR-173 allocation. Current MEMORY_TO_ROOT baseline is 30.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement234 + REP-016 + Plan204 + Stratification184 + current Internal-ID artifacts, and recompute the next controlled Priority-2 target from current evidence. Do not reopen EJR-173/EJR-406 or earlier repaired chains absent contradictory evidence. For any group outside Plan204's original bounded set, perform explicit disposition authorization before allocation/repair. Any replacement ID requires a separate complete-history vacancy proof. Preserve baseline 30 unless a separately authorized mutation and deterministic artifact prove drift.
