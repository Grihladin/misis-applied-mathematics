#ifndef SET_CONSTRUCTORS_TPP
#define SET_CONSTRUCTORS_TPP

#include "../set.hpp"

namespace custom {

template <class Key, class Compare, class Allocator>
set<Key, Compare, Allocator>::set()
    : m_nil_node(true, node_type::Color::Black) {
  m_root = nil_node();
}

template <class Key, class Compare, class Allocator>
set<Key, Compare, Allocator>::set(const Compare &comp, const Allocator &alloc)
    : m_comp(comp), m_allocator(alloc),
      m_nil_node(true, node_type::Color::Black) {
  m_root = nil_node();
}

template <class Key, class Compare, class Allocator>
set<Key, Compare, Allocator>::set(const Allocator &alloc)
    : m_allocator(alloc), m_nil_node(true, node_type::Color::Black) {
  m_root = nil_node();
}

} // namespace custom

#endif // SET_CONSTRUCTORS_TPP
