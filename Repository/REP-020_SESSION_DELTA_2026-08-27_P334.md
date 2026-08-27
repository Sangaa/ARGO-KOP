# P334 — Multi-Instance Execution Amendment Reconciliation

Status: `CLOSED / DOCUMENTED / NO-RUNTIME-MUTATION`

## Finding
Current `main` evidence reports GOV-013 version `1.1.2` and does not contain the previously claimed promoted `1.2.0` multi-instance amendment. Therefore the prior conversational claim that the amendment was already canonical is not accepted as repository truth.

## Action
Created `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` as a governance-controlled `PROPOSED` amendment. It defines repository-first re-entry, concurrent-work boundaries, shared evidence graph, evidence precedence, no-rebuild-from-memory, safe mutation and independent handoff.

## Important Correction
No canonical promotion is claimed in this checkpoint. The amendment must pass the existing governance/learning promotion path before becoming part of GOV-013's canonical authority.

## Operational Rule Now
Until promotion, the existing GOV-013 remains controlling. Future sessions may use the proposed model as analysis/design evidence but must not represent GOV-013A as canonical authority.

## Safety
No runtime code changed. No credentials or authority changed. No production mutation performed.

`GOV-013 = CANONICAL v1.1.2`
`GOV-013A = PROPOSED`
`RUNTIME = UNCHANGED`
`MAIN = DOCUMENTED`
`SESSION = CLOSED`
