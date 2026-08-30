# MUT-2026-08-30-P2-ID-AUDIT-OBSERVABILITY-181

**Status:** CLOSED / EXECUTION-VERIFIED / FAILURE-EVIDENCE PRESERVATION VERIFIED
**Baseline:** `main@c17a05fd169d94d0a472aebae484f1ca94ddbef5`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-PARSER-180.md`

## Gap proved before mutation

Lease 180 repaired the proved first-H1 parser overreach, but the exact-head Internal Document-ID Audit run `33292104449` remained failed at job `99205415647` while Full-Stack and M2 succeeded on the same HEAD. Multiple direct attempts to retrieve a usable failed-job log did not yield the failing assertion through the available connector surface.

The workflow `.github/workflows/internal-id-audit.yml` ran `pytest` before deterministic report generation/upload. Therefore a pytest failure prevented the report artifact from being generated and uploaded, hiding the exact audit findings needed by the required HARD-HOLD root-cause procedure.

This was classified as an evidence-observability defect, not evidence that the detector itself was correct or incorrect.

## Allowed paths

- `.github/workflows/internal-id-audit.yml`
- `Repository/MUT-2026-08-30-P2-ID-AUDIT-OBSERVABILITY-181.md`
- bounded Repository closure/learning evidence for 179-181 if required after verification

## Forbidden paths

- `Quality/Integration/internal_document_id_audit.py`
- `Quality/Integration/test_internal_document_id_audit.py`
- all document identity owners outside the evidence record above
- `Core/**`
- `Governance/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- `Release/**`
- `Repository/REP-001_*`
- `Repository/REP-002_*`
- `Repository/REP-014_*`
- `Repository/REP-016_*`
- `PROJECT_STATUS.md`
- `Repository/ROOM071_CURRENT_STATE.json`
- branch deletion or force ref mutation

## C1-C6 collision gate

- **C1 path collision:** PASS — transaction record is unique and the workflow path already existed.
- **C2 semantic collision:** PASS — audit rules and identities were forbidden from mutation under 181.
- **C3 authority collision:** PASS — no canonical/governance/release authority changed.
- **C4 promotion collision:** PASS — no audit result or domain state was promoted.
- **C5 evidence collision:** PASS — the change exists only to preserve deterministic failure evidence.
- **C6 handoff collision:** PASS — the preserved evidence handed the actual defect to Lease 182.

## Minimal repair contract

1. Preserve the existing pytest command and its ability to fail the job.
2. Ensure deterministic report generation executes even when pytest fails.
3. Ensure report artifact upload executes even when pytest fails.
4. Do not use `continue-on-error` to convert a failing audit into PASS.
5. Do not change detector/test semantics under this lease.
6. After merge, inspect the exact-head run and retrieve the deterministic report artifact or equivalent workflow evidence.
7. Treat any exposed identity finding as new evidence requiring its own root-cause classification; do not auto-repair identities.

## Verification and closure evidence

The observability repair succeeded at its intended purpose. Exact-head run `33298252068` on `0ce5d667ac9ff1f4af48281a7474041172d1b1b2` remained correctly failed but produced artifact `internal-document-id-audit-report` (`9728089302`). That artifact exposed the previously hidden failure family: 18 `explicit_heading_identity_conflicts`.

Those findings were not suppressed or cosmetically cleared. They were transferred into Lease 182, where direct representative inspection proved a detector identity-source defect.

After Lease 182 repair, exact-head Internal Document-ID Audit run `33298557071` on `e04b073f268aa1291bbb747429d92ac69d83e9ec` completed `SUCCESS` and produced artifact `9728177701`, proving the workflow continues to emit deterministic audit evidence in the successful case as well.

Lease 181 therefore closes only the diagnostic observability defect. It does not close Priority 2 identity reconciliation.

## Learning

`A FAILING AUDIT MUST PRESERVE ITS FAILURE EVIDENCE.`

`OBSERVABILITY IS PART OF VERIFIABILITY: A RED GATE WITHOUT RETAINED DIAGNOSTICS CAN BLOCK CORRECT ROOT-CAUSE GOVERNANCE.`

Final lease state:
`P2_ID_AUDIT_OBSERVABILITY_181 = CLOSED / EXECUTION-VERIFIED`.
