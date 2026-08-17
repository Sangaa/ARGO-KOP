# P323 — GOVERNED MUTATION HARNESS BOUNDARY

Date: 2026-08-17
Status: Recorded / Priority 1 Reconciliation / Integrity Hold
Checkpoint: P323

## Scope
Revalidate the controlled mutation/reconciliation harness boundary using the repository-native governed write dispatcher and its integration tests.

## Evidence

`Tools/GOVERNED_WRITE_DISPATCH.py` provides a real governed write-dispatch helper that:

- probes current existence before choosing Create vs Update;
- requires current SHA for Update;
- requires necessity evidence for material Create;
- rejects unsafe repository paths;
- requires exact post-write read-back verification.

`Quality/Integration/test_governed_write_dispatch.py` directly tests:

- existing-file → UPDATE using current SHA;
- missing-file → CREATE;
- necessity-evidence enforcement;
- read-back mismatch as a hard failure;
- parent-traversal rejection before repository I/O.

## Result

The mutation safety harness is therefore **PARTIAL / UNIT-LEVEL GOVERNED DISPATCH PROOF**.

It is not yet an end-to-end repository mutation/reconciliation harness because the inspected tests inject repository reader/writer/updater/read-back functions rather than executing the canonical repository connector against a real controlled test artifact and verifying automatic REP-001/002/011 reconciliation afterward.

No claim is made that the full mutation/reconciliation harness is complete.

## Learning

`Governed write-dispatch correctness ≠ end-to-end mutation/reconciliation proof.`

A tested mutation selector and read-back guard prove the helper boundary, not the complete repository control-plane reaction to a real mutation.

## State

- Priority 1: OPEN
- Controlled mutation/reconciliation harness: PARTIAL / UNIT-LEVEL ONLY
- Executable `SRV-009` consumer proof: OPEN
- Exhaustive internal-ID audit: OPEN / REVALIDATION REQUIRED
- Bidirectional graph closure: OPEN
- Integrity: HOLD
- Global PASS: NOT CLAIMED

## Next Safe Entry

Before implementing an end-to-end harness, enumerate the exact canonical connector surface and a disposable/reversible test artifact path. Do not allow a real harness mutation to touch protected canonical artifacts without explicit governed scope.

---

End of P323
