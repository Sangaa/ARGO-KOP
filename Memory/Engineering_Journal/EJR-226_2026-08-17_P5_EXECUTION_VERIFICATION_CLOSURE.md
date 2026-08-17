# EJR-226

---

# P5 EXECUTION VERIFICATION CLOSURE

Date: 2026-08-17
Status: `CLOSED / EXECUTION-VERIFIED`

## Original Evidence

P5 Controlled Mutation Harness workflow executed successfully on main.

- Workflow ID: `336293577`
- Earlier authoritative successful run: `32040965964`
- Earlier head SHA at execution: `192e9482c4ef7446b53ca195c11af2801f2705ce`
- Earlier job: `p5-harness` (`95420079544`)
- Run P5 fixture and dispatcher tests: `SUCCESS`
- Canonical-artifact immutability guard: `SUCCESS`

## New Learning / Regression Cause

A traditional replay of `MUT-2026-08-17-REP002-001` reached `PRE_COMMIT_VALIDATED` and passed its candidate test, but its push was rejected because the runner checked out an older `main` while the remote advanced before the write. This exposed a missing **write-boundary state gate**.

A transaction-start SHA check is necessary but insufficient. The governed sequence must be:

`READ CURRENT -> CAPTURE SHA -> BUILD/TEST -> RE-READ CURRENT IMMEDIATELY BEFORE WRITE -> WRITE ONLY IF STATE MATCHES -> READ-BACK`

For UPDATE the live SHA must equal the transaction SHA. For CREATE the path must still be absent. Otherwise abort with:

`CURRENT_STATE_CHANGED_BEFORE_WRITE`

No write is allowed after this failure.

## Implemented Regression Changes

- `Tools/GOVERNED_WRITE_DISPATCH.py`: second live-state probe immediately before CREATE/UPDATE.
- `Quality/P5/test_governed_dispatch_in_memory.py`: update-race and create-race tests.
- `Quality/P5/test_controlled_mutation_harness.py`: traditional-vs-fixture equivalence and successive-update regression tests.
- `Quality/P5_CONTROLLED_MUTATION_RECONCILIATION_HARNESS_TEST_MATRIX_2026-08-17.md`: P5-T13 through P5-T16 added.

## Verification Evidence

P5 workflow: `336293577`
Successful regression run: `32041698059`
Successful head: `2ad1c505e24092a4752d3977c6d8c2509d3b5a72`
Job: `p5-harness` (`95422049526`)

Verified:

- P5 fixture and dispatcher tests: `SUCCESS`
- Canonical-artifact immutability guard: `SUCCESS`
- Stale-state update race: `VERIFIED`
- Create race: `VERIFIED`
- Traditional vs fixture equivalence: `VERIFIED`
- Successive fixture update preservation: `VERIFIED`

## Decision

`P5 = EXECUTION-VERIFIED`

The regression update is now part of the executable P5 boundary. The fixture path supplements rather than replaces the traditional path.

The rule is repository-enforced and model-independent; future models must inherit it from the dispatcher and test matrix rather than memory of this incident.

## Next Safe Action

Proceed to P4 final disposition according to the active queue. Do not reopen P5 unless a regression is observed.

---

End of EJR-226
