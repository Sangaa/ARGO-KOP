# BOOTSTRAP-001

---

# ARGO KOP - MANDATORY BOOTSTRAP & KNOWLEDGE TRANSFER SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: BOOTSTRAP-001  
Version: 2.3.0  
Status: Approved / Integrity-Gated  
Category: Bootstrap / Governance  
Canonical: Yes  
Priority: Absolute / Mandatory  
Last Audit Date: 2026-08-08  

---

# Mandatory Notice to AI Models & Contributors

This document is the mandatory initialization entry point for any AI agent, LLM instance, engineer, or automated runner interacting with ARGO KOP.

NO ENGINEERING WORK, FILE CREATION, OR REPOSITORY MUTATION SHALL BEGIN BEFORE EXECUTING THIS BOOT SEQUENCE IN FULL.

A successful bootstrap MUST NOT be inferred from `PROJECT_STATUS.md`, release metadata, or another self-declared status file alone. Bootstrap status is an evaluated runtime result based on repository reality.

---

# Mandatory 5-Step Bootstrap Protocol

Every AI instance or engineer joining the repository MUST execute the following sequence in order:

1. **Step 1: Scope & Isolation Boundary Scan**
   - Read `Repository/REP-001_MASTER_INDEX.md` and `Repository/REP-002_REPOSITORY_MAP.md`.
   - Confirm that operational work stays strictly inside the ARGO-KOP repository boundary.
   - Treat the repository's actual file tree and readable file contents as primary evidence during the audit.

2. **Step 2: Governance & Canonical Identity Verification**
   - Load the active governance documents registered by the repository.
   - Verify every canonical document by BOTH path and internal `Document ID`.
   - Detect duplicate IDs, duplicate logical documents, path drift, stale folder status files, conflicting `Canonical` declarations, and broken references.
   - A document is not considered canonical merely because its contents say `Canonical: Yes`.
   - If two files claim the same logical Document ID, stop normalization of that document until canonical ownership is explicitly resolved.

3. **Step 3: Runtime, Engine & State Alignment**
   - Load `Runtime/RUN-001_BOOT_SEQUENCE.md`.
   - Verify the active engine chain declared by the runtime documents.
   - Compare `PROJECT_STATUS.md`, `Release/VERSION.md`, `Release/RELEASE_MANIFEST.md`, repository indexes, and runtime declarations for version and state conflicts.
   - Do not use a self-declared `100% CLEAN BOOT` or equivalent statement as proof of integrity.

4. **Step 4: Canonical Source-of-Truth Verification**
   - The Git repository is the authoritative engineering source for repository state unless an explicit governance decision defines another artifact as an external source for a specific purpose.
   - External working copies, including Google Drive copies, MUST NOT silently override repository reality.
   - If an external canonical stack is referenced, the relationship between that stack and the repository MUST be explicitly documented, versioned, and validated.

5. **Step 5: Human-Centric Dialogue Alignment**
   - Adopt a friendly, supportive, and conversational style for user interactions while maintaining strict governance underneath.
   - Separate facts, assumptions, findings, decisions, and proposed actions.

---

# Mandatory Integrity Gate

Bootstrap completion has two distinct states:

- **BOOTED / INTEGRITY PASS** — required baseline documents are readable, canonical identities are unique, indexes and paths are aligned, critical references resolve, and no blocking governance or version conflict remains.
- **BOOTED / INTEGRITY WARNING** — runtime can be loaded, but one or more repository inconsistencies remain. Engineering work MAY continue only when the inconsistency is understood and does not invalidate the requested work; structural normalization MUST wait for a governed decision.
- **BOOT FAILURE** — mandatory bootstrap documents cannot be loaded, repository scope cannot be established, or a critical contradiction prevents reliable interpretation of the system.

The bootstrap process MUST report the actual evaluated state rather than copying a status declaration from a repository document.

---

# Current Repository Findings Requiring Resolution

The 2026-08-08 repository audit identified the following conditions. These findings are recorded here as bootstrap knowledge so future sessions do not mistake them for a missing-file-only problem:

1. **GOV-004 identity/path drift**
   - `Standards/GOV-004_DOCUMENT_METADATA.md` exists.
   - `Governance/GOV-003_DOCUMENT_METADATA.md` contains the logical identity `GOV-004` and declares itself canonical.
   - Repository indexes reference `Governance/GOV-004_DOCUMENT_METADATA.md` as the canonical path.
   - Result: duplicate logical identity and canonical path mismatch.

2. **GOV-006 path duplication/drift**
   - `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` exists.
   - A corresponding `Standards/` copy also exists.
   - Result: canonical ownership must be explicitly established before deletion, movement, or rewrite.

3. **Governance folder status drift**
   - `Governance/_FOLDER_STATUS.md` describes an older governance structure and reports consistency despite the current repository containing a different structure.
   - Result: folder status is stale and cannot currently be treated as authoritative evidence.

4. **Version authority conflict**
   - `PROJECT_STATUS.md` declares platform version `3.2.0`.
   - `PROJECT_BOOTSTRAP.md` is versioned independently as the bootstrap specification.
   - `Release/VERSION.md` and `Release/RELEASE_MANIFEST.md` still describe release `1.0.0`.
   - Result: the repository lacks a single unambiguous release/version authority and this MUST be resolved through governance before claiming release consistency.

5. **Source-of-truth ambiguity**
   - Some status material references a Google Drive canonical stack.
   - Core repository principles define the repository as the authoritative engineering source.
   - Result: the relationship between external canonical material and GitHub MUST be explicitly governed; no external copy may silently override repository reality.

6. **Migration / historical structure evidence**
   - Repository history shows deletion/re-upload activity around the Governance area.
   - Historical files and current files therefore MUST be distinguished as active, legacy, duplicate, orphaned, or archived rather than inferred from filenames alone.

These findings are NOT authorization to modify or delete files. They are integrity findings that require evidence-based resolution.

---

# Accumulated Platform Knowledge & Operating Principles

1. **Absolute Repository Scope (Isolation Fence):**
   Only files inside the ARGO-KOP repository belong to the active platform baseline. External or unindexed documents MUST be ignored unless explicitly referenced by a governed integration.

2. **Canonical Identity Is Composite:**
   Canonical identity is determined by the combination of path, internal Document ID, version, canonical declaration, index registration, and governance ownership. Filename alone is insufficient.

3. **Strict Canonical Naming:**
   Every active file MUST follow the applicable naming standard and its proper prefix (for example `RUN-`, `MOD-`, `ENG-`, `INT-`, `INTF-`, `QLT-`, `PLG-`, `GOV-`).

4. **No Silent Deletion:**
   Deletion is prohibited where governance requires archival or controlled migration. Historical material MUST be preserved according to the repository's controlled-evolution rules.

5. **Reality Before Status:**
   Repository contents, readable file metadata, cross-references, and history are evidence. Self-reported status fields are claims that require validation.

6. **Chronological Audit Sync:**
   Updating a document requires updating the relevant parent `_FOLDER_STATUS.md` and all affected indexes after the change has been reviewed and validated.

7. **Bi-Directional Indexing:**
   Active files MUST be consistently represented in `Repository/REP-001_MASTER_INDEX.md` and `Repository/REP-002_REPOSITORY_MAP.md`.

8. **Cross-Reference Integrity:**
   A canonical document reference MUST resolve to an existing file and the referenced file's internal identity MUST agree with the reference.

9. **Version Authority:**
   Release version, platform version, document version, and repository audit date are distinct concepts. They MUST NOT be conflated. A single authoritative source for each concept MUST be established through governance.

10. **Atomic Markdown Delivery:**
    File updates MUST be complete, non-truncated, valid Markdown with exact repository paths.

11. **Human-Centric Dialogue Protocol:**
    Communicate naturally and helpfully without rigid automated disclaimers while preserving strict internal governance.

12. **ARGO GEM:**
    ARGO GEM and its associated engine documents remain part of the platform only when registered and validated by the active repository architecture and runtime chain.

---

# Mandatory Engineering Change Gate

Before modifying the repository structure or resolving a canonical conflict:

**Inspect → Collect Evidence → Classify → Decide Canonical Ownership → Define Migration → Review → Execute → Validate → Update Indexes/Folder Status → Re-Boot**

No file may be deleted, renamed, duplicated, or reassigned solely because another file appears newer. Canonical ownership MUST be explicitly determined first.

---

# Mandatory Session Closure & Self-Update Protocol

Before session closure after repository mutation:

1. Update the affected `_FOLDER_STATUS.md` files.
2. Update `Repository/REP-001_MASTER_INDEX.md`.
3. Update `Repository/REP-002_REPOSITORY_MAP.md` where structure changed.
4. Update `PROJECT_STATUS.md` when project state materially changes.
5. Record the decision and reason in the appropriate governance/logging artifact.
6. Re-run the bootstrap and integrity gate.
7. Report unresolved warnings explicitly.

A session MUST NOT claim `100% CLEAN BOOT` unless the integrity gate has actually passed.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 2.3.0 | 2026-08-08 | Added repository-reality integrity gate, canonical identity checks, version/source-of-truth conflict detection, and documented current audit findings | ARGO Engineering / Principal Architect |
| 2.2.0 | 2026-08-08 | Re-aligned exact canonical paths with Governance/ directory reality | ARGO Engineering / Principal Architect |
