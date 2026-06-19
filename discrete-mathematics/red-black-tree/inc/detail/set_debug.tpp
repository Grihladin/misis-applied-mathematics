#ifndef SET_DEBUG_TPP
#define SET_DEBUG_TPP

#include "../set.hpp"

namespace custom {

#ifdef DEBUG
template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::print_loop(node_pointer node,
                                              std::ofstream &file) {
  if (!node || node->is_nil_node()) {
    return;
  }
  int my_id = print_id++;
  static const char *k[] = {"r", "b"};
  file << std::to_string(my_id) << " [label=\""
       << std::to_string(node->value()) + k[node->is_black()] << "\"];\n";
  if (node->left_child() && !node->left_child()->is_nil_node())
    file << std::to_string(my_id) << " -> " << std::to_string(print_id) << "\n";
  print_loop(node->left_child(), file);
  if (node->right_child() && !node->right_child()->is_nil_node())
    file << std::to_string(my_id) << " -> " << std::to_string(print_id) << "\n";
  print_loop(node->right_child(), file);
}

template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::print(std::ofstream &file) {
  std::cout << "Printing" << std::endl;
  print_id = 0;
  file << "digraph AST {\n";
  file << "node [shape=box];\n";
  print_loop(m_root, file);
  file << "}\n";
}

template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::print_terminal() {
  std::cout << "\n🌳 Red-Black Tree Structure:" << std::endl;
  std::cout << "=============================" << std::endl;
  if (m_root->is_nil_node()) {
    std::cout << "Tree is empty" << std::endl;
  } else {
    print_terminal_recursive(m_root, "", true);
  }
  std::cout << "=============================" << std::endl;
  std::cout << "(R) = Red, (B) = Black" << std::endl << std::endl;
}

template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::print_terminal_recursive(
    node_pointer node, const std::string &prefix, bool is_last) {
  if (!node || node->is_nil_node()) {
    return;
  }

  std::cout << prefix;
  std::cout << (is_last ? "└── " : "├── ");
  std::cout << node->value() << (node->is_red() ? "(R)" : "(B)") << std::endl;

  std::string child_prefix = prefix + (is_last ? "    " : "│   ");

  // Print children if they exist
  bool has_left = node->left_child() && !node->left_child()->is_nil_node();
  bool has_right = node->right_child() && !node->right_child()->is_nil_node();

  if (has_left) {
    print_terminal_recursive(node->left_child(), child_prefix, !has_right);
  }
  if (has_right) {
    print_terminal_recursive(node->right_child(), child_prefix, true);
  }
}
#endif

} // namespace custom

#endif // SET_DEBUG_TPP
