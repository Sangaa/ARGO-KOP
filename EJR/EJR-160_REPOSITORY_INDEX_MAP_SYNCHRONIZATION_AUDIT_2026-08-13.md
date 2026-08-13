# EJR-160 — Repository Index / Map Synchronization Audit

Date: 2026-08-13
Status: Open / Integrity Hold
Scope: REP-001 ↔ REP-002 synchronization

## Finding

REP-001 currently indexes four physically constructed Memory Build-01 subdomains:

- Operational Memory
- Decision Memory
- Historical Memory
- Project Memory

REP-002 currently maps only Operational Memory from that Build-01 set. Therefore REP-001 and REP-002 are not fully synchronized on the currently declared Memory inventory.

## Secondary Drift

Both repository control documents retain `Last Audit Date: Aug 11, 2026`, although subsequent repository mutations and re-reads occurred on Aug 13, 2026. The date is stale and must be synchronized during the next controlled mutation.

## Safety Decision

No partial mutation is performed in this audit record. REP-001 and REP-002 are full-document replacement artifacts; updating one without the other would temporarily widen the inconsistency. The next mutation must update both documents from freshly fetched full content and preserve all existing content except the explicitly approved synchronization changes.

## Required Repair

1. Add Decision Memory, Historical Memory and Project Memory to REP-002 using the exact canonical paths already indexed by REP-001.
2. Synchronize both Last Audit Date fields to the actual audit date of the mutation.
3. Preserve Integrity Hold until REP-011 confirms review and relationship validation.
4. Re-read both documents after mutation.
5. Run repository regression checks for REP-001/REP-002 inventory equality for the declared Memory Build-01 scope.
6. Do not promote Memory subdomains to canonical authority merely because they are indexed.

## Acceptance Evidence

- REP-001 and REP-002 agree on the four Build-01 Memory subdomains.
- No stale physical path is introduced.
- Integrity Hold remains until cross-layer validation is complete.

## Guiding Rule

Inventory synchronization is not semantic authorization. Index first, validate relationships, then promote authority only with evidence.

---

End of Record
