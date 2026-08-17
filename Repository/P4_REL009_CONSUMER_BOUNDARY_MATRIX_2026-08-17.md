# P4 — REL-009 Consumer Boundary Matrix

Date: 2026-08-17
Status: `EXECUTION-VERIFIED / RELATIONSHIP-REMAINING-OPEN`
Authority: `GOV-013 / GOV-014 / GOV-015`

## Purpose
Protect unresolved `REL-009: RUN-010 → SRV-009` from speculative promotion.

This is a safety/evidence gate. It does not manufacture runtime evidence or authorize canonical relationship promotion.

## Required Promotion Evidence

A future `VERIFIED` promotion requires independent callable-consumer evidence from RUN-010 execution context to SRV-009 plus runtime execution evidence reaching that path.

Architectural prose, shared workflow descriptions, repository-wide audit completeness, or ENG-006 → SRV-009 proof alone are insufficient.

## Gate

| Gate | Condition | Current State |
|---|---|---|
| B01 | REL-009 exists in canonical registry | VERIFIED |
| B02 | Registry remains `REVALIDATION REQUIRED` until executable proof exists | VERIFIED |
| B03 | RUN-010 distinguishes relationship description from universal runtime-path proof | VERIFIED |
| B04 | Automated safety test prevents accidental `VERIFIED` promotion | EXECUTION-VERIFIED |
| B05 | Boundary gate integrated into proven Full-Stack CI | VERIFIED |
| B06 | CI execution on current HEAD | VERIFIED |
| B07 | Independent callable consumer source evidence | NOT FOUND |
| B08 | Independent runtime execution trace proving RUN-010 → SRV-009 | NOT FOUND |

## Execution Evidence

- Full-Stack workflow: `333498182`
- Successful run: `32046636097`
- Successful job: `95435955639`
- Verified stages:
  - P4 REL-009 consumer boundary safety gate: `SUCCESS`
  - Repository-wide audit: `SUCCESS`
  - Real runtime evidence emission: `SUCCESS`
  - Audit evidence upload: `SUCCESS`
  - Runtime evidence upload: `SUCCESS`

## Promotion Rule

Only when B06, B07 and B08 are satisfied may the relationship state be reconsidered.

Until then:

`REL-009 = DOCUMENTED / CONTRACTUAL / REVALIDATION REQUIRED`

## Current Evidence Boundary

- RUN-010 explicitly treats the execution chain as a relationship description, not proof that every runtime operation follows it.
- ENG-006 → SRV-009 executable evidence does not propagate to RUN-010 → SRV-009 automatically.
- The safety test is intentionally negative and side-effect free.
- CI verification of the safety gate proves the gate executes; it does not prove the relationship itself.

## Test Hardening Learning

The first CI implementation failed because the assertion searched for wording that differed from the canonical RUN-010 sentence even though the underlying evidence boundary was correct.

The final gate matches the canonical sentence exactly and keeps the assertion set minimal. This avoids turning harmless document-layout/wording drift into a false infrastructure failure while preserving the actual evidence boundary.

This learning is reusable for future repository safety gates: assert stable canonical evidence, not approximate paraphrases.

## Model-Independence

The gate is repository-controlled and does not depend on conversational memory or model identity.

---

End of Matrix
