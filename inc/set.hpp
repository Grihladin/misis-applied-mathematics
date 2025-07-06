#ifndef SET_H
#define SET_H

#include "set_node.hpp"
#include "utils.hpp"
#include <fstream>
#include <iostream>
#include <memory>

#define DEBUG

namespace custom {

template <class Key, class Compare = std::less<Key>,
          class Allocator = std::allocator<Key>>
class set {
public:
  using key_type = Key;
  using value_type = Key;
  using size_type = std::size_t;
  using difference_type = std::ptrdiff_t;
  using key_compare = Compare;
  using value_compare = Compare;
  using allocator_type = Allocator;
  using refernce = value_type &;
  using const_reference = const value_type &;
  using pointer = value_type *;
  using const_pointer = const value_type *;
  using node_type = details::SetNode<value_type>;

private:
  using node_pointer = node_type *;
  using node_const_pointer = const node_type *;
  typedef typename __rebind_alloc_helper<allocator_type, node_type>::type
      node_alloc_type;

  enum class RotateType {
    Left,
    Right,
  };

public:
  // Constructors
  set();
  set(const Compare &comp, const Allocator &alloc = Allocator());
  explicit set(const Allocator &alloc);

  // Modifiers
  bool insert(const value_type &value);
  bool insert(value_type &&value);
  size_type erase(const_reference value);

  // Observers
  allocator_type get_allocator() const noexcept;
  size_type size() const;
  bool empty() const;

#ifdef DEBUG
  // Debug methods
  void print(std::ofstream &file);
  void print_loop(node_pointer node, std::ofstream &file);
  void print_terminal();
  void print_terminal_recursive(node_pointer node, const std::string &prefix,
                                bool is_last);
  int print_id;
#endif

private:
  // Helper methods
  bool is_root(node_pointer node) const;
  bool is_left_child(node_pointer of_node) const;
  bool is_right_child(node_pointer of_node) const;
  bool has_uncle(node_pointer of_node) const;
  node_pointer uncle(node_pointer of_node) const;

  // Balancing methods
  void balance_after_insert(node_pointer new_node);
  void balance_after_delete(node_pointer node);

  // Rotation methods
  template <RotateType rt> constexpr void rotate(node_pointer node);

  // Tree operations
  node_pointer _btree_insert(value_type &&value);
  node_pointer _btree_find(const_reference value);
  node_pointer _btree_left_most(node_pointer node);
  node_pointer nil_node() const;

private:
  node_pointer m_root{nullptr};
  size_type m_size{0};
  key_compare m_comp{};
  allocator_type m_allocator{};
  node_alloc_type m_node_allocator{};
  node_type m_nil_node;
};

} // namespace custom

#include "detail/set.tpp"

#endif // SET_H
