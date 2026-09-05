# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 9 Matrix Addendum

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-8 EXACT-HEAD VERIFIED / MATERIAL UNIT 9 APPLIED / EXACT-HEAD CI PENDING`

Unit-8 exact-head: `c75555baf9ac816d31c561f531de9122f42cfc1c`

## Scope

Reconcile the current `MOD-004` downstream Runtime/Engine ripple targets against current endpoint content and historical P65 provisional evidence.

## Current-source finding

Unit 3 already repaired `MOD-004` so `RUN-004`, `RUN-008`, `RUN-009` and `ENG-007` are downstream compatibility/revalidation targets rather than semantic dependencies.

Current direct reads of all four endpoints show no direct `MOD-004` declaration:

- `RUN-004` defines context loading and current repository/folder/dependency validation but does not name `MOD-004` or the Memory Model;
- `RUN-008` defines runtime state and memory/learning boundaries but does not name `MOD-004`;
- `RUN-009` defines governed recovery and memory/learning boundaries but does not name `MOD-004`;
- `ENG-007` defines learning and memory-domain separation, directly naming `MEM-*` artifacts and `MOD-011`, but not `MOD-004`.

Therefore neither direction is currently registered from this quartet:

`MOD-004 → {RUN-004,RUN-008,RUN-009,ENG-007} = NONE / RIPPLE_ONLY`

and

`{RUN-004,RUN-008,RUN-009,ENG-007} → MOD-004 = NONE / NO_REVERSE_EDGE_PROVEN`.

## Historical evidence disposition

`REP-020_MATRIX_ADDENDUM_2026-08-15_P65.md` remains valid historical provenance for what was inspected at that time, but its forward dependency interpretation depended on the former undifferentiated `MOD-004` Dependencies section. Because Unit 3 changed the stable source contract, P65 cannot be promoted over current source truth.

Permanent rule reinforced:

`HISTORICAL PROVISIONAL EDGE != CURRENT RELATIONSHIP AUTHORITY`.

## Material

- `Repository/REP-014_PRIORITY12_MOD004_RIPPLE_EVIDENCE_2026-09-05_G.tsv`
- `Quality/Integrity/test_models_p12_mod004_ripple_targets.py`
- this Matrix addendum

## Non-claims

Unit 9 does not modify REP-014, does not assert repository-wide absence of every possible implementation consumer, does not close Models/P12, and does not weaken the already-verified Unit-3 semantic dependencies `MOD-004 → MOD-002/MOD-003/MOD-011`.

## Next gate

1. exact-head four-family CI for this Unit-9 Matrix head;
2. if green, continue current-source `MOD-011` non-Knowledge consumer/reference cohort and Models status/queue reconciliation;
3. canonical REP-014 stable-ID corrections remain pending a guaranteed full-content-preserving write path.
