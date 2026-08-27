# P330 — Q0 Evidence Intake Boundary

Status: `CLOSED / GOVERNED / NO-MUTATION`

## Action
Converted the recurring Q0 environment blocker into a canonical evidence-intake contract rather than repeatedly attempting an unavailable host execution.

## Result
The repository now distinguishes:
1. qualification-harness CI evidence; and
2. actual OpenHands runner observations required for Q0.

The contract lists the exact admissible Q0 fields, acceptance rule, secret-handling rule, and authority boundary.

## Decision
No Q0 PASS is claimed. No Q1-Q7 authority is granted. No credentials or side effects are introduced.

`Q0 = WAITING FOR EXTERNAL RUNNER EVIDENCE`
`Q1-Q7 = NOT AUTHORIZED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
`SESSION = CLOSED`
