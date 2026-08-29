# ARGO Control-Plane Convergence — Mutation Matrix

Transaction ID: `MUT-2026-08-29-CONTROL-PLANE-CONVERGENCE-001`
Protocols: `PROJECT_BOOTSTRAP / CORE-003 / GOV-006 / GOV-013 / GOV-013A / GOV-014 / GOV-016 / REP-015`
Base: `main@28e3ec16f1b0e6decee6623f77f48cda74e229c7`
Working branch: `argo/control-plane-convergence-20260829`
Status: `OPEN / PRE-MUTATION MATRIX ESTABLISHED / GAP RECONCILED`
Session mode: `SINGLE EXECUTOR`
Independent-review claim: `NONE — same-session verification must be labeled SELF_REVIEWED_NOT_INDEPENDENT`
Authority: `No new architectural or semantic authority created by this transaction`

## Entry evidence

Current-main re-entry established:

1. `PROJECT_BOOTSTRAP.md` requires repository-first, evidence-proportional review and bounded claims.
2. `CORE-003` requires one authoritative source per logical object, review before write, and controlled evolution.
3. `GOV-013` requires prior-learning retrieval, three-search treatment for material negative findings, minimal safe mutation, integration evidence, learning capture and deterministic closure.
4. `GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` is the indexed canonical mutation protocol with Document ID `GOV-014`.
5. `Governance/GOV-014_ARGO_SELF_ASSURANCE_AND_CAPABILITY_EVALUATION_PROTOCOL.md` also declares `GOV-014` and `CANONICAL`, creating a directly verified active identity collision.
6. `Governance/_FOLDER_STATUS.md` still claims the Governance baseline is clean as of 2026-08-08 and therefore predates the collision.
7. `REP-016` still records Priority 2 duplicate-ID audit as OPEN at checkpoint P351.
8. GitHub Control Room #71 and MAAT #74 are operationally stale: both were initialized against `main@94a9bbb...`, while current main is `28e3ec16...`.
9. There are currently no open pull requests; historical task issues #72/#73/#75 therefore cannot continue using their original PR assumptions without current-main reclassification.
10. Three materially different checks found no current active `Governance/GOV-015...` artifact, but `GOV-016` explicitly names `GOV-015 execution documentation and knowledge transfer` as a dependency. Therefore `GOV-015` is a demonstrated missing-governance dependency and MUST NOT be reused for Self-Assurance.
11. Three materially different checks found no current `GOV-017` artifact/reference. `GOV-017` is therefore the bounded candidate identity for the Self-Assurance migration, subject to index synchronization and post-write recheck.

## Governing decisions for this transaction

### D01 — Preserve canonical `GOV-014` ownership
`Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` retains `GOV-014` because it is already indexed as active canonical Governance authority and is consumed by the current mutation process.

### D02 — Migrate Self-Assurance identity rather than discard content
The self-assurance protocol remains materially useful, but its current ID/path is invalid. It will be migrated to `GOV-017`, whose absence was checked through independent retrieval methods. Historical conflicting content must be preserved under `Archive/Governance-Legacy/` before removal from the active conflicting path.

### D03 — Issue-native orchestration remains operational, not canonical authority
Control Room #71 and MAAT remain GitHub issue-native coordination surfaces. They may constrain work lanes and preserve handoffs, but they cannot override repository Governance, create semantic authority, or promote evidence.

### D04 — Parallel work uses explicit write leases
Future concurrent agents receive one task branch + exact semantic scope + allowed path globs + forbidden paths + baseline SHA. Reading may be broad; writing is lease-bounded. Shared semantic or file ownership means HOLD until reallocation.

### D05 — Independence is a property of evidence, not a role name
A role called MAAT/HORUS does not make a review independent when the same model/session performed the implementation. Same-session review must be `SELF_REVIEWED_NOT_INDEPENDENT`. Independent validation requires a distinct execution/evidence source sufficient for the claimed independence.

### D06 — Do not falsely close external evidence gaps
An issue/open point may be closed as completed or superseded only when current repository evidence makes its original work item no longer open. External/provider/cognitive-effect claims remain explicit HOLD/OPEN when the required evidence is unavailable.

### D07 — Repair the missing `GOV-015` contract rather than paper over it
Because `GOV-016` already depends on an execution-documentation/knowledge-transfer contract, the missing artifact is a demonstrated governance gap. Build only the minimum protocol needed to make session execution, handoff, provenance, parallel write leases, role boundaries and closure records deterministic. `GOV-015` will not create implementation or promotion authority.

### D08 — Self-Assurance becomes `GOV-017`
The existing Self-Assurance content is migrated to `GOV-017` with its claims preserved and its identity corrected. This keeps `GOV-015` available for its evidenced intended role and preserves `GOV-014` for controlled mutation.

## Planned change matrix

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | Governance Self-Assurance protocol identity | MIGRATE to `GOV-017` | remove active `GOV-014` collision without losing historical provenance | N | N |
| C02 | `Archive/Governance-Legacy/` | ADD | preserve pre-migration conflicting Self-Assurance artifact as historical evidence | N | N |
| C03 | `Governance/_FOLDER_STATUS.md` | UPDATE | replace stale CLEAN claim with current evidence and corrected active inventory | N | N |
| C04 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | register `GOV-015`, corrected `GOV-017`, and preserve canonical GOV-014 ownership | N | N |
| C05 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE if required | synchronize corrected canonical Governance paths | N | N |
| C06 | `Repository/REP-016_PHASE1_PARTITION_WORK_QUEUE.md` | UPDATE if safe/required | bind current duplicate-ID finding/disposition and current priority state without over-closing repository-wide audit | N | N |
| C07 | Control Room #71 | UPDATE | current-main snapshot, deterministic activation pipeline, write-lease contract, handoff/closure rules | N | N |
| C08 | MAAT #74 | UPDATE | stale-base reconciliation, lease/collision controller, independence boundary | N | N |
| C09 | HERMUZ #72 / HORUS #73 / HERMUZ #75 | RECLASSIFY/CLOSE where proven | eliminate obsolete task lanes already superseded by current main | N | N |
| C10 | historical open learning/session issues | RECLASSIFY/CLOSE where current evidence proves administrative completion | reduce open-work ambiguity without erasing evidence | N | N |
| C11 | current external/assurance gaps | HOLD/UPDATE | preserve unresolved evidence requirements instead of false closure | N | N |
| C12 | Engineering Journal | ADD | record re-evaluation, discovered defects, decisions, learning and closure evidence | N | N |
| C13 | CI / integration / exact-head verification | VERIFY | run/observe required checks on the promotion candidate before any main merge | N | N |
| C14 | Post-merge/current-main read-back | VERIFY | prove final persisted state and synchronize #71 | N | N |
| C15 | `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER_PROTOCOL.md` | ADD | satisfy the explicitly referenced GOV-016 dependency with minimum sufficient execution/handoff contract | N | N |
| C16 | `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` | VERIFY/UPDATE only if required | ensure its GOV-015 dependency resolves to the new exact canonical path without semantic broadening | N | N |

## Abort / hold conditions

Abort or hold the affected change if:

- candidate Governance identity is not proven unique;
- full source content cannot be read before replacement;
- a canonical path/ID change cannot be synchronized with its indexes;
- an issue's original closure condition is not demonstrably satisfied or superseded;
- required CI/check evidence fails or is not observable for a claim that depends on it;
- current `main` moves in a way that affects this transaction before promotion;
- an unexpected path or semantic collision appears.

## Intended bounded result

This transaction may establish a cleaner current control plane, unique Governance identities for the affected protocols, deterministic future agent write lanes, and explicit current open/HOLD work.

It does **not** by itself establish:

- repository-wide duplicate-ID closure;
- repository-wide Connected-Baseline closure;
- external provider authenticity;
- model-execution authenticity;
- independent cognitive improvement;
- global `BOOTED / INTEGRITY PASS`.
