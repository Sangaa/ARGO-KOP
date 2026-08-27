# MULTI-INSTANCE RE-ENTRY VALIDATION MATRIX

Status: `GOVERNED TEST SPEC / NO-AUTHORITY`
Parent: `GOV-013A`

## Objective
Provide an executable, evidence-based validation path for repository-first continuity across materially independent execution contexts without granting runtime or production authority.

## Test Contexts
A = window/instance 1
B = window/instance 2
C = optional third independent context

## Matrix
| ID | Scenario | Expected Result | Evidence |
|---|---|---|---|
| MI-01 | B enters after A changes repository | B reads current HEAD/change before acting | current ref + change inspection |
| MI-02 | B has stale conversational completion claim | repository evidence wins; item becomes reconciled/unreconciled as appropriate | checkpoint + current artifact |
| MI-03 | A and B target materially distinct seams | both may proceed within declared scopes | scope declarations + diffs |
| MI-04 | A and B target overlapping surface | mutation is paused until impact reconciliation | pre-check + comparison |
| MI-05 | A mutation changes a relationship consumed by B | B re-reads and revalidates affected relationship | relationship/test evidence |
| MI-06 | one context closes and another resumes | second context reconstructs state without originating conversation | independent handoff record |
| MI-07 | stale context attempts overwrite of newer change | newer repository state is preserved; stale mutation is rejected/reconciled | compare/diff evidence |
| MI-08 | CI result differs from session expectation | CI/current runtime evidence controls the decision | CI record |

## Pass Criteria
All applicable scenarios must show repository-first re-entry, stale-state detection, bounded mutation, relationship revalidation, and reconstructable handoff evidence.

## Non-Claims
This matrix does not itself prove multi-instance behavior. It is a validation specification. Passing requires actual independent executions and recorded evidence.

## Safety Boundary
No production credentials, no canonical-main destructive operation, and no live side-effect is required for the validation. Test mutations must use a governed non-production branch or isolated test surface.

## Promotion Rule
A successful run produces evidence for the learning promotion gate; it does not automatically promote GOV-013A.
