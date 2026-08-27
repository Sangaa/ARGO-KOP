# P307 — Executable Adapter Test Gate

Status: `CLOSED / ISOLATED / EVIDENCE-READY / NO-PRODUCTION-PROMOTION`

## Finding
A real `ENG-006 → SRV-009` production adapter already exists on the isolated branch and is backed by a provider-neutral `RepositoryConnector`. The adapter rejects unauthorized candidates, dispatches through the governed write dispatcher, and requires post-write read-back.

## Test surface
An isolated integration test already exercises:
- authorized candidate → governed dispatch → traceable accepted execution;
- unauthorized candidate → rejection before any connector call;
- create/update separation and current-identity protection through the connector fake.

## Boundary
This is implementation evidence for `ENG-006 → SRV-009`. It does NOT by itself prove `RUN-010 → ENG-006`, because the connected spine runner still selects `SIMULATED_REVIEW` and does not dispatch RUN-010 into this adapter.

## Decision
Do not promote or modify `main` from this evidence alone. The next gate is to execute this isolated adapter suite in CI and then prove the upstream RUN-010 consumer binding separately.

`ENG-006 → SRV-009 = IMPLEMENTED / ISOLATED TESTABLE`
`RUN-010 → ENG-006 = OPEN / NOT VERIFIED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
