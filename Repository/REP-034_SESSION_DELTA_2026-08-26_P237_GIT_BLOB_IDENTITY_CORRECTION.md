# REP-034 — P237 Git Blob Identity Correction

Status: `CLOSED / VERIFIED`

## Finding
Before exact-SHA execution, source inspection revealed that the P236 adapter used SHA-1 over raw bytes, while a Git blob SHA is SHA-1 over `blob <byte-length>\0<content>`.

## Correction
Updated `Runtime/Prototype/exact_blob_adapter.py` to compute the actual Git blob identity before harness invocation.

Correction commit: `7c4e783f5e513c7be7337826c9aa7db9e8b87a0d`
Post-write read-back: `PASS`.

## Control
No execution evidence was claimed from the incorrect implementation. No production/schema change. No main mutation.

## Session Closure
P237 closed after detecting, correcting, and reading back the identity calculation defect. Exact-SHA execution remains pending on the corrected isolated branch.
