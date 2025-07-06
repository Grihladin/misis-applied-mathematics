#ifndef SET_NODE_H
#define SET_NODE_H

#include <memory>

namespace custom {

// Forward declaration
template <class Key, class Compare, class Allocator> class set;

namespace details {

template <typename T> class SetNode {
  template <class Key, class Compare, class Allocator>
  friend class ::custom::set;

public:
  enum class Color {
    Red = 0,
    Black,
  };

  using node_type = SetNode;
  using node_pointer = node_type *;
  using value_type = T;
  using color_type = Color;
  using const_reference = const value_type &;

  explicit SetNode(const value_type &value) : m_value(value) {}
  explicit SetNode(value_type &&value) : m_value(std::move(value)) {}

  ~SetNode() = default;

  void set_parent(node_pointer pc) { m_parent = pc; }
  void set_left_child(node_pointer lc) { m_left_child = lc; }
  void set_right_child(node_pointer rc) { m_right_child = rc; }
  void set_color(color_type cl) { m_color = cl; }
  void set_value(const_reference val) { m_value = val; }
  void set_value(value_type &&val) { m_value = std::move(val); }

  node_pointer left_child() const { return m_left_child; }
  node_pointer right_child() const { return m_right_child; }
  node_pointer parent() const { return m_parent; }
  color_type color() const { return m_color; }

  bool is_red() const { return color() == color_type::Red; }
  bool is_black() const { return color() == color_type::Black; }
  bool is_nil_node() const { return m_is_nil_node; }
  const_reference value() const { return m_value; }
  value_type &&value() { return std::move(m_value); }

protected:
  SetNode(bool is_nil_node, color_type color)
      : m_color(color), m_is_nil_node(is_nil_node) {}

private:
  color_type m_color{Color::Red};
  node_pointer m_parent{nullptr};
  node_pointer m_left_child{nullptr};
  node_pointer m_right_child{nullptr};
  value_type m_value;
  bool m_is_nil_node{false};
};

} // namespace details
} // namespace custom

#endif // SET_NODE_H
