# P8 REL-010 Bounded Revalidation Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL010-REVALIDATION-001`
Priority: `8 — Governance`
State: `TYPE-CORRECTED MATERIAL CANDIDATE / CI PENDING`
Entry HEAD: `4354a16f4abc7c3311c9810d8c7cbf6a5f53634a`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-014`

## Legal-entry proof

Priority 8 remains OPEN. REL-003 is closed/verified. REL-004 was re-read and retained as `Revalidation Required` because current evidence does not justify a legal material correction or promotion. REL-010 is the next smallest material candidate requiring direct source review.

## Selected relationship

`MOD-011 → KNW-002 = DEPENDS_ON`

Current REP-014 state: `Revalidation Required`.

## Direct current evidence

- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md` is canonical but remains `Proposed / Future-Ready / Revalidation Required`.
- MOD-011 explicitly records a Temporal / Provenance Boundary: its current semantic content was materially mutated during a pre-failure session and is retained provisionally pending independent revalidation.
- MOD-011 names `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md` as a related document and requires Knowledge classification review for material source/provenance changes.
- `Knowledge/KNW-002_KNOWLEDGE_CLASSIFICATION.md` is canonical / `Integrity Hold / Revalidated` and explicitly states that MOD-011 defines the source/provenance semantic boundary consumed by classification.

## Hold determination

The two artifacts establish a material semantic coupling, but the source model carrying the asserted `DEPENDS_ON` edge is itself explicitly provisional and not fully semantically revalidated. Promoting REL-010 from `Revalidation Required` would therefore certify more than the current authority/evidence permits.

No REP-014 material mutation is legal at this checkpoint.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL010-01 | REP-014 REL-010 row | KEEP | `Revalidation Required` | Y | Y |
| P8-REL010-02 | MOD-011 | KEEP | no source mutation | Y | Y |
| P8-REL010-03 | KNW-002 | KEEP | no source mutation | Y | Y |
| P8-REL010-04 | this Matrix | CREATE | preserve HOLD + exact resume point | Y | Y |

## Forbidden boundaries

- no REL-010 promotion while MOD-011 semantic revalidation is unresolved;
- no queue promotion;
- no Priority-8 closure;
- no inferred reverse edge;
- no mutation of MOD-011 or KNW-002 under this transaction;
- no global graph/integrity PASS.

## Learning

A bidirectional documentary/semantic reference can establish coupling without being sufficient to promote a registry dependency when one endpoint explicitly declares its own semantic content provisional. Endpoint existence plus mutual reference is not a substitute for source-authority revalidation.

## Resume condition

Resume REL-010 only after current repository evidence independently revalidates the applicable MOD-011 semantic boundary, or supplies stronger governed evidence that legally resolves the relationship without over-certifying MOD-011.

`P8 REL-010 = HARD HOLD / PRE-MATERIAL ABORT / RESUME-SAFE`.

Priority 8 remains OPEN.

## Resume Phase — 2026-09-02

Resume HEAD: `dab69686a6100e63bb9323decb75451bf2e955b0`
Resume pre-write Matrix HEAD: `451f22c1af638e6d8915630b49fdd91c25c9d358`
Current REP-014 source blob: `5e0de8fc8ed0c9f28d9ef6e95315ae8f9e956dfc`
Resolved prerequisite: `MUT-2026-09-02-P8-MOD011-SEMANTIC-REVALIDATION-001` plus exact-head Runtime stale-guard side repair `MUT-2026-09-02-P8-MOD011-RUNTIME-STALE-GUARD-SR1`.

The former endpoint-provisional blocker is resolved only within MOD-011's inspected source/provenance semantic scope. MOD-011 remains `Proposed / Future-Ready`; Models-folder and repository-wide certification remain unchanged.

### Required relationship evidence

| Gate | Result | Evidence-bounded determination |
|---|---|---|
| SOURCE AUTHORITY | PASS / BOUNDED | `KNW-002` is Canonical / Integrity Hold / Revalidated and owns Knowledge Classification semantics |
| TARGET AUTHORITY | PASS / BOUNDED | `MOD-011` is Canonical / Proposed / Future-Ready / Revalidated and owns the inspected external-source/provenance semantic boundary |
| SEMANTIC DIRECTION | CURRENT ROW FAIL | KNW-002 explicitly says classification consumes MOD-011 source/evidence semantics; the necessary direction is `KNW-002 → MOD-011`, not the reverse |
| DEPENDENCY NECESSITY | PASS FOR CORRECTED EDGE | KNW-002's connected-source classification boundary relies on MOD-011 definitions; MOD-011 remains understandable without KNW-002 and names it as a downstream review/related surface |
| CONSUMER / IMPACT | PASS / BOUNDED | direct exact-row, semantic reverse, historical and Quality/Tools searches found no executable consumer of the old direction; impact is confined to REP-014 and this transaction record |
| TYPE FIT | `CONSUMES` | exact source wording is “Classification consumes those source and evidence semantics”; `REFERENCES` is too weak, generic `DEPENDS_ON` is less precise, and no `IMPLEMENTS/GOVERNS/VALIDATES` relation is supported |

Disposition: `TYPE CORRECTION REQUIRED`.

Authorized corrected row:

`REL-010 | KNW-002 | MOD-011 | CONSUMES | Revalidated within inspected scope`

### Resume Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL010-R1 | REP-014 REL-010 row | UPDATE | reverse direction to `KNW-002 → MOD-011`, replace `DEPENDS_ON` with `CONSUMES`, set bounded revalidated state | Y | PENDING CI |
| P8-REL010-R2 | all other REP-014 content | KEEP | byte-for-byte/content-equivalent | Y | Y |
| P8-REL010-R3 | MOD-011 / KNW-002 | KEEP | no endpoint mutation or promotion | Y | Y |
| P8-REL010-R4 | this Matrix | UPDATE | bind material compare, read-back, CI and closure evidence | Y | PENDING CI |

Material transaction atomicity: exactly one commit after this pre-write Matrix HEAD, exactly `2` changed paths (REP-014 + this Matrix), unexpected paths `0`.

Forbidden: no reverse companion edge, no endpoint maturity promotion, no Models/Knowledge folder certification, no Priority-8/Phase-1/global closure, no global graph or integrity PASS.

Closure requires immutable read-back, one-row REP-014 diff, four required exact-head workflows with full Runtime job split reviewed, Matrix reconciliation and closure-head verification.

Pre-write Matrix HEAD verification: Full-Stack `33682201838`, Runtime/Integration `33682201859`, Real Mutation Matrix `33682201952`, and M2 `33682201844` all succeeded; Runtime jobs `integration-tests`, `integrity-tests`, and `prototype-tests` all succeeded.
