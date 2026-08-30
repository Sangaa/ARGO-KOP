# P2 EJR IDENTITY STRATIFICATION — LEASE 184

Date: 2026-08-30
Execution role: HERMUZ / Room71
Baseline source audit: artifact `9728177701` at `e04b073f268aa1291bbb747429d92ac69d83e9ec`
Current-state repair evidence: `8448ce2d0e3872c2c3a02bfbe14b35e9506cc038`
State: `STRATIFIED / EJR OWNERS UNCHANGED / PRIORITY-2 OPEN`

## Authority boundary

Current repository evidence already classifies root `EJR/` as an engineering-journal/evidence/provenance surface. It does not gain Governance, Runtime, relationship, or canonical authority by existence.

`Memory/Engineering_Journal/_FOLDER_STATUS.md` independently keeps the Engineering Journal under Integrity Warning and states that active canonical identity uniqueness is not globally certified.

Therefore an EJR identity collision is primarily a provenance/traceability integrity problem unless another authority surface explicitly promotes the record. It is not automatically a competing platform-authority collision.

## Raw population

The exact-head Internal-ID artifact reported 122 ambiguous `EJR-*` keys.

Path-composition stratification of those 122 keys:

| Shape | Keys | Meaning |
|---|---:|---|
| `1 Memory + 1 root EJR` | 37 | parallel journal/evidence paths sharing an EJR number |
| `2 root EJR only` | 37 | repeated EJR numbers inside root evidence surface |
| `2 Memory only` | 29 | repeated EJR numbers inside Memory Engineering Journal |
| `1 Memory + 2 root EJR` | 5 | larger parallel-path reuse group |
| `3 root EJR only` | 5 | repeated root-EJR lineage/reuse group |
| `4 Memory only` | 2 | larger Memory reuse group |
| `1 Memory + 1 Repository evidence` | 1 | EJR-013 stale conflict-evidence shadow; repaired in current main |
| `3 Memory only` | 1 | larger Memory reuse group |
| `2 Memory + 1 root EJR` | 1 | mixed parallel-path reuse group |
| `4 Memory + 1 root EJR` | 1 | mixed parallel-path reuse group |
| `6 Memory only` | 1 | large Memory reuse group |
| `5 Memory only` | 1 | large Memory reuse group |
| `3 Memory + 1 root EJR` | 1 | mixed parallel-path reuse group |

Identity-source stratification from the same artifact:

- 116 keys were entirely first-H1 fallback groups;
- 6 keys contained exactly one explicit `Document ID` source plus first-H1 peers.

These are triage facts, not automatic collision dispositions.

## EJR-013 reconstructed disposition

EJR-013 was historically a real duplicate between two Memory journal records. Git history proves the second record was later explicitly removed by commit:

`226be7f9027bf90300a0c0888bc6d4878eece3c9` — `P2: remove superseded EJR-013 duplicate after EJR-181 preservation`.

The historical conflict note remained in Repository with an H1 beginning `EJR-013`, causing the current detector to reopen the closed historical conflict as if the Repository note were an EJR owner.

Current repair:

`Repository/REP-020_SESSION_DELTA_2026-08-17_EJR013_CONFLICT.md`

was reconciled at commit:

`8448ce2d0e3872c2c3a02bfbe14b35e9506cc038`

The repaired record now preserves the historical conflict while explicitly classifying itself as Repository conflict evidence, not an EJR owner.

Disposition:

`EJR-013 = HISTORICAL_TRUE_DUPLICATE_RESOLVED / STALE_CONFLICT_EVIDENCE_RECONCILED`.

No current EJR owner was renamed, deleted, reassigned, or promoted by Lease 184.

## Cross-folder reuse proof

`EJR-165` proves that cross-folder equality cannot be dismissed as a simple duplicated copy:

- `EJR/EJR-165_2026-08-14_P0_P1_SESSION_CLOSURE.md` records a 2026-08-14 P0/P1 closure.
- `Memory/Engineering_Journal/EJR-165_SESSION_CLOSURE_2026-08-13.md` records a different 2026-08-13 session about repository access and Master Relationship Matrix design.

They are materially different journal events sharing the same EJR number.

Therefore the safe class for the 37 exact `Memory + root EJR` pairs is:

`PARALLEL_JOURNAL_PATH / EJR-ID-REUSE / TRACEABILITY-CONFLICT-CANDIDATE`.

This classification does not say all 37 require rename. History/provenance consumers must be checked before any identity mutation.

## Current classes

### A. Resolved historical conflict with stale evidence shadow

- `EJR-013` — proved and reconciled.

### B. Parallel path / namespace reuse

At least 45 raw groups mix `Memory/Engineering_Journal/` with root `EJR/` (37 exact one+one pairs plus larger mixed groups).

Bounded class:

`PARALLEL_JOURNAL_PATH / EJR-ID-REUSE / CURRENT TRACEABILITY REVIEW REQUIRED`.

### C. Root-EJR repeated IDs

At least 42 raw groups are root-EJR-only repeated-ID groups (37 pairs + 5 triples).

Bounded class:

`ROOT_EJR_MULTI-RECORD ID REUSE / EVIDENCE-SURFACE TRACEABILITY HOLD`.

### D. Memory Engineering Journal repeated IDs

At least 34 raw groups are Memory-only repeated-ID groups across pairs and larger groups.

Bounded class:

`MEMORY_JOURNAL_MULTI-RECORD ID REUSE / TRACEABILITY HOLD`.

The categories overlap the raw count only according to their exact path composition and preserve all records read-only.

## Why Lease 184 does not auto-repair the remaining EJR IDs

The evidence proves both of these facts simultaneously:

1. EJR is a non-authoritative evidence/provenance surface; ID reuse does not automatically create platform authority collision.
2. Distinct journal events can reuse the same EJR number; therefore ID reuse is a real traceability ambiguity and cannot be silently suppressed.

A mass rename would risk breaking historical references and provenance. A detector exemption would hide genuine current traceability ambiguity.

Therefore:

`NON-AUTHORITATIVE != IDENTITY-IRRELEVANT`.

`EVIDENCE SURFACES STILL REQUIRE TRACEABLE IDENTITY`.

## Lease-184 bounded result

`P2_EJR_IDENTITY_STRATIFICATION_184 = READY_FOR_CLOSURE / STRATIFICATION COMPLETE`.

The work achieved:

- separated authority collision from evidence-traceability collision;
- reconstructed EJR-013 from current tree plus Git history;
- repaired one stale conflict-evidence surface without changing any EJR owner;
- reduced the 122-key problem into path/lineage classes suitable for future governed identity migration rather than blind cleanup.

Priority 2 remains OPEN because:

- current EJR traceability reuse remains unresolved outside the EJR-013 historical disposition;
- 15 canonical-unindexed records remain from the last exact-head audit;
- no updated Internal-ID artifact was triggered by the docs-only EJR-013 repair, so no new repository-wide count is claimed.

## Learning

- `STATUS DRIFT MUST NOT REOPEN CLOSED REALITY`.
- `HISTORICAL DUPLICATE != CURRENT DUPLICATE AFTER EXPLICIT DISPOSITION`.
- `A CONFLICT RECORD CAN BECOME A FALSE CONFLICT IF ITS TITLE IS PARSED AS THE IDENTITY IT DESCRIBES`.
- `NON-AUTHORITATIVE != IDENTITY-IRRELEVANT`.
- `EVIDENCE SURFACES STILL REQUIRE TRACEABLE IDENTITY`.
- `PARALLEL JOURNAL PATHS REQUIRE PROVENANCE-AWARE MIGRATION, NOT MASS RENAME`.

## Next legal action

Close Lease 184 as a classification/reconstruction subgate, then classify the 15 `canonical_unindexed_paths` from artifact `9728177701` into:

`SHOULD-BE-INDEXED / DECLARED-CANONICAL-BUT-DOMAIN-HOLD / LEGACY-OR-STALE-CANONICAL-CLAIM / NAVIGATION-SURFACE / UNRESOLVED`.

Any REP-001/REP-002 mutation requires a fresh protected mutation lease and same-change-set Matrix transaction.