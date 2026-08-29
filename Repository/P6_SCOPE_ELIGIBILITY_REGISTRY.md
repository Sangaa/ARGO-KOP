# P6 — SCOPE / ELIGIBILITY REGISTRY

Platform: ARGO KOP  
Document ID: P6-SCOPE-001  
Version: `1.1.0`  
Status: **Canonical P6 Scope Boundary Contract / EJR Policy Resolved**  
Authority: `GOV-013 + GOV-015 + GOV-016 + applicable ARGO governance authority`  
Development Baseline: `3.2.1`  
Purpose: Separate P6 scope/eligibility policy from changed-path correlation and execution evidence classification.

---

## 1. Boundary

P6 MUST NOT infer whether a repository path is within P6 scope from the existence or absence of a mapping in `REP-020`, `REP-014`, or another evidence surface.

Scope/eligibility is evaluated before correlation.

This registry expresses the currently authorized scope state. It does **not** grant relationship authority.

Required evaluation order:

`Changed Path → Scope / Eligibility → Correlation → Execution Evidence → Evidence Classification`

---

## 2. Scope States

The only valid P6 scope states are:

- `IN_SCOPE` — the path class is governed by P6 correlation under an explicit authority/evidence basis.
- `OUT_OF_SCOPE` — the path class is explicitly excluded from direct P6 impact correlation under an explicit authority/evidence basis.
- `UNRESOLVED` — scope policy has not been authoritatively decided; the correlator MUST NOT reinterpret this state as a missing mapping.

`UNRESOLVED` is a valid terminal policy state for a P6 evaluation. It MUST NOT be converted automatically to `UNMAPPED`, `MAPPED`, `PARTIAL`, `OUT_OF_SCOPE`, or any relationship state.

`OUT_OF_SCOPE` is also bounded: it means P6 direct impact correlation does not apply to that changed-path class. It does not mean the artifact has no evidentiary, historical, learning, governance, or architectural value.

---

## 3. Current Eligibility Registry

| Path Class | P6 Scope | Authority | Evidence | Correlation Rule |
|---|---|---|---|---|
| `Runtime/**` | `IN_SCOPE` | GOV-013 integration priority / current P6 contract | Existing P6 runtime/integration evidence surfaces | Correlate only after exact repository-relative path evaluation |
| `Engine/**` | `IN_SCOPE` | GOV-013 integration priority / current P6 contract | Existing P6 runtime/integration evidence surfaces | Correlate only after exact repository-relative path evaluation |
| `Services/**` | `IN_SCOPE` | GOV-013 integration priority / current P6 contract | Existing P6 service/runtime impact surfaces | Correlate only after exact repository-relative path evaluation |
| `Quality/Integration/**` | `IN_SCOPE` | Current P6 implementation/test scope | `Quality/Integration` P6 implementation and regression artifacts | Correlate only after exact repository-relative path evaluation |
| `Repository/REP-020*` | `IN_SCOPE` | GOV-013 / REP-020 evidence role | `REP-020` current control artifact | Correlate as evidence/control-plane impact; do not infer authority |
| `Repository/REP-014*` | `IN_SCOPE` | GOV-013 / REP-014 canonical relationship role | `REP-014` current control artifact | Correlate as relationship evidence; do not infer authority |
| `Repository/P6_*` | `IN_SCOPE` | Current P6 control contract | Current P6 artifacts | Correlate as P6 control-plane evidence |
| `EJR/**` | `OUT_OF_SCOPE` | GOV-015 execution/knowledge-transfer boundary + GOV-016 learning-promotion boundary | Issue #15, EJR-284, Mutation Matrix preflight treatment, current learning/authority separation | Return `NOT_APPLICABLE` for the EJR changed path; retain EJR as provenance/learning evidence; do not invent mapping/relationship authority |
| Other repository paths | `UNRESOLVED` unless an explicit governed registry entry exists | Applicable ARGO authority | Current repository evidence required | Do not infer scope from path existence or neighboring mappings |

---

## 4. Correlation Contract

For an evaluated changed path:

| Eligibility | Correlation result | Meaning |
|---|---|---|
| `IN_SCOPE` | `MAPPED` | Canonical mapping/evidence was located by the correlator |
| `IN_SCOPE` | `UNMAPPED` | No canonical mapping/evidence was located; this is a correlation finding, not a governance decision |
| `OUT_OF_SCOPE` | `NOT_APPLICABLE` | P6 direct impact correlation does not apply to this changed path; other evidence/provenance duties remain independent |
| `UNRESOLVED` | `POLICY_UNRESOLVED` | Governance policy is unresolved; the correlator MUST NOT classify this as a missing mapping |

`UNMAPPED` MUST NOT be emitted for a path whose scope state is `UNRESOLVED` or `OUT_OF_SCOPE`.

---

## 5. Evidence Boundary

Execution evidence and semantic/relationship evidence are distinct evidence classes.

The following states are independent and MUST NOT be implicitly promoted into one another:

`EXECUTION_VERIFIED`  
`CANONICAL_MAPPING_VERIFIED`  
`RELATIONSHIP_VERIFIED`

A CI PASS, runtime evidence artifact, fixture result, controlled synthetic result, Engineering Journal entry, or documentation record cannot by itself create canonical mapping or relationship authority.

Evidence maturity remains bounded by the strongest actually exercised layer:

`UNIT → CONTROLLED_SYNTHETIC → CANONICAL_REPOSITORY → INTEGRATION → RUNTIME`

Lower-level evidence MUST NOT promote a higher-level state automatically.

---

## 6. EJR Governance Decision — 2026-08-29

`EJR/**` is explicitly `OUT_OF_SCOPE` for **direct P6 implementation/relationship impact correlation**.

### Why

1. Under `GOV-015`, Engineering Journal material is an execution/learning/handoff evidence surface, not implementation or promotion authority by existence alone.
2. Under `GOV-016`, learning moves through observation, root cause, lesson, validation, promotion and transfer. A journal record does not automatically become a governance/runtime/relationship rule.
3. Existing Mutation Matrix preflight behavior already treats `EJR/**` as documentation/session evidence rather than a protected implementation mutation path.
4. Issue #15 specifically prohibited manufacturing `REP-020` mappings or classifier exceptions solely to convert EJR documentation changes to PASS.
5. P6 was architected so policy can be resolved in this registry without hard-coding the result into the correlator.

### Meaning

For an EJR-only changed path:

`EJR/** → OUT_OF_SCOPE → NOT_APPLICABLE → NO_AUTO_PROMOTION`.

This does **not** mean EJR is ignored.

EJR remains usable as:

- provenance;
- session evidence;
- failure/learning evidence;
- historical context;
- a candidate input to later governed promotion or decision.

If a transaction changes both an EJR and an in-scope implementation/control/relationship artifact, each changed path is evaluated independently. The EJR classification cannot suppress or promote the in-scope path.

No EJR relationship, `REP-020` mapping, runtime semantic claim, or authority is created by this scope decision.

Issue #15 may close after canonical regression verifies this state on the promotion candidate.

---

## 7. Mutation / Promotion Safety

1. The registry does not create relationship authority.
2. The registry does not modify `REP-020` relationship state merely to remove an `UNMAPPED` result.
3. `UNRESOLVED` cannot be auto-promoted to any resolved scope state.
4. `OUT_OF_SCOPE` cannot be reinterpreted as `MAPPED` merely because correlation text happens to mention the path.
5. Correlation cannot override this registry.
6. Execution evidence cannot override this registry.
7. Synthetic evidence cannot override this registry.
8. Any future change to an eligibility state requires explicit authority and fresh current-HEAD validation.
9. EJR evidence remains governed by its applicable provenance/learning/transfer controls even when P6 direct impact correlation is not applicable.

---

## 8. Verification Requirement

Any P6 implementation consuming this registry MUST have canonical repository tests that read this artifact from the repository and prove at minimum:

- an `IN_SCOPE` path resolves deterministically;
- an `OUT_OF_SCOPE` path becomes `NOT_APPLICABLE`, not `UNMAPPED`;
- mapping/relationship text cannot promote an `OUT_OF_SCOPE` path to `MAPPED`;
- an `UNRESOLVED` path remains `POLICY_UNRESOLVED`;
- `UNRESOLVED` cannot be promoted by correlation or execution evidence;
- execution evidence remains distinct from mapping/relationship verification.

---

## 9. Current Disposition

`P6 EJR SCOPE GOVERNANCE = RESOLVED / OUT_OF_SCOPE FOR DIRECT IMPACT CORRELATION`.

No REP-020 mapping was added to suppress the historical gap.  
No relationship was promoted.  
No runtime semantics were changed.  
No correlator hard-code was added.  
Unknown path classes remain `UNRESOLVED` unless separately governed.

---

End of P6 Scope / Eligibility Registry