"""GT-042 boundary probe: explicit child root with an omitted intermediate root."""
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Node:
    evidence_id: str
    provenance_root: Optional[str] = None
    provenance_parent: Optional[str] = None


def state(nodes: dict[str, Node]) -> str:
    visiting: set[str] = set()
    visited: set[str] = set()

    def walk(node_id: str) -> bool:
        if node_id in visiting:
            return True
        if node_id in visited:
            return False
        node = nodes[node_id]
        visiting.add(node_id)
        if node.provenance_parent:
            if node.provenance_parent not in nodes:
                visiting.remove(node_id)
                return True
            if walk(node.provenance_parent):
                return True
            parent = nodes[node.provenance_parent]
            if node.provenance_root and parent.provenance_root and node.provenance_root != parent.provenance_root:
                visiting.remove(node_id)
                return True
            # Current ARGO provenance boundary: an explicit child root may not
            # skip over a parent that omitted its own root declaration.
            if node.provenance_root and not parent.provenance_root and node.provenance_parent != node.provenance_root:
                visiting.remove(node_id)
                return True
        if node.provenance_root and node.provenance_root not in nodes:
            visiting.remove(node_id)
            return True
        visiting.remove(node_id)
        visited.add(node_id)
        return False

    return "INVALID PROVENANCE" if any(walk(k) for k in nodes) else "VALID PROVENANCE"


def test_gt042_explicit_child_root_cannot_skip_omitted_intermediate_root():
    root = Node("ROOT-A", provenance_root="ROOT-A")
    parent = Node("PARENT", provenance_root=None, provenance_parent="ROOT-A")
    child = Node("CHILD", provenance_root="ROOT-A", provenance_parent="PARENT")
    nodes = {x.evidence_id: x for x in (root, parent, child)}
    assert state(nodes) == "INVALID PROVENANCE"
