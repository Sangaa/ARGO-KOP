# AI-004

---

# CONTEXT LOADING

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

AI-004

Version

1.2.0

Status

Integrity Hold / Revalidated

Category

AI

Canonical

Yes

Last Audit

2026-08-08

---

# Purpose

Defines how an AI instance loads, validates and maintains context while operating inside ARGO KOP.

Context loading must be based on current repository evidence. It must never silently reconstruct missing state from memory or historical copies.

# Context Authority

Current repository content is the authoritative engineering context unless a governed rule establishes a different source for a specific purpose.

Priority is determined by authority and evidence, not by document age alone.

`PROJECT_BOOTSTRAP.md` defines the mandatory bootstrap protocol. It does not replace inspection of the repository artifacts required for the task.

# Context Sources

The following are context sources, not automatic proof of truth:

1. Current repository files and structure.
2. Applicable Constitution and Governance authority.
3. `PROJECT_BOOTSTRAP.md`.
4. Repository indexes and maps.
5. Canonical documents whose identity has been verified.
6. `_FOLDER_STATUS.md` as status evidence.
7. Repository Memory.
8. Conversation and working notes as temporary context only.

If sources conflict, the conflict must be recorded and resolved according to authority and evidence.

# Mandatory Loading Workflow

Repository Availability Gate

↓

Repository Enumeration

↓

Required File Inspection

↓

Evidence Classification

↓

Cross-Reference Review

↓

Authority / Canonical Identity Check

↓

Context Assembly

↓

Engineering Decision

No engineering proposal may depend on unavailable evidence.

# Folder Loading

When entering a folder, the AI shall inspect:

- folder contents;
- filenames;
- README/index files;
- internal document IDs;
- versions and status;
- references and dependencies;
- applicable Governance/Architecture authority;
- `_FOLDER_STATUS.md`, if present.

A folder name or status file alone cannot establish its logical role or completion.

# Completion Rule

The AI MUST NOT infer folder completion from:

- status-file age;
- numeric filename sequence;
- README claims alone;
- previous session state;
- conversation memory.

Completion requires evidence-gated validation of the applicable scope.

# Evidence States

- Verified — directly observed in the current repository.
- Partially Verified — only a defined subset was inspected.
- Unavailable — required evidence could not be inspected.
- Inferred — derived from observed evidence but not directly stated.
- Assumed — unsupported by repository evidence.

Unavailable evidence must remain disclosed and cannot be silently promoted.

# Repository Synchronization

Before engineering the AI shall:

- establish the current branch/ref;
- inspect the current repository state;
- identify the applicable baseline;
- inspect required artifacts;
- resolve or disclose material conflicts;
- validate the scope required for the intended change.

# Failure Conditions

Stop or constrain engineering when:

- required repository content is unavailable;
- canonical identity is ambiguous;
- architecture or governance conflict exists;
- a critical cross-reference cannot be resolved;
- evidence coverage is insufficient for the requested decision;
- repository corruption is detected.

# Persistence Boundary

Permanent context includes validated repository artifacts and governed repository memory.

Temporary context includes conversation, working notes and model state.

Temporary context never overrides current repository evidence.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `AI/AI-001_AI_MODEL.md`
- `AI/AI-003_AI_LIMITATIONS.md`
- `AI/AI-005_PROMPT_ENGINEERING.md`
- `Core/CORE-003_CONSTITUTION.md`

---

# Guiding Statement

Correct engineering begins with sufficient evidence, not with confidence about missing context.

---

End of Document
