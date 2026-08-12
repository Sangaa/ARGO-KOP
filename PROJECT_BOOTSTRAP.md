# BOOTSTRAP-001

---

# ARGO KOP - MANDATORY BOOTSTRAP & KNOWLEDGE TRANSFER SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: BOOTSTRAP-001
Version: 3.0.0
Status: Validated / Integrity Warning
Category: Bootstrap / Governance
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: 2026-08-12

---

# Mandatory Notice to AI Models & Contributors

This document is the mandatory initialization entry point for any AI agent, LLM instance, engineer, or automated runner interacting with ARGO KOP.

**No repository mutation may begin without enough current repository evidence to justify the specific mutation. The required evidence scope is proportional to the impact of the change.**

A successful bootstrap MUST NOT be inferred from `PROJECT_STATUS.md`, release metadata, memory, conversation history, folder names, ZIP snapshots, or another self-declared status file alone.

The engineering objective is not file-count throughput. **Construction quality, connectivity, evidence, verified seams, and reusable learning take priority over the number of files reviewed or modified.**

---

# 1. Evidence-Proportional Bootstrap

Bootstrap has two related questions:

1. **Can this session safely understand and perform the requested work?**
2. **Is the repository sufficiently reviewed to make a repository-wide integrity claim?**

These are not the same question.

A session may safely perform a **bounded, low-impact change** with scoped evidence when the required dependencies and affected consumers have been inspected and no unresolved blocker affects that scope.

A **repository-wide structural, canonical, architectural or integrity claim** requires repository-wide evidence coverage appropriate to that claim.

Do not perform a larger review merely because a smaller review is sufficient for the requested change, but do not make a global claim from local evidence.

When broad review is undertaken, **inspect the widest practical relevant scope while preserving evidence quality**. Broader inspection is valuable only when it improves relationship understanding and proof; it must not become a race to modify more files.

---

# 2. Repository Availability Gate

1. Establish the exact repository, branch/ref and accessible repository boundary.
2. Inspect the repository evidence required by the requested change.
3. For structural or repository-wide work, enumerate the relevant repository tree and inspect the affected domains broadly enough to establish relationships.
4. If required evidence cannot be inspected, mark it `Unavailable` and stop only the decision that depends on it.
5. Never fill unavailable content from memory, prior conversations, ZIP snapshots, cached summaries, assumptions, or inferred patterns.

An evidence limitation is a **scope boundary**, not automatically a reason to halt unrelated work.

---

# 3. Full Repository Review Gate

Before claiming repository-wide integrity, or before making a change whose impact is repository-wide:

- Review the complete current repository tree available through the repository source.
- Review indexes, status files, canonical documents, referenced documents and affected neighboring artifacts.
- Inspect filenames, internal identifiers, versions, status, ownership, paths and references together.
- Trace relevant references in both directions where practical.
- Compare duplicates, legacy copies, aliases, similarly named files and archived material before deciding ownership.
- Do not infer a layer, component, authority, or relationship from a folder name alone.

**A folder is a storage location until its contents and relationships establish its architectural meaning.**

---

# 4. Evidence Completeness Rule

For every significant conclusion, distinguish:

- **Verified:** directly observed in the current repository.
- **Partially Verified:** observed only for a defined subset of the required evidence.
- **Unavailable:** required evidence could not be inspected.
- **Inferred:** derived from observed evidence but not directly stated.
- **Assumed:** not supported by repository evidence.

`Unavailable` MUST NOT be silently converted into `Verified` or `Inferred`.

If unavailable evidence is material to the requested decision, the agent MUST warn the user before making that decision.

---

# 5. No Memory Substitution Rule

Conversation memory, prior session summaries, personal memory, generated summaries, previous ZIP files, external working copies, and remembered repository structure are non-authoritative context.

They MUST NOT substitute for current repository file contents.

If current repository contents contradict memory, current repository contents prevail.

---

# 6. No Folder-Assumption Rule

No agent may conclude that a folder represents a logical layer, component, authority domain, canonical collection, or complete inventory solely from:

- folder name;
- numeric filename sequence;
- `_FOLDER_STATUS.md`;
- README claims;
- previous session statements;
- expected architecture patterns.

The conclusion MUST be supported by inspected filenames, internal document identities, contents, references, indexes, ownership and dependency relationships.

---

# 7. Canonical Identity Verification

Verify every candidate canonical document by the combined evidence of:

- exact current path;
- filename;
- internal Document ID;
- version;
- status;
- canonical declaration;
- Repository index registration;
- applicable Governance authority;
- cross-references;
- duplicate/legacy evidence.

If two files claim the same logical identity, resolve ownership before changing either identity.

A duplicate-ID finding MUST be evaluated by at least:

**Document ID + Namespace/Domain + Artifact Class + Canonical Path + Authority**

A repeated numeric identifier in different semantic namespaces is not automatically a collision.

---

# 8. Mandatory Index and Reference Review

For affected structural work, review:

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- applicable `_FOLDER_STATUS.md` files
- relevant README/index files
- all canonical and affected cross-references

An index or status file is evidence, not proof by declaration.

---

# 9. Relationship Graph Verification Gate

The repository MUST be treated as a relationship graph, not merely a directory tree.

For every critical reference or dependency, validate the chain:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read After Mutation → Revalidate**

A textual reference or existing path is NOT sufficient to establish a valid dependency.

Where practical, validate relationships in both directions:

**Document → Target**

and

**Target → Authority / Consumers / Indexes**

A newly discovered conflict MUST be checked for propagation before local resolution is accepted.

---

# 10. Verified Seam Evidence Gate

For integration and connectivity work, a candidate seam MUST NOT be promoted merely because the participating files exist.

Use the evidence path:

**Candidate Seam → Contract Exists → Test Exists → Trace Evidence Exists → Verified Seam Registry → Semantic Integration Audit**

The verified seam evidence loader may establish **local artifact completeness** only. It MUST NOT be treated as proof of semantic correctness, runtime reachability, or repository-wide connectivity.

Incomplete seam evidence MUST be excluded from the verified registry rather than promoted by assumption.

The active connectivity objective is to prove actual paths across the repository, including source, contract, consumer, execution, trace and outcome where applicable.

---

# 11. Runtime, Engine & State Alignment

Load `Runtime/RUN-001_BOOT_SEQUENCE.md` when runtime or boot behavior is affected, or when performing a repository-wide integrity claim.

For repository-wide claims, compare the actual repository state against:

- `PROJECT_STATUS.md`
- `Release/VERSION.md`
- `Release/RELEASE_MANIFEST.md`
- Repository indexes
- Runtime declarations
- relevant Architecture and Governance authorities
- current Engine coordination and dependency declarations

Engine routing declarations are not verified integration contracts until their source, target, authority, compatibility and failure behavior are evidenced.

Do not use a self-declared `100% CLEAN BOOT` statement as proof of integrity.

---

# 12. Source-of-Truth Rule

The Git repository is the authoritative engineering source for repository state unless an explicit governed decision establishes another source for a specific purpose.

External copies, previous ZIP archives, generated summaries and conversation memory MUST NOT silently override current repository reality.

When a repository search/index result conflicts with direct inspection of a known current path, the discrepancy must be treated as an evidence-coverage issue and investigated; the search result must not automatically override the directly readable artifact.

---

# 13. Search & Error Recheck Gate

**Absence from one search result is never sufficient evidence that an artifact, commit, workflow run, test result, reference, or directory is absent.**

When a material finding depends on a negative result, the agent MUST perform an independent recheck before classifying it as a repository defect.

Preferred independent recheck pairs include:

- repository search → direct current-path read;
- commit search → direct commit/API or branch-history lookup;
- commit-associated workflow lookup → recent Actions-run listing → exact run/job lookup;
- index/reference lookup → target read → reverse consumer/authority search;
- test failure summary → job logs → affected source/test artifact inspection.

If the second method confirms the first result, classify the finding as **Verified**.

If the second method disproves it, classify the first result as an **Evidence Search Defect**, not a repository defect.

If the methods remain inconsistent, classify the evidence as **Unavailable / Discrepancy** and do not make a destructive or architectural decision from it.

Tool truncation, pagination, indexing delay and incomplete search coverage MUST be treated as evidence limitations rather than silent absence.

---

# 14. Change Gate

Use the smallest sufficient evidence scope for the requested change, while examining the widest practical relevant scope when broader connectivity or architectural relationships may be affected:

### Bounded Change

**Inspect → Read affected artifacts → Trace critical dependencies → Change → Re-read → Validate affected relationships → Update required indexes/status**

### Structural / Cross-Layer Change

**Enumerate → Read affected domains → Build Relationship Graph → Cross-Reference → Classify Evidence → Identify Conflict → Decide Canonical Ownership → Review Impact → Change → Re-read → Revalidate → Update Indexes/Status → Re-Boot**

### Repository-Wide Connectivity / Integrity Work

**Enumerate → Inspect Broadly → Build Relationship Graph → Populate Verified Seam Candidates → Validate Registry → Run Canonical Spine Audit → Expand to Full Repository Connectivity / End-to-End Audit → Produce GAP MAP → Fix Highest-Value Seams → Regression Test → Re-Audit → Close Checkpoint**

No deletion, rename, duplication, reassignment, normalization, or architectural proposal may skip the evidence required by its impact.

A mutation is not complete until the write target was verified, the write succeeded, the changed artifact was re-read, and the affected relationship/status/index evidence was revalidated.

**File count is never a completion criterion.** If fewer changes produce stronger verified connectivity, prefer fewer changes.

---

# 15. Construction Priority & Review Quality Principle

The agent must **inspect as broadly as practical, but prioritize construction quality and relationship integrity over throughput**.

When reviewing or modifying multiple artifacts:

1. Understand the current construction and its intended relationships before adding more.
2. Prioritize missing or broken seams over isolated file completion.
3. Prefer fixing a high-value cross-layer relationship over producing a larger number of superficial edits.
4. Do not modify a file merely to increase the apparent amount of progress.
5. Test and revalidate the path affected by a change before declaring it complete.
6. Preserve evidence boundaries and distinguish verified progress from inferred or planned work.

**A smaller set of correctly connected, tested and documented artifacts is higher-value than a larger set of superficially reviewed or modified files.**

---

# 16. Simplicity & Reviewability Principle

**No ARGO rule is sacred merely because it already exists.**

Rules, architectures, models, indexes and procedures remain reviewable when evidence shows that a simpler, safer, clearer or more accurate method exists.

When replacing an existing rule:

1. identify the observed problem or unnecessary complexity;
2. verify the proposed simpler method against affected dependencies;
3. preserve required traceability;
4. replace the old rule only when the new rule provides equal or better control;
5. record the reason for the change.

The goal is not maximum procedure. The goal is **minimum sufficient control with maximum useful evidence**.

---

# 17. Learning & Future Capability Gate

Future capability acquisition must follow a governed learning loop rather than uncontrolled feature expansion.

The preferred learning path is:

**Source / Book → Extract Knowledge → Verify Understanding → Practice → Test → Apply → Record Reusable Knowledge**

Learning quality is measured by demonstrated understanding, tested application and reusable knowledge, not by number of books, pages or concepts consumed.

The current repository connectivity gate takes precedence over future implementation work.

Future governed capability targets include:

### Android Applications

**Programming Fundamentals → Kotlin → Android Development → Architecture → Testing → Real Application Project**

### Roblox Game Development + AI

**Luau → Roblox Studio → Game Architecture → Gameplay Systems → State / Networking → AI Integration → Testing → Optimization**

For Roblox AI integration, the eventual implementation must expose testable relationships between:

**Game State → AI Input → Inference / Decision → Game Action → Player Feedback**

These targets preserve direction and future learning requirements. They do not authorize premature implementation while connected-baseline or connectivity gates remain open.

---

# 18. Mandatory Integrity Gate

Bootstrap completion has three states:

- **BOOTED / INTEGRITY PASS** — required baseline documents are readable, the required review scope has been completed, canonical identities are unique within that scope, indexes and paths are aligned, critical references resolve, and no blocking conflict remains within the claimed scope.
- **BOOTED / INTEGRITY WARNING** — runtime can be loaded, but one or more inconsistencies or evidence gaps remain. Bounded engineering work may continue when its evidence scope is sufficient; broader normalization or global claims remain constrained.
- **BOOT FAILURE** — mandatory bootstrap documents cannot be loaded, repository scope cannot be established, or a critical contradiction/evidence gap prevents reliable interpretation of the requested work.

The bootstrap process MUST report the evaluated state and evidence coverage. It MUST NOT copy a status declaration from a repository document as proof.

---

# 19. Accumulated Platform Knowledge & Operating Principles

1. Current repository evidence is the active engineering baseline.
2. Canonical identity is composite: path, internal ID, version, status, canonical declaration, index registration and applicable authority must agree.
3. Repository contents and cross-references are evidence; status fields are claims requiring validation.
4. Historical material should be preserved where controlled migration or traceability requires it.
5. Memory and prior sessions never replace current repository inspection.
6. Physical folders do not establish logical architecture by themselves.
7. Active files must be consistently represented in applicable repository indexes.
8. Canonical references must resolve and identities must agree.
9. Release, development baseline, document version and audit date are distinct concepts.
10. Updates must be complete, non-truncated and valid Markdown.
11. Missing or unreadable content must be explicitly disclosed.
12. Operational evidence precedes action.
13. Status drift is a finding, not a reason to normalize blindly.
14. Numeric sequence gaps are findings, not permission to invent artifacts.
15. Cross-layer review precedes local normalization when impact is cross-layer.
16. Tool-limited review constrains claims to the inspected scope.
17. Mutation is not validation; changed artifacts and affected relationships must be re-read.
18. Never claim full repository review without supporting evidence coverage.
19. Reusable session learning becomes canonical only after explicit recording, review and validation.
20. Relationship integrity is established through validated relationships, not file existence alone.
21. Critical dependencies should be checked bidirectionally where practical.
22. Material conflicts require propagation checks.
23. Local PASS cannot become global PASS without aggregated evidence.
24. Audit-derived rules are candidates until explicitly promoted.
25. New evidence may reopen a previously reviewed domain.
26. Simpler valid solutions should replace unnecessarily complex controls when traceability and safety are preserved.
27. Search/index evidence can be incomplete; direct readable repository evidence must be preserved and the discrepancy investigated.
28. Engine status must remain bounded by verified dependencies and consumers.
29. A route declaration is not a verified integration contract.
30. Failed or ambiguous mutations must not be bypassed with destructive or forceful operations.
31. Construction quality, connectivity, evidence and reusable learning outrank file-count throughput.
32. A session may be broad in inspection but must remain selective in mutation; quantity of edits is not progress by itself.
33. Every substantial session should leave a deterministic closure point: what was established, what evidence supports it, what remains unresolved, and the next target.
34. Future capability targets should be preserved as governed direction without interrupting the active build gate.
35. A negative search result is provisional until independently rechecked when it materially affects a decision.
36. Tool truncation, pagination and index incompleteness are evidence limitations, not proof of absence.
37. When independent evidence sources disagree, preserve the discrepancy and bound the decision instead of guessing.
38. A first-search failure must never directly become a repository defect without a second retrieval method where practical.

---

# 20. Mandatory Session Closure & Self-Update Protocol

After repository mutation:

1. Update affected `_FOLDER_STATUS.md` files where required by repository structure.
2. Update `Repository/REP-001_MASTER_INDEX.md` when active inventory changes.
3. Update `Repository/REP-002_REPOSITORY_MAP.md` when structure or canonical paths change.
4. Update `PROJECT_STATUS.md` when project state materially changes.
5. Update root navigation documents when a material canonical path, phase, authority or integrity rule changes.
6. Record the decision and reason in the appropriate governance/logging artifact when required.
7. Re-run the applicable bootstrap/integrity gate.
8. Re-read every mutated artifact and validate affected references, indexes, status claims and relationship evidence.
9. Record what was completed, what remains unresolved, evidence limitations, and the deterministic next target so the session can be safely closed and resumed at any point.
10. Never use the number of modified files as the session-completion metric.
11. If a material negative finding was used during the session, record whether it was independently rechecked and whether the second method confirmed, disproved, or left the finding unavailable.
12. Close only after the current branch/ref and final commit have been re-read directly from the repository source.

A session MUST NOT claim `100% CLEAN BOOT` unless the claimed scope has actually passed its integrity gate.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 3.0.0 | 2026-08-12 | Added mandatory independent recheck for material negative findings, explicit search/index/truncation evidence boundaries, discrepancy classification, and closure verification of final branch/ref/commit | ARGO Engineering / Repository Audit |
| 2.9.0 | 2026-08-12 | Added construction-quality-over-file-count priority, verified-seam evidence gate, full connectivity/E2E audit sequence, governed programming/mathematics learning path, future Android and Roblox+AI capability targets, and deterministic session-closure requirements | ARGO Engineering / Repository Audit |
| 2.8.0 | 2026-08-08 | Added namespace-aware identity auditing, direct-evidence precedence over incomplete search/index results, engine route verification boundaries, and explicit verified-write/post-write validation requirements; synchronized the live audit method | ARGO Engineering / Principal Architect |
| 2.7.0 | 2026-08-08 | Replaced blanket full-review-before-any-work rule with proportional evidence gates; added minimum-sufficient-control principle and explicit rule-replacement pathway | ARGO Engineering / Principal Architect |
| 2.6.0 | 2026-08-08 | Added relationship-graph verification, bidirectional dependency validation, conflict propagation, local-to-global evidence boundary, audit-derived rule promotion and reopen-on-new-evidence controls discovered during live repository audit | ARGO Engineering / Principal Architect |
| 2.5.0 | 2026-08-08 | Added operational lessons from live repository audit: mutation is not validation, status drift, numeric-sequence caution, cross-layer-first review, tool-limited evidence coverage, and explicit canonicalization of reusable session learning | ARGO Engineering / Principal Architect |
| 2.4.0 | 2026-08-08 | Added mandatory repository-wide evidence review, evidence-gap warnings, no-memory substitution rule, no-folder-assumption rule, and pre-proposal cross-reference gate | ARGO Engineering / Principal Architect |
| 2.3.0 | 2026-08-08 | Added repository-reality integrity gate, canonical identity checks, version/source-of-truth conflict detection, and documented audit findings | ARGO Engineering / Principal Architect |
| 2.2.0 | 2026-08-08 | Re-aligned exact canonical paths with Governance/ directory reality | ARGO Engineering / Principal Architect |

---

End of Document
