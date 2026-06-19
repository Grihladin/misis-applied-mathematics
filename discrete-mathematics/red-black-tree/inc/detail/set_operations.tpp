#ifndef SET_OPERATIONS_TPP
#define SET_OPERATIONS_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::node_pointer
set<Key, Compare, Allocator>::_btree_insert(value_type &&value) {
  node_pointer new_node = m_node_allocator.allocate(1);
  if (!new_node) {
    return nullptr;
  }

  std::construct_at(new_node, std::move(value));
  new_node->set_parent(nil_node());
  new_node->set_left_child(nil_node());
  new_node->set_right_child(nil_node());

  if (m_root->is_nil_node()) {
    m_root = new_node;
    return new_node;
  }

  node_pointer cur_node = m_root;
  while (cur_node) {
    if (m_comp(new_node->value(), cur_node->value())) {
      if (cur_node->left_child()->is_nil_node()) {
        new_node->set_parent(cur_node);
        cur_node->set_left_child(new_node);
        return new_node;
      }
      cur_node = cur_node->left_child();
    } else {
      if (cur_node->right_child()->is_nil_node()) {
        new_node->set_parent(cur_node);
        cur_node->set_right_child(new_node);
        return new_node;
      }
      cur_node = cur_node->right_child();
    }
  }
  return nullptr;
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::node_pointer
set<Key, Compare, Allocator>::_btree_find(const_reference value) {
  node_pointer cur_node = m_root;
  while (cur_node && !cur_node->is_nil_node()) {
    if (cur_node->value() == value) {
      return cur_node;
    }

    if (m_comp(value, cur_node->value())) {
      cur_node = cur_node->left_child();
    } else {
      cur_node = cur_node->right_child();
    }
  }
  return nullptr;
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::node_pointer
set<Key, Compare, Allocator>::_btree_left_most(node_pointer node) {
  if (!node) {
    return nullptr;
  }
  if (node->is_nil_node()) {
    return nil_node();
  }

  while (!node->left_child()->is_nil_node()) {
    node = node->left_child();
  }
  return node;
}

} // namespace custom

#endif // SET_OPERATIONS_TPP
