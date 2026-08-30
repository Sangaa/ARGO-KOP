# MUT-2026-08-30-P2-ID-AUDIT-OBSERVABILITY-181

**Status:** PREWRITE / LEASE ACTIVE / DIAGNOSTIC OBSERVABILITY
**Baseline:** `main@c17a05fd169d94d0a472aebae484f1ca94ddbef5`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-PARSER-180.md`

## Gap proved before mutation

Lease 180 repaired the proved first-H1 parser overreach, but the exact-head Internal Document-ID Audit run `33292104449` remains failed at job `99205415647` while Full-Stack and M2 succeeded on the same HEAD. Multiple direct attempts to retrieve a usable failed-job log did not yield the failing assertion through the available connector surface.

The current workflow `.github/workflows/internal-id-audit.yml` runs `pytest` before deterministic report generation/upload. Therefore any pytest failure prevents the report artifact from being generated and uploaded, hiding the exact audit findings needed by the required HARD-HOLD root-cause procedure.

This is an evidence-observability defect. It is not evidence that the detector is correct or incorrect, and it is not permission to weaken the detector or change repository identities.

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

- **C1 path collision:** PASS — new transaction record is unique and the workflow path already exists.
- **C2 semantic collision:** PASS — audit rules and identities are explicitly forbidden from mutation.
- **C3 authority collision:** PASS — no canonical/governance/release authority is changed.
- **C4 promotion collision:** PASS — no audit result or domain state is promoted by this lease.
- **C5 evidence collision:** PASS — the change exists only to preserve deterministic failure evidence that current step ordering suppresses.
- **C6 handoff collision:** PASS — 179/180 remain HARD HOLD until the real failing findings are exposed and resolved.

## Minimal repair contract

1. Preserve the existing pytest command and its ability to fail the job.
2. Ensure deterministic report generation executes even when pytest fails.
3. Ensure report artifact upload executes even when pytest fails.
4. Do not use `continue-on-error` to convert a failing audit into PASS.
5. Do not change detector/test semantics under this lease.
6. After merge, inspect the exact-head run and retrieve the deterministic report artifact or equivalent workflow evidence.
7. Treat any exposed identity finding as new evidence requiring its own root-cause classification; do not auto-repair identities.

## Learning candidate

`A FAILING AUDIT MUST PRESERVE ITS FAILURE EVIDENCE.`

A quality gate that suppresses its deterministic diagnostic output on failure weakens root-cause verification even when the gate correctly remains red.
