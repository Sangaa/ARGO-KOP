# KRS-003 — Three-Class Compression Pilot P260

Status: `ASSESSMENT / NOT CANONICAL`
Date: 2026-08-26
Baseline: `afc85d60829e677723838b31dac7a2b1c6195489`

## Objective
Compare three materially different artifact classes before any migration decision:

1. **Governance contract** — `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
2. **Knowledge/schema candidate** — `Repository/KRS-002_KNOWLEDGE_OBJECT_BLOB_CANDIDATE.md` and KRS-001 schema/pilot surfaces
3. **Engineering learning / assessment** — `Memory/Engineering_Journal/EJR-2026-08-26_ARCHITECTURE_REENTRY_KNOWLEDGE_COMPRESSION.md`

The purpose is to identify what can be represented as bounded structured objects while preserving authority, evidence, provenance, history and human reviewability. This is an assessment only.

## Comparative Findings

| Dimension | Governance contract | Knowledge/schema | Engineering learning |
|---|---|---|---|
| Primary role | Operating authority | Structured information model | Learning/decision trace |
| Stable identity | Document ID/version | Object ID/schema version | Journal identity/date |
| Authority/status | Explicit and canonical | Explicit candidate state | Explicit assessment state |
| Provenance | Protocol references and repository state | Source/evidence fields | Baseline and source context |
| Relationships | Mostly textual/reference-driven | Typed relation model | Assessment sequence/context |
| Evidence | Rules for evidence discipline | Evidence as first-class field | Findings and quality gates |
| Assertions/constraints | Strong | Strong | Partial/assessment-oriented |
| History | Git + version | Git + revision envelope | Git + dated journal record |
| Human auditability | High in Markdown | High if paired with readable source | High |
| Machine validation potential | High | High | Medium |
| Safe compression target | **Partial** | **High** | **Partial** |

## Duplication / Implicit Relationship Findings

- Governance defines rules that other artifacts operationalize; copying those rules into every object would create duplication and authority drift.
- Knowledge objects are the strongest compression target because identity, relations, evidence and constraints can be represented as fields rather than inferred from filenames and prose.
- Engineering learning should not be flattened into the same object class as executable/canonical knowledge without preserving its historical and epistemic status.
- Some relationships remain intentionally external: Git commit ancestry is authoritative for change history; governance authority must not be duplicated as object-local authority.

## Information-Loss Risks

1. Collapsing governance into ordinary records could erase authority precedence.
2. Flattening journal learning into canonical knowledge could erase uncertainty and historical context.
3. Replacing Markdown with opaque blobs could reduce human auditability.
4. Replacing Git history with an internal `history` field would weaken provenance.
5. Converting textual references into typed relations without evidence could create false dependencies.

## Compression Decision

**No repository-wide compression is proven.** The evidence supports a narrower conclusion:

> Use bounded Knowledge Objects for structured, relationship-heavy information; retain human-readable governance and learning surfaces where their authority or epistemic context is part of the meaning; connect them through explicit, evidence-backed references rather than duplicating their content.

## Pilot Metrics for Next Stage

For a representative migration candidate, measure:

- semantic field coverage;
- duplicated fact count;
- implicit vs explicit relationship count;
- provenance retention;
- evidence retention;
- human review effort;
- machine validation success;
- diff/mutation clarity;
- runtime consumer compatibility where applicable.

A candidate fails if any mandatory semantic/evidence element is lost, even when file count or byte count decreases.

## Decision Boundary

The candidate model remains `NON-CANONICAL`. The next stage may construct a small dual-representation sample only after selecting concrete source artifacts and defining equivalence assertions. No source artifact is deleted, retired or made non-canonical by this assessment.
