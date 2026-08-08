# BOOTSTRAP-001

---

# ARGO KOP - MANDATORY BOOTSTRAP & KNOWLEDGE TRANSFER SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: BOOTSTRAP-001
Version: 2.7.0
Status: Validated / Integrity Warning
Category: Bootstrap / Governance
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: 2026-08-08

---

# Mandatory Notice to AI Models & Contributors

This document is the mandatory initialization entry point for any AI agent, LLM instance, engineer, or automated runner interacting with ARGO KOP.

**No repository mutation may begin without enough current repository evidence to justify the specific mutation. The required evidence scope is proportional to the impact of the change.**

A successful bootstrap MUST NOT be inferred from `PROJECT_STATUS.md`, release metadata, memory, conversation history, folder names, or another self-declared status file alone.

---

# 1. Evidence-Proportional Bootstrap

Bootstrap has two related questions:

1. **Can this session safely understand and perform the requested work?**
2. **Is the repository sufficiently reviewed to make a repository-wide integrity claim?**

These are not the same question.

A session may safely perform a **bounded, low-impact change** with scoped evidence when the required dependencies and affected consumers have been inspected and no unresolved blocker affects that scope.

A **repository-wide structural, canonical, architectural or integrity claim** requires repository-wide evidence coverage appropriate to that claim.

Do not perform a larger review merely because a smaller review is sufficient for the requested change, but do not make a global claim from local evidence.

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

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read After Mutation**

A textual reference or existing path is NOT sufficient to establish a valid dependency.

Where practical, validate relationships in both directions:

**Document → Target**

and

**Target → Authority / Consumers / Indexes**

A newly discovered conflict MUST be checked for propagation before local resolution is accepted.

---

# 10. Runtime, Engine & State Alignment

Load `Runtime/RUN-001_BOOT_SEQUENCE.md` when runtime or boot behavior is affected, or when performing a repository-wide integrity claim.

For repository-wide claims, compare the actual repository state against:

- `PROJECT_STATUS.md`
- `Release/VERSION.md`
- `Release/RELEASE_MANIFEST.md`
- Repository indexes
- Runtime declarations
- relevant Architecture and Governance authorities

Do not use a self-declared `100% CLEAN BOOT` statement as proof of integrity.

---

# 11. Source-of-Truth Rule

The Git repository is the authoritative engineering source for repository state unless an explicit governed decision establishes another source for a specific purpose.

External copies, previous ZIP archives, generated summaries and conversation memory MUST NOT silently override current repository reality.

---

# 12. Change Gate

Use the smallest sufficient evidence scope for the requested change:

### Bounded Change

**Inspect → Read affected artifacts → Trace critical dependencies → Change → Re-read → Validate affected relationships → Update required indexes/status**

### Structural / Cross-Layer Change

**Enumerate → Read affected domains → Build Relationship Graph → Cross-Reference → Classify Evidence → Identify Conflict → Decide Canonical Ownership → Review Impact → Change → Re-read → Revalidate → Update Indexes/Status → Re-Boot**

### Repository-Wide Integrity Claim

Use the structural sequence above across the repository scope required to support the claim. Do not claim 100% without corresponding evidence coverage.

No deletion, rename, duplication, reassignment, normalization, or architectural proposal may skip the evidence required by its impact.

---

# 13. Simplicity & Reviewability Principle

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

# 14. Mandatory Integrity Gate

Bootstrap completion has three states:

- **BOOTED / INTEGRITY PASS** — required baseline documents are readable, the required review scope has been completed, canonical identities are unique within that scope, indexes and paths are aligned, critical references resolve, and no blocking conflict remains within the claimed scope.
- **BOOTED / INTEGRITY WARNING** — runtime can be loaded, but one or more inconsistencies or evidence gaps remain. Bounded engineering work may continue when its evidence scope is sufficient; broader normalization or global claims remain constrained.
- **BOOT FAILURE** — mandatory bootstrap documents cannot be loaded, repository scope cannot be established, or a critical contradiction/evidence gap prevents reliable interpretation of the requested work.

The bootstrap process MUST report the evaluated state and evidence coverage. It MUST NOT copy a status declaration from a repository document as proof.

---

# 15. Accumulated Platform Knowledge & Operating Principles

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

---

# 16. Mandatory Session Closure & Self-Update Protocol

After repository mutation:

1. Update affected `_FOLDER_STATUS.md` files where required by repository structure.
2. Update `Repository/REP-001_MASTER_INDEX.md` when active inventory changes.
3. Update `Repository/REP-002_REPOSITORY_MAP.md` when structure or canonical paths change.
4. Update `PROJECT_STATUS.md` when project state materially changes.
5. Record the decision and reason in the appropriate governance/logging artifact when required.
6. Re-run the applicable bootstrap/integrity gate.
7. Report unresolved warnings and evidence gaps explicitly.

A session MUST NOT claim `100% CLEAN BOOT` unless the claimed scope has actually passed its integrity gate.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 2.7.0 | 2026-08-08 | Replaced blanket full-review-before-any-work rule with proportional evidence gates; added minimum-sufficient-control principle and explicit rule-replacement pathway | ARGO Engineering / Principal Architect |
| 2.6.0 | 2026-08-08 | Added relationship-graph verification, bidirectional dependency validation, conflict propagation, local-to-global evidence boundary, audit-derived rule promotion and reopen-on-new-evidence controls discovered during live repository audit | ARGO Engineering / Principal Architect |
| 2.5.0 | 2026-08-08 | Added operational lessons from live repository audit: mutation is not validation, status drift, numeric-sequence caution, cross-layer-first review, tool-limited evidence coverage, and explicit canonicalization of reusable session learning | ARGO Engineering / Principal Architect |
| 2.4.0 | 2026-08-08 | Added mandatory repository-wide evidence review, evidence-gap warnings, no-memory substitution rule, no-folder-assumption rule, and pre-proposal cross-reference gate | ARGO Engineering / Principal Architect |
| 2.3.0 | 2026-08-08 | Added repository-reality integrity gate, canonical identity checks, version/source-of-truth conflict detection, and documented audit findings | ARGO Engineering / Principal Architect |
| 2.2.0 | 2026-08-08 | Re-aligned exact canonical paths with Governance/ directory reality | ARGO Engineering / Principal Architect |

---

End of Document
