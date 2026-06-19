#ifndef SET_HELPERS_TPP
#define SET_HELPERS_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::is_root(node_pointer node) const {
  return node == m_root;
}

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::is_left_child(node_pointer of_node) const {
  if (!of_node->parent()) {
    return false;
  }
  return of_node->parent()->left_child() == of_node;
}

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::is_right_child(node_pointer of_node) const {
  if (!of_node->parent()) {
    return false;
  }
  return of_node->parent()->right_child() == of_node;
}

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::has_uncle(node_pointer of_node) const {
  return !!uncle(of_node);
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::node_pointer
set<Key, Compare, Allocator>::uncle(node_pointer of_node) const {
  if (of_node->parent()->parent()->left_child() == of_node->parent()) {
    return of_node->parent()->parent()->right_child();
  } else {
    return of_node->parent()->parent()->left_child();
  }
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::node_pointer
set<Key, Compare, Allocator>::nil_node() const {
  return (node_pointer)&m_nil_node;
}

} // namespace custom

#endif // SET_HELPERS_TPP
