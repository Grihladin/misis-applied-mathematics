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

    def get_child(self, child_value: str) -> Optional["TreeNode"]:
        return self.children.get(child_value)

    def to_json(self) -> Dict[str, Any]:
        return {self.value: self._traverse()}

    def _traverse(self) -> Dict[str, Any]:
        return {key: child._traverse() for key, child in self.children.items()}

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=4)

    def find_node(self, search_value: str) -> Optional["TreeNode"]:
        if self.value == search_value:
            return self

        for child in self.children.values():
            found_child = child.find_node(search_value)
            if found_child is not None:
                return found_child

        return None

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
    child_2 = root.append_child("2")
    child_3 = child_2.append_child("3")

    child_4 = root.get_child("2")
    if child_4 is not None:
        child_4.append_child("4")
    else:
        print("Child '2' not found, cannot append '4'")

    child_5 = root.get_child("4")
    if child_5 is not None:
        child_5.append_child("5").append_child("7")
        child_5.append_child("6")
    else:
        print("Child '4' not found, cannot append '5', '6', or '7'")

    print(root)
    print(root.pretty_print())


if __name__ == "__main__":
    example_usage()
