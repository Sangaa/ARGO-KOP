# KRS-001 — Knowledge Reconciliation & Structural Migration Work Plan

Status: ACTIVE / GOVERNED WORK PLAN
Authority: GOV-013 + BOOTSTRAP-001

## Mandatory Session Path
1. BOOT — establish current repository, branch/ref and current commit.
2. LOAD — read PROJECT_BOOTSTRAP, GOV-013, current control-plane status and applicable authority.
3. RECOVER — inspect latest checkpoint, open work, matrices, EJR/session deltas and unfinished integration/CI state.
4. PRIOR-LEARNING — retrieve and classify relevant prior ARGO learning.
5. CURRENTNESS — inspect current content, identity, version/status, latest relevant change and later deltas/repairs for every material artifact used as evidence.
6. RELATIONSHIPS — inspect referenced targets and critical reverse consumers/authorities.
7. GAP — state the smallest verified gap before proposing mutation.
8. MATRIX — create/verify the mutation matrix before protected writes.
9. EXECUTE — perform the smallest sufficient mutation.
10. RE-READ — read every changed artifact from the repository after writing.
11. INTEGRATE — validate affected file↔file, module↔module, layer↔layer and test↔implementation relationships as applicable.
12. CI — inspect workflow, jobs, steps, logs and artifacts; a required failure is a hard hold.
13. RECONCILE — reconcile commit/file state, tests, runtime evidence, matrices and relationship state.
14. LEARN — record reusable learning and search/retrieval defects when materially useful.
15. CLOSE — update required indexes/status/EJR/session delta; record exact checkpoint and next target.
16. REPORT — concise report: completed / discovered / next action / blocker only.

## Mandatory Currentness Gate
Canonical, referenced, or VERIFIED status does not by itself establish current validity. Currentness is established proportionally to impact using current content, identity, version/status, latest relevant change, later EJR/session delta/repair/migration evidence, supersession/contradiction checks, and affected authority/consumers.

Classify evidence as CURRENT-VERIFIED, CURRENT-BUT-STALE-DEPENDENCY, HISTORICAL, SUPERSEDED, CONTRADICTED, UNRECONCILED, or UNKNOWN.

**Canonical identifies authority; current evidence establishes validity.**

## Structural Migration Principle
Migrate documents toward structured Knowledge Objects only when the pilot proves the structure improves traceability and validation. Preserve historical evidence. Blob/EDI-like segmentation is a structural target, not permission to create opaque monoliths.

## Pilot Boundary
First pilot: one canonical interface, architecture artifact, runtime artifact, EJR, repository record, mutation matrix, test, and governance artifact. No repository-wide rewrite is authorized until the pilot schema and migration method are validated.

## Mandatory Stop Conditions
Stop the affected decision when required current content is unavailable; a material relationship is contradictory/unreconciled; required CI fails; a protected write lacks a pre-write matrix; post-write re-read/relationship validation fails; migration would erase historical evidence; or a proposed change creates capability unsupported by a real architectural seam.

## Current Checkpoint
P224 = closed / execution-verified / non-production.
INTF-006 production provider/consumer remains unproven.
Next architectural work must pass the currentness/reconciliation gate before relying on legacy artifacts.
