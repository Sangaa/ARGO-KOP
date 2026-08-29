# ROOM71 DOCS GLOSSARY AUTHORITY DISPOSITION — LEASE 135

Date: 2026-08-29
Role: HERMUZ via Room71
Baseline observed before write: `ab8515b14d4fb28576ce37886d9bf249bc216464`
Authority: bounded current-repository evidence only

## Question

Does `Docs/GLOSSARY.md` remain a competing repository-wide terminology authority against `Core/CORE-000A_PLATFORM_GLOSSARY.md`?

## Current Evidence

### Docs glossary

`Docs/GLOSSARY.md`:
- internal Document ID `DOC-005`;
- Version `1.0.0`;
- Status `Approved`;
- Category `Documentation`;
- says that it defines the "official terminology used throughout ARGO KOP";
- carries no `Canonical: Yes` declaration in the inspected content;
- current repository search did not establish an active consumer or index authority for `DOC-005` / `Docs/GLOSSARY.md` beyond Connected-Baseline review evidence.

### Core glossary

`Core/CORE-000A_PLATFORM_GLOSSARY.md`:
- Document ID `CORE-000A`;
- Version `1.2.0`;
- Status `Official / Revalidated / Integrity Hold`;
- Classification `Core Reference`;
- explicitly says it defines the canonical terminology used throughout the ARGO KOP repository;
- includes explicit scope, authority-conflict, provenance, ambiguity, terminology-change and non-inference rules.

Current `Core/_FOLDER_STATUS.md` identifies `CORE-000A_PLATFORM_GLOSSARY.md` among known canonical Core artifacts independently revalidated on 2026-08-10.

## Disposition

For repository-wide terminology authority within the inspected current scope:

`CORE-000A_PLATFORM_GLOSSARY = CURRENT GOVERNED CORE TERMINOLOGY REFERENCE`

`DOCS/GLOSSARY DOC-005 = DOCUMENTATION / LEGACY EXPLANATORY SURFACE / NO COMPETING CORE AUTHORITY`

The phrase "official terminology" inside DOC-005 is therefore bounded by the artifact's Documentation scope and does not override the later revalidated Core Reference.

This resolves the authority ambiguity without deleting or rewriting DOC-005.

## Why No Mutation to Docs Yet

Current search evidence does not justify deleting the documentation artifact or silently rewriting all terminology references. A future Docs content-reconciliation transaction may either:
- retain DOC-005 as a user-facing explanatory glossary that explicitly points to CORE-000A; or
- archive/supersede it after known consumers and documentation navigation are reconciled.

That future migration is separate from the authority decision closed here.

## Learning

`LOCAL APPROVED WORDING != HIGHER-LAYER CANONICAL AUTHORITY`

`"OFFICIAL" IN BODY TEXT != REPOSITORY-WIDE AUTHORITY WHEN A LATER REVALIDATED CORE REFERENCE OWNS THE SEMANTIC SURFACE`

A semantic conflict can be closed by authority classification without immediately deleting useful explanatory material.

## Close State

`DOCS_GLOSSARY_REPOSITORY_WIDE_AUTHORITY_AMBIGUITY = CLOSED / CORE000A GOVERNS GENERAL TERMINOLOGY`

`DOC005_CONTENT_MIGRATION_OR_ARCHIVE = OPEN / NON_BLOCKING`

`CONNECTED_BASELINE_GLOBAL = NOT CLOSED BY THIS LEASE`
