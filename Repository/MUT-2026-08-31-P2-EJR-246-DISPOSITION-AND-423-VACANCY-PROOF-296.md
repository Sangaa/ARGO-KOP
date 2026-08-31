# MUT-2026-08-31-P2-EJR-246-DISPOSITION-AND-423-VACANCY-PROOF-296

Status: OPEN / EVIDENCE EXECUTION AUTHORIZED
Scope: evidence-only disposition confirmation for EJR-246 and complete-history vacancy proof for candidate EJR-423.
Opening main: `98c81b0920425b2dc9a14baf5026c72ddf46b56e`
Pre-write Matrix296: `759602558deddd46ba525b1c2f56c64c352ca0ea`

## Disposition under test

- `Memory/Engineering_Journal/EJR-246_2026-08-15_P65_SESSION_CLOSURE.md`: RETAINED first valid historical allocation unless stronger contradictory evidence emerges.
- `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`: DISPLACED legitimate content if complete-history successor vacancy is proven.
- Memory allocation: `899924bf6916129db59ef2a5eb035c5f969ea5c7` at 2026-08-15T07:35:51Z.
- Root allocation: `35ec18ca6a0444ecc945e72fe10ac4374713dbdd` at 2026-08-17T18:54:52Z.

Final census evidence before this lease: artifact `9762099086`, digest `sha256:8fd78bcb0fa025989cd16bd30c74d54a9bdc29429ea3d6e44df69b91e5966193`, expected=14, observed=14, decision=CENSUSED. EJR-246 has only cohort-governance exact-ID references and no exact-member-path consumers.

Both records are preserved unchanged in this lease. Current search absence for EJR-423 is not treated as vacancy proof.

## Required hard gate

Dedicated workflow must use complete checkout history and `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-423`, upload the exact JSON evidence, and fail closed unless `decision == VACANT`.

Identity mutation is explicitly forbidden in Lease296. If the gate succeeds, EJR-423 becomes reserved only for displaced root EJR-246 and a separate governed repair lease is required.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
