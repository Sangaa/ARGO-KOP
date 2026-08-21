# P6 — SCOPE / ELIGIBILITY REGISTRY

Platform: ARGO KOP  
Document ID: P6-SCOPE-001  
Status: **Canonical P6 Scope Boundary Contract / Governance-Non-Resolving**  
Authority: `GOV-013` + applicable ARGO governance authority  
Development Baseline: `3.2.1`  
Purpose: Separate P6 scope/eligibility policy from changed-path correlation and execution evidence classification.

---

## 1. Boundary

P6 MUST NOT infer whether a repository path is within P6 scope from the existence or absence of a mapping in `REP-020`, `REP-014`, or another evidence surface.

Scope/eligibility is evaluated before correlation.

This registry expresses the currently authorized scope state. It does **not** itself resolve unresolved governance questions and does not grant relationship authority.

Required evaluation order:

`Changed Path → Scope / Eligibility → Correlation → Execution Evidence → Evidence Classification`

---

## 2. Scope States

The only valid P6 scope states are:

- `IN_SCOPE` — the path class is governed by P6 correlation under an explicit authority/evidence basis.
- `OUT_OF_SCOPE` — the path class is explicitly excluded from P6 correlation under an explicit authority/evidence basis.
- `UNRESOLVED` — scope policy has not been authoritatively decided; the correlator MUST NOT reinterpret this state as a missing mapping.

`UNRESOLVED` is a valid terminal policy state for a P6 evaluation. It MUST NOT be converted automatically to `UNMAPPED`, `MAPPED`, `PARTIAL`, `OUT_OF_SCOPE`, or any relationship state.

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
| `EJR/**` | `UNRESOLVED` | Governance decision required | GitHub Issue #15 + EJR-285 / EJR-284 evidence | Return `POLICY_UNRESOLVED`; never infer `UNMAPPED` |
| Other repository paths | `UNRESOLVED` unless an explicit governed registry entry exists | Applicable ARGO authority | Current repository evidence required | Do not infer scope from path existence or neighboring mappings |

---

## 4. Correlation Contract

For an evaluated changed path:

| Eligibility | Correlation result | Meaning |
|---|---|---|
| `IN_SCOPE` | `MAPPED` | Canonical mapping/evidence was located by the correlator |
| `IN_SCOPE` | `UNMAPPED` | No canonical mapping/evidence was located; this is a correlation finding, not a governance decision |
| `OUT_OF_SCOPE` | `NOT_APPLICABLE` | P6 correlation does not apply |
| `UNRESOLVED` | `POLICY_UNRESOLVED` | Governance policy is unresolved; the correlator MUST NOT classify this as a missing mapping |

`UNMAPPED` MUST NOT be emitted for a path whose scope state is `UNRESOLVED`.

---

## 5. Evidence Boundary

Execution evidence and semantic/relationship evidence are distinct evidence classes.

The following states are independent and MUST NOT be implicitly promoted into one another:

`EXECUTION_VERIFIED`  
`CANONICAL_MAPPING_VERIFIED`  
`RELATIONSHIP_VERIFIED`

A CI PASS, runtime evidence artifact, fixture result, or controlled synthetic result cannot by itself create canonical mapping or relationship authority.

Evidence maturity remains bounded by the strongest actually exercised layer:

`UNIT → CONTROLLED_SYNTHETIC → CANONICAL_REPOSITORY → INTEGRATION → RUNTIME`

Lower-level evidence MUST NOT promote a higher-level state automatically.

---

## 6. EJR Governance Boundary

`EJR/**` is intentionally `UNRESOLVED` in this revision.

This is **not** a decision that EJR is in-scope or out-of-scope.

Issue #15 remains the authoritative governance decision gate for the EJR policy. Until that decision is recorded, P6 must expose `POLICY_UNRESOLVED` rather than manufacture a correlation defect.

This artifact therefore repairs the boundary without pre-deciding the governance question.

---

## 7. Mutation / Promotion Safety

1. The registry does not create relationship authority.
2. The registry does not modify `REP-020` relationship state merely to remove an `UNMAPPED` result.
3. `UNRESOLVED` cannot be auto-promoted to any resolved scope state.
4. Correlation cannot override this registry.
5. Execution evidence cannot override this registry.
6. Synthetic evidence cannot override this registry.
7. Any change to an eligibility state requires explicit authority and fresh current-HEAD validation.
8. Issue #15 must remain open until an authoritative governance decision resolves the EJR policy.

---

## 8. Verification Requirement

Any P6 implementation consuming this registry MUST have canonical repository tests that read this artifact from the repository and prove at minimum:

- an `IN_SCOPE` path resolves deterministically;
- an `OUT_OF_SCOPE` path does not become `UNMAPPED`;
- an `UNRESOLVED` path remains `POLICY_UNRESOLVED`;
- `UNRESOLVED` cannot be promoted by correlation or execution evidence;
- execution evidence remains distinct from mapping/relationship verification.

---

## 9. Current Disposition

`P6 SCOPE BOUNDARY REPAIR / STEP 01 = CONTRACT MATERIALIZED`

No EJR governance decision has been made.  
No REP-020 mapping was added to suppress the existing gap.  
No relationship was promoted.  
No runtime semantics were changed.

---

End of P6 Scope / Eligibility Registry
