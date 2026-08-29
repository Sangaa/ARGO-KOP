# HORUS — SEMANTIC EXPERIENCE AUDIT

Date: 2026-08-29
Role: HORUS / ANALYZE_META_LEARNING_AND_EVIDENCE
Control Room: 71
Entry baseline: `main@2cf3366564f8ce2fee3f16f385d34ec2f13a5221`
Working branch: `horus/room71-semantic-experience-audit-20260829`
Status: `HORUS-REPORTED / ANALYTICAL / NON-AUTHORITATIVE`
Authority: NONE
Promotion: NOT AUTHORIZED
Mutation boundary: `HORUS/**` only

## 1. Purpose

Test the semantic body of reusable ARGO experience before expanding retrieval machinery.

The audit asks whether a lesson can be reconstructed as:

`SOURCE → OBSERVED FACTS → INFERENCE → INVARIANT → BOUNDARY → COUNTERINDICATION → TRANSFER CLAIM → CURRENT APPLICABILITY`

It does not re-promote Memory records, rewrite Knowledge, or modify the Experience Spine implementation.

## 2. Sources inspected

Primary reusable-memory source:

- `Memory/MEM-009_MEMORY_EVOLUTION.md`

Primary provenance samples:

- `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md`
- `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`
- `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md`

Reasoning / failure boundaries:

- `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`
- `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md` — candidate, noncanonical, used only as bounded analytical support.

Current implementation/evidence context:

- `Knowledge/Learning/experience_spine.py`
- `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md`
- `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001.md`
- latest Room71 bounded inventory/reconciliation records available at re-entry.

## 3. Audit classes

These classes are HORUS analytical labels only.

- `A` — STRUCTURALLY SOUND / TRANSFER-CANDIDATE
- `B` — USEFUL BUT BOUNDED
- `C` — HISTORICALLY VALUABLE / CURRENTLY STALE
- `D` — CORRELATED SUPPORT ONLY
- `E` — SEMANTIC CONFLICT
- `F` — OVER-GENERALIZED
- `G` — CONTENT INSUFFICIENT
- `H` — AUTHORITY-CONTAMINATED

## 4. Sample audit

### SEA-01 — CI success is scope-bound

**Source:** MEM-009 lesson 1; EJR-211.

**Observed facts:** Passing workflows repeatedly coexisted with independent repository blockers.

**Inference:** A successful workflow demonstrates successful execution only over the workflow's tested surface.

**Invariant:** `PASS SIGNAL STRENGTH MUST NOT EXCEED TESTED SCOPE`.

**Boundary:** If a workflow is itself proven to exhaustively cover the target claim, its PASS may support that bounded exhaustive claim. It still does not establish unrelated authority or semantics.

**Counterindication:** A test suite whose coverage contract exactly matches the claim and whose execution identity is verified is stronger evidence than an ad-hoc partial CI pass.

**Transfer claim:** Applies to CI, audits, focused tests, connector checks and other bounded validation channels.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-02 — Documentation is not execution proof

**Source:** MEM-009 lesson 2; EJR-211.

**Observed facts:** Markdown, indexes and matrices declared relationships whose executable consumer path was still unverified.

**Inference:** A declaration proves the declaration and its provenance; it does not prove runtime execution of the declared edge.

**Invariant:** `DECLARED RELATIONSHIP != EXECUTED RELATIONSHIP`.

**Boundary:** Documentation can be authoritative for a normative declaration when the document itself has that authority. The invariant is about factual execution claims, not whether governance text can prescribe behavior.

**Counterindication:** Direct current execution evidence bound to the exact consumer/producer identity can establish execution even when documentation is incomplete.

**Transfer claim:** Applies to architecture graphs, handoffs, relationship registries, tests and runtime claims.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-03 — Historical evidence remains historical until reconciled

**Source:** MEM-009 lesson 3; EJR-211.

**Observed facts:** Closed or unmerged PRs contained useful evidence but were not current-main state.

**Inference:** Evidence can remain valid as provenance while losing fitness for a current-state claim.

**Invariant:** `PROVENANCE VALIDITY AND CURRENT-STATE FITNESS ARE DIFFERENT DIMENSIONS`.

**Boundary:** Historical evidence is fully appropriate for historical claims and may support lineage or hypothesis formation. It must be reconciled before being used as present-state evidence.

**Counterindication:** If the historical artifact is proven byte/semantic-equivalent to the current authoritative state for the exact claim, reconciliation may establish current applicability.

**Transfer claim:** Applies to branches, PRs, archived records, prior runs and superseded documents.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-04 — Search scope limits the claim

**Source:** MEM-009 lesson 4; EJR-211.

**Observed facts:** Search results can be heuristic, truncated or namespace-limited.

**Inference:** Search failure or success is evidence about the queried retrieval surface unless completeness of that surface is established.

**Invariant:** `RETRIEVAL SCOPE BOUNDS ABSENCE/COMPLETENESS CLAIMS`.

**Boundary:** A demonstrably complete authoritative enumeration of the defined universe can support an exhaustive claim within that universe.

**Counterindication:** `truncated:false` for a recursive Git tree can establish enumeration completeness for that queried tree; it does not establish semantic correctness.

**Transfer claim:** Applies to repository search, connector discovery, API listings and inventory checks.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-05 — Persistence is not correctness

**Source:** MEM-009 lesson 5; EJR-211.

**Observed facts:** Successful commits proved that bytes were persisted while semantic/runtime correctness still required separate validation.

**Inference:** Transport/storage success is a different claim layer from semantic correctness.

**Invariant:** `PERSISTED != VALIDATED`.

**Boundary:** Persistence is sufficient evidence for a persistence claim. It becomes part of a correctness chain only when paired with claim-appropriate validation.

**Counterindication:** None that collapses the two claims; only stronger evidence can connect them.

**Transfer claim:** Applies to Git writes, database persistence, artifact upload, memory publication and generated files.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-06 — Independent negative-search confirmation

**Source:** MEM-009 lesson 6; EJR-214.

**Observed facts:** Repository search returned no P30 delta while direct authoritative-path retrieval found the file on `main`.

**Inference:** One negative retrieval result did not establish absence.

**Invariant:** `MATERIAL ABSENCE CLAIM REQUIRES COMPLETENESS OR INDEPENDENT CONFIRMATION`.

**Boundary:** The exact internal search/index defect was not proven and must not be generalized into a specific connector defect claim.

**Counterindication:** An authoritative exhaustive enumeration may make a second heuristic search unnecessary for the same bounded universe.

**Transfer claim:** Applies to negative search, identity audit and resource-discovery claims.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-07 — Search-result freshness reconciliation

**Source:** MEM-009 lesson 7; EJR-219.

**Observed facts:** Positive repository search results were pinned to an older commit while authoritative `main` was nine commits ahead.

**Inference:** A positive hit proves discoverability at its returned ref, not automatically current-state truth.

**Invariant:** `POSITIVE DISCOVERY != CURRENTNESS`.

**Boundary:** If returned evidence identity/ref is the authoritative current ref, no stale-ref reconciliation gap exists for that claim.

**Counterindication:** Search content may still happen to equal current content despite a stale ref; equality must be checked rather than assumed.

**Transfer claim:** Applies to search indexes, cached APIs, replicated stores and any retrieval system returning explicit version identity.

**Current applicability:** HIGH.

**Class:** `A`.

### SEA-08 — Failure can preserve a good idea

**Source:** GOV-016, supported by repeated repository repair practice.

**Observed facts:** Failures have been classified separately as idea, implementation, test, infrastructure, model-assumption, governance, evidence or schema failures.

**Inference:** A failed execution does not identify which conceptual layer failed unless evidence distinguishes it.

**Invariant:** `FAILED OUTCOME DOES NOT BY ITSELF INVALIDATE THE UNDERLYING IDEA`.

**Boundary:** When evidence does establish `IDEA_FAILURE`, preserving the idea as an active reusable solution would be incorrect. The reusable residue may instead be a negative pattern or boundary lesson.

**Counterindication:** Repeated failure across sound independent implementations can increase evidence against the idea, subject to scope and shared-cause analysis.

**Transfer claim:** Applies to design experiments, workflows, tests, connectors and learning mechanisms.

**Current applicability:** HIGH.

**Class:** `A/B` — structurally sound, but the transferred conclusion must preserve the failure class.

## 5. Semantic findings

### F1 — The sampled promoted lessons are not empty slogans

All seven sampled MEM-009 reusable lessons can be reconstructed into facts, inference, invariant, boundary and current applicability using recorded provenance. No sampled lesson required inventing a source event.

### F2 — The largest semantic risk is boundary loss during compression

The short MEM-009 statements are sound only when their evidence boundary travels with them.

Examples:

- `Search scope limits the claim` must retain the exception for demonstrably complete enumeration.
- `Historical evidence remains historical` must not imply historical evidence is useless; it remains fit for historical/provenance claims.
- `Documentation is not execution proof` must not deny normative authority to an actually authoritative governance declaration.

Therefore:

`SHORT INVARIANT WITHOUT BOUNDARY CAN BECOME OVER-GENERALIZED EXPERIENCE`.

### F3 — Current Experience Spine metadata is mostly sufficient for retrieval safety, not full semantic reconstruction

Current projection metadata can represent:

- source identity/type;
- evidence state;
- authority state;
- evidence correlation group;
- applicability boundaries;
- counterindications;
- contradictions;
- structural task matching;
- supersession exclusion.

It does not need to duplicate the full source evidence or create a second Memory schema.

However, semantic reconstruction reveals one recurring distinction that deserves explicit analytical attention:

`OBSERVED FACT != INFERENCE != INVARIANT`.

This distinction can remain in the source knowledge record/provenance rather than being added immediately to the retrieval profile. No schema expansion is justified by this audit alone.

### F4 — Evidence independence is not record count

EJR-211 explicitly describes lessons as repeated and independently rechecked across review rounds, while Experience Spine separately models correlated evidence groups. The reusable lesson is not "more records = stronger truth" but that confidence depends on whether observations are materially independent for the claim.

### F5 — Currentness is claim-dependent

Historical evidence may be stale for a current-state claim while remaining authoritative evidence of what happened historically. Search results may be stale for current state while still proving a prior discoverability event.

Therefore currentness must attach to the claim layer, not globally label the source "good" or "bad".

## 6. Newly discovered cross-experience invariants

This audit supports several new HORUS candidate experiences, documented separately in `HORUS_CANDIDATE_EXPERIENCE_UNITS_2026-08-29.md`.

The strongest are:

1. `DISCOVERY FAILURE IS A CLAIM ABOUT THE SEARCH SURFACE, NOT THE RESOURCE UNIVERSE`.
2. `INDEPENDENCE IS A PROPERTY OF EVIDENCE LINEAGE, NOT RESULT COUNT`.
3. `FAILURE MAY PRODUCE REUSABLE DESIGN KNOWLEDGE WITHOUT VALIDATING THE FAILED IMPLEMENTATION`.
4. `CURRENTNESS IS CLAIM-LAYER SPECIFIC`.
5. `EXECUTION VISIBILITY MUST BE BOUND TO THE CLAIM BEING MADE`.
6. `STRUCTURAL CLEANLINESS CAN EXPOSE, NOT ELIMINATE, SEMANTIC RISK`.
7. `NEGATIVE EVIDENCE STRENGTH IS LIMITED BY THE ENUMERATION GUARANTEE`.

These are candidates, not promoted Memory lessons.

## 7. Experience Spine recommendation

Do not expand the Experience Spine schema merely because this audit found richer semantics.

Recommended rule:

`PRESERVE RICH SEMANTICS AT SOURCE; PROJECT ONLY THE MINIMUM SAFE RETRIEVAL BOUNDARIES`.

Only add a projection field when repeated audits show that omission causes an actual retrieval or reasoning failure that cannot be safely recovered from source/provenance.

## 8. Eye-of-the-world observation

Across CI, search, version freshness, documentation, persistence, failure handling and Room71 reconciliation, the same deeper pattern recurs:

> ARGO becomes unsafe when evidence from one layer is silently promoted into a stronger claim at another layer.

Examples of prohibited silent lifts:

- CI PASS → repository integrity;
- Markdown declaration → runtime execution;
- historical PR → current-main behavior;
- search miss → resource absence;
- search hit → currentness;
- commit success → semantic correctness;
- failed implementation → bad idea;
- multiple correlated records → independent confirmation;
- clean inventory → semantic correctness;
- retrieval mechanics → cognitive improvement.

Candidate meta-invariant:

`DO NOT LET EVIDENCE CROSS A CLAIM-LAYER BOUNDARY WITHOUT AN EXPLICIT BRIDGE`.

This is a HORUS analytical synthesis. It is not governance authority.

## 9. Required next verification

HERMUZ should independently test whether:

1. the seven candidate experience units are genuinely distinct rather than restatements of existing canonical lessons;
2. their boundaries are supported by current repository evidence;
3. any deserve promotion to reusable learning;
4. the meta-invariant adds explanatory power without duplicating GOV-018 or existing MEM-009 wording;
5. no new Experience Spine schema field is needed before a real failure demonstrates the gap.

A later independent IGT remains necessary to test cognitive effect.

## 10. Closure

`SEMANTIC SAMPLE AUDIT = COMPLETED / HORUS-REPORTED`.

`SAMPLED EXPERIENCE BODY = RECONSTRUCTABLE / BOUNDARY-SENSITIVE`.

`SCHEMA EXPANSION = NOT JUSTIFIED BY THIS AUDIT`.

`NEW EXPERIENCE UNITS = CANDIDATE ONLY / PROMOTION NOT AUTHORIZED`.

Final invariant:

`GOOD EXPERIENCE IS NOT A SHORT RULE; IT IS A RULE WITH ITS EVIDENCE, CLAIM LAYER, BOUNDARY, FAILURE CONDITIONS AND CURRENT APPLICABILITY STILL RECOVERABLE.`
