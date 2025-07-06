#ifndef SET_MODIFIERS_TPP
#define SET_MODIFIERS_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::insert(const value_type &value) {
  return insert(value_type(value));
}

template <class Key, class Compare, class Allocator>
bool set<Key, Compare, Allocator>::insert(value_type &&value) {
  node_pointer new_node = _btree_insert(std::move(value));
  if (!new_node) {
    return false;
  }

  balance_after_insert(new_node);
  return true;
}

template <class Key, class Compare, class Allocator>
typename set<Key, Compare, Allocator>::size_type
set<Key, Compare, Allocator>::erase(const_reference value) {
  node_pointer node_to_delete = _btree_find(value);
  if (!node_to_delete || node_to_delete->is_nil_node()) {
    return 0;
  }

  auto children_count = [](node_pointer node) -> size_t {
    return (size_t)(!node->left_child()->is_nil_node()) +
           (size_t)(!node->right_child()->is_nil_node());
  };

  auto destroy_node = [this](node_pointer node) {
    if (node && node->is_nil_node()) {
      return;
    }
    std::destroy_at(node);
    this->m_node_allocator.deallocate(node, 1);
  };

  if (children_count(node_to_delete) == 0) {
    if (is_root(node_to_delete)) {
      m_root = nil_node();
    } else {
      if (is_left_child(node_to_delete)) {
        node_to_delete->parent()->set_left_child(nil_node());
      } else {
        node_to_delete->parent()->set_right_child(nil_node());
      }
    }
    return 1;
  }

  node_pointer left_most = _btree_left_most(node_to_delete->right_child());
  node_pointer child = left_most->right_child();
  if (left_most == nil_node()) {
    child = nil_node();
    left_most = node_to_delete->left_child();
  }

  child->set_parent(left_most->parent());
  if (is_root(left_most)) {
    m_root = child;
  } else {
    if (is_left_child(left_most)) {
      left_most->parent()->set_left_child(child);
    } else {
      left_most->parent()->set_right_child(child);
    }
  }

  if (node_to_delete != left_most) {
    node_to_delete->set_value(std::move(left_most->value()));
  }

  if (left_most->is_black()) {
    balance_after_delete(child);
  }

  destroy_node(left_most);
  return 1;
}

} // namespace custom

#endif // SET_MODIFIERS_TPP
