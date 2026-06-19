#ifndef SET_BALANCE_TPP
#define SET_BALANCE_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::balance_after_insert(node_pointer new_node) {
  while (!is_root(new_node) && new_node->parent()->is_red()) {
    if (has_uncle(new_node) && uncle(new_node)->is_red()) {
      new_node->parent()->set_color(node_type::Color::Black);
      new_node->parent()->parent()->set_color(node_type::Color::Red);
      uncle(new_node)->set_color(node_type::Color::Black);
      new_node = new_node->parent()->parent();
    } else {
      if (is_left_child(new_node->parent())) {
        if (is_right_child(new_node)) {
          new_node = new_node->parent();
          rotate<RotateType::Left>(new_node);
        }
        new_node->parent()->set_color(node_type::Color::Black);
        new_node->parent()->parent()->set_color(node_type::Color::Red);
        rotate<RotateType::Right>(new_node->parent()->parent());
      } else {
        if (is_left_child(new_node)) {
          new_node = new_node->parent();
          rotate<RotateType::Right>(new_node);
        }
        new_node->parent()->set_color(node_type::Color::Black);
        new_node->parent()->parent()->set_color(node_type::Color::Red);
        rotate<RotateType::Left>(new_node->parent()->parent());
      }
    }
  }

  m_root->set_color(node_type::Color::Black);
}

template <class Key, class Compare, class Allocator>
void set<Key, Compare, Allocator>::balance_after_delete(node_pointer node) {
  while (!is_root(node) && node->is_black()) {
    if (is_left_child(node)) {
      node_pointer brother = node->parent()->right_child();
      if (brother && brother->is_red()) {
        brother->set_color(node_type::Color::Black);
        node->parent()->set_color(node_type::Color::Red);
        rotate<RotateType::Left>(node->parent());
        brother = node->parent()->right_child();
      }
      if (brother->left_child()->is_black() &&
          brother->right_child()->is_black()) {
        brother->set_color(node_type::Color::Red);
        node = node->parent();
      } else {
        if (brother->right_child()->is_black()) {
          brother->left_child()->set_color(node_type::Color::Black);
          brother->set_color(node_type::Color::Red);
          rotate<RotateType::Right>(brother);
          brother = node->parent()->right_child();
        }
        brother->set_color(node->parent()->color());
        node->parent()->set_color(node_type::Color::Black);
        brother->right_child()->set_color(node_type::Color::Black);
        rotate<RotateType::Left>(node->parent());
        node = m_root;
      }
    } else {
      node_pointer brother = node->parent()->left_child();
      if (brother && brother->is_red()) {
        brother->set_color(node_type::Color::Black);
        node->parent()->set_color(node_type::Color::Red);
        rotate<RotateType::Right>(node->parent());
        brother = node->parent()->left_child();
      }
      if (brother->left_child()->is_black() &&
          brother->right_child()->is_black()) {
        brother->set_color(node_type::Color::Red);
        node = node->parent();
      } else {
        if (brother->left_child()->is_black()) {
          brother->right_child()->set_color(node_type::Color::Black);
          brother->set_color(node_type::Color::Red);
          rotate<RotateType::Left>(brother);
          brother = node->parent()->left_child();
        }
        brother->set_color(node->parent()->color());
        node->parent()->set_color(node_type::Color::Black);
        brother->left_child()->set_color(node_type::Color::Black);
        rotate<RotateType::Right>(node->parent());
        node = m_root;
      }
    }
  }

  m_root->set_color(node_type::Color::Black);
}

template <class Key, class Compare, class Allocator>
template <typename set<Key, Compare, Allocator>::RotateType rt>
constexpr void set<Key, Compare, Allocator>::rotate(node_pointer node) {
  if constexpr (rt == RotateType::Left) {
    //    p <-(node)         b
    //  a   b      ---->   p   d
    //     c d            c a
    if (node->right_child()->is_nil_node()) {
      return;
    }

    node_pointer node_p = node;
    node_pointer node_b = node->right_child();
    node_pointer node_c = node_b->left_child();

    node_b->set_left_child(node_p);
    node_b->set_parent(node_p->parent());
    if (node_p->parent()) {
      if (is_left_child(node_p)) {
        node_p->parent()->set_left_child(node_b);
      } else {
        node_p->parent()->set_right_child(node_b);
      }
    }
    node_p->set_parent(node_b);

    node_p->set_right_child(node_c);
    node_c->set_parent(node_p);

    if (is_root(node_p)) {
      m_root = node_b;
    }
  } else if constexpr (rt == RotateType::Right) {
    //    p <-(node)         a
    //  a   b      ---->   c   p
    // c d                    d b
    if (node->left_child()->is_nil_node()) {
      return;
    }

    node_pointer node_p = node;
    node_pointer node_a = node->left_child();
    node_pointer node_d = node_a->right_child();

    node_a->set_right_child(node_p);
    node_a->set_parent(node_p->parent());
    if (node_p->parent()) {
      if (is_left_child(node_p)) {
        node_p->parent()->set_left_child(node_a);
      } else {
        node_p->parent()->set_right_child(node_a);
      }
    }
    node_p->set_parent(node_a);

    node->set_left_child(node_d);
    node_d->set_parent(node_p);

    if (is_root(node_p)) {
      m_root = node_a;
    }
  }
}

} // namespace custom

#endif // SET_BALANCE_TPP
