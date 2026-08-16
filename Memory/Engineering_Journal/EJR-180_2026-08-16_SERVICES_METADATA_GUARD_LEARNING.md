# EJR-180 — Services Metadata / Inventory Guard Learning

Date: 2026-08-16

## Trigger
A new Services identity/inventory guard initially failed in CI even though the Services artifacts and inventory were valid.

## Evidence
The failures came from heterogeneous authoritative formats:

- some service documents use a two-line `Document ID` field;
- `SRV-010` uses `Document ID: SRV-010` inline;
- some canonical metadata uses two-line `Canonical` / `Yes`;
- `SRV-010` uses `Canonical: Yes` inline;
- `Services/_FOLDER_STATUS.md` describes the inventory as `` `SRV-001` through `SRV-010` `` rather than repeating every identifier.

## Root Cause
The regression guard initially assumed textual uniformity where the repository only guarantees semantic identity and authority.

## Correction
The guard was updated to accept the verified metadata forms while still requiring:

`Filename Identity → Document Identity → Canonical Declaration → Folder Inventory Consistency`

The source artifacts were not modified because they were not defective.

## Verification
- Runtime / Integration / Integrity Run #487: PASS.
- Full-Stack Repository Audit Run #700: PASS.

## Learning Rule
**Integrity guards must normalize known authoritative metadata variants and validate semantic invariants; they must not impose artificial textual uniformity on valid source artifacts.**

A guard failure must first be classified as:

1. source artifact defect;
2. inventory inconsistency;
3. parser/guard defect;
4. unsupported but valid format variation.

Only the first two justify changing authoritative repository content without additional evidence.

## Reuse
This rule applies to future Core, Models, Services, Interfaces, Runtime and other namespace identity guards.
