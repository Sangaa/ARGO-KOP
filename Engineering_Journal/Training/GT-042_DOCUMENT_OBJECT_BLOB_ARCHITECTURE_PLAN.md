# GT-042 — Document Object / BLOB Architecture Plan

## Status
TRAINING-RECORDED / POST-TRAINING PRIORITY

## Purpose
Record the architectural improvement identified during GitHub tooling training: ARGO should eventually evaluate moving from a file-centric mutation model toward a Document Object / BLOB-oriented model that preserves complete content, content identity, structure, provenance, and controlled mutation independently of the storage backend.

## Trigger
The current training exposed a recurring boundary around large/complete file reads and controlled full-file replacement. GitHub Git Blob semantics provide a useful reference model: a blob has content identity and complete content, while higher layers can map structure, sections, and mutations onto that content.

## Proposed Direction
Evaluate an ARGO Document Object abstraction rather than making Git Blob itself the ARGO architecture:

- Identity: document_id, content_hash/blob identity, version.
- Envelope: type, encoding, source, provenance.
- Payload: complete content/blob.
- Structure: sections, records, relationships.
- Mutation: read, patch, replace, merge, verify.
- Backend adapters: Git Blob, ordinary files, database BLOBs, EDI payloads, object storage, or other suitable stores.

## Important Architectural Rule
Git Blob is a backend representation/reference model, not the ARGO domain model. ARGO should remain backend-independent.

## Required Post-Training Sequence
1. Finish the current GitHub tooling training and capability mapping.
2. Re-evaluate the existing integration tests using the newly learned tool and document semantics.
3. Re-run the test suite and establish a clean baseline before declaring the current test layer complete.
4. Close/retire the training tests only after the clean baseline and evidence are reconciled.
5. Study and compare file/document architectures, including Blob/EDI-style representations, before changing the repository-wide document model.
6. Design and validate the new document architecture on new/low-risk ARGO artifacts first.
7. Migrate or refactor legacy files only after the new model is proven and migration priorities are established.

## Priority Principle
Do not refactor legacy files merely because a new representation is attractive. First prove the new model on controlled artifacts, verify integrity and mutation behavior, then migrate according to risk, dependency, value, and evidence.

## Relationship to GT-041
GT-041 remains focused on the immediate test-fixture contract investigation. This document records a broader post-training architectural improvement and must not be used as justification for changing production contracts before the planned reassessment.

## Decision Gate
No repository-wide document migration is authorized by this note. It is a required improvement/research item for post-training architectural review.
