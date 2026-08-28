# P412 — P410 Artifact Attribution Investigation

Date: 2026-08-28
Status: `CLOSED / INVESTIGATION-VERIFIED / PROCESS-CORRECTION / NO NEW ARCHITECTURAL LEARNING / NO RUNTIME MUTATION`
Protocol: `GOV-013`

## QUESTION
Why did P410 report `Runtime/Execution/test_run010_authorized_caller.py` as already added when the later investigation initially found it absent at the claimed point?

## EVIDENCE RECONCILIATION
P410 commit `f2eafc63baab27f216c7d01ee953531c9f4e8cde` contains only the session-delta documentation `Repository/REP-082_SESSION_DELTA_2026-08-28_P410.md` in its commit diff. Its own text nevertheless states that `Runtime/Execution/test_run010_authorized_caller.py` was added.

A direct compare of P410 HEAD to P411 HEAD `de48a6f7d06ff6a4c1624ed3518932d307188efa` shows exactly three files added after P410: the P411 mutation matrix, the caller test `Quality/Integration/test_run010_authorized_caller.py`, and the P411 session delta. Therefore the caller test was not part of P410's committed change; it was actually introduced during the P411 interval.

The current PR changed-files list confirms the caller test exists now, but that current existence cannot retroactively prove P410 attribution.

## ROOT CAUSE
The discrepancy is an **attribution/state-verification failure**, not an architectural discovery and not evidence that GitHub lost a committed file.

P410 recorded the intended mutation as if it were already committed, while the Git commit evidence shows that the artifact was committed only in the subsequent P411 interval. The failure was therefore premature closure/reporting without exact-HEAD file read-back at the P410 boundary.

The earlier assistant statement that the artifact was simply "not present" was also incomplete: it failed to distinguish **not present at P410's exact committed state** from **present in the later PR state**. P411 corrected the artifact, and P412 now corrects the causal attribution.

## PROCESS CORRECTION
For every claimed mutation, closure requires all four independently checked facts:
1. write action result;
2. resulting commit SHA;
3. exact branch/HEAD attribution;
4. direct read-back of the claimed path from that exact HEAD.

A later artifact may not be used as evidence for an earlier checkpoint. A session report may not claim an artifact as implemented merely because the mutation was intended or a tool operation was attempted.

## LEARNING DISPOSITION
No new architectural learning is claimed. This is a **process correction to evidence attribution** using existing GOV-013 principles. Existing knowledge was available but was not applied rigorously enough at P410 closure.

## DECISION
No code mutation is justified by this investigation. The repository state is now internally reconciled: P410 documentation over-attributed the artifact; P411 introduced the artifact; P412 records the causal correction. No runtime, canonical, governance, or production wiring changes are made.

## CLOSE
`P412 CLOSED / ROOT CAUSE IDENTIFIED / ATTRIBUTION CORRECTED / PROCESS CORRECTION / NO RUNTIME MUTATION / NO PROMOTION`

## NEXT CHECKPOINT
Resume only from the actual current HEAD. If execution evidence is required, run CI against that exact HEAD and attribute results only to that SHA.
