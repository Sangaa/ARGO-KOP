# ARC-006

---

# DEPENDENCY MODEL

---

Platform

ARGO KOP

Knowledge Operating Platform

---

Document ID

ARC-006

Version

1.3.1

Status

Validated / Integrity Hold

Category

Architecture

Development Baseline

3.2.1

Latest Official Release

1.0.0

Last Audit

2026-08-13

---

# Purpose

Defines the dependency model of ARGO KOP. It governs logical dependency direction, ownership and qualification rather than physical folder layout.

# Canonical Dependency Direction

Identity / Core

↓

Governance

↓

Architecture

↓

Repository

↓

Knowledge / Specifications / Standards

↓

Memory

↓

Cognition / Engine

↓

Runtime / Services / AI

↓

Projects / Applied Artifacts

Dependencies must not reverse this direction unless explicitly authorized by a governed architectural decision.

# Allowed Dependencies

## Core

Depends on: None at the architectural layer level.

## Governance

May depend on: Core.

## Architecture

May depend on: Core, Governance.

## Repository

May depend on: Core, Governance, Architecture.

## Knowledge / Specifications / Standards

May depend on: Repository, Architecture and applicable Governance rules.

## Memory

May depend on: Knowledge, Repository and applicable Governance rules.

## Cognition / Engine

May depend on: Knowledge, Memory, Repository and approved Architecture interfaces.

## Runtime / Services / AI

May depend on: approved lower-level platform interfaces and the applicable runtime contracts. AI providers do not acquire platform authority through integration.

Runtime external integrations MUST consume approved interface contracts rather than bypassing the Architecture / Governance dependency model.

External connectors, APIs, services and evidence sources are integration mechanisms, not architectural authorities.

Authorization, provenance and execution status remain runtime/security concerns and do not create upward authority.

## Projects / Applied Artifacts

May depend on approved platform capabilities and documented interfaces. Projects MUST NOT redefine platform architecture or governance.

# Integration Dependency Boundary

An external integration creates a dependency only when the platform relies on that integration for a defined operation or required evidence.

Such a dependency MUST identify, as applicable:

- provider / connector identity;
- interface contract;
- consuming runtime capability;
- authorization boundary;
- provenance requirements;
- expected execution outcomes;
- failure / timeout / unknown handling;
- recovery implications;
- owning authority.

Connector availability does not establish architectural dependency authority or permission to act.

An external result MUST remain distinguishable from the platform's own validated state.

`UNKNOWN` external execution status MUST NOT be converted into architectural or repository success.

# Memory / Learning Boundary

User, session and project experience may depend on Runtime and approved Memory mechanisms, but experience captured during runtime does not become a dependency of canonical platform architecture merely because it was observed or reused.

Promotion of learned experience into canonical platform knowledge requires applicable governance and validation.

# Dependency Qualification

Every claimed architectural dependency MUST be:

- necessary;
- explicitly documented;
- traceable to a current canonical artifact or interface;
- owned;
- architecturally justified;
- free of circular dependency;
- compatible with the current layer model;
- consistent with applicable runtime/security boundaries.

A textual reference to a file path does not by itself establish an architectural dependency.

# Authority Rule

A dependency does not transfer authority.

A lower layer may consume an approved contract from a higher layer but cannot use that dependency to rewrite or redefine the higher layer.

An external provider may supply capability or evidence but cannot become a source of ARGO platform authority through integration.

# Prohibited Dependencies

- Lower layers rewriting higher-layer authority.
- Projects redefining Core, Governance or Architecture.
- Repository artifacts silently overriding Constitution or Governance.
- Memory rewriting Architecture without a governed decision.
- Undocumented cross-component dependencies.
- Circular dependencies.
- Using folder placement as implicit authority.
- External connectors bypassing approved interface or authorization boundaries.
- Treating external execution success as repository or architectural authority without validation.

# Validation

A new or materially changed dependency requires review of:

1. Layer direction.
2. Ownership.
3. Traceability.
4. Canonicality of referenced artifact.
5. Circularity.
6. Compatibility with `ARC-004_LAYER_MODEL.md`.
7. Compatibility with `ARC_MAP.md`.
8. Compatibility with Repository and Governance authority.
9. Interface contract alignment when an external integration is involved.
10. Authorization / provenance requirements when applicable.
11. Runtime failure and recovery behavior when applicable.

Validation failure blocks acceptance until corrected or explicitly dispositioned by the applicable authority.

# Related Documents

- `Architecture/ARC_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Runtime/RUN-007_RUNTIME_SECURITY.md`
- `Runtime/RUN-008_RUNTIME_STATE.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/INTF-010_INTEGRATIONS.md`

---

# Guiding Statement

Explicit, traceable dependencies produce stable architecture; integration capability never becomes authority merely by being connected.

---

End of Document
