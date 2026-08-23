# EJR-314 — CONNECTOR REGISTRATION BOUNDARY REVIEW

Date: 2026-08-23  
Status: CLOSED — DOCUMENTED BOUNDARY  
Checkpoint: ACTIONS_CONNECTOR_EXPOSURE_GAP / REGISTRATION-LAYER REVIEW

## Objective

Determine whether the repository contains an identifiable implementation of the connector/tool-registration layer capable of exposing the already-implemented `list_workflow_runs(head_sha=...)` operation to the current HERMUZ session.

## Evidence Reviewed

1. `Interfaces/INTF-001_INTERFACE_SPEC.md` defines `INTF-API` as the operational service-dispatch boundary and requires deterministic dispatch, payload validation, and traceable execution. It does not itself define the session tool registry.
2. `Interfaces/INTF-010_INTEGRATIONS.md` defines the canonical connector boundary:
   `External Source / Application → Connector / Adapter → Interface Contract → ARGO Runtime`.
   It explicitly states that connectors are integration mechanisms and must not silently redefine ARGO authority.
3. `Plugins/PLG-001_PLUGIN_ARCHITECTURE.md` defines a plugin registration/manifest architecture, including manifest validation, interface binding adapter, capability declarations, and requested interface permissions. This is an architectural specification, not proof that a live session tool registry is implemented.
4. Repository history confirms `INTF-010_INTEGRATIONS.md` is a canonical interface artifact and is indexed in the Interfaces inventory.
5. Search for a repository implementation specifically identified as a `tool registry` produced no matching commit evidence.

## Finding

The repository clearly defines architectural concepts for registration, interface binding, operational dispatch, and plugin capability declaration. However, the reviewed evidence does **not** establish the existence of a concrete, session-facing tool registry/manifest loader that can dynamically expose repository connector methods to the current HERMUZ session.

Therefore the previously documented `ACTIONS_CONNECTOR_EXPOSURE_GAP` remains unresolved.

## Important Boundary

Do not conflate:

- connector implementation in repository code;
- interface/connector architecture;
- plugin registration specification;
- runtime service dispatch;
- actual session tool exposure.

These are separate evidence layers.

## Decision

1. Do not modify `PLG-001`, `INTF-001`, or `INTF-010` merely to solve the current GitHub Actions observation problem.
2. Do not invent a tool registry implementation from an architectural specification.
3. Do not add another GitHub connector.
4. Do not run further GitHub execution probes from this checkpoint.
5. Keep P6 at `IMPLEMENTED / EXECUTION EVIDENCE PENDING`.
6. Treat the session tool surface as an external capability boundary unless concrete registry implementation evidence becomes available.

## Reusable Learning

**Architecture specification ≠ runtime implementation ≠ session capability.**

A documented registration/binding mechanism proves intended architecture, not that the current session can dynamically register or expose a new operation.

This is a general ARGO rule for future connector investigations: establish evidence separately for provider capability, repository implementation, interface contract, runtime registration, and session exposure before claiming end-to-end availability.

## P6 State

`IMPLEMENTED / EXECUTION EVIDENCE PENDING`

Run-ID discovery: NOT DISCOVERED  
Connector implementation: PRESENT  
Interface architecture: PRESENT  
Concrete session registry implementation: NOT VERIFIED  
Session exposure: NOT EXPOSED  
Mutation in this checkpoint: DOCUMENTATION ONLY
