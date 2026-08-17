# ARGO KOP

---

# Knowledge Operating Platform

Platform: ARGO KOP  
Official Release: 1.0.0  
Development Baseline: 3.2.1  
Status: Connected-Baseline Integrity Validation  
Canonical: Yes  
Last Audit Date: 2026-08-08

---

## What is ARGO KOP?

**ARGO KOP (Knowledge Operating Platform)** is a cognitive engineering platform designed to transform fragmented organizational knowledge into a structured, governed, traceable, reusable, and continuously evolving engineering asset.

The platform preserves knowledge, maintains architectural consistency, separates repository evidence from assumptions, and supports disciplined collaboration between people and AI systems.

ARGO KOP is governed by its repository rather than by any single AI model or session memory.

## Current Repository State

The repository is currently in a **Connected-Baseline Integrity Validation** phase.

The current objective is to verify that critical artifacts, identities, authorities, references, indexes, status claims, and cross-layer relationships agree with the actual repository contents.

Recent audit work has corrected or revalidated several identity and authority boundaries, including:

- `Architecture/ARC_MAP.md` no longer competes with `ARC-001` as a canonical document identity.
- The former Lifecycle `GOV-005` identity has been migrated to `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`.
- `Engine/ENG-010_ENGINE_COORDINATION.md` is now `3.1.1 / Integrity Hold / Revalidated` and explicitly separates routing declarations from verified integration contracts.
- `Engine/ENG-011_MARITIME_GAME_ENGINE.md` is now `1.0.1 / Integrity Hold` with explicit dependency and authority boundaries.
- `Repository/REP-001_MASTER_INDEX.md` and `Repository/REP-002_REPOSITORY_MAP.md` have been synchronized for the currently verified inventory scope.

These corrections do **not** constitute repository-wide PASS certification.

**A successful file mutation, an existing path, or a local PASS does not certify the repository globally.**

The current development baseline is not an official release. `Release/VERSION.md` is authoritative for that distinction.

## System Structure

The repository is a connected system rather than a simple folder tree.

The current top-level relationship model is maintained in [`SYSTEM_MAP.md`](SYSTEM_MAP.md). Principal domains include Core, Governance, Repository, Architecture, Lifecycle, Knowledge, Memory, Models, Interfaces, Runtime, Engine, Decision, AI, Services, Intelligence, Quality, Release, Logs and Future.

**Folder names alone do not establish logical ownership or completeness.**

## Mandatory Onboarding & Bootstrap Sequence

Any engineer, contributor, or AI model interacting with this repository **MUST** follow the repository-first boot protocol defined in [`PROJECT_BOOTSTRAP.md`](PROJECT_BOOTSTRAP.md).

No engineering work or repository mutation should begin by relying on remembered repository state, previous sessions, ZIP snapshots, or inferred folder structure when current repository evidence is available.

If required content cannot be inspected, that evidence gap must remain explicit.

### HERMUZ Continuation Command

The canonical continuation phrase for the HERMUZ session build protocol is:

> **«أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»**

When this phrase is received, load and apply [`Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`](Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md) together with `PROJECT_BOOTSTRAP.md` and current repository evidence. Do not require the user to resend the protocol. Continue from the latest verified checkpoint and highest-priority safe work; do not restart completed work merely because the conversation changed.

HERMUZ is an operating protocol and does not override ARGO constitutional, governance, architecture, release, or domain authority.

### Mandatory Failure-to-Learning Protocol

**Every engineer, contributor, and AI model MUST apply [`GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`](GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md).**

An unexpected failure must not be silently fixed, ignored, or reduced to a generic `FAILED` state. It must be analyzed from evidence, classified, root-caused where possible, corrected or safely contained, regression-tested when practical, and transferred into reusable knowledge according to its validated scope.

The mandatory chain is:

**Failure → Evidence → Root Cause → Failure Class → Corrective Pattern → Regression Test → Reuse → Knowledge Transfer**

**Bad Idea ≠ Bad Implementation ≠ Bad Test ≠ Bad Execution Channel.**

This protocol is mandatory for all models so that ARGO continuously converts failures into bounded, verified, reusable capability rather than merely accumulating successful outcomes.

## Core Repository Navigation

- **System Map:** [`SYSTEM_MAP.md`](SYSTEM_MAP.md)
- **Master Repository Index:** [`Repository/REP-001_MASTER_INDEX.md`](Repository/REP-001_MASTER_INDEX.md)
- **Repository Relationship Map:** [`Repository/REP-002_REPOSITORY_MAP.md`](Repository/REP-002_REPOSITORY_MAP.md)
- **Platform Bootstrap:** [`PROJECT_BOOTSTRAP.md`](PROJECT_BOOTSTRAP.md)
- **HERMUZ Session Protocol:** [`Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`](Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md)
- **Failure-to-Learning Protocol:** [`GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`](GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md)
- **Platform Status:** [`PROJECT_STATUS.md`](PROJECT_STATUS.md)
- **Vision:** [`VISION.md`](VISION.md)
- **Runtime Sequence:** [`Runtime/RUN-001_BOOT_SEQUENCE.md`](Runtime/RUN-001_BOOT_SEQUENCE.md)
- **Version Authority:** [`Release/VERSION.md`](Release/VERSION.md)
- **Security Policy:** [`SECURITY.md`](SECURITY.md)

## Engineering Rule

The repository is reviewed as a **relationship graph**.

For material dependencies, the expected verification chain is:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read → Revalidate**

A reference is not a validated dependency merely because its path exists.

A local PASS is bounded to its inspected scope. A global integrity claim requires evidence coverage sufficient to support that claim.

## Self-Evolution Rule

ARGO KOP is intended to learn from both successful and unsuccessful engineering outcomes, but a failure or observation does not automatically become a canonical rule.

The current operational learning path is:

**Observed → Recorded → Re-examined → Tested → Governed → Reused**

GOV-016 adds the mandatory failure-analysis branch:

**Failure → Evidence → Root Cause → Correction → Verification → Memory → Reuse**

New audit-derived rules remain candidates until explicitly promoted through the applicable authority path.

## Vision

See [`VISION.md`](VISION.md) for the long-term purpose and design philosophy.

See [`START_HERE.md`](START_HERE.md) for the recommended entry path.

## License & Intellectual Property

Refer to `LICENSE.md` and `NOTICE.md` for the repository's applicable ownership and licensing terms. These files remain subject to current repository verification during the connected-baseline audit.

---

**Knowledge Organized. Decisions Preserved. Intelligence Connected.**
