# KRS-002 — Knowledge Object / Blob Candidate Model

Status: `CANDIDATE / NOT CANONICAL`
Version: `0.1.0`
Date: 2026-08-26

## Intent
Define a compact, connected representation for a bounded knowledge object without replacing the current ARGO artifacts.

## Record Envelope
```text
KO
├── identity
├── control
├── provenance
├── relations
├── evidence
├── assertions
├── constraints
├── history
├── payload
└── integrity
```

## Required Semantics
- `identity`: stable object ID, namespace, artifact class.
- `control`: lifecycle/status, authority class, canonicality state.
- `provenance`: source object(s), origin, evidence references, derivation.
- `relations`: typed links such as `REFERENCES`, `CONSUMES`, `DEPENDS_ON`, `IMPLEMENTS`, with evidence.
- `evidence`: evidence item, source, strength, scope, verification state.
- `assertions`: claims separated from evidence and assumptions.
- `constraints`: governing rules and invariants.
- `history`: revisions and transitions; Git history remains authoritative for file changes.
- `payload`: domain-specific information.
- `integrity`: checksums/validation markers when applicable.

## Design Rule
The record stores **meaning and relationships**; Git stores authoritative change history. A Blob is not a replacement for Git provenance.

## Relationship Rule
A relation type cannot be promoted by field presence alone. It requires the same evidence discipline used by REP-014/HERMUZ.

## Migration Rule
No existing artifact is replaced by this candidate. Migration requires semantic equivalence, provenance preservation, relationship validation, integration/regression evidence, and explicit promotion.

## Pilot Requirement
Select a small set of materially different existing artifacts, encode them as candidate objects, then compare:

`source information → candidate information → relationships → evidence → traceability → human reviewability`

Any loss or ambiguity blocks migration.

## Non-Goals
- replacing all Markdown;
- making one giant repository blob;
- eliminating human-readable canonical documents;
- reducing file count as an independent success metric;
- creating a new authority layer before the existing model is reconciled.
