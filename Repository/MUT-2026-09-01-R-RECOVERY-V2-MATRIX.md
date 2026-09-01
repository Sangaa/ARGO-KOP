# R RECOVERY V2 MUTATION MATRIX

Transaction: `MUT-2026-09-01-R-RECOVERY-V2`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RECOVERY-COMPLETE / RETURN-TO-R`
Entry HEAD: `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`
Pre-write V2 Matrix HEAD: `28ddda52577cbffaa24d0f43ba01f3ac49ea698b`
Material recovery candidate: `fad267c623c181aaa792a085f0d921105c034074`
Original incident: `c38783c38962063a7fc38f6c99adad3547e4e6fd`
Recovery V1 Matrix: `671123cc83655bc35e8d07b60e0c416eb5b396e9`
V1 sequencing deviation: `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`

## Recovery result

The unintended empty artifact `Repository/INVALID_SHOULD_NOT_CREATE.tmp` is absent from the material recovery candidate.

Absence/effect evidence is independently supported by:

1. direct exact-head fetch at `fad267c6...` -> `404 Not Found`;
2. compare `28ddda52... -> fad267c6...` -> exactly one commit, exactly two paths, temp artifact `removed`, this Matrix `modified`;
3. exact candidate commit metadata -> only the temp path and this Matrix appear in the commit file set.

The incident commit remains preserved in Git history. Recovery V1 sequencing failure also remains preserved. No reset, force push, concealment, or history rewrite was used.

## Authorized V2 material change-set result

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| RV2-01 | `Repository/INVALID_SHOULD_NOT_CREATE.tmp` | REMOVE unintended empty artifact | Y | Y |
| RV2-02 | this Matrix | UPDATE/rebind V2 candidate state | Y | Y |

Atomicity: `1 commit / 2 authorized paths / unexpected path expansion 0`.

## Candidate CI / integration evidence

Exact candidate: `fad267c623c181aaa792a085f0d921105c034074`

Triggered workflows observed on this exact head:

- Full-Stack Repository Audit — run `33528942741` — `SUCCESS`.
  - checkout-SHA binding — SUCCESS;
  - Mutation Matrix preflight — SUCCESS;
  - Mutation Matrix semantic regression — SUCCESS;
  - current-change-set Matrix enforcement — SUCCESS;
  - repository-wide audit — SUCCESS;
  - runtime evidence emission — SUCCESS.
- ARGO Runtime Prototype and Integration Tests — run `33528942723` — `SUCCESS`.
  - integrity-tests — SUCCESS;
  - prototype-tests — SUCCESS;
  - integration-tests — SUCCESS.
- M2 Multi-Channel Proposal Training — run `33528942717` — `SUCCESS`.
- Real Mutation Matrix Regression — `NOT TRIGGERED ON THIS CHANGE SET`; no run is invented and no PASS is claimed for a nonexistent run.

The triggered candidate verification surface is green. Full-Stack and Runtime/Integration, the mandatory checkpoint evidence specified by V2, both passed.

## Failure chain retained

1. `c38783c3...` — `IMPLEMENTATION_FAILURE / ORIGINAL WRITE NON-COMPLIANT`: wrong repository write action created an unauthorized empty temp path outside the R Matrix.
2. First recovery-Matrix attempt — `INFRASTRUCTURE/TOOLING LIMITATION`: connector blocked the request before repository mutation.
3. `86d4ea5c...` — `IMPLEMENTATION_FAILURE / MATRIX-SEQUENCING NON-COMPLIANCE`: the authorized incident record was written separately, violating Recovery V1 atomicity.
4. V2 corrected the remaining repository state using a pre-write Matrix and an atomic two-path Git Data material commit.

## What did not change

- Transaction-R semantic finding and focused test remain unchanged.
- RUN-002 and CORE-003 source content remain unchanged.
- REP-014 remains v1.2.14 with REL-001..072 unchanged.
- Core status remains v1.3.11 / Priority 7 OPEN.
- No relationship, dependency, authority, certification, Phase-1, Connected-Baseline, repository-wide-graph, or Global-PASS promotion occurred.

## Learning disposition

Existing GOV-014 and GOV-014A were sufficient authority to identify both execution failures. Therefore no new governance document/rule is justified.

Retained `SESSION-LEARNING`:

`BEFORE WRITE-CAPABLE INVOCATION -> VERIFY ACTION TYPE -> EXACT PATH(S) -> MATRIX AUTHORIZATION -> REQUIRED ATOMICITY -> WHETHER MAIN MOVES`.

A second bounded observation also exists: the unauthorized `.tmp` incident commit passed the triggered Full-Stack/Runtime/M2 workflows. This proves only that green CI is not equivalent to transaction-scope authorization proof for that exact incident. Whether CI should gain a new generic regression for this mechanism remains a future candidate requiring separate scope/evidence; V2 does not promote that candidate.

## Closure boundary

V2 is a side-repair only. On successful exact-head verification of the closure commit containing this Matrix, the legal continuation is:

`SIDE-REPAIR CLOSED -> RETURN TO PREVIOUS GLOBAL PRIORITY -> RESUME TRANSACTION R`.

This closure does not itself close R or Priority 7.

The state declared at the top of this file is effective only when the exact closure HEAD itself passes the applicable triggered verification surface. If closure-head verification fails, V2 returns to `OPEN/HOLD` and the failure must be preserved under GOV-016.
