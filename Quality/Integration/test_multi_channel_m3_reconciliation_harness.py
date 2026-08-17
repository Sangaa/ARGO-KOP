from Runtime.Prototype.multi_channel_m3_reconciliation_harness import Proposal, reconcile


def test_conflicting_proposals_become_explicit_conflict():
    result = reconcile([
        Proposal("TASK-001", "CH-001", "shipment:A", "A"),
        Proposal("TASK-002", "CH-002", "shipment:A", "B"),
    ])
    assert result["status"] == "CONFLICT"
    assert result["canonical_mutation"] is False
    assert result["automatic_merge"] is False
    assert result["conflicts"]


def test_non_conflicting_proposals_reconcile_without_mutation():
    result = reconcile([
        Proposal("TASK-001", "CH-001", "shipment:A", "A"),
        Proposal("TASK-002", "CH-002", "shipment:A", "A"),
        Proposal("TASK-003", "CH-003", "shipment:B", "B"),
    ])
    assert result["status"] == "RECONCILED"
    assert result["canonical_mutation"] is False
    assert result["automatic_merge"] is False
    assert len(result["decisions"]) == 2
