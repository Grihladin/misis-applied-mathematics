import json
import sys
from typing import Dict, Optional, Any

class TreeNode:
    def __init__(self, value: str, children: Optional[Dict[str, "TreeNode"]] = None, parent: Optional["TreeNode"] = None) -> None:
        self.children = children if children is not None else {}
        self.value = value
        self.parent = parent

    def append_child(self, child_value: str) -> "TreeNode":
        child_node = TreeNode(child_value, parent=self)
        self.children[child_value] = child_node
        return child_node

    def get_child(self, child_value: str) -> "TreeNode":
        return self.children[child_value]

    def to_json(self) -> Dict[str, Any]:
        return {self.value: self._traverse()}

    def _traverse(self) -> Dict[str, Any]:
        return {key: child._traverse() for key, child in self.children.items()}

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)

    def find_node(self, search_value: str) -> "TreeNode":
        if self.value == search_value:
            return self

        for child in self.children.values():
            try:
                return child.find_node(search_value)
            except KeyError:
                continue

        raise KeyError(f"Child with value '{search_value}' not found.")

    def append_from_dict(self, value: str, dict_: Dict[str, Any], parent: Optional["TreeNode"] = None) -> "TreeNode":
        node = TreeNode(value=value, parent=parent)
        for key, child_dict in dict_.items():
            node.children[key] = node.append_from_dict(value=key, dict_=child_dict, parent=node)

        return node

    @classmethod
    def from_file(cls, filename: str) -> "TreeNode":
        with open(filename, "r") as file:
            data = json.load(file)
        root_key = next(iter(data))
        root = TreeNode(root_key)
        for key, child_data in data[root_key].items():
            root.children[key] = root.append_from_dict(value=key, dict_=child_data, parent=root)
        return root

    def pretty_print(self) -> str:
        content = self.value
        for child in self.children.values():
            content += f" {child.value}"
        if self.parent:
            content += f" {self.parent.value}"
        content += "\n"

        for child in self.children.values():
            content += child.pretty_print()

        return content

def example_usage() -> None:
    root = TreeNode("1")
    node_2 = root.append_child("2")
    node_2.append_child("3")
    node_4 = node_2.append_child("4")
    node_4.append_child("5").append_child("7")
    node_4.append_child("6")

    print(root)
    print(root.pretty_print())

if __name__ == "__main__":
    example_usage()
