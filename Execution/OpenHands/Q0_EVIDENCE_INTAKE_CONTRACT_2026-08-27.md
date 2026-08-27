# P330 — Q0 External Evidence Intake Contract

Status: `GOVERNED / NO-MUTATION / NO-AUTHORIZATION`

## Purpose
Close the recurring ambiguity between repository CI evidence and actual OpenHands Q0 qualification evidence.

## Rule
Repository CI may verify the qualification harness, but cannot substitute for observations from the actual OpenHands execution environment.

## Required Q0 evidence
A Q0 submission is admissible only when it records, from the actual runner:
- OpenHands exact version and source/release;
- Python/runtime version;
- workspace identity and isolation boundary;
- model/provider identity (without secrets);
- permissions/capability state;
- network/sandbox state;
- Git identity/configuration relevant to execution;
- enabled integrations relevant to later gates;
- timestamp and runner identity sufficient for reproducibility.

## Acceptance
`Q0 PASS` requires all required fields to be observed and internally consistent. Missing, inferred, redacted beyond verification, or repository-only evidence yields `INSUFFICIENT EVIDENCE`, not PASS.

## Security
Never submit tokens, API keys, cookies, private keys, or other secrets. Secret presence may be represented as `PRESENT/REDACTED` only where the gate requires proving existence rather than value.

## Authority boundary
Q0 is identity-only. A successful Q0 submission grants no repository write authority and does not authorize Q1-Q7.

`Q0 = WAITING FOR EXTERNAL RUNNER EVIDENCE`
`Q1-Q7 = NOT AUTHORIZED`
`REL-009 = OPEN`
`MAIN = UNCHANGED`
