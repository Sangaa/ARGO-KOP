# MUT-2026-08-30-P2-EJR-IDENTITY-STRATIFICATION-184

Date: 2026-08-30
Lease: `R71-20260830-P2-EJR-IDENTITY-STRATIFICATION-184`
Execution role: HERMUZ
Entry baseline: `main@310be157fa0dd9ede39f7c874c68a30741eafe94`
Status: `CLOSED / EJR STRATIFICATION COMPLETE / OWNERS READ-ONLY`

## Trigger

Lease 183 classified all 23 non-EJR ambiguity keys without identity mutation. The remaining raw audit population was dominated by 122 `EJR-*` keys.

Current Journal authority/evidence boundaries establish:

- `Memory/Engineering_Journal/_FOLDER_STATUS.md` remains `INTEGRITY WARNING / CONNECTED-BASELINE AUDIT` and explicitly states active canonical identity uniqueness is not globally certified.
- `Memory/Engineering_Journal/SESSION_INDEX.md` distinguishes Journal document identity from session identity and states that index/navigation evidence does not prove artifact truth.
- root `EJR/` is already classified by current Room71 evidence as an evidence/provenance surface, not Governance/Runtime/relationship authority.
- historical Journal records must be preserved; current repository reality controls current state.

## Closed reconstruction — EJR-013

The previous exact-head Internal-ID artifact reported EJR-013 as ambiguous between a current Memory journal record and `Repository/REP-020_SESSION_DELTA_2026-08-17_EJR013_CONFLICT.md`.

Current reconstruction proved that a second Memory EJR-013 historically existed but was explicitly removed by commit:

`226be7f9027bf90300a0c0888bc6d4878eece3c9` — `P2: remove superseded EJR-013 duplicate after EJR-181 preservation`.

Its creation commit was:

`da23da7229739ff181e3bd79208416aef85a8fbc` — `docs: record runtime graph status reconciliation`.

Current-main absence of the removed path was confirmed through:

- direct current-path fetch: 404;
- repository code search: no result;
- current directory enumeration: path absent.

The retained conflict-evidence note had become stale and its old structural H1 caused the detector to treat the evidence note as a current EJR owner. The note was reconciled at:

`8448ce2d0e3872c2c3a02bfbe14b35e9506cc038`

without mutating any EJR owner.

Disposition:

`EJR-013 = HISTORICAL_TRUE_DUPLICATE_RESOLVED / STALE_CONFLICT_EVIDENCE_RECONCILED`.

## Population stratification

Detailed evidence:

`Repository/P2_EJR_IDENTITY_STRATIFICATION_184_2026-08-30.md`

Raw 122-key path composition from artifact `9728177701`:

- 37 = one `Memory/Engineering_Journal` + one root `EJR/`;
- 37 = two root `EJR/` records;
- 29 = two Memory Engineering Journal records;
- 5 = one Memory + two root EJR;
- 5 = three root EJR;
- 2 = four Memory;
- 1 = one Memory + one Repository evidence record (EJR-013, reconciled);
- remaining small groups = larger Memory/mixed reuse sets.

Identity-source shape:

- 116 keys entirely first-H1 fallback;
- 6 keys with exactly one explicit `Document ID` plus first-H1 peers.

## Cross-folder proof

EJR-165 demonstrates that cross-folder ID equality can represent materially different journal events rather than copied files:

- root `EJR/EJR-165_2026-08-14_P0_P1_SESSION_CLOSURE.md` records a 2026-08-14 P0/P1 closure;
- `Memory/Engineering_Journal/EJR-165_SESSION_CLOSURE_2026-08-13.md` records a different 2026-08-13 repository-access / relationship-matrix-design session.

Therefore parallel EJR paths cannot be mass-collapsed as duplicates or migration copies without provenance reconstruction.

## Bounded classification

- `HISTORICAL_TRUE_DUPLICATE_RESOLVED`: EJR-013 proved.
- mixed Memory/root groups: `PARALLEL_JOURNAL_PATH / EJR-ID-REUSE / TRACEABILITY REVIEW REQUIRED`.
- root-only repeated groups: `ROOT_EJR_MULTI-RECORD ID REUSE / EVIDENCE-SURFACE TRACEABILITY HOLD`.
- Memory-only repeated groups: `MEMORY_JOURNAL_MULTI-RECORD ID REUSE / TRACEABILITY HOLD`.

These classes do not suppress the raw audit findings and do not authorize rename/delete/reassignment.

## C1-C6 closure

- C1 PASS — unique Lease 184 record and bounded evidence record.
- C2 PASS — EJR owners remained read-only; only stale Repository evidence was reconciled.
- C3 PASS — no canonical authority was created/promoted.
- C4 PASS — EJR stratification does not close P2 or Memory.
- C5 PASS — EJR-013 reconstruction uses triple current retrieval + Git history; cross-folder reuse uses direct current content.
- C6 PASS — safe next work is the separately observable 15 canonical-unindexed paths.

## Learning retained

`STATUS DRIFT MUST NOT REOPEN CLOSED REALITY.`

`A CONFLICT RECORD CAN BECOME A FALSE CONFLICT IF ITS TITLE IS PARSED AS THE IDENTITY IT DESCRIBES.`

`HISTORICAL DUPLICATE != CURRENT DUPLICATE AFTER EXPLICIT DISPOSITION.`

`NON-AUTHORITATIVE != IDENTITY-IRRELEVANT.`

`EVIDENCE SURFACES STILL REQUIRE TRACEABLE IDENTITY.`

`PARALLEL JOURNAL PATHS REQUIRE PROVENANCE-AWARE MIGRATION, NOT MASS RENAME.`

## Closure result

`P2_EJR_IDENTITY_STRATIFICATION_184 = CLOSED / CLASSIFICATION-VERIFIED / EJR OWNERS UNCHANGED`

`PRIORITY_2_REPOSITORY_WIDE_IDENTITY_RECONCILIATION = OPEN`

No updated repository-wide Internal-ID count is claimed because the docs-only EJR-013 evidence repair did not trigger the dedicated Internal Document-ID Audit workflow.

## Next legal action

Open a fresh classification lease for the 15 `canonical_unindexed_paths` from artifact `9728177701`.

Classify each into:

`SHOULD-BE-INDEXED / DECLARED-CANONICAL-BUT-DOMAIN-HOLD / LEGACY-OR-STALE-CANONICAL-CLAIM / NAVIGATION-SURFACE / UNRESOLVED`.

Any REP-001/REP-002 mutation requires its own protected Mutation Matrix transaction and cannot be folded into this closed lease.