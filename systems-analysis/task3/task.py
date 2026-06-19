import json
import math
from dataclasses import asdict, dataclass
from typing import Any, Callable, Optional, List


@dataclass
class RelationshipMetrics:
    direct_management: int
    direct_subordination: int
    indirect_management: int
    indirect_subordination: int
    subordination: int

    def to_list(self) -> List[int]:
        return [
            self.direct_management,
            self.direct_subordination,
            self.indirect_management,
            self.indirect_subordination,
            self.subordination,
        ]


class TreeNode:
    def __init__(self, identifier: str, children: Optional[dict[str, "TreeNode"]] = None, parent: Optional["TreeNode"] = None) -> None:
        self.children = children if children is not None else {}
        self.identifier = identifier
        self.parent = parent
        self.relationship_metrics = RelationshipMetrics(0, 0, 0, 0, 0)
        self.node_count = 0

    def add_child(self, identifier: str) -> "TreeNode":
        child_node = TreeNode(identifier, parent=self)
        self.children[identifier] = child_node
        return child_node

    def calculate_node_count(self) -> None:
        self.node_count = 0

        def increment_node_count(node: "TreeNode") -> None:
            self.node_count += 1

        self.depth_first_search(increment_node_count)
        self.depth_first_search(lambda node: setattr(node, 'node_count', self.node_count))

    def depth_first_search(self, action: Callable[["TreeNode"], None]) -> None:
        action(self)
        for child in self.children.values():
            child.depth_first_search(action)

    def to_json(self) -> dict[str, Any]:
        return {self.identifier: {"relationship": asdict(self.relationship_metrics), "children": self._traverse_children()}}

    def _traverse_children(self) -> dict[str, Any]:
        return {key: child.to_json()[key] for key in self.children}

    def find_node(self, identifier: str) -> "TreeNode":
        if self.identifier == identifier:
            return self
        for child in self.children.values():
            try:
                return child.find_node(identifier)
            except KeyError:
                continue
        raise KeyError(f"Node with identifier '{identifier}' not found")

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)

    def update_relationships(self) -> None:
        for child in self.children.values():
            self.relationship_metrics.direct_management += 1
            child.relationship_metrics.direct_subordination += 1
            child.relationship_metrics.subordination = len(self.children) - 1

            child.depth_first_search(lambda grandchild: self._update_indirect_relationship(grandchild))
            child.update_relationships()

    def _update_indirect_relationship(self, node: "TreeNode") -> None:
        self.relationship_metrics.indirect_management += 1
        node.relationship_metrics.indirect_subordination += 1

    @classmethod
    def from_csv(cls, input_: str) -> "TreeNode":
        rows = [row.split(",") for row in input_.splitlines()]
        root = cls(rows[0][0])
        for row in rows:
            root.find_node(row[0]).add_child(row[1])
        root.update_relationships()
        root.calculate_node_count()
        return root

    def calculate_self_entropy(self) -> float:
        entropy = 0.0
        for count in self.relationship_metrics.to_list():
            probability = count / (self.node_count - 1)
            if probability > 0:
                entropy += probability * math.log(probability, 2)
        return -entropy

    def calculate_total_entropy(self) -> float:
        total_entropy = 0.0

        def add_entropy(node: "TreeNode") -> None:
            nonlocal total_entropy
            total_entropy += node.calculate_self_entropy()

        self.depth_first_search(add_entropy)
        return total_entropy

    def to_csv_format(self) -> str:
        nodes = []
        self.depth_first_search(lambda node: nodes.append(node))
        return "\n".join([",".join(map(str, node.relationship_metrics.to_list())) for node in sorted(nodes, key=lambda n: n.identifier)])


def calculate_entropy_from_csv(input_: str) -> float:
    matrix = [[int(value) for value in row.split(",")] for row in input_.splitlines()]
    n = len(matrix)
    total_entropy = 0.0

    for row in matrix:
        entropy = sum(prob * math.log(prob, 2) for prob in [rel / (n - 1) for rel in row if rel > 0])
        total_entropy -= entropy

    return total_entropy


if __name__ == "__main__":
    input_data = "0,1,3,0,0,0,1\n0,0,1,0,0,1,0\n0,0,2,0,0,1,0\n1,0,0,0,1,0,0\n0,0,1,0,0,1,0\n0,1,0,0,0,0,1\n1,0,0,0,1,0,0\n0,1,1,1,0,0,1\n0,0,1,0,0,0,1\n1,0,0,0,1,0,0\n0,0,1,0,0,1,0"
    print(calculate_entropy_from_csv(input_data))
