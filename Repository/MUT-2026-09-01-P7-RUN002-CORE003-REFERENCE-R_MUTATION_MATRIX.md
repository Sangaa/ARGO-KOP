# MUTATION MATRIX — P7 RUN-002 → CORE-003 INITIALIZATION AUTHORITY REFERENCE — R

Transaction: `MUT-2026-09-01-P7-RUN002-CORE003-REFERENCE-R`
Work Lease: `HERMUZ-P7-R-RUN002-CORE003-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / VALIDATION-FIRST / PRIORITY-7-OPEN`
Entry HEAD: `abfa867f2fa5d34ac1430f39e2c40143327f1018`
Pre-write Matrix HEAD: `33ce1e490b07fa1a123930b3c7dd958c471924c3`
Material candidate: `c5c695597a6df18876ff83542c65bed2797fe98f`
Side-repair closure before R resumption: `411b63b4ed62186a1dde00212071766241d582d7`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020`

## Bounded validated finding

Direct evidence supports only:

`RUN-002 → CORE-003 = REFERENCES`

Disposition: `INTENTIONAL ONE-WAY / INITIALIZATION-AUTHORITY-RESOLUTION-ALIGNED / NON-DEPENDENCY`.

RUN-002 is canonical/critical initialization, requires validation before execution, verifies declared dependencies, prevents Runtime READY under failed/held integrity, enters governed FAULT/HOLD when required authority cannot be resolved, and directly lists CORE-003. The Constitution's broad applicability remains background authority and does not authorize a separately enumerated `CORE-003 → RUN-002` row without stronger source-specific evidence.

## Material change-set result

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| R-01 | `Quality/Integrity/test_run002_core003_initialization_authority_reference.py` | CREATE bounded direct-source/negative-semantics regression | Y | Y |
| R-02 | `Repository/P7_RUN002_CORE003_INITIALIZATION_AUTHORITY_REFERENCE_2026-09-01_R.md` | CREATE bounded validation record | Y | Y |
| R-03 | this Matrix | UPDATE in same material change set | Y | Y |

Material atomicity: compare `33ce1e49... -> c5c69559...` established exactly one material commit, exactly the three authorized paths, unexpected path expansion `0`.

## Candidate exact-head verification

Exact material candidate: `c5c695597a6df18876ff83542c65bed2797fe98f`

Required four workflows all completed `SUCCESS`:

- Full-Stack Repository Audit — `33527139317` — SUCCESS.
  - exact checkout SHA binding — SUCCESS;
  - Mutation Matrix preflight — SUCCESS;
  - Matrix semantic enforcement — SUCCESS;
  - current-change-set Matrix enforcement — SUCCESS;
  - repository-wide audit — SUCCESS.
- ARGO Runtime Prototype and Integration Tests — `33527139372` — SUCCESS.
  - integrity-tests — SUCCESS;
  - prototype-tests — SUCCESS;
  - integration-tests — SUCCESS.
- Real Mutation Matrix Regression — `33527139367` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33527139347` — SUCCESS.

No R semantic/material CI failure occurred.

## Interruption and governed side-repair

During R closure preparation, an implementation error invoked a direct repository write instead of Git-object preparation and created the unauthorized empty path `Repository/INVALID_SHOULD_NOT_CREATE.tmp` in commit `c38783c38962063a7fc38f6c99adad3547e4e6fd`.

A first recovery sequence then violated its own requested atomicity when the authorized incident record was written separately in commit `86d4ea5cf392fd28f777f7f13affadd64d04b8d0`.

Both failures are preserved and classified under the recovery evidence:

- `Repository/R_UNAUTHORIZED_TMP_INCIDENT_2026-09-01.md`;
- `Repository/MUT-2026-09-01-R-RECOVERY-MATRIX.md`;
- `Repository/MUT-2026-09-01-R-RECOVERY-V2-MATRIX.md`.

Recovery V2 used a pre-write Matrix and Git Data atomic mutation. Material recovery candidate `fad267c623c181aaa792a085f0d921105c034074` removed the temp artifact with exactly two authorized paths and zero path expansion. The closure commit `411b63b4ed62186a1dde00212071766241d582d7` passed the actual triggered closure surface:

- Full-Stack Repository Audit — `33529159247` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33529159117` — SUCCESS;
- M2 Multi-Channel Proposal Training — `33529159017` — SUCCESS;
- Real Mutation Matrix Regression — not triggered on that recovery closure change set; no nonexistent PASS is claimed.

Full-Stack closure job passed exact-SHA binding, Matrix enforcement and repository-wide audit; Runtime integrity/prototype/integration jobs all succeeded.

Comparison `c5c69559... -> 411b63b4...` shows the side-repair's net repository delta consists only of the three recovery evidence files. The R Matrix, R validation record and focused R test retain the same blobs as the original validated material candidate. Therefore the side-repair did not alter R semantics and the original R Work Lease resumes rather than being replaced by a new semantic transaction.

## KEEP / non-authority

- RUN-002 source unchanged.
- CORE-003 source unchanged.
- REP-014 remains unchanged by R.
- REP-020 and Core status remain unchanged by R.
- No `RUN-002 → CORE-003` DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES.
- No `CORE-003 → RUN-002` row of any type.
- No executable coupling, Runtime/Core certification, Priority-7/Phase-1/Connected-Baseline/repository-wide-graph/Global-PASS closure.

## Prior learning and failure-to-learning disposition

P/Q and N/O remain directly applicable; REL-037/038 remains transferable but not mechanically copied; ARC_MAP navigation-only boundary remains negative transferable evidence against relationship inflation.

The closure interruption produced real learning but did not expose a missing governance rule: GOV-014/GOV-014A already required pre-write authorization and transactional discipline. Retained session-level execution lesson:

`BEFORE WRITE-CAPABLE INVOCATION -> VERIFY ACTION TYPE -> EXACT PATH(S) -> MATRIX AUTHORIZATION -> REQUIRED ATOMICITY -> WHETHER MAIN MOVES`.

The incident also showed that green CI on the accidental commit did not equal transaction-scope authorization proof. That is retained as a bounded candidate for later CI-coverage analysis, not promoted here to a new rule or test without separate validation.

## Closure contract

This R closure commit is documentation/control reconciliation only: update this Matrix and the R transaction record. It does not alter the material candidate, test, sources, registry or folder state.

The state at the top becomes authoritative only if the exact R closure HEAD passes the original R requirement:

`FOUR REQUIRED WORKFLOWS -> FULL-STACK JOB/STEP REVIEW -> RUNTIME JOB REVIEW`.

If any required R closure workflow fails or is absent when the R trigger contract requires it, R returns to HOLD and the failure is preserved under GOV-016.

## Post-closure continuation boundary

R is validation-only. Closure does **not** authorize a REP-014 mutation. After exact closure-head verification, the next legal action is a fresh Priority-7 recomputation under live evidence. `RUN-002 → CORE-003 = REFERENCES` may be considered for registry synchronization only if current evidence establishes that registration is materially required; REP-014 is deliberately not a complete graph.
