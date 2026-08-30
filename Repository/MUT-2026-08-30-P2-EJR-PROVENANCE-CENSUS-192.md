# P2 EJR PROVENANCE CENSUS — LEASE 192

Transaction ID: `MUT-2026-08-30-P2-EJR-PROVENANCE-CENSUS-192`
Lease: `R71-20260830-P2-EJR-PROVENANCE-CENSUS-192`
Protocol: HERMUZ / GOV-014
Status: `OPEN / PREWRITE / ANALYTICAL CLASSIFICATION BEFORE IDENTITY MUTATION`
Entry head: `ed4036c86a0e5c2e3900776106eedfbaf7a47793`

## Scope

Continue Priority 2 historical/provenance identity reconciliation from Lease 191 by classifying the bounded EJR ambiguity groups that contain at least one explicit `Document ID` owner claim.

The Lease MUST NOT rename, delete, suppress, or normalize any EJR identity merely to reduce audit counts.

## Proven entry evidence

Lease 191 exact-head artifact `9731526902` exposes structured `ambiguous_duplicate_records` while preserving the original ambiguity/pass-fail semantics.

Current artifact census:

- ambiguous groups: `144`;
- EJR ambiguous groups: `121`;
- EJR groups containing at least one `DOCUMENT_ID_FIELD`: exactly `6`;
- bounded groups: `EJR-003`, `EJR-026`, `EJR-180`, `EJR-181`, `EJR-182`, `EJR-183`.

## Investigation question

For each bounded group determine whether the members represent:

- `OWNER` — an identity allocation supported by provenance and chronology;
- `SHADOW` — an explicitly historical/noncanonical retained identity;
- `HISTORICAL REUSE` — a distinct journal record that independently reused an occupied EJR number;
- `UNRESOLVED MULTI-CLAIM` — evidence is insufficient to name a unique owner safely.

## Safety boundary

An explicit metadata field is stronger parsing evidence than H1 fallback, but it is **not by itself proof of chronological ownership**.

Before any repair allocation, the allocator must account for both explicit metadata identities and identity-bearing H1/filename claims already present in repository history.

Priority 2 remains OPEN. No global integrity/boot claim is authorized by this Lease.
