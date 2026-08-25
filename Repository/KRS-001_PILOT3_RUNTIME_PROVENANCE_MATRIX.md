# KRS-001 Pilot 3 — Runtime / Provenance Currentness & Relationship Matrix

Status: PRE-WRITE / CONTROLLED
Purpose: establish the evidence boundary before objectization of one runtime/provenance artifact.

## Selected corpus
Primary source: `Runtime/Prototype/PROTOTYPE_INTEGRATION_CONTRACT.md`
Source blob SHA: `37a78805de9f26c66bf84e080c14db83b5ebc544`
Current source ref: to be resolved to an immutable commit SHA before objectization.

Related evidence surfaces:
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md` blob `93328ca4138f0389f23b8468973f10cf2849b28d`
- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md`

## Currentness checks
| Check | Required proof | State |
|---|---|---|
| Exact source content | Fetch current file | PASS |
| Exact source blob identity | GitHub blob SHA | PASS |
| Immutable source commit | Commit containing exact blob | PENDING |
| Last direct change | Commit metadata | PENDING |
| Related artifact currency | Fetch + compare refs | PENDING |
| Relationship semantics | Source text + related contracts | PENDING |
| Runtime execution evidence | Workflow/run/job evidence | PENDING |
| Evidence layer classification | Structural vs runtime separated | PENDING |
| Migration mutation SHA | Only after objectization | N/A |
| CI correlation | Exact mutation SHA | N/A |

## Relationship candidates
1. Contract -> RUN-011: `REFERENCES / DEFINES-BOUNDARY` (to verify)
2. Contract -> RUN-012: `REFERENCES / TEST-CONTRACT` (to verify)
3. Contract -> ENG-013: `RELATED-CANONICAL-CONTRACT` (to verify)
4. Contract -> ENG-014: `RELATED-VALIDATION-CONTRACT` (to verify)

A relationship is not accepted merely because a path appears in a Related Artifacts list.

## Expected schema pressure points
Pilot 3 must test whether v0.3 can represent:
- immutable source blob + immutable source commit together;
- structural contract evidence separately from executable runtime evidence;
- integrity hold as a currentness/authority state without implying execution failure;
- relationship evidence without promoting related documents into evidence of execution;
- historical vs current runtime claims.

## Gate
No Knowledge Object is created in this step. First resolve immutable source commit, direct-change history, relationship evidence, and runtime evidence surfaces. If these checks reveal a schema gap, return to v0.3 refinement before objectization.
