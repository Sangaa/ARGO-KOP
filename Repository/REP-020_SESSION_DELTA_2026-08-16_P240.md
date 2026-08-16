# REP-020 — SESSION DELTA P240

Date: 2026-08-16  
Status: Recorded / Priority 1 Reconciliation Support / Integrity Hold  
Checkpoint: P240

## Change

A governed repository write-dispatch layer was added so future HERMUZ mutations choose the GitHub operation from current repository state:

```text
Existence Probe
    ├── confirmed existing + current SHA → UPDATE
    └── confirmed not-found → CREATE
```

The layer then requires post-write read-back and exact content verification.

Artifacts:

- `Tools/GOVERNED_WRITE_DISPATCH.py`
- `Quality/Integration/test_governed_write_dispatch.py`
- `Repository/GOVERNED_WRITE_DISPATCH_CONTRACT.md`

## Why This Was Necessary

During the current construction cycle, write-tool misuse exposed repeated classes of avoidable failure:

- update attempted for a non-existing path;
- stale or incorrect ref used for read-back;
- stale SHA used for sequential mutation;
- ambiguity between creating Evidence and updating an existing artifact;
- test collector executing a stale duplicate guard.

These failures were operationally recoverable but violated the intended evidence-first mutation sequence and consumed build cycles.

## Creation Necessity Rule

The new dispatcher requires every non-trivial created artifact to state:

- purpose;
- importance class;
- necessity evidence;
- intended target content.

This is specifically designed to prevent file proliferation and to force a reasoned decision between:

`UPDATE EXISTING → REUSE EXISTING → CREATE NEW`

## Verification

The dispatcher test suite covers:

- existing file → Update using current SHA;
- missing file → Create;
- missing necessity evidence → hard failure;
- read-back content mismatch → hard failure;
- invalid path traversal → hard failure.

Repository write behavior remains a connector concern; this layer governs the decision and verification protocol rather than granting new mutation authority.

## Learning Disposition

The observed write failures are now durable engineering knowledge through:

`Repository/GOVERNED_WRITE_DISPATCH_CONTRACT.md`

No new Memory authority is created. The record extends the existing HERMUZ mutation discipline and preserves the distinction between tool mechanics, repository evidence and authority.

## Non-Closure

Priority 1 Control-Plane reconciliation remains open. This change improves mutation safety and traceability; it does not certify repository-wide integrity or close the Phase-1 queue.
