# EJR-336A — Multi-Instance Repository-First Learning

Status: `REUSABLE-LEARNING / VALIDATED-BOUNDARY / NOT-AUTHORITY`

## Observation
Parallel AI/window/platform execution can cause session-local knowledge to diverge from current repository state.

## Root Cause
A session is transient context; the repository is the durable shared project state. Treating conversation memory as authoritative creates stale-continuation risk.

## General Rule Candidate
Every continuation must re-enter through current repository evidence, reconcile recent changes, define a bounded scope, and revalidate relationships after mutation.

## Evidence Boundary
The principle is supported by repeated operational tests in the project, including the discovery that conversational claims can disagree with current repository state. This establishes a reusable learning candidate, but not independent statistical validation across separate instances.

## Reuse
Applicable to concurrent AI agents, browser windows, platforms, and human/AI collaboration. It does not grant mutation authority.

## Promotion Requirement
Independent validation across materially separate execution contexts is required before promoting the candidate to a new governing rule/default practice.

`SOURCE = P336/P336A`
`PROMOTION = PENDING`
`AUTHORITY = NONE`
