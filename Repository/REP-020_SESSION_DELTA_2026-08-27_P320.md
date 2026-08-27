# P320 — Real Provider Binding Gate

Status: `IMPLEMENTED / ISOLATED / CI-PENDING / NO-PROMOTION`

## Completed
Added a fail-closed provider factory that constructs the existing concrete GitHub connector from environment configuration and supplies it to the existing ENG-006 → SRV-009 adapter.

## Safety
No credentials are committed. Missing configuration raises `GITHUB_CONNECTOR_CONFIGURATION_INCOMPLETE`. Existing authorization, SHA revalidation, post-write read-back, and connector failure semantics remain delegated to existing components.

## Test
Added a fail-closed configuration test. No live repository mutation is performed by the test.

## Boundary
This establishes the real-provider binding seam but does not claim live end-to-end execution. A controlled non-canonical target and CI evidence are still required before any promotion decision.

`RUN-010 → ENG-006 → SRV-009 = BOUND / LIVE EXECUTION NOT VERIFIED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
`SESSION = CLOSED`
