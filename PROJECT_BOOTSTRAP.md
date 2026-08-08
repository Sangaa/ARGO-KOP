# BOOTSTRAP-001

---

# ARGO KOP - MANDATORY BOOTSTRAP & KNOWLEDGE TRANSFER SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: BOOTSTRAP-001
Version: 2.4.0
Status: Approved / Integrity-Gated
Category: Bootstrap / Governance
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: 2026-08-08

---

# Mandatory Notice to AI Models & Contributors

This document is the mandatory initialization entry point for any AI agent, LLM instance, engineer, or automated runner interacting with ARGO KOP.

**NO ENGINEERING WORK, FILE CREATION, REPOSITORY MUTATION, OR CHANGE PROPOSAL SHALL BEGIN BEFORE THE REPOSITORY HAS BEEN REVIEWED TO THE MAXIMUM VERIFIABLE SCOPE.**

A successful bootstrap MUST NOT be inferred from `PROJECT_STATUS.md`, release metadata, memory, conversation history, folder names, or another self-declared status file alone. Bootstrap status is an evaluated runtime result based on repository evidence.

---

# Mandatory Repository-First Review Protocol

Every AI instance or engineer MUST execute the following sequence before proposing or executing a repository change.

## 0. Repository Availability Gate

1. Establish the exact repository, branch/ref and accessible repository boundary.
2. Enumerate the repository structure using repository evidence.
3. Attempt to inspect the contents of **all files relevant to the repository-wide review**, not only index/status files.
4. If any required file, directory listing, file content, history, or cross-reference cannot be inspected with the available tools, **STOP before making a proposal that depends on the unavailable evidence and issue an explicit warning identifying what could not be inspected and why.**
5. Never fill unavailable content from memory, prior conversations, ZIP snapshots, cached summaries, assumptions, or inferred patterns.

## 1. Full Repository Review Gate

Before suggesting a structural, canonical, architectural, governance, or cross-layer change:

- Review the complete current repository tree available through the repository source.
- Review the contents of the files in scope, including indexes, status files, canonical documents, referenced documents, and affected neighboring artifacts.
- Inspect filenames, internal identifiers, versions, status, ownership, paths and references together.
- Trace relevant references in both directions where practical: document → referenced artifact and artifact → referencing authority.
- Compare duplicates, legacy copies, aliases, similarly named files and archived material before deciding ownership.
- Do not infer a layer, component, authority, or relationship from a folder name alone.

**A folder is a storage location until its contents and relationships establish its architectural meaning.**

## 2. Evidence Completeness Rule

For every proposed change, the reviewing agent MUST distinguish:

- **Verified:** directly observed in the current repository.
- **Partially Verified:** observed only for a defined subset of the required evidence.
- **Unavailable:** required evidence could not be inspected.
- **Inferred:** derived from observed evidence but not directly stated.
- **Assumed:** not supported by repository evidence.

`Unavailable` MUST NOT be silently converted into `Verified` or `Inferred`.

If evidence required for a decision is unavailable, the agent MUST warn the user before proposing the decision.

## 3. No Memory Substitution Rule

Conversation memory, prior session summaries, personal memory, generated summaries, previous ZIP files, external working copies, and remembered repository structure are **non-authoritative context**.

They MUST NOT substitute for current repository file contents.

If current repository contents contradict memory, **current repository contents prevail**.

If current contents are unavailable, the agent MUST report the gap instead of reconstructing the missing content from memory.

## 4. No Folder-Assumption Rule

No agent may conclude that a folder represents a logical layer, component, authority domain, canonical collection, or complete inventory solely from:

- folder name;
- numeric filename sequence;
- `_FOLDER_STATUS.md`;
- README claims;
- previous session statements;
- expected architecture patterns.

The conclusion MUST be supported by inspected filenames, internal document identities, contents, references, indexes, ownership and dependency relationships.

## 5. Canonical Identity Verification

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

If two files claim the same logical identity, stop normalization of that identity until ownership is explicitly resolved.

## 6. Mandatory Index and Reference Review

Review:

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- applicable `_FOLDER_STATUS.md` files
- relevant README/index files
- all canonical and affected cross-references

An index or status file is evidence, not proof by declaration.

## 7. Runtime, Engine & State Alignment

Load `Runtime/RUN-001_BOOT_SEQUENCE.md` and the active runtime chain.

Compare the actual repository state against:

- `PROJECT_STATUS.md`
- `Release/VERSION.md`
- `Release/RELEASE_MANIFEST.md`
- Repository indexes
- Runtime declarations
- relevant Architecture and Governance authorities

Do not use a self-declared `100% CLEAN BOOT` or equivalent statement as proof of integrity.

## 8. Source-of-Truth Rule

The Git repository is the authoritative engineering source for repository state unless an explicit governed decision establishes another source for a specific purpose.

External copies, including Google Drive material, previous ZIP archives, generated summaries, or conversation memory, MUST NOT silently override current repository reality.

## 9. Change Gate

The mandatory sequence is:

**Inspect → Enumerate → Read → Cross-Reference → Classify Evidence → Identify Conflict → Decide Canonical Ownership → Define Change → Review Impact → Execute → Validate → Update Indexes/Status → Re-Boot**

No deletion, rename, duplication, reassignment, normalization, or architectural proposal may skip the evidence and cross-reference stages.

## 10. Human-Centric Dialogue Alignment

Maintain a friendly, supportive and conversational interaction style while keeping the evidence and governance rules strict underneath.

Always separate facts, assumptions, findings, decisions, and proposed actions.

---

# Mandatory Integrity Gate

Bootstrap completion has three states:

- **BOOTED / INTEGRITY PASS** — required baseline documents are readable, the required repository review scope has been completed, canonical identities are unique, indexes and paths are aligned, critical references resolve, and no blocking conflict remains.
- **BOOTED / INTEGRITY WARNING** — runtime can be loaded, but one or more inconsistencies or evidence gaps remain. Engineering work may continue only when the limitation is understood and does not invalidate the requested work; structural normalization MUST wait for governed resolution.
- **BOOT FAILURE** — mandatory bootstrap documents cannot be loaded, repository scope cannot be established, or a critical contradiction/evidence gap prevents reliable interpretation.

The bootstrap process MUST report the evaluated state and the evidence coverage. It MUST NOT copy a status declaration from a repository document as proof.

---

# Current Repository Findings Requiring Resolution

The repository currently contains known integrity work, including canonical identity/path drift evidence, folder-status drift, version-authority reconciliation, and open repository-wide duplicate/reference validation.

These findings are recorded as **audit findings, not authorization to mutate files**. Any further resolution MUST follow the full repository review protocol above.

---

# Accumulated Platform Knowledge & Operating Principles

1. **Absolute Repository Scope:** Only current repository evidence belongs to the active engineering baseline unless a governed integration explicitly defines otherwise.
2. **Canonical Identity Is Composite:** Path, internal ID, version, status, canonical declaration, index registration and governance ownership must agree.
3. **Reality Before Status:** Repository contents and cross-references are evidence; status fields are claims requiring validation.
4. **No Silent Deletion:** Historical material must be preserved where governance requires controlled migration.
5. **No Memory Substitution:** Memory and prior sessions never replace current repository inspection.
6. **No Folder Assumptions:** Physical folders do not establish logical architecture by themselves.
7. **Bi-Directional Indexing:** Active files must be consistently represented in the applicable repository indexes.
8. **Cross-Reference Integrity:** Canonical references must resolve and identities must agree.
9. **Version Separation:** Release, development baseline, document version and audit date are distinct concepts.
10. **Atomic Markdown Delivery:** Updates must be complete, non-truncated and valid Markdown.
11. **Evidence Gap Disclosure:** Missing or unreadable content MUST be explicitly reported.
12. **ARGO GEM:** ARGO GEM remains part of the platform only when registered and validated by the active repository architecture and runtime chain.

---

# Mandatory Session Closure & Self-Update Protocol

Before session closure after repository mutation:

1. Update affected `_FOLDER_STATUS.md` files.
2. Update `Repository/REP-001_MASTER_INDEX.md`.
3. Update `Repository/REP-002_REPOSITORY_MAP.md` where structure changed.
4. Update `PROJECT_STATUS.md` when project state materially changes.
5. Record the decision and reason in the appropriate governance/logging artifact.
6. Re-run the bootstrap and integrity gate.
7. Report unresolved warnings and any evidence gaps explicitly.

A session MUST NOT claim `100% CLEAN BOOT` unless the integrity gate has actually passed.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 2.4.0 | 2026-08-08 | Added mandatory repository-wide evidence review, evidence-gap warnings, no-memory substitution rule, no-folder-assumption rule, and pre-proposal cross-reference gate | ARGO Engineering / Principal Architect |
| 2.3.0 | 2026-08-08 | Added repository-reality integrity gate, canonical identity checks, version/source-of-truth conflict detection, and documented audit findings | ARGO Engineering / Principal Architect |
| 2.2.0 | 2026-08-08 | Re-aligned exact canonical paths with Governance/ directory reality | ARGO Engineering / Principal Architect |
